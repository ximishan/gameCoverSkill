---
name: game-cover-maker
description: Create high-attention Chinese game-sharing cover images from a supplied game screenshot, key art, poster, or local image path. Use when the user asks for 手游分享封面、游戏封面、汉化版封面、Steam移植封面、安卓游戏分享图、游戏推荐封面, or wants a bold Chinese thumbnail with large white/yellow text, black outlines, strong contrast, and a 4:5 feed layout. Prefer deterministic text rendering with the bundled Pillow script so Chinese titles are accurate and readable.
---

# Game Cover Maker

Create a bold, high-CTR Chinese game-sharing cover from an existing game image. The visual language should feel like a busy mobile-game discovery feed: recognizable game art, huge readable words, white/yellow emphasis, thick black outlines, and very little small text.

The user's explicit instructions always take precedence over this skill.

## Default output

Unless the user specifies otherwise:

- Canvas: 1080×1350 (4:5)
- Input: use the supplied screenshot/key art as the background; do not redraw game characters with AI
- Text blocks: 2–3 only
- Primary title: white, extra-bold, black stroke
- Main selling point / CTA: yellow, extra-bold, black stroke
- Optional small tag: white or yellow on a dark rounded rectangle
- Bottom area: add a dark gradient behind text for readability
- Output: PNG
- Generate one final cover; generate 3 variants only when the user asks for multiple versions

## Copy hierarchy

Keep the cover readable at thumbnail size. Prefer this order:

1. Optional tag: `Steam移植` / `中文汉化` / `安卓直装` / `完整版` / `新游`
2. Game name or one sharp selling point
3. Large yellow CTA or version label: `手游分享` / `中文汉化版` / `完整版` / `至尊合集`

Do not put paragraphs on the cover. Prefer 4–8 Chinese characters per emphasized line. Avoid more than 12 Chinese characters on one line.

If the user only gives a game name and image, infer a conservative copy set:

- top tag: `游戏分享`
- main title: the game name
- bottom emphasis: `手游分享`

If the user mentions 汉化、移植、Steam、安卓、完整版、MOD、合集, use only claims the user supplied. Do not invent edition/version claims.

## Composition rules

- Preserve the most recognizable game character/logo area.
- Prefer a center-crop that fills the canvas.
- Use a subtle darkening pass on the background so large text wins visually.
- Use a black text stroke thick enough to remain readable on bright art.
- Make the yellow phrase the strongest visual anchor.
- Use no more than two font sizes in the main text system plus one small tag size.
- Keep all important text inside 6% side margins and 5% top/bottom margins.
- Do not cover a face when a small vertical shift can avoid it.
- Do not add unrelated icons, fake platform logos, fake ratings, download counts, or false claims.

## Rendering workflow

Use `scripts/render_cover.py` whenever a local or mounted input image is available. Deterministic Pillow rendering is preferred over image generation because Chinese text must be exact.

Run from the skill directory:

```bash
python scripts/render_cover.py INPUT_IMAGE \
  --output OUTPUT.png \
  --title "游戏名" \
  --tag "中文汉化" \
  --accent "手游分享"
```

Useful options:

```bash
--ratio 4:5        # default; also supports 3:4, 9:16, 1:1, 16:9
--position bottom  # bottom | center | split
--font PATH        # optional explicit Chinese bold font
--no-darken        # keep original image brightness
--no-gradient      # disable bottom readability gradient
```

If the user asks for three variants, render:

```bash
python scripts/render_cover.py INPUT --output cover-classic.png --title "..." --tag "..." --accent "..." --position bottom
python scripts/render_cover.py INPUT --output cover-center.png  --title "..." --tag "..." --accent "..." --position center
python scripts/render_cover.py INPUT --output cover-split.png   --title "..." --tag "..." --accent "..." --position split
```

## Text layout guidance

### `bottom` — default
Best for character/key-art backgrounds. Small tag near top, title above the bottom third, yellow CTA at the bottom.

### `center`
Best when the background has empty space in the middle or the game logo sits near the top.

### `split`
Best when the art has a subject on one side. Put the title in the upper third and the yellow CTA in the lower third.

## Font behavior

The script automatically searches common Chinese fonts on Windows/macOS/Linux, including Microsoft YaHei, SimHei, DengXian, PingFang, and Noto Sans CJK. Never bundle or redistribute font files. If automatic detection fails, ask the user for a local font path or pass `--font`.

## Quality gate

Before presenting the result, verify:

- exact Chinese wording is correct
- game name is not accidentally changed
- no text is clipped
- yellow emphasis is clearly the largest/strongest element
- black outline is visible around white/yellow text
- the cover still reads when visually reduced to about 250 px wide
- no unsupported claims were invented

Return the generated file(s) directly. Keep commentary short unless the user asks for design analysis.
