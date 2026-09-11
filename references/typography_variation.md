# Typography & Text-Style Variation

This reference controls how titles, tags, feature badges, version labels, accent text, and the fixed swipe cue behave across game covers.

The goal is to avoid a batch where every image has the same red tag, the same title fill, the same yellow feature strip, and the same bottom banner even though the backgrounds are different.

## Core principle

**Keep the copy exact; vary the presentation.**

Text content must stay exactly as supplied by the user, but the visual treatment may change between covers when the user requests multiple images.

For known games, text styling should support the game's visual identity rather than overwrite it.

## Default behavior

When requested count >= 2:

- automatically enable **text-style diversity** together with scene diversity
- keep all wording identical across the batch unless the user explicitly requests different copy
- vary at least 3 text-design dimensions between neighboring covers
- do not force every text element to use the same color family
- do not force a large bottom banner when the user did not supply an accent/CTA
- keep the main title's **layout top anchor fixed at exactly 35% of canvas height** across all batch members
- keep the fixed swipe cue **“佑滑自取” + right arrow** at the same ~75% vertical position on every cover

If the user explicitly asks for a unified series identity, keep a shared design system but still allow subtle variation in badge placement, panel shape, or emphasis color.

## Fixed title coordinate

**The main title vertical coordinate is a hard layout constraint, not a style suggestion.**

Default rules:

- **All ratios:** the main game title layout top anchor is exactly `y = 0.35 × canvas height` unless the user explicitly requests a different title height.
- On a 1080×1920 `9:16` canvas, this resolves to about **Y=672**, which matches a CapCut target around **Y=670**.
- Font metrics, antialiasing, outline, or shadow may visually extend a few pixels around the 35% anchor, but the underlying title layout coordinate must remain unchanged.
- Batch diversity, genre templates, tag height, long copy, or feature-card layout must never alter the 35% title anchor.
- `9:16`: no essential top tag, outline, shadow, sticker, or text panel may enter the top **9%** of the canvas.
- `9:16`: when a top tag exists, place it around **9–11%** height; the artwork gap between the tag and the fixed 35% title anchor is intentional.
- `4:5` / `3:4`: keep top tags and auxiliary top labels below the top **6%** unsafe zone; the main title still begins at exactly 35%.
- square / landscape: keep at least **4%** top breathing room for auxiliary top labels; the main title still begins at exactly 35%.
- keep left/right text edges at least **4–5%** inside the canvas, including stroke, shadow, and panel decoration.
- measure the full visible text bounds, including outline, drop shadow, stickers, ribbons, and panels—not only the font baseline.

When title copy is long, resolve overflow in this order:

1. wrap/reflow the title
2. reduce font size slightly
3. tighten title line spacing if needed
4. move supporting feature/version copy lower or reflow it above the fixed swipe cue
5. simplify decorative panels

Do **not** solve overflow by changing the title's 35% vertical anchor.

## Fixed swipe cue at 75%

Every default cover includes a fixed swipe/self-service cue inspired by the supplied reference image.

Hard rules:

- the literal text is **`佑滑自取`**
- preserve those four characters exactly; **do not autocorrect `佑` to `右`**
- the cue's visual center sits at approximately `y = 0.75 × canvas height`
- the text uses **very bold white characters with a thick black outline and black drop shadow**, similar to the reference image
- a **large bright red arrow pointing right** sits immediately to the right of the text
- the arrow also has a black outer outline so it remains visible over busy game footage/artwork
- keep the cue fully inside the canvas with comfortable left/right margins
- the cue is a fixed system element, not a user-supplied `accent`
- if the user does not provide an `accent`, omit the optional large bottom accent panel but **still keep `佑滑自取` + the right arrow**
- batch diversity may not remove this cue, change its wording, flip the arrow, or materially change its ~75% vertical position

For a 1080×1920 `9:16` canvas, the cue center is around **Y=1440**. For a 1080×1440 `3:4` canvas, the cue center is around **Y=1080**.

Keep feature/version cards above this fixed cue whenever possible. If supporting copy would collide with it, shrink/reflow the supporting copy rather than moving the fixed cue away from 75%.

## Deterministic rendering requirement

When the user expects exact title placement, exact Chinese copy, or the fixed swipe cue, the normal production path is:

1. generate or prepare the game artwork/background **without the main title or promotional text**
2. render the final main title, supporting copy, and fixed swipe cue with `scripts/render_cover.py`
3. verify the title layout top anchor equals `0.35 × canvas height`
4. verify the `佑滑自取` cue is centered around `0.75 × canvas height` and points right

Do not rely on a generative image model to satisfy exact 35% / 75% coordinates. Direct image-generation typography is only acceptable when the user explicitly asks for all text to be generated inside the image; in that case, placement can only be approximate and must not be described as pixel-exact.

## Variation dimensions

Vary any combination of:

1. **Title treatment**
   - solid white + dark outline
   - game-palette multicolor title
   - gold/metallic title for historical/strategy titles
   - two-tone title
   - light title with colored drop-shadow
   - title on a ribbon/plaque
   - title without a panel, using outline + shadow only

2. **Tag treatment**
   - speech-bubble tag
   - pill badge
   - corner sticker
   - ribbon tab
   - framed plaque
   - small floating label

3. **Feature-card treatment**
   - one long strip
   - two compact chips
   - stacked cards
   - icon + text pill
   - sticker cards attached to the scene edge
   - minimal text with only an outline/shadow and no filled panel

4. **Version treatment**
   - compact corner badge
   - small capsule below features
   - tiny footer tab
   - side label
   - neutral monochrome badge

5. **Color role assignment**
   - do not repeat the same mapping on every image
   - e.g. one cover may use pink tag + yellow feature card; another may use blue tag + cream feature card; another may use mint tag + coral feature card
   - keep colors compatible with the game's palette

6. **Text alignment / horizontal placement**
   - centered title stack at the fixed 35% vertical anchor
   - left-aligned title cluster at the fixed 35% vertical anchor
   - split left/right feature cards below the title
   - centered title with asymmetric supporting badges
   - horizontally offset title while preserving the exact same vertical anchor

7. **Emphasis method**
   - size
   - color
   - outline thickness
   - shadow
   - panel contrast
   - decorative icon

Vertical main-title placement and the fixed `佑滑自取` cue are **not** variation dimensions.

Do not vary all dimensions randomly. The design should still feel intentional.

## Batch rule

For a batch of 4, a good default is:

- Cover A — strongest brand/game-color title; simple tag; one long feature strip
- Cover B — white or light title with colored outline; pill tag; compact feature chips
- Cover C — two-tone or gradient title; corner tag; asymmetric feature cards
- Cover D — cleaner/minimal title; small floating badges; more of the background remains visible

The four covers should still belong to one series, but should not look like the same text layer pasted over four different backgrounds.

The main title's layout top coordinate remains exactly `0.35 × canvas height` across the whole batch. Variation may move the title left/right or change alignment/treatment, but must not change its vertical anchor unless the user explicitly requests another height.

The fixed `佑滑自取` + right-arrow cue stays at approximately `0.75 × canvas height` on every batch member.

## Known-game identity rule

For existing games, derive text colors and shapes from:

1. the game's established visual palette and UI language
2. the supplied screenshot/reference
3. the genre template

Do not use the same generic red/yellow/white system for every title.

Examples:

- cozy-life-sim: pastel pink / sky blue / mint / warm yellow / cream, rounded badges, playful sticker shapes
- historical strategy: navy / parchment / gold / burgundy, framed plaques, restrained ornamental accents
- horror: off-white / charcoal / dark red, distressed or minimal panels
- racing: white / cyan / orange, slanted labels and speed-line geometry
- retro/pixel: cream / neon cyan / magenta / purple with pixel-block shapes

## Cozy-life-sim example

For four `米加小镇` covers, do not use this exact overlay four times:

- red `手机直装` speech bubble
- rainbow game title
- yellow feature strip
- green `自带菜单` badge
- red bottom banner

Instead rotate the text system while preserving the game's playful identity:

1. rainbow title + pink tag + cream/yellow feature strip
2. white title with pink/blue outline + mint tag + small peach feature cards
3. pink/blue two-tone title + yellow corner sticker + blue version/menu chip
4. cleaner white title + colored shadow + several small pastel stickers instead of one giant feature bar

For `9:16`, keep the tag near 9–11% height and keep all four main-title layout anchors at exactly **35%**. Do not pack the typography stack against the top edge.

On every cover, retain the fixed `佑滑自取` + red right-arrow cue around 75% height.

If no `accent` is supplied, do **not** invent or duplicate a separate bottom CTA just to fill space. The fixed swipe cue is the only default lower CTA.

## Exact-copy rule

Typography diversity must never alter the copy.

Do not:

- rewrite `无广版` as `无广告版`
- turn `自带菜单` into `内置菜单`
- change fixed `佑滑自取` to `右滑自取`
- merge two supplied features into one sentence
- split a version number incorrectly
- invent an extra slogan, rating, download count, platform, or feature

If exact copy matters, generate clean artwork/background and use deterministic text rendering afterward.

## Quality gate

Before returning a cover or multi-cover batch, verify:

- the text content is exact on every cover
- no title, tag, badge, outline, shadow, arrow, or panel is clipped by the top/left/right canvas edge
- the main title layout top anchor equals exactly `0.35 × canvas height` on every default-layout cover
- glyph/stroke/shadow pixels may extend around the anchor, but no layout rule has moved the title vertically
- batch variation changes styling/horizontal placement without changing title height
- top-tag height does not push the main title down
- the fixed `佑滑自取` cue is present and centered around ~75% of canvas height
- the cue uses white text + thick black outline/shadow and a red arrow pointing right
- feature/version cards do not collide with the fixed swipe cue
- the upper portion of the cover remains available for artwork/background and the small top tag
- deterministic text rendering is used whenever exact 35% / 75% placement is required
- neighboring covers do not reuse the same title fill + tag shape + feature-card colors + optional accent treatment
- title remains readable at thumbnail size
- text colors fit the game's actual art direction
- decorative typography does not hide important characters or scene elements
- no extra optional accent/banner was invented when the user did not provide one
- the batch feels related, but not copy-pasted
