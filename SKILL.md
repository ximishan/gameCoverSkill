---
name: game-cover-maker
description: Create high-attention Chinese game-sharing covers from supplied screenshots/key art or newly generated clean game backgrounds. Automatically infer the game's genre and switch cover templates for action/roguelike/shooter/RPG/strategy/casual/horror/racing/simulation/survival/anime/retro games. Supports exact Chinese text, DLC/save/version/platform callouts, and multiple output sizes. Prefer image generation for clean artwork/background and deterministic Pillow rendering for final Chinese text.
---

# Game Cover Maker

Create bold Chinese game-sharing covers for discovery feeds and short-video platforms. The skill should not make every game look the same: it must route each game to a genre-appropriate background treatment and overlay template while keeping the wording exact and readable at thumbnail size.

The user's explicit wording, target size, genre/style override, and platform claims always take precedence.

## Core workflow

Use a two-stage workflow whenever possible:

1. **Determine game type and template**
   - Infer genre from the user's description, game name, screenshots, or known game context.
   - Default to automatic routing; do not ask the user to choose a style when the genre is reasonably clear.
   - If the genre is genuinely ambiguous, use `general` rather than blocking the task.
   - The renderer also supports `--genre auto` as a fallback keyword detector.
2. **Create or prepare a clean background**
   - If the user supplied a screenshot, poster, key art, or local image, use it directly when suitable.
   - If no usable artwork is supplied, generate a new original background matching the detected genre.
   - Generated backgrounds must contain **no text, no title, no platform logo, no UI label, no watermark**.
   - Leave negative space for the title, feature blocks, and bottom platform/CTA area.
   - Do not imitate an official cover exactly; create an original scene with the same genre/mood.
3. **Render exact copy deterministically** with `scripts/render_cover.py`.
   - Chinese game names, DLC wording, version numbers, and platform labels must be exact.
   - Do not rely on image generation to spell important Chinese text.
4. **Quality-check each requested size independently**.
   - Reflow text and crop the source separately for each aspect ratio.
   - Never stretch one finished cover into another size.

## Automatic genre routing

Use the closest genre family below. Detailed design/background guidance lives in `references/genre_templates.md`.

| Genre | Renderer value | Template behavior |
| --- | --- | --- |
| 动作 | `action` | 红黑冲击、笔刷块、强攻击感 |
| Roguelike / 肉鸽 | `roguelike` | 深红黑、地牢感、危险氛围 |
| 射击 | `shooter` | 橙黑战术、斜切面板、速度/火力感 |
| RPG / ARPG | `rpg` | 深蓝紫 + 金色、史诗框体 |
| 策略 / SLG / 塔防 | `strategy` | 海军蓝 + 金色、指挥/战役感 |
| 休闲 / 益智 / 卡牌 | `casual` | 高亮蓝橙、圆角卡片、轻松清晰 |
| 恐怖 / 惊悚 | `horror` | 低饱和黑红、压迫感、血色强调 |
| 赛车 / 竞速 | `racing` | 青橙霓虹、斜切面板、极速感 |
| 模拟 / 经营 / 建造 | `simulation` | 青绿、圆角、干净现代 |
| 生存 / 末日 | `survival` | 橄榄/土黄、粗粝笔刷、荒野感 |
| 二次元 / 动漫 | `anime` | 粉紫 + 青色霓虹、圆角/高饱和 |
| 像素 / 复古 | `retro` | 紫粉/青色、像素块面板 |
| 未识别 | `general` | 通用高冲击黄白黑红模板 |

### Auto-routing rules

- If the user explicitly says a genre, pass it with `--genre`.
- If the genre is obvious from the game name/context, pass the inferred genre explicitly.
- Otherwise use `--genre auto`; the script checks keywords in title/tag/features.
- A user style request such as “不要红黑，做成清爽卡通风” overrides the genre default.

Example: `重生细胞` should route to `roguelike`; a colorful puzzle/card game should route to `casual`; a dark survival horror game should route to `horror` or `survival` depending on the main selling point.

## Default copy hierarchy

Unless the user asks for another arrangement:

1. Top tag: `Steam移植游戏` / `中文汉化` / `安卓直装` / `完整版`
2. Giant game title
3. Up to 3 feature callouts, e.g. `解锁全部DLC`, `内置存档`
4. Optional version badge, e.g. `版本号 1.0.78`
5. Giant bottom emphasis: `PC+安卓`, `手游分享`, `中文完整版`

Use only claims provided by the user or clearly visible in supplied source material. Do not invent DLC status, unlocked content, save status, MOD functions, version numbers, platform availability, ratings, or download counts.

Keep feature lines short. Prefer 4–10 Chinese characters per emphasized line. Do not put paragraphs on the cover.

## Output sizes

Use the user's exact requested size when supplied.

| Preset | Pixels | Ratio | Typical use |
| --- | ---: | ---: | --- |
| `feed-4x5` | 1080×1350 | 4:5 | Default feed/game-share cover |
| `portrait-3x4` | 1080×1440 | 3:4 | Portrait poster/card |
| `vertical-9x16` | 1080×1920 | 9:16 | Full-screen vertical cover |
| `square-1x1` | 1080×1080 | 1:1 | Square card |
| `landscape-16x9` | 1920×1080 | 16:9 | Standard horizontal thumbnail |
| `landscape-16x10` | 1600×1000 | 16:10 | Wide game card |

For any other size:

```bash
--size WIDTHxHEIGHT
```

Example: `--size 1242x1660`.

## Rendering examples

### Automatic genre template

```bash
python scripts/render_cover.py background.png \
  --output reborn-cell.png \
  --title "重生细胞" \
  --tag "Steam移植游戏" \
  --feature "解锁全部DLC" \
  --feature "内置存档" \
  --version "1.0.78" \
  --accent "PC+安卓" \
  --genre auto \
  --preset feed-4x5
```

`重生细胞` is recognized as `roguelike`, so the renderer chooses the corresponding darker impact template.

### Explicit genre override

```bash
python scripts/render_cover.py background.png \
  --output anime-cover.png \
  --title "超忍机" \
  --tag "二次元动作" \
  --feature "中文完整版" \
  --feature "内置存档" \
  --accent "安卓直装" \
  --genre anime \
  --preset feed-4x5
```

### Several sizes

Render each output separately:

```bash
--preset feed-4x5
--preset portrait-3x4
--preset vertical-9x16
--preset landscape-16x9
```

Do not resize the already-rendered result.

## Background-generation guidance

When no usable art is supplied, generate the background first. Always align the artwork with the detected genre. Read `references/genre_templates.md` for concrete prompt fragments.

General requirements:

- one recognizable main subject or scene
- strong depth and lighting
- calmer/emptier upper zone for title
- some left-middle breathing room for feature callouts
- enough bottom contrast for the final platform/CTA block
- no text, logos, UI, watermark, fake rating badges, or fake storefront marks

## Font behavior

The renderer searches common Chinese fonts on Windows/macOS/Linux, including Microsoft YaHei, SimHei, DengXian, PingFang, and Noto CJK. Never bundle or redistribute font files. If automatic detection fails, pass a local font path with `--font`.

## Quality gate

Before returning a cover, verify:

- detected genre/template is sensible for the game
- background mood matches that genre
- exact Chinese wording matches the user's copy
- game name, version, and platform text are unchanged
- no unsupported claims were invented
- no text is clipped
- no important subject is hidden unnecessarily
- title remains readable at about 250 px preview width
- template colors/shapes are visibly different across different game genres
- each requested output size was reflowed rather than stretched
- generated backgrounds contain no accidental text/logos that conflict with the deterministic overlay

Return the generated image file(s) directly. Keep commentary short unless the user asks for design analysis.