# Genre Template Reference

This file defines the visual families used by `game-cover-maker`. Genre determines the broad cover system, but for known games the real game's identity must remain recognizable. Always combine this file with `references/game_identity.md`.

For multi-image requests, also combine these rules with `references/batch_variation.md`. A genre must not force every cover to reuse the same face, costume, camera angle, or scene.

## Action — `action`

Overlay: red/black impact theme, rough brush panels, huge white title, yellow CTA, aggressive contrast.

Background: dynamic hero mid-attack, debris/sparks, strong diagonal motion, hard rim light, dark environment, subject centered or lower-right, clean upper title zone.

For known games, preserve the protagonist/enemy silhouette and rendering language rather than creating a generic action hero.

Batch ideas: hero close-up, enemy/boss focus, wide combat scene, environment/weapon/ability-dominant scene.

## Roguelike — `roguelike`

Overlay: deeper crimson/black, rugged brush geometry, gold-yellow emphasis.

Background: dungeon/castle/underworld mood, dangerous enemies, high-contrast magical/fire lighting.

For known titles, preserve the game's actual pixel/illustration/3D language instead of replacing it with generic dark fantasy.

Batch ideas: hero, boss, dungeon panorama, relic/weapon/portal-centered composition.

## Shooter — `shooter`

Overlay: tactical orange/black, slanted panels, compact military-tech feel.

Background: weapon/action subject, smoke, battlefield/urban combat depth, motion lines; reserve text space.

Batch ideas: single soldier, squad, vehicle scene, battlefield/urban wide shot.

## RPG — `rpg`

Overlay: navy/purple + gold, framed panels, epic/fantasy tone.

Background: hero party, magic, grand city/castle/world vista, cinematic light.

For known RPGs, character identity and art direction are more important than generic fantasy styling.

Batch ideas: main hero, party ensemble, villain/monster, world/city panorama.

## Strategy — `strategy`

Overlay: dark navy + muted gold, framed/command-board geometry, controlled visual hierarchy.

Background: battlefield overview, commanders, tactical maps, cities, units, defensive lines, strategic scale.

For civilization/4X-style strategy, do not default every image to the same Greco-Roman male ruler. Rotate between leader archetypes, council scenes, map-only/wonders scenes, city panoramas, and different cultural visual traditions when the game supports them.

Suggested 4-cover civilization-style rotation:

1. classical leader portrait
2. East Asian / non-European strategist or scholar scene
3. female ruler/diplomat or multi-leader council
4. no-dominant-human map/wonders/city panorama

Best for: RTS, tower defense, conventional SLG, civilization-style strategy.

Do not use this as the first choice for Paradox-style country/empire simulation when `grand-strategy` is more accurate.

## Grand Strategy — `grand-strategy`

Overlay: imperial navy, parchment gold, dark burgundy accents, ornate framed panels, premium historical/command-room feeling.

Background direction:

- continental/world/galactic map as a major anchor
- ruler, statesman, general, diplomat, court, parliament, or war-room subject
- armies/fleets shown at national scale, not only close-up combat
- flags, borders, seals, compass, globe, parchment, treaties, trade routes, capitals
- controlled composition; avoid excessive explosion/fire effects
- palette: deep navy / royal blue / parchment beige / antique gold; optional burgundy

For batches, rotate dominant concepts: monarch portrait, diplomatic council, war-room table, naval/capital panorama, female ruler/diplomat/scholar, map-first/no-human overview.

Best for: 欧陆风云4, 钢铁雄心4, 十字军之王3, 维多利亚3, 群星 and similar nation-scale systemic strategy games.

## Casual — `casual`

Overlay: bright sky blue/orange, rounded white/cream cards, softer dark stroke, clean spacing.

Background: colorful friendly scene, simple shapes, large recognizable objects, daylight/soft lighting, uncluttered composition.

Do not use generic kawaii/chibi styling for a known game if its actual character design is different.

Best for: puzzle, card, party, cozy, family games.

## Horror — `horror`

Overlay: black/blood-red, low-saturation, distressed brush blocks, red CTA.

Background: fog, abandoned interiors, silhouettes, narrow light source, ominous figure, strong darkness around edges; avoid excessive gore.

## Racing — `racing`

Overlay: cyan/orange neon, slanted speed panels, strong diagonals.

Background: car/bike in motion, road light trails, city/night track, forward-motion camera.

For licensed/known racing titles, preserve recognizable vehicle classes and visual world cues when references are available.

## Simulation — `simulation`

Overlay: clean, friendly, readable panels. Default can use teal/green, but **the real game's own palette and art direction take priority**.

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

Useful scenes: home/bedroom/kitchen, town street, school, hospital, restaurant, mall, clothing store, supermarket, playground, multi-location collage.

For batches, change locations and activities while keeping the same character-design and prop language across every image.

Best for: life simulation, town role-play, dollhouse, simulator, tycoon, management, city-builder.

## Survival — `survival`

Overlay: olive/brown/orange, rough rugged panels, worn outdoor feel.

Background: wilderness/post-apocalypse, improvised gear, storm/fire/sunset, isolated character, resource-scarcity atmosphere.

## Anime — `anime`

Overlay: magenta/purple + cyan neon, rounded panels, high saturation.

Background: anime-style hero group or single character, dramatic pose, magical/neon effects.

Only route here when the game is actually anime-styled or the user explicitly wants anime styling. Never use `anime` merely because characters are cute.

## Retro — `retro`

Overlay: purple/pink/cyan, pixel-block panel shapes, cream/white title.

Background: pixel-art or retro-inspired scene, arcade lighting, limited-palette feel.

Known pixel games should remain pixel-like instead of becoming realistic illustrations.

## General — `general`

Overlay: classic high-impact template.

Use only when a genre cannot be inferred reliably. For known games with recognizable art direction, game identity still overrides this fallback.

## Prompt / identity rule

Do not request an exact recreation of an official cover unless editing a supplied image. Instead, preserve the recognizable game's character/art/environment language while creating a fresh composition. When deterministic text rendering is used, request no text/logos/watermarks in the background.

## Batch reference rule

Do not automatically attach previous AI-generated covers of the same game as positive visual references when the goal is variety. Use real game references for identity and previous AI outputs as a record of concepts to avoid.