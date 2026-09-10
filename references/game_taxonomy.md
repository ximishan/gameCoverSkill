# Game Taxonomy Reference

Use this reference before choosing a cover template. Separate **genre**, **visual subtype**, and **presentation/marketing tags**.

For known games, taxonomy chooses the template, but `references/game_identity.md` decides how faithfully the real game's visual language must be preserved.

## 1. Genre = what kind of game it is

Examples:

- `grand-strategy` — 大战略 / 宏大战略
- `strategy` — RTS / SLG / 塔防 / 4X / 常规策略
- `roguelike` — 肉鸽 / Roguelike
- `shooter` — FPS / TPS / 枪战
- `rpg` — RPG / ARPG / JRPG
- `simulation` — 模拟 / 经营 / 建造 / 生活模拟
- `casual` — 益智 / 派对 / 轻休闲

Genre decides the broad visual system.

## 2. Visual subtype = how this specific family should look

Subtypes refine a genre without requiring a separate renderer enum.

Examples:

- `civilization-4x` under `strategy`
- `cozy-life-sim` under `simulation`
- `city-builder` under `simulation`
- `historical-grand-strategy` under `grand-strategy`
- `sci-fi-grand-strategy` under `grand-strategy`

The subtype is especially important for games whose art direction is distinctive.

### Cozy life-sim / dollhouse

Use `simulation + cozy-life-sim` for titles such as 米加小镇 / Miga-style life sims, 托卡-style world games, 阿凡达世界, and similar dollhouse role-play games.

Do not route them to generic `anime` just because the characters are cute. Do not replace their recognizable 2D dollhouse/cartoon visual language with generic kawaii chibi art.

Preferred visual identity when supported by references:

- simple rounded 2D character proportions
- compact facial features
- light/flat shading
- dollhouse rooms and cutaway interiors
- everyday props, shops, schools, hospitals, restaurants, streets, furniture
- colorful playful composition rather than cinematic realism

## 3. Presentation tag = how the cover introduces it

Examples:

- `大型单机`
- `PC单机`
- `Steam移植`
- `中文汉化`
- `安卓直装`
- `手机直装`
- `完整版`
- `大战略`
- `历史策略`

Presentation tags help viewers understand the release quickly. They do not replace the underlying genre or visual identity.

## 4. Feature claim = specific supplied selling point

Examples:

- `解锁全部DLC`
- `完全汉化`
- `内置存档`
- `解锁全部地图和家具`
- `版本号 11.0.78`
- `PC+安卓`

Feature claims must come from the user or another reliable supplied source. Never invent them.

## Examples

| Game | Genre | Visual subtype | Useful cover tags |
| --- | --- | --- | --- |
| 欧陆风云4 | `grand-strategy` | `historical-grand-strategy` | 大型单机 / 大战略 / 历史策略 |
| 钢铁雄心4 | `grand-strategy` | `historical-grand-strategy` | 大型单机 / 二战战略 / 大战略 |
| 十字军之王3 | `grand-strategy` | `historical-grand-strategy` | 大型单机 / 王朝经营 / 大战略 |
| 维多利亚3 | `grand-strategy` | `historical-grand-strategy` | 大型单机 / 国家经营 / 大战略 |
| 群星 | `grand-strategy` | `sci-fi-grand-strategy` | 大型单机 / 星际战略 / 大战略 |
| 文明6 | `strategy` | `civilization-4x` | 大型单机 / 策略 / 多文明 |
| 米加小镇 | `simulation` | `cozy-life-sim` | 手机直装 / 无广告版 / 生活模拟 |

## Grand Strategy vs ordinary Strategy

Use `grand-strategy` when the player primarily controls a country, realm, civilization-scale polity, or empire through several interlocking systems such as diplomacy, economy, politics, religion, trade, technology, colonization, warfare, or long-term national development.

Use ordinary `strategy` for tactical battles, RTS base/unit control, tower defense, conventional SLG, or 4X games whose visual identity is better represented by leaders, cities, wonders, and map development than Paradox-style geopolitical simulation.

## About “大型单机”

`大型单机` is a broad audience-facing descriptor, not a technical genre. It can be useful when a title is a substantial PC game with a meaningful single-player experience, but it must not imply:

- the game has no multiplayer
- the game works fully offline
- the game is AAA
- the game is large only because of file size

When precision matters, keep the internal classification separate from the visible copy.

## Identity-routing rule

For a known title, do not let taxonomy erase the game's recognizable look.

Example:

```text
米加小镇
Genre: simulation
Subtype: cozy-life-sim
Identity mode: game-faithful
Presentation tag: 手机直装
```

This should produce a polished cover that still resembles the actual game's visual world, not a generic cute mobile-game poster.