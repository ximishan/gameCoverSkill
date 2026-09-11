# Typography & Text-Style Variation

This reference controls how titles, tags, feature badges, version labels, and accent text vary across game covers.

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
- keep the main title's **vertical top anchor fixed around 40% of canvas height** across all batch members

If the user explicitly asks for a unified series identity, keep a shared design system but still allow subtle variation in badge placement, panel shape, or emphasis color.

## Text safe area

**Text visibility overrides decorative placement and batch variation.** Never push title/tag text toward the top edge just to create a different composition.

The main title follows a fixed vertical-anchor rule unless the user explicitly overrides it.

Default safe-area rules:

- **All ratios:** the main game title should begin at approximately **40% of canvas height from the top**
- **All ratios:** treat `y = 0.40 × canvas height` as the default top anchor for the first title line
- allow only small optical correction for stroke/shadow, normally within about **38–42%** of canvas height
- do not move the title above **38%** merely to fit more supporting copy or to create batch variation
- `9:16`: no essential top tag, outline, shadow, sticker, or text panel may enter the top **9%** of the canvas
- `9:16`: when a top tag exists, place the tag around **9–11%** height; the large artwork gap between the tag and the 40% title anchor is intentional
- `4:5` / `3:4`: keep top tags and auxiliary top labels below the top **6%** unsafe zone, while the main title still remains anchored around 40%
- square / landscape: keep at least **4%** top breathing room for any auxiliary top label, while the main title still remains anchored around 40%
- keep left/right text edges at least **4–5%** inside the canvas, including stroke, shadow, and panel decoration
- measure the full visible text bounds, including outline, drop shadow, stickers, ribbons, and panels—not only the font baseline

When text is long, resolve overflow in this order:

1. wrap/reflow the title
2. reduce font size slightly
3. tighten title line spacing if needed
4. move supporting feature/version copy lower
5. simplify decorative panels

Do **not** solve overflow by moving the title upward from the 40% anchor.

For direct image-generation typography, explicitly describe the main title as **starting around the 40% vertical position**, fully inside frame, with the upper portion of the image left primarily for artwork/background and any small top tag. If the title drifts high, treat the cover as failed and regenerate/fix it.

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
   - centered title stack at the 40% vertical anchor
   - left-aligned title cluster whose top still begins around 40%
   - split left/right feature cards below the title
   - centered title with asymmetric supporting badges
   - horizontally offset title while preserving the same vertical anchor

7. **Emphasis method**
   - size
   - color
   - outline thickness
   - shadow
   - panel contrast
   - decorative icon

Do not vary all dimensions randomly. The design should still feel intentional.

## Batch rule

For a batch of 4, a good default is:

- Cover A — strongest brand/game-color title; simple tag; one long feature strip
- Cover B — white or light title with colored outline; pill tag; compact feature chips
- Cover C — two-tone or gradient title; corner tag; asymmetric feature cards
- Cover D — cleaner/minimal title; small floating badges; more of the background remains visible

The four covers should still belong to one series, but should not look like the same text layer pasted over four different backgrounds.

The main title height remains fixed across the whole batch. Variation may move the title left/right or change alignment/treatment, but must keep its top edge around the **40% vertical line** unless the user explicitly requests another height.

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

For `9:16`, keep the tag near 9–11% height and keep all four main titles anchored around **40%**. Do not pack the whole typography stack against the top edge.

If no `accent` is supplied, do **not** invent or duplicate a bottom CTA just to fill space. Let the artwork breathe.

## Exact-copy rule

Typography diversity must never alter the copy.

Do not:

- rewrite `无广版` as `无广告版`
- turn `自带菜单` into `内置菜单`
- merge two supplied features into one sentence
- split a version number incorrectly
- invent an extra slogan, rating, download count, platform, or feature

If image generation cannot reliably spell important text, generate clean artwork/background and use deterministic text rendering afterward.

## Quality gate

Before returning a multi-cover batch, verify:

- the text content is exact on every cover
- no title, tag, badge, outline, shadow, or panel is clipped by the top/left/right canvas edge
- the main title starts around the intended **40% vertical position** on every cover
- the title's first visible pixels normally remain within about **38–42%** unless the user explicitly requests another height
- batch variation changes styling/horizontal placement without raising the title
- the upper portion of the cover remains available for artwork/background and the small top tag
- neighboring covers do not reuse the same title fill + tag shape + feature-card colors + CTA treatment
- title remains readable at thumbnail size
- text colors fit the game's actual art direction
- decorative typography does not hide important characters or scene elements
- no extra accent/banner was invented when the user did not provide one
- the batch feels related, but not copy-pasted