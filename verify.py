#!/usr/bin/env python3
"""Verify generated HTML, search data, and EPUB structure."""

from __future__ import annotations

import json
import re
import zipfile
from pathlib import Path, PurePosixPath
from xml.etree import ElementTree

PROJECT_ROOT = Path(__file__).resolve().parent
SITE_ROOT = PROJECT_ROOT / "site"
EPUB_PATH = PROJECT_ROOT / "starlight-guidebook-science-zh.epub"
RAW_MARKERS = (
    "<entity ",
    "<reagent ",
    "<reagent-group ",
    "<microwave-group ",
    "<deep-fryer-group ",
    "<lawset-list",
    "<tech-discipline ",
    "动态试剂组：",
    "动态微波炉配方组：",
    "动态油炸锅配方组：",
    "动态法则组列表",
    "**",
)


def check_site() -> int:
    pages = list(SITE_ROOT.rglob("*.html"))
    if not pages:
        raise AssertionError("no generated HTML pages")
    index_source = (SITE_ROOT / "index.html").read_text(encoding="utf-8")
    if "（未翻译，约 " not in index_source:
        raise AssertionError("index does not list untranslated Guidebook entries")
    if "已译" in index_source or "未译 " in index_source:
        raise AssertionError("index still displays translated/untranslated counts")
    for obsolete in ("计划排除", "未翻译内容", "其他部门 SOP"):
        if obsolete in index_source:
            raise AssertionError(f"index contains obsolete category {obsolete!r}")
    dynamic_pages = {
        "lawsets.html": "lawset-card",
        "chemical-elements.html": "reagent-card",
        "food-pizza.html": "recipe-card",
        "food-deep-fried.html": "recipe-card",
    }
    for filename, marker in dynamic_pages.items():
        source = (SITE_ROOT / filename).read_text(encoding="utf-8")
        if marker not in source:
            raise AssertionError(f"{filename} does not contain generated {marker}")
    failures: list[str] = []
    for page in pages:
        source = page.read_text(encoding="utf-8")
        for marker in RAW_MARKERS:
            if marker in source:
                failures.append(f"{page.name}: unrendered marker {marker!r}")
        for href in re.findall(r'href="([^"]+)"', source):
            if href.startswith(("http:", "https:", "#", "mailto:")):
                continue
            target = (page.parent / href.split("#", 1)[0]).resolve()
            if not target.exists():
                failures.append(f"{page.name}: missing link {href}")
    if failures:
        raise AssertionError("\n".join(failures))
    return len(pages)


def check_search() -> int:
    search_source = (SITE_ROOT / "assets" / "search.js").read_text(encoding="utf-8")
    prefix = "window.GUIDEBOOK_SEARCH = "
    start = search_source.index(prefix) + len(prefix)
    end = search_source.index(";\n", start)
    rows = json.loads(search_source[start:end])
    if not rows:
        raise AssertionError("search index is empty")
    return len(rows)


def check_epub() -> int:
    failures: list[str] = []
    with zipfile.ZipFile(EPUB_PATH) as archive:
        names = archive.namelist()
        if not names or names[0] != "mimetype":
            failures.append("mimetype is not the first EPUB entry")
        if archive.getinfo("mimetype").compress_type != zipfile.ZIP_STORED:
            failures.append("mimetype must be uncompressed")
        xml_documents: list[tuple[str, ElementTree.Element]] = []
        for name in names:
            if not name.endswith((".xml", ".xhtml", ".opf")):
                continue
            try:
                document = ElementTree.fromstring(archive.read(name))
            except ElementTree.ParseError as error:
                failures.append(f"{name}: {error}")
                continue
            xml_documents.append((name, document))
        for name, document in xml_documents:
            for element in document.iter():
                href = element.attrib.get("href")
                if not href or href.startswith(("http:", "https:", "#")):
                    continue
                target = str(PurePosixPath(name).parent / href.split("#", 1)[0])
                if target not in names:
                    failures.append(f"{name}: missing EPUB target {target}")
    if failures:
        raise AssertionError("\n".join(failures))
    return len(xml_documents)


def main() -> int:
    page_count = check_site()
    search_count = check_search()
    epub_count = check_epub()
    print(f"HTML pages: {page_count}")
    print(f"search entries: {search_count}")
    print(f"EPUB XML documents: {epub_count}")
    print("verification passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
