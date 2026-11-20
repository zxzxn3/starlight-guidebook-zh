#!/usr/bin/env python3
"""Read Starlight Guidebook pages and dynamic data from the launcher cache."""

from __future__ import annotations

import html
import os
import re
import sqlite3
import subprocess
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

DEFAULT_CONTENT_DB = Path.home() / ".local/share/Space Station 14/launcher/content.db"
CONTENT_DB = Path(os.environ.get("STARLIGHT_CONTENT_DB") or DEFAULT_CONTENT_DB)
PROJECT_ROOT = Path(__file__).resolve().parent
SOURCE_ROOT = PROJECT_ROOT / "source"
FORK_ID = "starlight"

PAGE_SPECS = (
    ("science", "ServerInfo/Guidebook/Science/Science.xml"),
    ("technologies", "ServerInfo/Guidebook/Science/Technologies.xml"),
    ("anomalous-research", "ServerInfo/Guidebook/Science/AnomalousResearch.xml"),
    ("scanners-and-vessels", "ServerInfo/Guidebook/Science/ScannersAndVessels.xml"),
    ("ape", "ServerInfo/Guidebook/Science/APE.xml"),
    ("xenoarchaeology", "ServerInfo/Guidebook/Science/Xenoarchaeology.xml"),
    ("unlocking-nodes", "ServerInfo/Guidebook/Science/UnlockingNodes.xml"),
    ("analysis-console", "ServerInfo/Guidebook/Science/AnalysisConsole.xml"),
    ("robotics", "ServerInfo/Guidebook/Science/Robotics.xml"),
    ("cyborgs", "ServerInfo/_Starlight/Guidebook/Science/Cyborgs.xml"),
    (
        "science-sop",
        "ServerInfo/Guidebook/StarlightSOP/ScienceSOP/science-sop-intro.xml",
    ),
    (
        "science-sop-general",
        "ServerInfo/Guidebook/StarlightSOP/ScienceSOP/science-sop-genproc-intro.xml",
    ),
    (
        "research-guidelines",
        "ServerInfo/Guidebook/StarlightSOP/ScienceSOP/researchguidelines.xml",
    ),
    (
        "sop-anomaly-research",
        "ServerInfo/Guidebook/StarlightSOP/ScienceSOP/anomalyresearch.xml",
    ),
    (
        "sop-artifact-research",
        "ServerInfo/Guidebook/StarlightSOP/ScienceSOP/artifactresearch.xml",
    ),
    (
        "sop-item-distribution",
        "ServerInfo/Guidebook/StarlightSOP/ScienceSOP/itemdistribution.xml",
    ),
    (
        "science-sop-staff",
        "ServerInfo/Guidebook/StarlightSOP/ScienceSOP/science-sop-staff-intro.xml",
    ),
    (
        "sop-research-director",
        "ServerInfo/Guidebook/StarlightSOP/ScienceSOP/researchdirector.xml",
    ),
    (
        "sop-scientist",
        "ServerInfo/Guidebook/StarlightSOP/ScienceSOP/scientist.xml",
    ),
    (
        "sop-research-assistant",
        "ServerInfo/Guidebook/StarlightSOP/ScienceSOP/researchassistant.xml",
    ),
    (
        "sop-roboticist",
        "ServerInfo/Guidebook/StarlightSOP/ScienceSOP/roboticist.xml",
    ),
    (
        "science-sop-appendix",
        "ServerInfo/Guidebook/StarlightSOP/ScienceSOP/science-sop-appendix.xml",
    ),
)


class GuidebookLoader(yaml.SafeLoader):
    pass


def _unknown_yaml_tag(loader: GuidebookLoader, suffix: str, node: yaml.Node) -> Any:
    if isinstance(node, yaml.ScalarNode):
        return loader.construct_scalar(node)
    if isinstance(node, yaml.SequenceNode):
        return loader.construct_sequence(node)
    return loader.construct_mapping(node)


GuidebookLoader.add_multi_constructor("!", _unknown_yaml_tag)


@dataclass(frozen=True)
class Technology:
    id: str
    name: str
    discipline: str
    tier: int
    cost: int
    prerequisites: tuple[str, ...]


@dataclass(frozen=True)
class GuideEntry:
    id: str
    name_key: str
    text: str
    department: str
    order: int
    children: tuple[str, ...]
    rule_entry: bool


def open_content() -> sqlite3.Connection:
    if not CONTENT_DB.exists():
        raise SystemExit(f"Starlight launcher content database not found: {CONTENT_DB}")
    return sqlite3.connect(f"file:{CONTENT_DB}?mode=ro", uri=True)


def content_version(connection: sqlite3.Connection) -> str:
    row = connection.execute(
        """
        SELECT ForkVersion
        FROM ContentVersion
        WHERE ForkId = ?
        ORDER BY LastUsed DESC
        LIMIT 1
        """,
        (FORK_ID,),
    ).fetchone()
    return str(row[0]) if row else "unknown"


def read_text(connection: sqlite3.Connection, path: str) -> str:
    row = connection.execute(
        """
        SELECT c.Data, c.Compression
        FROM ContentManifest AS m
        JOIN ContentVersion AS v ON v.Id = m.VersionId
        JOIN Content AS c ON c.Id = m.ContentId
        WHERE v.ForkId = ? AND m.Path = ?
        """,
        (FORK_ID, path),
    ).fetchone()
    if row is None:
        raise FileNotFoundError(path)
    data, compression = row
    if compression == 2:
        data = subprocess.run(
            ["zstd", "-d", "-c"],
            input=data,
            stdout=subprocess.PIPE,
            check=True,
        ).stdout
    return data.decode("utf-8", errors="replace")


def iter_manifest_paths(connection: sqlite3.Connection, pattern: str) -> Iterable[str]:
    rows = connection.execute(
        """
        SELECT m.Path
        FROM ContentManifest AS m
        JOIN ContentVersion AS v ON v.Id = m.VersionId
        WHERE v.ForkId = ? AND m.Path LIKE ?
        ORDER BY m.Path
        """,
        (FORK_ID, pattern),
    )
    yield from (str(row[0]) for row in rows)


def parse_ftl(text: str) -> dict[str, str]:
    values: dict[str, str] = {}
    current_key: str | None = None
    current_lines: list[str] = []

    def flush() -> None:
        if current_key is not None:
            values[current_key] = "\n".join(current_lines).strip()

    for line in text.splitlines():
        if line.startswith("#"):
            continue
        if line and not line[0].isspace() and "=" in line:
            flush()
            key, value = line.split("=", 1)
            current_key = key.strip()
            current_lines = [value.strip()]
        elif current_key is not None and line[:1].isspace():
            current_lines.append(line.strip())
    flush()
    return values


def locale_values(connection: sqlite3.Connection) -> dict[str, str]:
    values: dict[str, str] = {}
    for path in iter_manifest_paths(connection, "Locale/en-US/%/__merged.ftl"):
        values.update(parse_ftl(read_text(connection, path)))
    return values


def xml_to_markdown(text: str) -> str:
    text = re.sub(r"^\s*<Document>\s*", "", text)
    text = re.sub(r"\s*</Document>\s*$", "", text)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = re.sub(
        r'<GuideEntityEmbed\s+Entity="([^"]+)"(?:\s+Caption="([^"]*)")?\s*/>',
        lambda match: _entity_markdown(match.group(1), match.group(2)),
        text,
    )
    text = re.sub(
        r'<GuideReagentEmbed\s+Reagent="([^"]+)"\s*/>',
        lambda match: f'\n<reagent id="{match.group(1)}"></reagent>\n',
        text,
    )
    text = re.sub(
        r'<GuideTechDisciplineEmbed\s+Discipline="([^"]+)"\s*/>',
        lambda match: f'\n<tech-discipline id="{match.group(1)}"></tech-discipline>\n',
        text,
    )
    text = re.sub(r"<Box>\s*", "\n", text)
    text = re.sub(r"\s*</Box>", "\n", text)
    text = re.sub(
        r'\[textlink="([^"]+)"\s+link="([^"]+)"\]',
        lambda match: f"[{match.group(1)}]({match.group(2)})",
        text,
    )
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def original_markdown(text: str) -> str:
    text = xml_to_markdown(text)
    text = _table_to_markdown(text)
    text = _dynamic_embeds_to_markdown(text)
    text = _bbcode_to_markdown(text)
    text = re.sub(
        r"</?(?:Box|ColorBox|Label|PanelContainer)[^>]*>",
        " ",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(r"<CommandButton[^>]*/?>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\n[ \t]+\n", "\n\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def _table_to_markdown(text: str) -> str:
    def replace_table(match: re.Match[str]) -> str:
        columns = int(match.group(1))
        cells = re.findall(
            r"<ColorBox[^>]*>(.*?)</ColorBox>",
            match.group(2),
            re.DOTALL,
        )
        values = [_table_cell(cell) for cell in cells]
        rows = [
            values[index : index + columns]
            for index in range(0, len(values), columns)
            if len(values[index : index + columns]) == columns
        ]
        if not rows:
            return "\n"
        header = rows[0]
        body = rows[1:]
        lines = [
            "| " + " | ".join(header) + " |",
            "| " + " | ".join("---" for _ in header) + " |",
        ]
        lines.extend("| " + " | ".join(row) + " |" for row in body)
        return "\n" + "\n".join(lines) + "\n"

    return re.sub(
        r'<Table\s+Columns="(\d+)"[^>]*>(.*?)</Table>',
        replace_table,
        text,
        flags=re.DOTALL,
    )


def _table_cell(value: str) -> str:
    value = re.sub(
        r'<entity\s+id="([^"]+)"(?:\s+caption="([^"]*)")?\s*></entity>',
        lambda match: match.group(2) or match.group(1),
        value,
    )
    value = re.sub(r"<[^>]+>", " ", value)
    value = _bbcode_to_markdown(value)
    return " ".join(value.split()).replace("|", r"\|")


def _dynamic_embeds_to_markdown(text: str) -> str:
    labels = {
        "GuideMicrowaveGroupEmbed": "Microwave recipe group",
        "GuideDeepFryerGroupEmbed": "Deep fryer recipe group",
        "GuideReagentGroupEmbed": "Reagent group",
        "GuideReagentEmbed": "Reagent",
        "GuideLawsetListEmbed": "Lawset list",
    }
    for tag, label in labels.items():
        text = re.sub(
            rf"<{tag}\s+([^>]*?)/>",
            lambda match, label=label: f"\n> {label}: `{match.group(1).strip()}`\n",
            text,
        )
    return text


def _bbcode_to_markdown(text: str) -> str:
    text = re.sub(
        r'\[textlink="([^"]+)"\s+link="([^"]+)"\s*/?\]',
        r"[\1](\2)",
        text,
    )
    text = re.sub(
        r'\[keybind="([^"]+)"\s*/?\]',
        r"<kbd>\1</kbd>",
        text,
    )
    text = re.sub(
        r'\[protodata="([^"]+)"\s+comp="([^"]+)"\s+member="([^"]+)"[^\]]*\]',
        r"`\1.\2.\3`",
        text,
    )
    text = re.sub(
        r"\[bold\](.*?)\[/bold\]",
        r"<strong>\1</strong>",
        text,
        flags=re.DOTALL,
    )
    text = re.sub(
        r"\[bolditalic\](.*?)\[/bolditalic\]",
        r"<strong><em>\1</em></strong>",
        text,
        flags=re.DOTALL,
    )
    text = re.sub(
        r"\[italic\](.*?)\[/italic\]",
        r"<em>\1</em>",
        text,
        flags=re.DOTALL,
    )
    text = re.sub(
        r"\[italics\](.*?)\[/italics\]",
        r"<em>\1</em>",
        text,
        flags=re.DOTALL,
    )
    text = re.sub(r"\[color=[^\]]+\](.*?)\[/color\]", r"\1", text, flags=re.DOTALL)
    text = re.sub(r"\[/?(?:color|head|lightblue|red|colopr)[^\]]*\]", "", text)
    return text


def _entity_markdown(entity_id: str, caption: str | None) -> str:
    caption_attr = f' caption="{html.escape(caption, quote=True)}"' if caption else ""
    return f'\n<entity id="{entity_id}"{caption_attr}></entity>\n'


def technologies(
    connection: sqlite3.Connection, locales: dict[str, str]
) -> list[Technology]:
    entries: dict[str, Technology] = {}
    for path in iter_manifest_paths(connection, "Prototypes/%Research/__merged.yml"):
        if "/Partials/" in path:
            continue
        for document in yaml.load_all(
            read_text(connection, path), Loader=GuidebookLoader
        ):
            if not isinstance(document, list):
                continue
            for item in document:
                if not isinstance(item, dict) or item.get("type") != "technology":
                    continue
                tech_id = str(item.get("id") or "")
                name_key = str(item.get("name") or "")
                if not tech_id or not name_key:
                    continue
                entries[tech_id] = Technology(
                    id=tech_id,
                    name=locales.get(name_key, _humanize(tech_id)),
                    discipline=str(item.get("discipline") or "Other"),
                    tier=int(item.get("tier") or 0),
                    cost=int(item.get("cost") or 0),
                    prerequisites=tuple(
                        str(value)
                        for value in item.get("technologyPrerequisites") or []
                    ),
                )
    return sorted(
        entries.values(), key=lambda tech: (tech.discipline, tech.tier, tech.name)
    )


def guide_entries(connection: sqlite3.Connection) -> list[GuideEntry]:
    entries: dict[str, dict[str, Any]] = {}
    partials: list[dict[str, Any]] = []
    for path in iter_manifest_paths(connection, "Prototypes/%Guidebook/__merged.yml"):
        for document in yaml.load_all(
            read_text(connection, path), Loader=GuidebookLoader
        ):
            if not isinstance(document, list):
                continue
            for item in document:
                if not isinstance(item, dict) or item.get("type") != "guideEntry":
                    continue
                entry_id = str(item.get("id") or "")
                if not entry_id:
                    continue
                if "/Partials/" in path:
                    partials.append(item)
                    continue
                current = entries.setdefault(entry_id, {"id": entry_id, "children": []})
                for key, value in item.items():
                    if key != "children":
                        current[key] = value
                if item.get("children"):
                    current["children"] = [
                        str(child) for child in item.get("children") or []
                    ]
    for item in partials:
        entry_id = str(item.get("id") or "")
        if not entry_id:
            continue
        current = entries.setdefault(entry_id, {"id": entry_id, "children": []})
        if item.get("children"):
            current["children"] = [
                *current.get("children", []),
                *(str(child) for child in item.get("children") or []),
            ]
    return [
        GuideEntry(
            id=entry_id,
            name_key=str(item.get("name") or ""),
            text=str(item.get("text") or "").lstrip("/"),
            department=str(item.get("department") or ""),
            order=int(item.get("order") or item.get("priority") or 0),
            children=tuple(item.get("children") or ()),
            rule_entry=bool(item.get("ruleEntry")),
        )
        for entry_id, item in sorted(entries.items())
        if item.get("text")
    ]


def guide_word_counts(
    connection: sqlite3.Connection,
    paths: Iterable[str],
) -> dict[str, int]:
    counts: dict[str, int] = {}
    for path in sorted(set(paths)):
        text = read_text(connection, path)
        text = re.sub(r"<!--.*?-->", " ", text, flags=re.DOTALL)
        text = re.sub(r"<[^>]+>", " ", text)
        text = html.unescape(text)
        counts[path] = len(re.findall(r"[A-Za-z0-9]+(?:['’-][A-Za-z0-9]+)*", text))
    return counts


def _humanize(value: str) -> str:
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", value)
    return value.replace("_", " ").strip()


def extract_sources() -> None:
    SOURCE_ROOT.mkdir(parents=True, exist_ok=True)
    with open_content() as connection:
        for page_id, path in PAGE_SPECS:
            source = xml_to_markdown(read_text(connection, path))
            header = f"---\nid: {page_id}\nsource: {path}\n---\n\n"
            (SOURCE_ROOT / f"{page_id}.md").write_text(
                header + source,
                encoding="utf-8",
            )
    print(f"wrote {len(PAGE_SPECS)} pages to {SOURCE_ROOT}")


def source_version() -> str:
    with open_content() as connection:
        return content_version(connection)


if __name__ == "__main__":
    extract_sources()
