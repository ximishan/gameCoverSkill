---
name: game-cover-maker
description: Create high-attention Chinese game-sharing covers from screenshots/key art or newly generated clean game backgrounds. Automatically infer game type and switch templates for action/roguelike/shooter/RPG/strategy/grand-strategy/casual/horror/racing/simulation/survival/anime/retro games. Supports exact Chinese text, DLC/save/version/platform callouts, large-PC-game descriptors, multiple output sizes, and strong same-game batch diversity. Prefer image generation for clean artwork/background and deterministic Pillow rendering for final Chinese text.
---

# Game Cover Maker

Create bold Chinese game-sharing covers for discovery feeds and short-video platforms. Do not make every game look the same. First identify the game's real genre, then choose a genre-appropriate background treatment and overlay template while keeping wording exact and readable at thumbnail size.

The user's explicit wording, target size, genre/style override, platform claims, and requested cover count always take precedence.

## Core workflow

1. **Classify the game before designing**
   - Separate **genre** from **marketing descriptor**.
   - Genre examples: `grand-strategy`, `strategy`, `roguelike`, `shooter`, `rpg`.
   - Descriptor examples: `大型单机`, `PC单机`, `Steam移植`, `完全汉化`.
   - Never treat `大型单机` as a genre. It may be used as a top tag only when supported by the game/context.
   - If the genre is reasonably clear, infer it automatically rather than asking the user.
   - If ambiguous, use `general`.
2. **Plan batch diversity before generating backgrounds**
   - If requested count >= 2, automatically enable **diversity mode**.
   - Read `references/batch_variation.md`.
   - Build one distinct visual concept per requested image before generation.
   - Each concept should differ from the others on at least 4 meaningful dimensions such as subject, character archetype, camera, scene, composition, secondary anchor, lighting, or palette emphasis.
   - Do not generate four near-identical rulers and call them four variants.
3. **Create or prepare a clean background**
   - Use supplied screenshot/poster/key art when suitable.
   - If no usable artwork is supplied, generate an original background matching the detected genre and the assigned batch concept.
   - Generated backgrounds must contain **no text, no title, no platform logo, no UI label, no watermark** when the deterministic text-render workflow is available.
   - Leave negative space for title, feature blocks, version badge, and bottom platform/CTA.
   - Do not recreate an official cover exactly.
4. **Render exact copy deterministically** with `scripts/render_cover.py` when practical.
   - Game names, DLC wording, version numbers, Chinese text, and platform labels must be exact.
   - Do not rely on image generation to spell important text when exact overlay rendering is available.
5. **Quality-check every requested size and every batch member independently**.
   - Re-crop and reflow each ratio.
   - Never stretch a finished cover into another size.
   - Reject or regenerate near-duplicate batch members.

## Same-game batch diversity

This is a hard requirement when the user requests multiple images of the same game.

### Do not anchor to previous faces

When the same game was already generated earlier in the current conversation, **do not automatically reuse those generated images as positive image references**. Reusing them can anchor the model to the same face, clothing, pose, globe, or composition.

Use earlier outputs as **concept history to avoid**, not as visual references to imitate.

Only reuse an earlier image as a positive reference when the user explicitly asks for one of these:

- same character / same face
- same visual identity
- edit this exact cover
- make a close variant of this exact design

Otherwise describe the shared genre style textually and deliberately change the dominant subject and scene.

### Mandatory variation dimensions

For each cover in a batch, vary at least 4 of:

- primary subject
- age/gender/cultural visual archetype or non-human/no-human subject
- character count
- camera distance and angle
- environment/scene category
- subject position and title composition
- secondary visual anchor
- lighting/time/weather
- palette emphasis within the selected genre

Tiny prop swaps do not count.

For a batch of 4, do not use the same dominant human archetype more than once unless the game has one fixed protagonist and the user asks for consistency. For genres that permit it, strongly prefer at least one cover with **no dominant human character**.

### Example: Civilization-style batch

For 4 covers of `文明6`, avoid four versions of a laurel-crowned Roman-looking man.

Prefer something like:

1. Classical statesman portrait + globe + ancient city
2. East Asian imperial strategist/scholar + strategy map room
3. Female ruler/diplomat from a different visual tradition + cultural capital/court
4. No dominant human + giant world map + wonders + districts + ships + armies

Keep the required text consistent while changing the background concept substantially.

## Automatic genre routing

Detailed design guidance lives in `references/genre_templates.md`; taxonomy guidance lives in `references/game_taxonomy.md`; batch variation guidance lives in `references/batch_variation.md`.

| Genre | Renderer value | Template behavior |
| --- | --- | --- |
| 动作 | `action` | 红黑冲击、粗笔刷、强攻击感 |
| Roguelike / 肉鸽 | `roguelike` | 深红黑、地牢/危险氛围 |
| 射击 | `shooter` | 橙黑战术、斜切面板、速度/火力感 |
| RPG / ARPG | `rpg` | 深蓝紫 + 金色、史诗框体 |
| 普通策略 / RTS / SLG / 塔防 | `strategy` | 海军蓝 + 金色、指挥/战役感 |
| 大战略 / Grand Strategy | `grand-strategy` | 帝国蓝 + 羊皮纸金、地图/外交/国家经营感 |
| 休闲 / 益智 / 卡牌 | `casual` | 高亮蓝橙、圆角卡片、轻松清晰 |
| 恐怖 / 惊悚 | `horror` | 低饱和黑红、压迫感 |
| 赛车 / 竞速 | `racing` | 青橙霓虹、斜切面板、极速感 |
| 模拟 / 经营 / 建造 | `simulation` | 青绿、圆角、干净现代 |
| 生存 / 末日 | `survival` | 橄榄/土黄、粗粝荒野感 |
| 二次元 / 动漫 | `anime` | 粉紫 + 青色霓虹、高饱和 |
| 像素 / 复古 | `retro` | 紫粉/青色、像素块面板 |
| 未识别 | `general` | 通用高冲击模板 |

### Grand Strategy routing

`grand-strategy` is distinct from generic `strategy`.

Typical examples:

- `欧陆风云4` / Europa Universalis
- `钢铁雄心4` / Hearts of Iron
- `十字军之王3` / Crusader Kings
- `维多利亚3` / Victoria
- `群星` / Stellaris

Common gameplay signals:

- control of a country/realm/empire rather than one small army
- diplomacy, economy, trade, religion, politics, technology, colonization or national management
- large world/continental/galactic map
- long time span and systemic simulation

For this family, prefer **map + nation/leader + army/navy + diplomatic/imperial symbols + navy/gold/parchment**. Avoid treating it like an explosive action poster.

### Auto-routing rules

- If the user explicitly gives a genre, pass it with `--genre`.
- If the game name/context makes the genre clear, pass the inferred genre explicitly.
- Otherwise use `--genre auto`.
- More-specific families win over broad ones: `grand-strategy` must be checked before `strategy`.
- A user style override such as “不要帝国蓝，做成冷战红黑风” overrides the default template.

Examples:

- `重生细胞` → `roguelike`
- `欧陆风云4` → `grand-strategy`
- colorful puzzle/card game → `casual`
- generic RTS/tower defense → `strategy`

## Genre vs marketing copy

The Skill should distinguish what the game **is** from what the cover **says**.

For example, `欧陆风云4` can be classified internally as:

- genre: `grand-strategy`
- platform: `PC`
- presentation descriptor: `大型单机` or `PC单机` when appropriate
- feature claims: only those supplied by the user, e.g. `解锁全部DLC`, `完全汉化`

For mainstream audiences, `大型单机` may be a clearer top tag than `大战略`; for strategy-focused audiences, `大战略` is more precise. Do not automatically claim a game is offline-only just because `大型单机` is used as a presentation tag.

## Default copy hierarchy

Unless the user asks for another arrangement:

1. Top tag: `大型单机` / `大战略` / `Steam移植游戏` / `中文汉化` / `安卓直装` / `手机直装`
2. Giant game title
3. Up to 3 feature callouts, e.g. `解锁全部DLC`, `完全汉化`, `中文汉化`, `内置存档`
4. Optional version badge, e.g. `版本号 11.0.78`
5. Giant bottom emphasis: exactly the user's `accent` value, e.g. `PC`, `PC+安卓`, `手游分享`, `-免谷歌`

Use only claims provided by the user or clearly supported by supplied context. Do not invent DLC status, unlocked content, save status, MOD functions, version numbers, platform availability, ratings, download counts, or offline-only claims.

## Output sizes

| Preset | Pixels | Ratio | Typical use |
| --- | ---: | ---: | --- |
| `feed-4x5` | 1080×1350 | 4:5 | Default feed/game-share cover |
| `portrait-3x4` | 1080×1440 | 3:4 | Portrait poster/card |
| `vertical-9x16` | 1080×1920 | 9:16 | Full-screen vertical cover |
| `square-1x1` | 1080×1080 | 1:1 | Square card |
| `landscape-16x9` | 1920×1080 | 16:9 | Standard horizontal thumbnail |
| `landscape-16x10` | 1600×1000 | 16:10 | Wide game card |

Custom exact size:

```bash
--size WIDTHxHEIGHT
```

Example: `--size 1242x1660`.

## Rendering examples

### Grand strategy auto-routing

```bash
python scripts/render_cover.py background.png \
  --output eu4.png \
  --title "欧陆风云4" \
  --tag "大型单机" \
  --feature "解锁全部DLC" \
  --feature "完全汉化" \
  --version "11.0.78" \
  --accent "PC" \
  --genre auto \
  --preset feed-4x5
```

The renderer should detect `欧陆风云4` as `grand-strategy`, not generic `strategy`.

### Several sizes

Render each separately:

```bash
--preset feed-4x5
--preset portrait-3x4
--preset vertical-9x16
--preset landscape-16x9
```

## Background-generation guidance

When no usable art is supplied, generate the background first and align it with the detected genre and assigned batch concept.

General requirements:

- one clear primary subject or visual anchor
- genre-appropriate environment and palette
- calmer upper zone for title
- breathing room for feature callouts
- enough bottom contrast for platform/CTA
- no text, logos, UI, watermark, fake rating badges, or fake storefront marks when exact overlay rendering is used
- for multiple covers, deliberately change the primary subject rather than just changing props behind the same person

For `grand-strategy`, prioritize maps, borders, flags, monarchs/generals/diplomats, fleets, armies, capitals, parliament/court/war-room objects, parchment, seals, compass/globe elements, and a controlled premium composition.

## Font behavior

The renderer searches common Chinese fonts on Windows/macOS/Linux, including Microsoft YaHei, SimHei, DengXian, PingFang, and Noto CJK. Never bundle or redistribute font files. If automatic detection fails, pass a local font path with `--font`.

## Quality gate

Before returning a cover or batch, verify:

- genre/template is sensible for the game
- `grand-strategy` was not collapsed into generic `strategy` when clearly applicable
- background mood matches the detected genre
- exact Chinese wording matches the user's copy
- game name, version, feature text, tag, and accent are unchanged
- marketing descriptors do not create unsupported factual claims
- no text is clipped
- no important subject is hidden unnecessarily
- title remains readable at about 250 px preview width
- different genres visibly use different visual systems
- every output size was reflowed rather than stretched
- generated backgrounds contain no accidental text/logos that conflict with the final overlay
- in a multi-image batch, no two covers share the same dominant face + costume + camera combination
- in a 4-image batch, strongly prefer at least 3 clearly different subject concepts and at least one different character-count or no-human composition
- previous same-game outputs were not accidentally reused as positive image references in diversity mode

Return the generated image file(s) directly. Keep commentary short unless the user asks for design analysis.