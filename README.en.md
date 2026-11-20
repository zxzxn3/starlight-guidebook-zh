# Starlight Guidebook Chinese

[中文](README.md)

An unofficial Chinese translation of the Starlight Space Station 14 Guidebook.

**The Chinese text in this project was translated by DeepSeek. The project maintainer is responsible for human proofreading, arrangement, and publishing.**

Online preview: <https://zxzxn3.github.io/starlight-guidebook-zh/>

## Current Progress

The contents preserve the complete Starlight Guidebook tree. All currently visible entries have been translated, covering 397 Chinese pages.

If upstream adds new entries, untranslated pages will show their source word count and link to a locally generated English page. Those pages preserve Guidebook internal links, entity references, tables, and visible rule markers.

Silicon lawsets, reagents, reaction recipes, microwave recipes, and deep-fryer recipes are generated from the client content cache during the build. Their names and text remain in English.

Covered content:

- The complete `How To Play SS14` subtree
- Translation conventions and the Chinese-English glossary
- Server rules, Metashield, and cross-round memory
- Reference tables for chemicals, drinks, food recipes, and writing formats
- General SOPs, alert levels, command, security, engineering, cargo, salvage, service, and medical SOPs
- Corporate law, the crime list, sentencing, trials, and special entity clauses
- Science overview, technology tree, and research procedures
- Anomalous research, A.P.E., and scanning equipment
- Xenoarchaeology, artifact nodes, and experiment procedures
- Robotics and cyborgs
- Starlight science SOP

All currently visible Guidebook entries have been translated. Future work mainly consists of following upstream Guidebook updates and maintaining terminology.

### Terminology

Game UI, item, device, job, and mechanic names are usually annotated with their English originals the first time they appear in the text. Entity cards that already show an English entity ID, repeated terms, and ordinary Chinese prose are not annotated individually.

## Viewing Locally

After cloning the repository, open `site/index.html` directly.

## Rebuilding

Requirements:

- Python 3.11 or later
- `zstd`
- A Starlight client installation and its content cache

Create an environment and install dependencies:

```fish
python -m venv .venv
source .venv/bin/activate.fish
python -m pip install -r requirements.txt
```

Build the site and EPUB:

```fish
python build_site.py
```

The build reads this path by default:

```text
~/.local/share/Space Station 14/launcher/content.db
```

Set `STARLIGHT_CONTENT_DB` to use another path:

```fish
set -x STARLIGHT_CONTENT_DB /path/to/content.db
```

Validate the generated output:

```fish
python verify.py
```

Extract the English source text again from the client content cache:

```fish
python guidebook_source.py
```

## Repository Layout

- `content/`: Chinese Markdown pages
- `data/`: Chinese entity labels
- `templates/`: HTML, CSS, and EPUB templates
- `guidebook_source.py`: reads client content, FTL, and technology data
- `build_site.py`: builds the static site, search index, and EPUB
- `verify.py`: validates links, search data, and EPUB structure
- `site/`: generated static site

## License and Attribution

- Build scripts and site code are licensed under the MIT License; see [LICENSE](LICENSE).
- The Chinese translations and text adapted from the upstream Guidebook are licensed under CC BY-SA 3.0; see [LICENSE-CONTENT.md](LICENSE-CONTENT.md).
- Upstream projects, copyright, and licensing details are listed in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

This project is not affiliated with or endorsed by Space Wizards Federation or Starlight.
