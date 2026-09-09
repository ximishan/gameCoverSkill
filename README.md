# game-cover-maker

Codex skill for quickly creating high-attention Chinese game-sharing covers.

It can automatically switch visual templates by game type instead of making every game use the same red/yellow layout. Current genre families:

`action` · `roguelike` · `shooter` · `rpg` · `strategy` · `casual` · `horror` · `racing` · `simulation` · `survival` · `anime` · `retro` · `general`

## Example

```bash
python scripts/render_cover.py background.png \
  --output cover.png \
  --title "重生细胞" \
  --tag "Steam移植游戏" \
  --feature "解锁全部DLC" \
  --feature "内置存档" \
  --version "1.0.78" \
  --accent "PC+安卓" \
  --genre auto \
  --preset feed-4x5
```

With `--genre auto`, the renderer attempts to infer a genre from the title/tag/features. A Codex agent using the Skill should normally infer the genre from the user's game/context and pass an explicit genre when it is clear.

## Sizes

Built-in presets:

- `feed-4x5` — 1080×1350
- `portrait-3x4` — 1080×1440
- `vertical-9x16` — 1080×1920
- `square-1x1` — 1080×1080
- `landscape-16x9` — 1920×1080
- `landscape-16x10` — 1600×1000

Custom exact size:

```bash
--size 1500x2000
```

See `SKILL.md` and `references/genre_templates.md` for the full workflow and template rules.