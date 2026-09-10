# Game Identity Preservation

This reference prevents the cover generator from producing a visually attractive image that no longer looks like the requested game.

## Core principle

For an existing recognizable game, **game recognizability comes before generic genre stylization**.

A cover should answer two questions at thumbnail size:

1. What game is this?
2. Why should I click it?

The genre template helps with question 2, but it must not destroy question 1.

## Identity modes

### 1. `game-faithful` — default for known games

Use this when the user names an existing game and does not ask for a redesign.

Preserve the game's recognizable visual language:

- character proportions and silhouette language
- face/eye/mouth simplification level
- line-art thickness and rendering style
- typical clothing and accessory language
- environment scale and prop style
- recurring world/location motifs
- camera feeling typical of gameplay or official screenshots
- overall color and shading behavior

Create a new composition for the cover, but keep the game visually identifiable.

### 2. `genre-inspired`

Use only when:

- the title is unknown or fictional,
- reliable visual references are unavailable,
- or the user explicitly asks for an original redesign / inspired look.

In this mode, the genre template can drive the artwork more strongly.

### 3. `exact-reference-edit`

Use when the user supplies a specific screenshot/image and asks to turn that exact image into a cover or keep its characters/scene.

Preserve the source characters and scene as closely as practical; mainly change crop, lighting/readability, and overlay layout.

## Reference priority

For a known game, use references in this order when tools and permissions allow:

1. user-supplied screenshot or artwork from the current request
2. official/publisher/developer screenshots or key art
3. official store screenshots
4. reliable gameplay screenshots
5. textual reconstruction only as a fallback

Do not use previously AI-generated covers as the primary identity reference unless the user explicitly asks to preserve that generated character or design.

## Critical rule: do not replace the game's art style with a generic substitute

Bad examples:

- a flat dollhouse-style life-sim becomes generic anime chibi
- a pixel game becomes glossy 3D fantasy art
- a hand-drawn indie game becomes realistic cinematic CGI
- a fixed iconic protagonist becomes a random same-genre hero

The cover can be more dramatic, cleaner, brighter, or more readable than a raw screenshot, but the viewer should still recognize the game family immediately.

## Life-sim / dollhouse subtype

For games such as 米加小镇 / Miga-style life simulation, 托卡-style world games, 阿凡达世界, and similar dollhouse role-play titles, use a **cozy-life-sim subtype** under `simulation` rather than generic `casual` anime-chibi art.

Identity cues to preserve when supported by references:

- flat or lightly shaded 2D cartoon look
- simple rounded character proportions
- compact facial features rather than large anime eyes
- dollhouse / cutaway room presentation
- lots of interactable household, school, shop, hospital, restaurant, and street props
- colorful but not glossy 3D rendering
- playful sticker-like interface/cover accents without turning the characters into generic kawaii mascots

For `米加小镇`, the default goal is: **looks like a polished promotional cover made from the same visual world as the game**, not “a cute game vaguely similar to 米加小镇.”

## Batch rule: identity lock + concept variation

When generating multiple covers for one known game:

- lock the game's art style and character-design language across the batch
- vary which in-game character archetypes, locations, activities, camera views, and compositions are featured
- do not vary the art style so much that each image looks like a different game
- do not reuse one AI-generated face as the batch anchor unless requested

For example, four covers for a dollhouse life-sim can vary as:

1. town street / outdoor social scene
2. home / bedroom / kitchen scene
3. mall / dress-up / supermarket scene
4. school + hospital + restaurant multi-location collage

But all four should preserve the same game-like character proportions, line style, and prop language.

## Quality gate

Before returning a cover of a known game, ask:

- Would a player recognize the game from the image even if the title text were hidden?
- Do the characters look like they belong to that game rather than a generic genre substitute?
- Are scene props and environments consistent with the game's visual world?
- Did genre styling enhance the game identity rather than overwrite it?

If the answer is no, regenerate or use a better visual reference.