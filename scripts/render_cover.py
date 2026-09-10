#!/usr/bin/env python3
import argparse
from pathlib import Path
from typing import List, Tuple

from PIL import Image, ImageDraw, ImageEnhance, ImageFont

SIZE_PRESETS = {
    "feed-4x5": (1080, 1350),
    "portrait-3x4": (1080, 1440),
    "vertical-9x16": (1080, 1920),
    "square-1x1": (1080, 1080),
    "landscape-16x9": (1920, 1080),
    "landscape-16x10": (1600, 1000),
}
RATIOS = {
    "4:5": SIZE_PRESETS["feed-4x5"],
    "3:4": SIZE_PRESETS["portrait-3x4"],
    "9:16": SIZE_PRESETS["vertical-9x16"],
    "1:1": SIZE_PRESETS["square-1x1"],
    "16:9": SIZE_PRESETS["landscape-16x9"],
    "16:10": SIZE_PRESETS["landscape-16x10"],
}

FONT_CANDIDATES = [
    r"C:\Windows\Fonts\msyhbd.ttc",
    r"C:\Windows\Fonts\msyh.ttc",
    r"C:\Windows\Fonts\simhei.ttf",
    r"C:\Windows\Fonts\Dengb.ttf",
    "/System/Library/Fonts/PingFang.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
]

WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)

# panel_shape, tag, panel_a, panel_b, accent, shadow, version, stroke,
# brightness, contrast, saturation
THEMES = {
    "general": ("brush", (220,20,24,235), (0,0,0,215), (35,35,35,215),
                (255,218,0,255), (220,20,24,255), (220,20,24,235), BLACK, .86, 1.08, 1.08),
    "action": ("brush", (205,18,28,240), (5,5,5,220), (30,30,30,215),
               (255,219,0,255), (232,35,25,255), (205,18,28,240), BLACK, .84, 1.12, 1.12),
    "roguelike": ("brush", (160,16,28,240), (8,8,12,225), (28,22,35,220),
                  (255,205,0,255), (186,22,38,255), (126,18,30,240), BLACK, .82, 1.14, 1.08),
    "shooter": ("slant", (242,91,24,240), (12,18,22,225), (30,40,46,220),
                (255,178,25,255), (242,91,24,255), (242,91,24,240), BLACK, .84, 1.15, 1.02),
    "rpg": ("frame", (108,72,180,235), (18,23,46,220), (28,35,64,215),
            (247,201,72,255), (103,63,168,255), (145,95,190,235), BLACK, .88, 1.08, 1.08),
    "strategy": ("frame", (150,110,35,235), (14,29,48,225), (24,44,66,220),
                 (239,194,72,255), (145,105,35,255), (120,85,25,235), BLACK, .88, 1.10, .96),
    "grand-strategy": ("frame", (122,37,30,242), (10,31,58,232), (20,46,78,226),
                       (244,196,72,255), (176,132,48,255), (133,55,35,242),
                       (10,15,24,255), .90, 1.09, .94),
    "casual": ("rounded", (32,149,243,235), (255,255,255,225), (255,244,214,225),
               (255,112,67,255), (32,125,220,255), (255,183,77,240),
               (38,66,92,255), .96, 1.03, 1.18),
    "horror": ("brush", (125,0,14,245), (0,0,0,232), (28,20,22,228),
               (220,38,38,255), (120,0,12,255), (95,0,12,240), BLACK, .70, 1.20, .78),
    "racing": ("slant", (0,185,220,240), (9,14,24,222), (24,30,42,218),
               (255,125,35,255), (0,170,210,255), (255,102,35,240), BLACK, .90, 1.15, 1.18),
    "simulation": ("rounded", (30,145,124,235), (12,54,52,215), (23,72,68,210),
                   (255,210,78,255), (21,122,112,255), (44,155,136,235), BLACK, .92, 1.06, 1.04),
    "survival": ("brush", (111,88,38,240), (25,28,20,225), (45,45,34,220),
                 (226,151,55,255), (104,73,33,255), (92,77,39,240), BLACK, .80, 1.14, .92),
    "anime": ("rounded", (231,66,152,235), (36,18,58,218), (23,38,72,215),
              (82,224,255,255), (231,66,152,255), (118,81,210,235),
              (24,18,38,255), .92, 1.08, 1.20),
    "retro": ("pixel", (117,64,180,240), (24,18,48,225), (48,32,72,220),
              (255,91,179,255), (73,211,255,255), (73,84,170,240), BLACK, .92, 1.10, 1.22),
}

# Specific families must come before broad ones.
KEYWORDS = {
    "grand-strategy": [
        "grand strategy", "grand-strategy", "大战略", "宏大战略",
        "欧陆风云", "europa universalis",
        "钢铁雄心", "hearts of iron",
        "十字军之王", "crusader kings",
        "维多利亚3", "维多利亚 3", "victoria 3",
        "群星", "stellaris",
    ],
    "roguelike": ["roguelike", "肉鸽", "地牢", "重生细胞", "dead cells", "哈迪斯", "hades"],
    "shooter": ["射击", "fps", "tps", "枪战", "火力掩护", "cover fire", "使命召唤", "战地"],
    "horror": ["恐怖", "惊悚", "丧尸", "僵尸", "horror", "生化危机"],
    "racing": ["赛车", "竞速", "漂移", "racing", "forza", "极品飞车"],
    "strategy": ["策略", "slg", "rts", "塔防", "文明", "帝国", "strategy"],
    "simulation": ["模拟", "经营", "建造", "农场", "城市", "simulator", "tycoon"],
    "survival": ["生存", "末日", "荒野", "饥荒", "survival", "craft"],
    "anime": ["二次元", "动漫", "少女", "anime", "gacha", "忍者", "超忍机"],
    "retro": ["像素", "复古", "pixel", "retro", "8-bit", "16-bit"],
    "casual": ["休闲", "益智", "消除", "卡牌", "扑克牌", "dice", "puzzle", "casual"],
    "rpg": ["rpg", "角色扮演", "幻想", "魔法", "最终幻想", "勇者", "冒险"],
    "action": ["动作", "act", "格斗", "战斗", "类魂", "souls", "boss", "英雄"],
}


def find_font(explicit=None):
    if explicit:
        p = Path(explicit)
        if p.exists():
            return str(p)
        raise FileNotFoundError(f"Font not found: {explicit}")
    for candidate in FONT_CANDIDATES:
        if Path(candidate).exists():
            return candidate
    raise FileNotFoundError("No Chinese font found. Pass --font with a local Chinese font path.")


def parse_size(value):
    raw = value.lower().replace("×", "x").strip()
    if "x" not in raw:
        raise argparse.ArgumentTypeError("Size must look like 1080x1350")
    w, h = raw.split("x", 1)
    try:
        w, h = int(w), int(h)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("Size must contain integer pixels") from exc
    if w < 320 or h < 320:
        raise argparse.ArgumentTypeError("Width and height must both be at least 320 px")
    return w, h


def resolve_size(size, preset, ratio):
    if size:
        return size
    if preset:
        return SIZE_PRESETS[preset]
    if ratio:
        return RATIOS[ratio]
    return SIZE_PRESETS["feed-4x5"]


def detect_genre(title, tag, features, accent):
    haystack = " ".join([title or "", tag or "", accent or "", *features]).lower()
    for genre, words in KEYWORDS.items():
        if any(word.lower() in haystack for word in words):
            return genre
    return "general"


def cover_crop(img, size):
    tw, th = size
    sw, sh = img.size
    scale = max(tw / sw, th / sh)
    nw, nh = int(sw * scale), int(sh * scale)
    img = img.resize((nw, nh), Image.Resampling.LANCZOS)
    left = max(0, (nw - tw) // 2)
    top = max(0, (nh - th) // 2)
    return img.crop((left, top, left + tw, top + th))


def split_text(text, max_chars=8):
    text = (text or "").strip()
    if not text:
        return []
    if "\n" in text:
        return [x.strip() for x in text.splitlines() if x.strip()]
    result = []
    while text:
        result.append(text[:max_chars].strip())
        text = text[max_chars:].strip()
    return result


def fit_font(draw, lines, font_path, max_width, start_size, min_size, stroke):
    size = start_size
    while size >= min_size:
        font = ImageFont.truetype(font_path, size=size)
        widths = [draw.textbbox((0, 0), line, font=font, stroke_width=stroke)[2] for line in (lines or [" "])]
        if max(widths) <= max_width:
            return font
        size -= 4
    return ImageFont.truetype(font_path, size=min_size)


def text_size(draw, text, font, stroke=0):
    box = draw.textbbox((0, 0), text, font=font, stroke_width=stroke)
    return box[2] - box[0], box[3] - box[1]


def top_safe_layout(w, h):
    ratio = h / max(w, 1)
    if ratio >= 1.55:
        return 0.09, 0.165
    if h > w:
        return 0.06, 0.115
    return 0.04, 0.085


def add_readability_layers(img, genre):
    w, h = img.size
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    max_alpha = 135 if genre in {"casual", "anime", "simulation"} else 175
    steps = 80
    for i in range(steps):
        t = i / (steps - 1)
        alpha_top = int(max_alpha * (1 - t) ** 2 * .65)
        alpha_bottom = int(max_alpha * t ** 2)
        y1 = int(h * t)
        y2 = int(h * (i + 1) / steps) + 1
        alpha = max(alpha_top, alpha_bottom if t > .55 else 0)
        if alpha:
            d.rectangle((0, y1, w, y2), fill=(0, 0, 0, alpha))
    img.alpha_composite(overlay)


def draw_panel(draw, rect, fill, shape, outline=None, width=3):
    x1, y1, x2, y2 = rect
    if shape == "rounded":
        radius = max(10, int((y2 - y1) * .22))
        draw.rounded_rectangle(rect, radius=radius, fill=fill, outline=outline, width=width)
    elif shape == "slant":
        n = max(8, int((y2 - y1) * .22))
        pts = [(x1+n,y1),(x2,y1),(x2-n,y2),(x1,y2)]
        draw.polygon(pts, fill=fill)
        if outline:
            draw.line(pts + [pts[0]], fill=outline, width=width)
    elif shape == "pixel":
        n = max(6, int((y2 - y1) * .14))
        pts = [(x1+n,y1),(x2-n,y1),(x2-n,y1+n),(x2,y1+n),(x2,y2-n),
               (x2-n,y2-n),(x2-n,y2),(x1+n,y2),(x1+n,y2-n),(x1,y2-n),
               (x1,y1+n),(x1+n,y1+n)]
        draw.polygon(pts, fill=fill)
        if outline:
            draw.line(pts + [pts[0]], fill=outline, width=width)
    elif shape == "frame":
        draw.rectangle(rect, fill=fill, outline=outline, width=width)
        inset = max(5, int((y2-y1)*.10))
        draw.rectangle((x1+inset,y1+inset,x2-inset,y2-inset),
                       outline=outline, width=max(1, width//2))
    else:
        n = max(5, int((y2-y1)*.16))
        pts = [(x1,y1+n),(x1+n,y1),(x2-2*n,y1+n//2),(x2,y1+n),
               (x2-n,y2),(x1+2*n,y2-n//2),(x1,y2-n)]
        draw.polygon(pts, fill=fill)
        if outline:
            draw.line(pts + [pts[0]], fill=outline, width=width)


def draw_tag(draw, text, font_path, w, h, theme):
    tag_safe, _ = top_safe_layout(w, h)
    if not text:
        return int(h * tag_safe)
    shape, tag_color, _, _, accent, _, _, stroke_color, *_ = theme
    size = max(30, int(min(w,h)*.045))
    font = ImageFont.truetype(font_path, size=size)
    stroke = max(3, int(size*.09))
    tw, th = text_size(draw, text, font, stroke)
    px, py = int(size*.40), int(size*.20)
    x, y = int(w*.045), int(h*tag_safe)
    rect = (x, y, x+tw+px*2, y+th+py*2)
    outline = accent if shape == "frame" else None
    draw_panel(draw, rect, tag_color, shape, outline, max(2,int(w*.003)))
    draw.text((x+px,y+py-2), text, font=font, fill=WHITE,
              stroke_width=stroke, stroke_fill=stroke_color)
    return rect[3]


def draw_title(draw, title, font_path, w, h, theme, start_y=None):
    lines = split_text(title, 7)
    _, title_safe = top_safe_layout(w, h)
    if not lines:
        return int(h*max(.12, title_safe))
    _, _, _, _, _, shadow, _, stroke_color, *_ = theme
    stroke = max(7, int(w*.012))
    font = fit_font(draw, lines, font_path, int(w*.92),
                    int(w*.145), int(w*.072), stroke)
    y = int(h*title_safe)
    if start_y is not None:
        y = max(y, int(start_y))
    for line in lines:
        tw, th = text_size(draw, line, font, stroke)
        x = int((w-tw)/2)
        s = max(4, int(w*.006))
        draw.text((x+s,y+s), line, font=font, fill=shadow,
                  stroke_width=stroke, stroke_fill=stroke_color)
        draw.text((x,y), line, font=font, fill=WHITE,
                  stroke_width=stroke, stroke_fill=stroke_color)
        y += th + int(h*.010)
    return y


def draw_features(draw, features, version, font_path, w, h, start_y, theme):
    shape, _, panel_a, panel_b, accent, _, version_color, stroke_color, *_ = theme
    y = max(start_y, int(h*.32))
    x = int(w*.045)
    max_panel_w = int(w*.74)
    base_size = max(34, int(w*.066))
    stroke = max(4, int(w*.006))
    outline = accent if shape == "frame" else None

    for idx, feature in enumerate(features[:3]):
        lines = split_text(feature, 10)
        font = fit_font(draw, lines, font_path, max_panel_w,
                        base_size, int(w*.046), stroke)
        for line in lines:
            tw, th = text_size(draw, line, font, stroke)
            px, py = int(font.size*.34), int(font.size*.18)
            panel_w = min(max_panel_w, tw+px*2)
            rect = (x, y, x+panel_w, y+th+py*2)
            panel = panel_a if idx % 2 == 0 else panel_b
            draw_panel(draw, rect, panel, shape, outline, max(2,int(w*.003)))
            fill = accent if idx % 2 == 0 else WHITE
            draw.text((x+px,y+py-2), line, font=font, fill=fill,
                      stroke_width=stroke, stroke_fill=stroke_color)
            y = rect[3] + int(h*.012)

    if version:
        text = version if version.startswith("版本") else f"版本号 {version}"
        font = ImageFont.truetype(font_path, size=max(28,int(w*.048)))
        tw, th = text_size(draw, text, font, stroke)
        px, py = int(font.size*.30), int(font.size*.16)
        rect = (x, y, min(w-int(w*.045), x+tw+px*2), y+th+py*2)
        draw_panel(draw, rect, version_color, shape, outline, max(2,int(w*.003)))
        draw.text((x+px,y+py-2), text, font=font, fill=WHITE,
                  stroke_width=stroke, stroke_fill=stroke_color)


def draw_bottom_accent(draw, text, font_path, w, h, theme):
    if not text:
        return
    shape, _, panel_a, _, accent, _, _, stroke_color, *_ = theme
    lines = split_text(text, 7)
    stroke = max(8, int(w*.013))
    font = fit_font(draw, lines, font_path, int(w*.92),
                    int(w*.165), int(w*.080), stroke)
    heights = [text_size(draw,line,font,stroke)[1] for line in lines]
    total_h = sum(heights) + max(0,len(lines)-1)*int(h*.008)
    y = h - int(h*.050) - total_h
    panel_top = max(int(h*.60), y-int(h*.025))
    outline = accent if shape == "frame" else None
    draw_panel(draw, (int(w*.02),panel_top,int(w*.98),h-int(h*.025)),
               panel_a, shape, outline, max(2,int(w*.003)))
    for line, th in zip(lines, heights):
        tw, _ = text_size(draw, line, font, stroke)
        x = int((w-tw)/2)
        draw.text((x,y), line, font=font, fill=accent,
                  stroke_width=stroke, stroke_fill=stroke_color)
        y += th + int(h*.008)


def render(input_path, output_path, title, tag, features, version, accent,
           size, font_path, genre, darken, readability):
    if genre == "auto":
        genre = detect_genre(title, tag, features, accent)
    if genre not in THEMES:
        raise ValueError(f"Unsupported genre: {genre}")
    theme = THEMES[genre]

    img = Image.open(input_path).convert("RGB")
    img = cover_crop(img, size)
    if darken:
        img = ImageEnhance.Brightness(img).enhance(theme[8])
        img = ImageEnhance.Contrast(img).enhance(theme[9])
        img = ImageEnhance.Color(img).enhance(theme[10])
    img = img.convert("RGBA")
    if readability:
        add_readability_layers(img, genre)

    draw = ImageDraw.Draw(img)
    w, h = img.size
    tag_end = draw_tag(draw, tag, font_path, w, h, theme)
    title_end = draw_title(draw, title, font_path, w, h, theme,
                           tag_end + int(h*.025))
    draw_features(draw, features, version, font_path, w, h,
                  title_end + int(h*.025), theme)
    draw_bottom_accent(draw, accent, font_path, w, h, theme)

    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.suffix.lower() in {".jpg", ".jpeg"}:
        img.convert("RGB").save(out, quality=95, optimize=True)
    else:
        img.save(out, optimize=True)
    print(f"genre={genre}")
    print(str(out.resolve()))


def main():
    ap = argparse.ArgumentParser(
        description="Render a genre-aware Chinese game-sharing cover with exact text."
    )
    ap.add_argument("input", help="Input screenshot, key art, poster, or generated background")
    ap.add_argument("--output", "-o", default="game-cover.png")
    ap.add_argument("--title", required=True, help="Game title")
    ap.add_argument("--tag", default="游戏分享", help="Top presentation tag")
    ap.add_argument("--feature", action="append", default=[],
                    help="Selling point; repeat up to three times")
    ap.add_argument("--version", default="", help="Version number")
    ap.add_argument("--accent", default="手游分享", help="Large bottom emphasis")
    ap.add_argument("--genre", choices=["auto", *THEMES.keys()], default="auto",
                    help="Genre template; auto checks title/tag/features")
    ap.add_argument("--preset", choices=SIZE_PRESETS.keys(), default=None)
    ap.add_argument("--ratio", choices=RATIOS.keys(), default=None)
    ap.add_argument("--size", type=parse_size, default=None,
                    help="Custom exact size such as 1242x1660")
    ap.add_argument("--font", default=None)
    ap.add_argument("--no-darken", action="store_true")
    ap.add_argument("--no-readability-layer", action="store_true")
    args = ap.parse_args()

    render(
        args.input, args.output, args.title, args.tag, args.feature,
        args.version, args.accent,
        resolve_size(args.size, args.preset, args.ratio),
        find_font(args.font), args.genre,
        not args.no_darken, not args.no_readability_layer,
    )


if __name__ == "__main__":
    main()
