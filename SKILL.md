---
name: game-cover-maker
description: Create high-attention Chinese game-sharing covers from a supplied screenshot/key art or from a newly generated clean game-style background. Use for 手游分享封面、Steam移植封面、PC+安卓封面、汉化版封面、DLC/存档/版本号封面、游戏推荐封面, or when the user wants bold white/yellow Chinese typography, thick black outlines, red/black brush panels, and multiple output sizes. Prefer image generation for artwork/background and deterministic Pillow rendering for exact Chinese text.
---

# Game Cover Maker

Create bold Chinese game-sharing covers in the visual language of busy game discovery feeds: dramatic game art, huge readable title, white/yellow emphasis, thick black outlines, red/black brush-stroke panels, and a strong bottom platform/CTA block.

The user's explicit wording, target size, and platform claims always take precedence over this skill.

## Core workflow

Use a two-stage workflow whenever possible:

1. **Create or prepare a clean background**
   - If the user supplied a screenshot, poster, key art, or local image, use it directly.
   - If the user did not supply artwork, generate a game-appropriate action background that matches the game's genre and mood.
   - When generating artwork, request **no text, no logos, no UI labels, no watermarks**. Leave useful negative space for title and feature blocks.
   - Do not imitate an official cover exactly. Create an original background with a similar genre/mood.
2. **Render all Chinese wording deterministically** with `scripts/render_cover.py`.
   - This keeps game names, DLC claims, version numbers, and platform labels exact.
   - Do not rely on image generation to spell important Chinese text when exact wording matters.

## Default visual hierarchy

Unless the user asks for another layout, use this order:

1. Top tag: `Steam移植游戏` / `中文汉化` / `安卓直装` / `完整版`
2. Giant game title: e.g. `重生细胞`
3. Feature callouts: up to 3 items, e.g. `解锁全部DLC`, `内置存档`
4. Optional version badge: e.g. `版本号 1.0.78`
5. Giant bottom emphasis: e.g. `PC+安卓`, `手游分享`, `中文完整版`

Visual rules:

- Game title: white, extra-bold, very large, heavy black stroke; optional red shadow/brush accent.
- Primary selling point: yellow with black stroke on a dark/black brush panel.
- Secondary selling point: white with black stroke on a dark panel.
- Version badge: smaller red/black brush strip, white/yellow text.
- Bottom emphasis: the strongest yellow element, very large, heavy black stroke, red brush backing.
- Keep important text inside safe margins and readable around 250 px preview width.
- Preserve the most recognizable character/scene area.
- Do not cover a face or central action subject if a small shift can avoid it.

## Copy rules

Use only claims provided by the user or clearly visible in supplied source material.

Do not invent:

- DLC status
- unlocked content
- save-file status
- MOD functionality
- version number
- platform availability
- ratings/download counts
- “破解/无限资源/全解锁” claims unless the user explicitly supplies them

Keep emphasized lines short. Prefer 4–10 Chinese characters per feature line. Do not turn cover copy into paragraphs.

## Output sizes

The renderer supports multiple generic game-cover shapes. Use the user's exact requested size when supplied.

### Built-in presets

| Preset | Pixels | Ratio | Typical use |
| --- | ---: | ---: | --- |
| `feed-4x5` | 1080×1350 | 4:5 | Default feed/game-share cover |
| `portrait-3x4` | 1080×1440 | 3:4 | Portrait game poster/card |
| `vertical-9x16` | 1080×1920 | 9:16 | Full-screen vertical cover |
| `square-1x1` | 1080×1080 | 1:1 | Square card/avatar-style cover |
| `landscape-16x9` | 1920×1080 | 16:9 | Standard horizontal thumbnail |
| `landscape-16x10` | 1600×1000 | 16:10 | Wide game card |

The preset names describe generic canvases, not guaranteed official upload requirements for any third-party platform.

### Custom size

For any other size, use:

```bash
--size WIDTHxHEIGHT
```

Example:

```bash
--size 1242x1660
```

`--size` overrides `--preset` and `--ratio`.

If the user asks for several sizes, render the same design in every requested size and check each one separately for text clipping and subject coverage. Do not simply stretch one finished image.

## Rendering examples

### Rich poster style

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

### 9:16 version

```bash
python scripts/render_cover.py background.png \
  --output reborn-cell-9x16.png \
  --title "重生细胞" \
  --tag "Steam移植游戏" \
  --feature "解锁全部DLC" \
  --feature "内置存档" \
  --version "1.0.78" \
  --accent "PC+安卓" \
  --preset vertical-9x16
```

### Exact custom dimensions

```bash
python scripts/render_cover.py background.png \
  --output custom-cover.png \
  --title "游戏名" \
  --tag "游戏分享" \
  --feature "中文完整版" \
  --accent "PC+安卓" \
  --size 1500x2000
```

### Backward-compatible ratio usage

```bash
--ratio 4:5
--ratio 3:4
--ratio 9:16
--ratio 1:1
--ratio 16:9
--ratio 16:10
```

## Background-generation guidance

When no usable game art is supplied, generate a clean background before rendering text.

The background prompt should describe:

- game genre: roguelike / action / RPG / strategy / casual / racing / survival, etc.
- dominant subject: protagonist, vehicle, monster, battlefield, city, dungeon, etc.
- atmosphere and palette appropriate to the game
- dramatic depth and lighting
- empty or calmer areas near the upper/title zone and left feature zone when possible
- **no text, no title, no Chinese/English words, no platform logos, no watermark**

For a dark action roguelike, a good composition is: central or lower-right protagonist, dark castle/dungeon environment, bright action lighting, upper area available for the title, left-middle space available for feature tags, bottom area with enough contrast for a giant platform label.

## Font behavior

The script searches common Chinese fonts on Windows/macOS/Linux, including Microsoft YaHei, SimHei, DengXian, PingFang, and Noto CJK. Never bundle or redistribute font files. If automatic detection fails, pass a local font path with `--font`.

## Quality gate

Before returning a cover, verify all of the following:

- exact Chinese wording matches the user's copy
- game name is unchanged
- version number is exact
- platform text is exact
- no text is clipped
- no important subject is hidden unnecessarily
- title remains readable at thumbnail size
- yellow emphasis is visually dominant
- black outline remains visible on bright and dark regions
- custom/multiple sizes were reflowed rather than stretched
- generated backgrounds contain no accidental text/logos that conflict with the deterministic overlay
- no unsupported claims were invented

Return the generated image file(s) directly. Keep commentary short unless the user asks for design analysis.