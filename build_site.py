#!/usr/bin/env python3
"""Build the Chinese Starlight guidebook as HTML and EPUB."""

from __future__ import annotations

import html
import json
import re
import shutil
import zipfile
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markdown_it import MarkdownIt

import guidebook_source

PROJECT_ROOT = Path(__file__).resolve().parent
CONTENT_ROOT = PROJECT_ROOT / "content"
TEMPLATE_ROOT = PROJECT_ROOT / "templates"
SITE_ROOT = PROJECT_ROOT / "site"
EPUB_PATH = PROJECT_ROOT / "starlight-guidebook-science-zh.epub"
ENTITY_LABELS = PROJECT_ROOT / "data" / "entity_labels_zh.yml"

STARLIGHT_RULES_ENTRY = "StarlightRuleset"
ARTIFACT_GUIDE_PARENT = "Xenoarchaeology"
ARTIFACT_GUIDE_ENGLISH_TITLE = "Artifact Guide"
DISCIPLINE_ZH = {
    "Industrial": "工业",
    "Arsenal": "军备",
    "Experimental": "实验",
    "CivilianServices": "民用服务",
    "Biochemical": "生物化学",
    "Other": "其他",
}


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        value = " ".join(data.split())
        if value:
            self.parts.append(value)

    def text(self) -> str:
        return " ".join(self.parts)


def plain_text(value: str) -> str:
    parser = TextExtractor()
    parser.feed(value)
    return parser.text()


def summary(value: str, limit: int = 72) -> str:
    text = plain_text(value)
    return text if len(text) <= limit else text[:limit].rstrip() + "…"


def build_guide_tree(
    pages: list[dict[str, Any]],
    entries: list[guidebook_source.GuideEntry],
    locales: dict[str, str],
    word_counts: dict[str, int],
) -> list[dict[str, Any]]:
    entries_by_id = {entry.id: entry for entry in entries}
    page_by_source = {
        page["source"]: page
        for page in pages
        if page.get("source", "").startswith("ServerInfo/")
    }
    roots = set(entries_by_id)
    for entry in entries:
        roots.difference_update(entry.children)
    visited: set[str] = set()
    placed_pages: set[str] = set()

    def localized_title(entry: guidebook_source.GuideEntry) -> str:
        page = page_by_source.get(entry.text)
        if page:
            return str(page["title"])
        return locales.get(entry.name_key) or guidebook_source._humanize(entry.id)

    def translated_title(
        page: dict[str, Any],
        entry: guidebook_source.GuideEntry,
    ) -> str:
        title = str(page["title"])
        english = locales.get(entry.name_key) or guidebook_source._humanize(entry.id)
        normalized_title = title.casefold()
        variants = {english.casefold(), english.casefold().removesuffix("s")}
        normalized_english = english.casefold()
        if (
            f"（{normalized_english}）" in normalized_title
            or f"({normalized_english})" in normalized_title
        ):
            return title
        trailing_name = re.search(r"[（(]([^（）()]*)[）)]\s*$", title)
        if trailing_name and any(
            variant in trailing_name.group(1).casefold()
            for variant in variants
            if variant
        ):
            return f"{title[: trailing_name.start()]}（{english}）"
        return f"{title}（{english}）"

    def build_node(entry_id: str) -> dict[str, Any] | None:
        entry = entries_by_id.get(entry_id)
        if entry is None or entry_id in visited:
            return None
        if entry.rule_entry and entry.id != STARLIGHT_RULES_ENTRY:
            return None
        visited.add(entry_id)

        page = page_by_source.get(entry.text)
        if page:
            placed_pages.add(str(page["id"]))
            title = translated_title(page, entry)
            url = str(page["url"])
            page_id = str(page["id"])
        else:
            words = word_counts.get(entry.text, 0)
            title = f"{localized_title(entry)}（未翻译，约 {words:,} 词）"
            url = None
            page_id = None

        children = [
            child
            for child_id in entry.children
            if (child := build_node(child_id)) is not None
        ]
        return {
            "id": entry.id,
            "page_id": page_id,
            "title": title,
            "url": url,
            "children": children,
        }

    root_entries = sorted(
        (entries_by_id[entry_id] for entry_id in roots),
        key=lambda entry: (entry.order, localized_title(entry).casefold()),
    )
    tree = [
        node for entry in root_entries if (node := build_node(entry.id)) is not None
    ]

    artifact_page = next(
        (page for page in pages if page["id"] == "artifact-guide"),
        None,
    )
    if artifact_page:
        artifact_node = {
            "id": str(artifact_page["id"]),
            "page_id": str(artifact_page["id"]),
            "title": (f"{artifact_page['title']}（{ARTIFACT_GUIDE_ENGLISH_TITLE}）"),
            "url": str(artifact_page["url"]),
            "children": [],
        }

        def attach_artifact(nodes: list[dict[str, Any]]) -> bool:
            for node in nodes:
                if node["id"] == ARTIFACT_GUIDE_PARENT:
                    node["children"].append(artifact_node)
                    return True
                if attach_artifact(node["children"]):
                    return True
            return False

        if not attach_artifact(tree):
            raise ValueError(f"Guidebook parent not found: {ARTIFACT_GUIDE_PARENT}")
        placed_pages.add(str(artifact_page["id"]))

    missing_pages = sorted(
        page["id"] for page in pages if page["id"] not in placed_pages
    )
    if missing_pages:
        raise ValueError(
            "translated pages are missing from the Guidebook tree: "
            + ", ".join(missing_pages)
        )
    return tree


def order_pages_by_tree(
    pages: list[dict[str, Any]],
    tree: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    order: list[str] = []

    def visit(nodes: list[dict[str, Any]]) -> None:
        for node in nodes:
            if node["page_id"]:
                order.append(str(node["page_id"]))
            visit(node["children"])

    visit(tree)
    positions = {page_id: index for index, page_id in enumerate(order)}
    return sorted(
        pages,
        key=lambda page: positions.get(str(page["id"]), len(positions)),
    )


def load_pages() -> list[dict[str, Any]]:
    pages: list[dict[str, Any]] = []
    for path in sorted(CONTENT_ROOT.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            raise ValueError(f"missing front matter: {path}")
        _, header, body = text.split("---", 2)
        metadata = yaml.safe_load(header)
        metadata["body"] = body.lstrip()
        metadata["url"] = f"{metadata['id']}.html"
        pages.append(metadata)
    pages.sort(key=lambda page: page["id"])
    return pages


def entity_card(entity_id: str, caption: str | None, labels: dict[str, str]) -> str:
    label = caption or labels.get(entity_id) or guidebook_source._humanize(entity_id)
    return (
        '<span class="entity-card">'
        f"<strong>{html.escape(label)}</strong>"
        f"<small>{html.escape(entity_id)}</small>"
        "</span>"
    )


def reagent_card(reagent_id: str) -> str:
    labels = {
        "Artifexium": ("神器激活剂", "Artifexium"),
        "ArtifactGlue": ("神器胶", "Artifact Glue"),
    }
    label, english = labels.get(reagent_id, (reagent_id, reagent_id))
    return (
        '<span class="entity-card reagent-card">'
        f"<strong>{html.escape(label)}</strong>"
        f"<small>{html.escape(english)}</small>"
        "</span>"
    )


def tech_table(
    discipline: str,
    technologies: list[guidebook_source.Technology],
    locales: dict[str, str],
) -> str:
    selected = [tech for tech in technologies if tech.discipline == discipline]
    rows: list[str] = []
    tech_by_id = {tech.id: tech for tech in technologies}
    for tech in selected:
        prerequisites = (
            ", ".join(
                tech_by_id.get(
                    item,
                    guidebook_source.Technology(
                        item,
                        guidebook_source._humanize(item),
                        "",
                        0,
                        0,
                        (),
                    ),
                ).name
                for item in tech.prerequisites
            )
            or "—"
        )
        rows.append(
            "<tr>"
            f"<td>{html.escape(tech.name)}</td>"
            f"<td>{tech.tier}</td>"
            f"<td>{tech.cost:,}</td>"
            f"<td>{html.escape(prerequisites)}</td>"
            "</tr>"
        )
    title = DISCIPLINE_ZH.get(discipline, discipline)
    return (
        f'<div class="tech-table-wrap"><h3>{html.escape(title)}学科</h3>'
        '<table class="tech-table"><thead><tr>'
        "<th>科技</th><th>等级</th><th>研究点</th><th>前置</th>"
        "</tr></thead><tbody>" + "".join(rows) + "</tbody></table></div>"
    )


def replace_embeds(
    body: str,
    labels: dict[str, str],
    technologies: list[guidebook_source.Technology],
    locales: dict[str, str],
) -> str:
    def entity(match: re.Match[str]) -> str:
        return entity_card(match.group(1), match.group(2), labels)

    body = re.sub(
        r'<entity\s+id="([^"]+)"(?:\s+caption="([^"]*)")?\s*></entity>',
        entity,
        body,
    )
    body = re.sub(
        r'<reagent\s+id="([^"]+)"\s*></reagent>',
        lambda match: reagent_card(match.group(1)),
        body,
    )
    body = re.sub(
        r'<tech-discipline\s+id="([^"]+)"\s*></tech-discipline>',
        lambda match: tech_table(match.group(1), technologies, locales),
        body,
    )
    return body


def render_pages(
    pages: list[dict[str, Any]],
    labels: dict[str, str],
    technologies: list[guidebook_source.Technology],
    locales: dict[str, str],
) -> tuple[list[dict[str, Any]], Any]:
    markdown = MarkdownIt("commonmark", {"html": True})
    markdown.enable("table")
    markdown.enable("strikethrough")
    rendered: list[dict[str, Any]] = []
    for index, page in enumerate(pages):
        if page.get("rendered"):
            content = page["body"]
        else:
            body = re.sub(r"^\s*# .+?\n+", "", page["body"], count=1)
            body = replace_embeds(body, labels, technologies, locales)
            body = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", body)
            content = markdown.render(body)
        rendered.append(
            {
                **page,
                "content": content,
                "text": plain_text(content),
                "summary": summary(content),
                "previous": pages[index - 1] if index else None,
                "next": pages[index + 1] if index + 1 < len(pages) else None,
            }
        )
    environment = Environment(
        loader=FileSystemLoader(TEMPLATE_ROOT),
        autoescape=select_autoescape(("html", "xhtml", "xml")),
    )
    return rendered, environment


def build_site(
    pages: list[dict[str, Any]],
    environment: Any,
    version: str,
    guide_tree: list[dict[str, Any]],
) -> None:
    if SITE_ROOT.exists():
        shutil.rmtree(SITE_ROOT)
    (SITE_ROOT / "assets").mkdir(parents=True)
    (SITE_ROOT / ".nojekyll").write_text("", encoding="utf-8")
    shutil.copy(TEMPLATE_ROOT / "style.css", SITE_ROOT / "assets" / "style.css")
    page_template = environment.get_template("page.html")
    for page in pages:
        output = page_template.render(
            **page,
            root="",
            guide_tree=guide_tree,
            version=version,
            page_id=page["id"],
        )
        (SITE_ROOT / page["url"]).write_text(output, encoding="utf-8")
    index = environment.get_template("index.html").render(
        guide_tree=guide_tree,
        version=version,
    )
    (SITE_ROOT / "index.html").write_text(index, encoding="utf-8")
    search_rows = [
        {
            "title": page["title"],
            "url": page["url"],
            "summary": page["summary"],
            "text": page["text"],
        }
        for page in pages
    ]
    search_js = (
        "window.GUIDEBOOK_SEARCH = "
        + json.dumps(
            search_rows,
            ensure_ascii=False,
            separators=(",", ":"),
        )
        + ";\n"
    )
    shutil.copy(TEMPLATE_ROOT / "search.js", SITE_ROOT / "assets" / "search.js")
    (SITE_ROOT / "assets" / "search-index.js").write_text(search_js, encoding="utf-8")
    search_path = SITE_ROOT / "assets" / "search.js"
    search_path.write_text(
        search_js + "\n" + search_path.read_text(encoding="utf-8"),
        encoding="utf-8",
    )


def epub_style() -> str:
    return """
body { font-family: serif; line-height: 1.65; color: #111; }
h1, h2, h3 { font-family: sans-serif; line-height: 1.25; }
h1 { page-break-before: always; }
a { color: #6b2c72; }
.entity-card { display: inline-block; margin: .25em .4em .25em 0; padding: .35em .55em; border: 1px solid #bbb; }
.entity-card strong, .entity-card small { display: block; }
.tech-table { width: 100%; border-collapse: collapse; font-size: .82em; }
.tech-table th, .tech-table td { padding: .25em; border-bottom: 1px solid #ccc; text-align: left; }
"""


def build_epub(
    pages: list[dict[str, Any]],
    environment: Any,
    version: str,
) -> None:
    page_template = environment.get_template("epub_page.xhtml")
    with zipfile.ZipFile(EPUB_PATH, "w") as archive:
        archive.writestr(
            "mimetype",
            "application/epub+zip",
            compress_type=zipfile.ZIP_STORED,
        )
        archive.writestr(
            "META-INF/container.xml",
            """<?xml version="1.0"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles>
</container>""",
        )
        archive.writestr("OEBPS/style.css", epub_style())
        nav_items = []
        manifest_items = []
        spine_items = []
        for page in pages:
            filename = page["url"].replace(".html", ".xhtml")
            content = (
                page["content"].replace('href="', 'href="').replace('.html"', '.xhtml"')
            )
            xhtml = page_template.render(title=page["title"], content=content)
            archive.writestr(f"OEBPS/{filename}", xhtml)
            manifest_items.append(
                f'<item id="{page["id"]}" href="{filename}" media-type="application/xhtml+xml"/>'
            )
            spine_items.append(f'<itemref idref="{page["id"]}"/>')
            nav_items.append(
                f'<li><a href="{filename}">{html.escape(page["title"])}</a></li>'
            )
        nav = (
            '<?xml version="1.0" encoding="utf-8"?>'
            '<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml" '
            'xmlns:epub="http://www.idpf.org/2007/ops" lang="zh-CN"><head>'
            '<title>目录</title><link rel="stylesheet" href="style.css"/>'
            '</head><body><nav epub:type="toc"><h1>Starlight 科学指南</h1><ol>'
            + "".join(nav_items)
            + "</ol></nav></body></html>"
        )
        archive.writestr("OEBPS/nav.xhtml", nav)
        opf = (
            '<?xml version="1.0" encoding="utf-8"?>'
            '<package xmlns="http://www.idpf.org/2007/opf" version="3.0" '
            'unique-identifier="bookid" xml:lang="zh-CN"><metadata '
            'xmlns:dc="http://purl.org/dc/elements/1.1/">'
            '<dc:identifier id="bookid">starlight-guidebook-science-zh</dc:identifier>'
            "<dc:title>Starlight 科学指南</dc:title><dc:language>zh-CN</dc:language>"
            f'<meta property="dcterms:source">Starlight {html.escape(version)}</meta>'
            "</metadata><manifest>"
            '<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>'
            '<item id="css" href="style.css" media-type="text/css"/>'
            + "".join(manifest_items)
            + "</manifest><spine>"
            + "".join(spine_items)
            + "</spine></package>"
        )
        archive.writestr("OEBPS/content.opf", opf)


def main() -> int:
    if not CONTENT_ROOT.exists():
        raise SystemExit(f"translated content directory not found: {CONTENT_ROOT}")
    pages = load_pages()
    labels = yaml.safe_load(ENTITY_LABELS.read_text(encoding="utf-8")) or {}
    with guidebook_source.open_content() as connection:
        version = guidebook_source.content_version(connection)
        locales = guidebook_source.locale_values(connection)
        technologies = guidebook_source.technologies(connection, locales)
        entries = guidebook_source.guide_entries(connection)
        word_counts = guidebook_source.guide_word_counts(
            connection,
            (entry.text for entry in entries),
        )
    tree = build_guide_tree(pages, entries, locales, word_counts)
    pages = order_pages_by_tree(pages, tree)
    rendered, environment = render_pages(pages, labels, technologies, locales)
    build_site(rendered, environment, version, tree)
    build_epub(rendered, environment, version)
    print(f"built {len(rendered)} pages for Starlight {version}")
    print(SITE_ROOT / "index.html")
    print(EPUB_PATH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
