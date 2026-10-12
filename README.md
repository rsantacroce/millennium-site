# Millennium: website

The website for [Millennium](https://github.com/rsantacroce/millennium), an online RPG set
around 1999–2003, written in Rust with Bevy.

**Live:** <https://rsantacroce.github.io/millennium-site/>

| Page | What's on it |
|---|---|
| [`index.html`](index.html) | The landing page: what the game is, screenshots, how to play, the tech |
| [`manual.html`](manual.html) | The player manual: installing, controls, your first day, skills, money, fighting, hacking, cars, houses, chat, hosting, troubleshooting |
| [`assets.html`](assets.html) | Everything in the game: zones, characters, objects, items, quests, shops, recipes, rivals, hacks, factions, cars, races, music, sounds and models |

Plain HTML and CSS (a Windows 2000 look, like the game's own UI), with a little JavaScript for the
taskbar clock and the asset search box. No build step except for the asset list.

## Updating the asset list

The tables on `assets.html` are generated from the game's own data, so they always match it.
With the game checked out next to this repository (`../world` by default):

```sh
python3 build.py              # or: python3 build.py path/to/millennium
```

This runs `cargo run -p shared --example catalog` in the game and drops its tables into
`assets.template.html`, writing `assets.html`. Edit the template, not `assets.html`, for anything
outside the generated tables (the music, sound and model sections are in the template).

## Screenshots

`images/` holds screenshots from the game itself (2560x1440 captures, resized to 1600 px JPEGs).

## Publishing

GitHub Pages serves the `main` branch as is (`.nojekyll` turns off Jekyll processing).
