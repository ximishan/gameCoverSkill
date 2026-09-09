# game-cover-maker

Codex skill for quickly turning an existing game screenshot or key art into a bold Chinese game-sharing cover.

Example:

```bash
python scripts/render_cover.py game.jpg \
  --output cover.png \
  --title "地牢英雄" \
  --tag "中文汉化" \
  --accent "手游分享"
```

Default output is 1080×1350 (4:5).

Install as a personal Codex skill by placing the `game-cover-maker` folder under your Codex skills directory, or keep it as a repo-local skill according to your Codex setup.
