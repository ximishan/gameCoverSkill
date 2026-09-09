# game-cover-maker

Codex skill for quickly creating high-attention Chinese game-sharing covers.

It automatically switches visual templates by game type instead of making every game use the same red/yellow layout.

Current genre families:

`action` · `roguelike` · `shooter` · `rpg` · `strategy` · `grand-strategy` · `casual` · `horror` · `racing` · `simulation` · `survival` · `anime` · `retro` · `general`

## New: Grand Strategy

Paradox-style country/empire games now use a dedicated `grand-strategy` route instead of generic `strategy`.

Examples:

- 欧陆风云4
- 钢铁雄心4
- 十字军之王3
- 维多利亚3
- 群星

The template uses maps, rulers/generals/diplomats, fleets/armies, parchment, seals, navy blue and antique gold rather than an action-game explosion style.

The Skill also distinguishes **genre** from **presentation tags**. For example, `欧陆风云4` can route internally to `grand-strategy` while the top cover tag says `大型单机` for a mainstream audience.

See `references/game_taxonomy.md` for the distinction.

## Example

```bash
python scripts/render_cover.py background.png \
  --output eu4.png \
  --title "欧陆风云4" \
  --tag "大型单机" \
  --feature "解锁全部DLC" \
  --feature "完全汉化" \
  --version "11.0.78" \
  --accent "PC" \
  --genre auto \
  --preset feed-4x5
```

With `--genre auto`, `欧陆风云4` should be detected as `grand-strategy` before the broader `strategy` family.

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

See `SKILL.md`, `references/genre_templates.md`, and `references/game_taxonomy.md` for the full workflow and template rules.