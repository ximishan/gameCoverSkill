# Batch Variation & Subject Diversity

This reference controls diversity when generating 2 or more covers for the same game. The goal is to make the covers look like different creative concepts, not near-duplicate reskins.

For known games, diversity must happen **inside the game's real visual identity**. Do not create variety by changing the title into a different art style or a different-looking game.

## Default behavior

When requested count >= 2, automatically enable **diversity mode**.

Before generating images, build a variation plan with one row per image. Each row must differ on at least 4 of these dimensions:

1. Primary subject
2. Subject identity/archetype
3. Character count
4. Camera distance/angle
5. Scene/location
6. Composition
7. Secondary visual anchor
8. Activity/action
9. Lighting/time/weather
10. Palette emphasis within the same game/genre family

Tiny prop swaps do not count.

## Identity lock

When the title is a known game, first lock:

- character proportion language
- face simplification style
- line/shading style
- environment/prop language
- overall game-world visual identity

Then vary concepts inside that lock.

Bad variation for a dollhouse life-sim:

- generic anime girl in bedroom
- glossy 3D chibi family in kitchen
- mascot-style kawaii mall
- flat cartoon school

These may all be cute, but they look like different games.

Good variation:

- same game-like 2D character language in town street
- same game-like 2D language in home/kitchen
- same game-like 2D language in mall/supermarket
- same game-like 2D language in school/hospital/restaurant collage

## Strong anti-duplication rule

For a batch of 4 covers, do not use the same dominant human archetype more than once unless the game has a fixed iconic protagonist and the user wants consistency.

For games with a fixed protagonist, preserve recognizability but vary pose, camera, environment, lighting, equipment state, and composition strongly.

For games with many interchangeable characters, vary the cast and location while preserving the game's character-design system.

## Previous outputs are NOT default identity references

When the user asks for more covers of the same game later in the same conversation, do not automatically feed previous AI-generated covers back into image generation as the primary visual reference. This can lock the model onto accidental AI-created faces and art drift.

Use previous AI outputs only to understand what concepts have already been used and avoid repetition.

For known commercial games, identity should come from:

1. user-supplied game screenshot/art
2. official/publisher/store screenshots when available
3. reliable gameplay references
4. textual reconstruction only as fallback

Only reuse a previous AI-generated cover as a positive reference when the user explicitly asks to preserve that generated character/design or edit that exact image.

## Session diversity

If covers for the same title were already generated earlier in the conversation, track and avoid repeating:

- dominant character/cast
- camera angle
- main environment
- dominant visual anchor
- title/layout placement
- activity

But do not intentionally drift away from the real game's art style just to appear different.

## Recommended 4-cover plans

### Grand Strategy
1. Monarch/statesman portrait + continental map
2. Diplomatic/war council + tabletop map
3. Naval/army/capital panorama
4. Diplomat/queen/scholar or map-only empire overview

### Civilization / 4X Strategy
1. Classical leader + globe/wonders
2. Multi-culture council + world map table
3. Female/non-European leader + city/culture scene
4. Map-and-wonders panorama with no dominant human

### Cozy life-sim / dollhouse
Keep the game's authentic cartoon/character language consistent across all four.

1. town street / café / park / outdoor social scene
2. home / bedroom / kitchen / furniture scene
3. mall / clothing / supermarket / dress-up scene
4. school + hospital + restaurant / multi-location collage

Do not replace the game's actual-looking characters with generic anime chibi just to make the covers more colorful.

### Action / Roguelike
1. Hero close action pose
2. Enemy/boss-dominant scene
3. Wide environmental combat scene
4. Weapon/ability/environment-dominant composition

### Shooter
1. Soldier close-up
2. Squad scene
3. Vehicle/battlefield wide shot
4. Urban/tactical or weapon-dominant composition

### RPG / Anime
1. Main hero portrait
2. Party ensemble
3. Villain/monster/magic-dominant scene
4. World/city/environment panorama

### Racing
1. Front three-quarter hero car
2. Rear chase angle
3. Multi-car race scene
4. Cockpit/city-track/environment-dominant scene

## Quality gate for batches

Before returning a batch, verify:

- all covers still look like the same requested game
- known-game character/art identity has not drifted into a generic substitute
- no two covers share the same dominant face + costume + camera combination unless required by a fixed protagonist
- at least one cover changes character count
- at least one cover changes environment category
- at least one cover changes camera distance
- for 4+ covers, prefer at least one environment/map/multi-scene composition where appropriate
- previous AI-generated covers were not accidentally used as the main identity reference
