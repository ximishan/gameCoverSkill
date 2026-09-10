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

If the user explicitly asks for a unified series identity, keep a shared design system but still allow subtle variation in badge placement, panel shape, or emphasis color.

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

6. **Text alignment / placement**
   - centered stack
   - upper-left title cluster
   - split left/right feature cards
   - title high + feature badges mid-frame
   - title mid-frame + small top tag

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
- neighboring covers do not reuse the same title fill + tag shape + feature-card colors + CTA treatment
- title remains readable at thumbnail size
- text colors fit the game's actual art direction
- decorative typography does not hide important characters or scene elements
- no extra accent/banner was invented when the user did not provide one
- the batch feels related, but not copy-pasted
