#!/usr/bin/env python3
"""Builds assets.html: the game's catalog tables dropped into assets.template.html.

    python3 build.py [path/to/millennium]   (default: ../world)

The tables come from the game itself (`cargo run -p shared --example catalog`), so run this
whenever the game's content changes.
"""
import pathlib
import subprocess
import sys

here = pathlib.Path(__file__).resolve().parent
game = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else here.parent / "world").resolve()
catalog = subprocess.run(
    ["cargo", "run", "--quiet", "-p", "shared", "--example", "catalog"],
    cwd=game, check=True, capture_output=True, text=True,
).stdout
template = (here / "assets.template.html").read_text()
assert "<!-- CATALOG -->" in template
(here / "assets.html").write_text(template.replace("<!-- CATALOG -->", catalog.rstrip()))
print(f"assets.html: {catalog.count('<tr>')} table rows from {game}")
