# Batch Variation & Subject Diversity

This reference controls diversity when generating 2 or more covers for the same game. The goal is to make the covers look like different creative concepts, not near-duplicate reskins.

For known games, diversity must happen **inside the game's real visual identity**. Do not create variety by changing the title into a different art style or a different-looking game.

Also read `references/typography_variation.md`. Scene diversity and text-layer diversity are separate requirements: different backgrounds should not receive the exact same pasted-on text system by default.

## Default behavior

When requested count >= 2, automatically enable **diversity mode**.

**Hard title-height constraint:** batch diversity never includes vertical title-height variation. Unless the user explicitly requests another height, every cover keeps the main title's top anchor at approximately **40% of canvas height**. Normal optical correction is limited to about **38–42%**. Vary title styling, width, horizontal alignment, panels, colors, and supporting badges instead of moving the title upward or downward.

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

In addition, vary at least 3 text-design dimensions between neighboring covers, such as title treatment, tag shape, feature-card treatment, version-badge placement, color-role assignment, or **horizontal** text alignment. Do not vary the main title's vertical top anchor.

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

## Text-layer anti-duplication rule

Do not treat typography as a fixed transparent overlay pasted onto every batch member.

Bad batch:

- same red top tag
- same rainbow title
- same yellow feature strip
- same green menu/version badge
- same red bottom CTA
- only the background changes

Good batch:

- same exact copy, but different title treatment
- different tag shapes/positions within their safe zone
- different feature-card arrangements
- different but game-compatible color role assignments
- different version-badge placement
- one cleaner cover with fewer filled panels if the user did not request an accent

The title can look different, but its top edge should still sit around the same **40% vertical line** on every cover.

If the user explicitly asks for a unified series template, keep stronger consistency; otherwise default to visible text-layer variation in batches.

Never create diversity by changing the wording. Copy stays exact.

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
- title treatment / horizontal alignment, while keeping the vertical top anchor fixed around 40%
- activity
- title treatment
- tag shape/color
- feature-card arrangement
- accent/banner treatment

But do not intentionally drift away from the real game's art style just to appear different.

## Recommended 4-cover plans

### Grand Strategy
1. Monarch/statesman portrait + continental map; framed gold title; small burgundy tag
2. Diplomatic/war council + tabletop map; light title with dark outline; paired feature plaques
3. Naval/army/capital panorama; title on parchment/navy panel; compact side badges
4. Diplomat/queen/scholar or map-only empire overview; cleaner title treatment and minimal badges

### Civilization / 4X Strategy
1. Classical leader + globe/wonders; gold title
2. Multi-culture council + world map table; white title with navy/gold outline
3. Female/non-European leader + city/culture scene; burgundy/navy two-tone accents
4. Map-and-wonders panorama with no dominant human; clean centered title and compact feature chips

### Cozy life-sim / dollhouse
Keep the game's authentic cartoon/character language consistent across all four.

1. town street / café / park; playful multicolor title + pink tag + cream feature strip
2. home / bedroom / kitchen; white/pastel title + mint tag + small rounded feature card
3. mall / clothing / supermarket; pink-blue title + yellow corner tag + compact menu/version chip
4. school + hospital + restaurant collage; cleaner title + several small pastel stickers instead of one repeated giant strip

Do not replace the game's actual-looking characters with generic anime chibi just to make the covers more colorful.

### Action / Roguelike
1. Hero close action pose; huge white title + yellow accent
2. Enemy/boss-dominant scene; red title panel + compact feature chips
3. Wide environmental combat scene; outlined title without full panel
4. Weapon/ability/environment-dominant composition; asymmetric title + corner badges

### Shooter
1. Soldier close-up
2. Squad scene
3. Vehicle/battlefield wide shot
4. Urban/tactical or weapon-dominant composition

Use orange/black/white roles differently across the four rather than repeating the exact same slanted panels.

### RPG / Anime
1. Main hero portrait
2. Party ensemble
3. Villain/monster/magic-dominant scene
4. World/city/environment panorama

Vary framed title, gradient title, floating chips, and cleaner text treatments while keeping the game's brand colors.

### Racing
1. Front three-quarter hero car
2. Rear chase angle
3. Multi-car race scene
4. Cockpit/city-track/environment-dominant scene

Rotate cyan/orange/white emphasis and slanted label placement.

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
- text content is identical to the supplied copy unless the user requested copy changes
- every main title begins around **40% of canvas height**, normally within roughly **38–42%**, unless the user explicitly overrides the title height
- neighboring covers do not reuse the same title treatment + tag shape + feature-card arrangement + color-role mapping
- if the user did not supply an accent/CTA, no extra bottom banner is invented merely for symmetry
