# Genre Template Reference

This file defines the visual families used by `game-cover-maker`. Genre determines the broad cover system, but for known games the real game's identity must remain recognizable. Always combine this file with `references/game_identity.md`.

For multi-image requests, also combine these rules with `references/batch_variation.md` and `references/typography_variation.md`. A genre defines a **palette family and design language**, not one fixed color mapping. Do not force every cover in the same genre to use the exact same title color, tag color, feature-card color, or panel arrangement.

## Action — `action`

Visual family: red/black/yellow/white impact language, rough brush panels, huge title, aggressive contrast.

Allowed text variation: one cover may use white title + yellow accent, another yellow title + black/red panel, another outlined white title with no full panel, another red-white split title. Stay aggressive without copy-pasting the same overlay.

Background: dynamic hero mid-attack, debris/sparks, strong diagonal motion, hard rim light, dark environment, subject centered or lower-right, clean upper title zone.

For known games, preserve the protagonist/enemy silhouette and rendering language rather than creating a generic action hero.

## Roguelike — `roguelike`

Visual family: deep crimson/black, charcoal, gold-yellow emphasis, rugged geometry.

Allowed text variation: alternate crimson, charcoal, parchment, gold, white, and muted purple roles between title/tag/features without losing the dark-danger mood.

Background: dungeon/castle/underworld mood, dangerous enemies, high-contrast magical/fire lighting.

For known titles, preserve the game's actual pixel/illustration/3D language instead of replacing it with generic dark fantasy.

## Shooter — `shooter`

Visual family: tactical orange/black/white/gray, slanted geometry, compact military-tech feel.

Allowed text variation: rotate orange accent between tag, title stroke, feature card, and CTA; do not make every label orange.

Background: weapon/action subject, smoke, battlefield/urban combat depth, motion lines; reserve text space.

## RPG — `rpg`

Visual family: navy/purple/gold/cream, framed panels, epic/fantasy tone.

Allowed text variation: gold title, white title with violet outline, cream title on dark plaque, or gradient/magical treatment depending on the actual game art direction.

Background: hero party, magic, grand city/castle/world vista, cinematic light.

For known RPGs, character identity and art direction are more important than generic fantasy styling.

## Strategy — `strategy`

Visual family: dark navy, muted gold, parchment, burgundy, white; command-board geometry and controlled hierarchy.

Allowed text variation: gold title on one cover, white/navy outlined title on another, parchment plaque title on another, cleaner map-first typography on another.

Background: battlefield overview, commanders, tactical maps, cities, units, defensive lines, strategic scale.

For civilization/4X-style strategy, do not default every image to the same Greco-Roman male ruler. Rotate between leader archetypes, council scenes, map-only/wonders scenes, city panoramas, and different cultural visual traditions when the game supports them.

Best for: RTS, tower defense, conventional SLG, civilization-style strategy.

Do not use this as the first choice for Paradox-style country/empire simulation when `grand-strategy` is more accurate.

## Grand Strategy — `grand-strategy`

Visual family: imperial navy, parchment gold, dark burgundy, antique brass, cream, controlled premium historical/command-room feeling.

Allowed text variation: ornate gold title, parchment/ink title, white title with gold linework, burgundy plaque title, or cleaner map-first typography. Keep it premium; do not make all four covers identical navy-gold plaques.

Background direction:

- continental/world/galactic map as a major anchor
- ruler, statesman, general, diplomat, court, parliament, or war-room subject
- armies/fleets shown at national scale, not only close-up combat
- flags, borders, seals, compass, globe, parchment, treaties, trade routes, capitals
- controlled composition; avoid excessive explosion/fire effects

For batches, rotate dominant concepts: monarch portrait, diplomatic council, war-room table, naval/capital panorama, female ruler/diplomat/scholar, map-first/no-human overview.

Best for: 欧陆风云4, 钢铁雄心4, 十字军之王3, 维多利亚3, 群星 and similar nation-scale systemic strategy games.

## Casual — `casual`

Visual family: bright sky blue, warm yellow, coral, mint, cream, white, rounded cards and friendly spacing.

Allowed text variation: playful multicolor title, white title with colorful outline, two-tone title, sticker letters, or clean solid title. Rotate pink/blue/yellow/mint/coral across tags and features rather than fixing one color per role.

Background: colorful friendly scene, simple shapes, large recognizable objects, daylight/soft lighting, uncluttered composition.

Do not use generic kawaii/chibi styling for a known game if its actual character design is different.

## Horror — `horror`

Visual family: charcoal, off-white, blood-red, dirty gray, muted brown; distressed/minimal panels.

Allowed text variation: off-white distressed title, dark-red title, monochrome type with a single red accent, or minimal title without a filled panel.

Background: fog, abandoned interiors, silhouettes, narrow light source, ominous figure, strong darkness around edges; avoid excessive gore.

## Racing — `racing`

Visual family: cyan, orange, white, black, electric blue; slanted speed geometry.

Allowed text variation: alternate cyan/orange roles across title stroke, tags, chips, and CTA. Use white space and clean panels on at least some covers.

Background: car/bike in motion, road light trails, city/night track, forward-motion camera.

For licensed/known racing titles, preserve recognizable vehicle classes and visual world cues when references are available.

## Simulation — `simulation`

Visual family: clean, friendly, readable panels. Default can use teal/green, but **the real game's own palette and art direction take priority**.

Text treatment should be especially flexible because simulation games vary widely. Derive text colors/shapes from the specific game rather than imposing one universal teal template.

Background: city/farm/shop/workspace/building/life scene, organized composition, readable lighting.

### Cozy-life-sim / dollhouse subtype

Use this subtype under `simulation` for 米加小镇 / Miga-style life sims, 托卡-style world games, 阿凡达世界, and similar everyday role-play/dollhouse titles.

Do not automatically turn them into generic anime chibi or glossy 3D art.

When supported by visual references, preserve:

- flat or lightly shaded 2D cartoon rendering
- simple rounded doll-like proportions
- compact facial features
- thick/simple contour language
- cutaway room / dollhouse framing
- dense everyday interactive props
- playful, colorful environments without cinematic realism

Typography/panel family: pastel pink, sky blue, mint, warm yellow, coral, cream, white, dark outline; rounded speech bubbles, stickers, pills, small tabs, simple cards.

Do not use this exact text recipe on every image. For a four-cover batch, rotate for example:

1. multicolor title + pink tag + cream/yellow feature strip
2. white title with blue/pink outline + mint tag + peach feature card
3. pink-blue two-tone title + yellow corner tag + blue compact badge
4. clean white title with colored shadow + small pastel stickers and more visible artwork

Useful scenes: home/bedroom/kitchen, town street, school, hospital, restaurant, mall, clothing store, supermarket, playground, multi-location collage.

For batches, change locations and activities while keeping the same character-design and prop language across every image.

Best for: life simulation, town role-play, dollhouse, simulator, tycoon, management, city-builder.

## Survival — `survival`

Visual family: olive, brown, rust, dusty yellow, charcoal, rugged outdoor feel.

Rotate which tone owns the title/tag/features instead of repeating one brown/yellow overlay.

Background: wilderness/post-apocalypse, improvised gear, storm/fire/sunset, isolated character, resource-scarcity atmosphere.

## Anime — `anime`

Visual family: magenta, purple, cyan, white, black, sometimes gold depending on the actual title.

Allowed text variation: neon outline, solid white with colored shadow, gradient title, compact character-colored badges, or cleaner title without a large panel.

Background: anime-style hero group or single character, dramatic pose, magical/neon effects.

Only route here when the game is actually anime-styled or the user explicitly wants anime styling. Never use `anime` merely because characters are cute.

## Retro — `retro`

Visual family: purple, pink, cyan, cream, dark navy; pixel-block shapes.

Allowed text variation: pixel white/cream title, neon title, two-tone arcade title, or small block tags.

Background: pixel-art or retro-inspired scene, arcade lighting, limited-palette feel.

Known pixel games should remain pixel-like instead of becoming realistic illustrations.

## General — `general`

Use a high-impact but flexible design family. Prefer the known game's own palette when available instead of defaulting every unknown cover to red/yellow/white.

## Prompt / identity rule

Do not request an exact recreation of an official cover unless editing a supplied image. Instead, preserve the recognizable game's character/art/environment language while creating a fresh composition. When deterministic text rendering is used, request no text/logos/watermarks in the background.

## Batch reference rule

Do not automatically attach previous AI-generated covers of the same game as positive visual references when the goal is variety. Use real game references for identity and previous AI outputs as a record of concepts to avoid.

## Text-layer rule

A genre palette is a set of compatible colors, not a fixed template. For batches, distribute those colors differently across title, tag, features, version/menu badge, and optional accent. See `references/typography_variation.md` for the hard anti-copy-paste rules.