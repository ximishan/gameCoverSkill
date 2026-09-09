# game-cover-maker

Codex skill for quickly generating eye-catching Chinese game-sharing covers.

The recommended workflow is now:

1. Use an existing game screenshot/key art, or generate a clean game-style background with no text.
2. Use `scripts/render_cover.py` to render exact Chinese wording, feature callouts, version number, and platform text.
3. Export one or more requested sizes without stretching the finished design.

## Example

```bash
python scripts/render_cover.py background.png \
  --output reborn-cell.png \
  --title "重生细胞" \
  --tag "Steam移植游戏" \
  --feature "解锁全部DLC" \
  --feature "内置存档" \
  --version "1.0.78" \
  --accent "PC+安卓" \
  --preset feed-4x5
```

## Built-in sizes

| Preset | Size | Ratio |
| --- | ---: | ---: |
| `feed-4x5` | 1080×1350 | 4:5 |
| `portrait-3x4` | 1080×1440 | 3:4 |
| `vertical-9x16` | 1080×1920 | 9:16 |
| `square-1x1` | 1080×1080 | 1:1 |
| `landscape-16x9` | 1920×1080 | 16:9 |
| `landscape-16x10` | 1600×1000 | 16:10 |

These are generic game-cover canvases rather than guaranteed official third-party platform requirements.

For any exact size:

```bash
--size 1242x1660
```

`--size` overrides preset/ratio settings.

The old ratio syntax is still supported:

```bash
--ratio 4:5
--ratio 3:4
--ratio 9:16
--ratio 1:1
--ratio 16:9
--ratio 16:10
```

## Cover fields

- `--tag`: top label, such as `Steam移植游戏`
- `--title`: game name
- `--feature`: selling point; repeat up to 3 times
- `--version`: version number
- `--accent`: giant bottom label, such as `PC+安卓`

The script uses local Chinese fonts and Pillow so important wording is rendered deterministically instead of depending on AI-generated text.

Install as a personal Codex skill by placing this project in your Codex skills directory, or keep it as a repo-local skill according to your Codex setup.
