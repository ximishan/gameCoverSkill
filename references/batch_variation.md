# Batch Variation & Subject Diversity

This reference controls diversity when generating 2 or more covers for the same game. The goal is to make the covers look like different creative concepts, not near-duplicate reskins.

## Default behavior

When requested count >= 2, automatically enable **diversity mode**.

Before generating images, build a variation plan with one row per image. Each row must differ on at least 4 of these dimensions:

1. **Primary subject** — ruler, female leader, general, scholar, diplomat, explorer, council, army, vehicle, creature, no-human/map-only, etc.
2. **Subject identity/archetype** — age, gender presentation, cultural/historical visual archetype, silhouette, costume, hair/headwear, equipment.
3. **Camera** — close portrait, three-quarter portrait, back view, full body, low angle, overhead, wide establishing shot, tabletop view.
4. **Scene** — throne room, war room, map table, balcony, battlefield overview, naval harbor, city panorama, diplomatic court, wilderness, dungeon, garage, etc.
5. **Composition** — subject left/right/center, title high/center, split layout, map-dominant, character-dominant, scenery-dominant.
6. **Secondary visual anchor** — globe, parchment map, fleet, city, weapon, monster, vehicle, magical effect, landmark cluster, technology object.
7. **Lighting/time** — dawn, daylight, sunset, night, candlelit interior, fog, storm, neon.
8. **Palette emphasis** — stay inside the genre family but vary dominant balance, e.g. navy/gold vs parchment/burgundy.

Do not count tiny prop changes as meaningful variation.

## Strong anti-duplication rule

For a batch of 4 covers, do **not** use the same dominant human archetype more than once unless the user explicitly asks for character consistency.

Bad batch:
- Roman-looking male ruler + globe
- Roman-looking male ruler + map
- Roman-looking male ruler + harbor
- Roman-looking male ruler + council

Good batch:
- ruler portrait + globe
- multi-leader council + map table
- female statesperson/diplomat + court/city
- map-and-wonders panorama with no dominant person

For games with one iconic fixed protagonist, keep the protagonist recognizable only when the user asks to preserve that character. Even then, vary pose, camera, environment, lighting, equipment state, and composition strongly.

## Previous outputs are NOT default image references

When the user asks for more covers of the same game later in the same conversation, do **not** automatically feed previous generated covers back into image generation as visual references. Doing so can lock the model onto the same face, costume, pose, or composition.

Use previous outputs only to understand what has already been used and to avoid repetition. Describe the shared style textually instead.

Only reuse an earlier cover as an image reference when the user explicitly asks to:
- preserve the same character
- continue the same visual identity
- edit that exact image
- create a close variant of that exact design

When diversity is the goal, treat prior covers as **negative concept history**, not positive image references.

## Session diversity

If covers for the same title were already generated earlier in the current conversation, inspect the concepts already used and exclude them from the next batch where possible.

Track at minimum:
- dominant character archetype
- camera angle
- main environment
- dominant visual anchor
- title/layout placement

A new batch should introduce new concept families rather than merely changing facial details.

## Recommended 4-cover plan by genre

### Grand Strategy
1. Monarch/statesman portrait + continental map
2. Multi-person diplomatic/war council + tabletop map
3. Naval/army/capital panorama, no close portrait
4. Diplomat/queen/scholar or map-only empire overview

### Civilization / 4X Strategy
1. Classical leader + globe/wonders
2. Multi-culture council + world map table
3. Female or non-European leader archetype + city/culture scene
4. Map-and-wonders panorama with no dominant human

### Action / Roguelike
1. Hero close action pose
2. Enemy/boss-dominant scene
3. Wide environmental combat scene
4. Weapon/ability/environment-dominant composition

### Shooter
1. Soldier close-up
2. Squad scene
3. Vehicle/battlefield-dominant wide shot
4. Urban/tactical map or weapon-dominant composition

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

## Civilization 6 example

For four covers of `文明6`, avoid four variants of the same laurel-crowned Roman-looking man.

A better plan:

- Cover A: Roman/classical statesman, close three-quarter portrait, globe + ancient city.
- Cover B: Chinese/East Asian imperial strategist or scholar, war-room/map-table scene.
- Cover C: female ruler/diplomat from a different visual tradition, palace/cultural-city scene.
- Cover D: no dominant human; giant world map, wonders, ships, districts, armies and trade routes.

The text layer can remain consistent while the background concept changes substantially.

## Quality gate for batches

Before returning a batch, verify:

- no two covers share the same dominant face + costume + camera combination
- at least one cover changes the number of people
- at least one cover changes the environment category
- at least one cover changes the camera distance
- for 4+ covers, strongly prefer at least one no-dominant-human composition when the genre permits
- prior same-game outputs in the conversation were not accidentally reused as positive image references
