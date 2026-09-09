# Genre Template Reference

This file defines the visual families used by `game-cover-maker`. The goal is not merely to recolor one layout: different game types should feel like different cover systems while preserving the same high-readability information hierarchy.

## Action — `action`

Overlay: red/black impact theme, rough brush panels, huge white title, yellow CTA, aggressive contrast.

Background prompt direction: dynamic hero mid-attack, debris/sparks, strong diagonal motion, hard rim light, dark environment, subject centered or lower-right, clean upper title zone.

Best for: action games, fighting, soulslike, boss-rush.

## Roguelike — `roguelike`

Overlay: deeper crimson/black than action, rugged brush geometry, gold-yellow emphasis.

Background: dungeon/castle/underworld mood, dangerous enemies, high-contrast magical/fire lighting, repeat-run/harsh-world feeling without literal text.

Best for: Dead Cells-like, Hades-like, dungeon roguelikes.

## Shooter — `shooter`

Overlay: tactical orange/black, slanted panels, compact military-tech feel.

Background: weapon/action subject, muzzle light or explosive highlights, smoke, battlefield/urban combat depth, motion lines; reserve upper/left text space.

Best for: FPS/TPS, military shooters, run-and-gun.

## RPG — `rpg`

Overlay: navy/purple + gold, framed panels, epic/fantasy tone.

Background: hero party, magic, grand city/castle/world vista, cinematic light, fewer chaotic foreground objects near text.

Best for: JRPG, ARPG, fantasy adventure.

## Strategy — `strategy`

Overlay: dark navy + muted gold, framed/command-board geometry, controlled visual hierarchy.

Background: battlefield overview, commanders, tactical maps, cities, units, defensive lines, strategic scale, more negative space than action templates.

Best for: RTS, tower defense, conventional SLG, civilization-style strategy.

Do **not** use this as the first choice for Paradox-style country/empire simulation when `grand-strategy` is more accurate.

## Grand Strategy — `grand-strategy`

Overlay: imperial navy, parchment gold, dark burgundy accents, ornate framed panels, premium historical/command-room feeling. The visual system should feel less like a mobile SLG ad and more like a large PC strategy title while retaining thumbnail readability.

Background prompt direction:

- large continental/world/galactic map as a major visual anchor
- ruler, statesman, general, diplomat, court, parliament, or war-room subject
- armies and fleets shown as part of a larger national-scale system, not just close-up combat
- flags, borders, seals, compass, globe, parchment, treaties, trade routes, capital/city silhouettes
- strong depth but controlled composition; avoid excessive explosion/fire effects
- reserve a clean upper/center title zone and one side for feature cards
- palette: deep navy / royal blue / parchment beige / antique gold; optional burgundy accent

Best for:

- `欧陆风云4` / Europa Universalis
- `钢铁雄心4` / Hearts of Iron
- `十字军之王3` / Crusader Kings
- `维多利亚3` / Victoria
- `群星` / Stellaris
- other nation/realm/empire-scale systemic strategy games

Suggested top tags:

- mainstream audience: `大型单机`, `PC单机`
- strategy audience: `大战略`, `历史策略`, `国家经营`

These are presentation tags, not the genre itself. Do not imply offline-only play or another unsupported capability.

### Historical grand-strategy background prompt skeleton

> Original grand-strategy game key art, early-modern or industrial-era geopolitical campaign, antique continental map, ruler or general in a command room, armies and sailing fleet in the middle distance, royal seals and parchment documents, navy blue and antique gold palette, cinematic but controlled lighting, premium PC strategy-game poster composition, clear upper title zone and side space for feature badges, no text, no logo, no watermark, no UI.

### Sci-fi grand-strategy background prompt skeleton

> Original galactic grand-strategy key art, star map and political borders, capital station or flagship, diplomatic council silhouettes, multiple fleets at strategic scale, dark navy space palette with gold/cyan interface-inspired framing but no actual UI, clean title zone, premium empire-management poster composition, no text, no logo, no watermark.

## Casual — `casual`

Overlay: bright sky blue/orange, rounded white/cream cards, softer dark stroke, clean spacing.

Background: colorful friendly scene, simple shapes, large recognizable objects, daylight/soft studio lighting, uncluttered composition.

Best for: puzzle, card, party, cozy, family games.

## Horror — `horror`

Overlay: black/blood-red, low-saturation, distressed brush blocks, red CTA instead of cheerful yellow dominance.

Background: fog, abandoned interiors, silhouettes, narrow light source, ominous creature/figure, strong darkness around edges; avoid excessive gore.

Best for: horror, thriller, zombie, dark survival horror.

## Racing — `racing`

Overlay: cyan/orange neon, slanted speed panels, strong diagonals.

Background: car/bike in motion, road light trails, city/night track, wheel/vehicle angle creating forward motion, plenty of motion blur away from text.

Best for: racing, drifting, vehicle action.

## Simulation — `simulation`

Overlay: teal/green, rounded clean panels, modern interface-like clarity without fake UI.

Background: city/farm/shop/workspace/building scene, bright readable lighting, organized composition, realistic or polished stylized visuals.

Best for: simulator, tycoon, management, city-builder.

## Survival — `survival`

Overlay: olive/brown/orange, rough rugged panels, worn outdoor feel.

Background: wilderness/post-apocalypse, improvised gear, storm/fire/sunset, isolated character, resource-scarcity atmosphere.

Best for: crafting, wilderness, apocalypse, extraction-survival.

## Anime — `anime`

Overlay: magenta/purple + cyan neon, rounded panels, high saturation, energetic but cleaner than action.

Background: original anime-style hero group or single character, dramatic pose, neon/magical effects, clear face visibility, clean upper title zone.

Best for: anime action, gacha, character collectors, stylized JRPG.

## Retro — `retro`

Overlay: purple/pink/cyan, pixel-block panel shapes, cream/white title.

Background: pixel-art or retro-inspired scene, arcade lighting, limited-palette feel, simple readable silhouette.

Best for: pixel games, retro ports, 8-bit/16-bit inspired titles.

## General — `general`

Overlay: classic red/black brush, white title, yellow CTA.

Use only when a genre cannot be inferred reliably. It should remain a safe high-attention fallback, not the default for known game types.

## Prompt safety rule

When generating a new background, never request exact recreation of an official game cover. Describe the genre, mood, subject, composition, and lighting. Request no text/logos/watermarks. Final exact text is added by the renderer.