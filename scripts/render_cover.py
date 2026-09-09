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
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
]

WHITE = (255, 255, 255, 255)
YELLOW = (255, 218, 0, 255)
BLACK = (0, 0, 0, 255)
RED = (220, 20, 24, 235)
DARK = (0, 0, 0, 205)


def find_font(explicit: str | None) -> str:
    if explicit:
        p = Path(explicit)
        if p.exists():
            return str(p)
        raise FileNotFoundError(f"Font not found: {explicit}")
    for candidate in FONT_CANDIDATES:
        if Path(candidate).exists():
            return candidate
    raise FileNotFoundError(
        "No Chinese font found automatically. Pass --font with a local Chinese bold font path, "
        "for example C:\\Windows\\Fonts\\msyhbd.ttc"
    )


def parse_size(value: str) -> Tuple[int, int]:
    raw = value.lower().replace("×", "x").strip()
    if "x" not in raw:
        raise argparse.ArgumentTypeError("Size must look like 1080x1350")
    w, h = raw.split("x", 1)
    try:
        width, height = int(w), int(h)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("Size must contain integer pixels") from exc
    if width < 320 or height < 320:
        raise argparse.ArgumentTypeError("Width and height must both be at least 320 px")
    return width, height


def resolve_size(size, preset, ratio):
    if size:
        return size
    if preset:
        return SIZE_PRESETS[preset]
    if ratio:
        return RATIOS[ratio]
    return SIZE_PRESETS["feed-4x5"]


def cover_crop(img: Image.Image, size: Tuple[int, int]) -> Image.Image:
    tw, th = size
    sw, sh = img.size
    scale = max(tw / sw, th / sh)
    nw, nh = int(sw * scale), int(sh * scale)
    img = img.resize((nw, nh), Image.Resampling.LANCZOS)
    left = max(0, (nw - tw) // 2)
    top = max(0, (nh - th) // 2)
    return img.crop((left, top, left + tw, top + th))


def split_text(text: str, max_chars: int = 8) -> List[str]:
    text = (text or "").strip()
    if not text:
        return []
    if "\n" in text:
        return [x.strip() for x in text.splitlines() if x.strip()]
    if len(text) <= max_chars:
        return [text]
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


def add_readability_layers(img: Image.Image) -> Image.Image:
    w, h = img.size
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    px = overlay.load()
    for y in range(h):
        top_t = max(0.0, 1.0 - y / max(1, h * 0.42))
        bot_t = max(0.0, (y - h * 0.62) / max(1, h * 0.38))
        alpha = int(min(170, 70 * top_t + 150 * (bot_t ** 1.5)))
        if alpha:
            for x in range(w):
                px[x, y] = (0, 0, 0, alpha)
    img.alpha_composite(overlay)
    return img


def brush_points(x, y, width, height, notch):
    return [
        (x, y + notch), (x + notch, y),
        (x + width - notch * 2, y + notch // 2),
        (x + width, y + notch),
        (x + width - notch, y + height),
        (x + notch * 2, y + height - notch // 2),
        (x, y + height - notch),
    ]


def draw_brush_panel(draw, rect, fill=RED):
    x1, y1, x2, y2 = rect
    width, height = x2 - x1, y2 - y1
    notch = max(5, int(height * 0.16))
    draw.polygon(brush_points(x1, y1, width, height, notch), fill=fill)


def draw_tag(draw, text, font_path, w, h):
    if not text:
        return
    size = max(30, int(min(w, h) * 0.045))
    font = ImageFont.truetype(font_path, size=size)
    stroke = max(3, int(size * 0.09))
    tw, th = text_size(draw, text, font, stroke)
    px, py = int(size * 0.40), int(size * 0.20)
    x, y = int(w * 0.045), int(h * 0.035)
    rect = (x, y, x + tw + px * 2, y + th + py * 2)
    draw_brush_panel(draw, rect, RED)
    draw.text((x + px, y + py - 2), text, font=font, fill=WHITE,
              stroke_width=stroke, stroke_fill=BLACK)


def draw_title(draw, title, font_path, w, h):
    lines = split_text(title, max_chars=7)
    if not lines:
        return int(h * 0.12)
    stroke = max(7, int(w * 0.012))
    font = fit_font(draw, lines, font_path, int(w * 0.92), int(w * 0.145), int(w * 0.072), stroke)
    y = int(h * 0.085)
    for line in lines:
        tw, th = text_size(draw, line, font, stroke)
        x = int((w - tw) / 2)
        shadow = max(4, int(w * 0.006))
        draw.text((x + shadow, y + shadow), line, font=font, fill=RED,
                  stroke_width=stroke, stroke_fill=BLACK)
        draw.text((x, y), line, font=font, fill=WHITE,
                  stroke_width=stroke, stroke_fill=BLACK)
        y += th + int(h * 0.010)
    return y


def draw_features(draw, features, version, font_path, w, h, start_y):
    y = max(start_y, int(h * 0.30))
    x = int(w * 0.045)
    max_panel_w = int(w * 0.72)
    base_size = max(34, int(w * 0.066))
    stroke = max(4, int(w * 0.006))

    for idx, feature in enumerate(features[:3]):
        lines = split_text(feature, max_chars=10)
        font = fit_font(draw, lines, font_path, max_panel_w, base_size, int(w * 0.046), stroke)
        for line in lines:
            tw, th = text_size(draw, line, font, stroke)
            px, py = int(font.size * 0.34), int(font.size * 0.18)
            panel_w = min(max_panel_w, tw + px * 2)
            rect = (x, y, x + panel_w, y + th + py * 2)
            draw_brush_panel(draw, rect, DARK)
            fill = YELLOW if idx % 2 == 0 else WHITE
            draw.text((x + px, y + py - 2), line, font=font, fill=fill,
                      stroke_width=stroke, stroke_fill=BLACK)
            y = rect[3] + int(h * 0.012)

    if version:
        text = version if version.startswith("版本") else f"版本号 {version}"
        font = ImageFont.truetype(font_path, size=max(28, int(w * 0.048)))
        tw, th = text_size(draw, text, font, stroke)
        px, py = int(font.size * 0.30), int(font.size * 0.16)
        rect = (x, y, min(w - int(w * 0.045), x + tw + px * 2), y + th + py * 2)
        draw_brush_panel(draw, rect, RED)
        draw.text((x + px, y + py - 2), text, font=font, fill=WHITE,
                  stroke_width=stroke, stroke_fill=BLACK)


def draw_bottom_accent(draw, text, font_path, w, h):
    if not text:
        return
    lines = split_text(text, max_chars=7)
    stroke = max(8, int(w * 0.013))
    font = fit_font(draw, lines, font_path, int(w * 0.92), int(w * 0.165), int(w * 0.080), stroke)
    heights = [text_size(draw, line, font, stroke)[1] for line in lines]
    total_h = sum(heights) + max(0, len(lines) - 1) * int(h * 0.008)
    y = h - int(h * 0.050) - total_h
    panel_top = max(int(h * 0.60), y - int(h * 0.025))
    draw_brush_panel(draw, (int(w * 0.02), panel_top, int(w * 0.98), h - int(h * 0.025)), RED)
    for line, th in zip(lines, heights):
        tw, _ = text_size(draw, line, font, stroke)
        x = int((w - tw) / 2)
        draw.text((x, y), line, font=font, fill=YELLOW,
                  stroke_width=stroke, stroke_fill=BLACK)
        y += th + int(h * 0.008)


def render(input_path, output_path, title, tag, features, version, accent,
           size, font_path, darken, readability):
    img = Image.open(input_path).convert("RGB")
    img = cover_crop(img, size)
    if darken:
        img = ImageEnhance.Brightness(img).enhance(0.86)
        img = ImageEnhance.Contrast(img).enhance(1.08)
        img = ImageEnhance.Color(img).enhance(1.08)
    img = img.convert("RGBA")
    if readability:
        img = add_readability_layers(img)

    draw = ImageDraw.Draw(img)
    w, h = img.size
    draw_tag(draw, tag, font_path, w, h)
    title_end = draw_title(draw, title, font_path, w, h)
    draw_features(draw, features, version, font_path, w, h, title_end + int(h * 0.02))
    draw_bottom_accent(draw, accent, font_path, w, h)

    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.suffix.lower() in {".jpg", ".jpeg"}:
        img.convert("RGB").save(out, quality=95, optimize=True)
    else:
        img.save(out, optimize=True)
    print(str(out.resolve()))


def main():
    ap = argparse.ArgumentParser(description="Render a high-attention Chinese game-sharing cover with exact text.")
    ap.add_argument("input", help="Input screenshot, key art, poster, or generated background")
    ap.add_argument("--output", "-o", default="game-cover.png")
    ap.add_argument("--title", required=True, help="Game title")
    ap.add_argument("--tag", default="游戏分享", help="Top tag, e.g. Steam移植游戏")
    ap.add_argument("--feature", action="append", default=[], help="Selling point; repeat up to three times")
    ap.add_argument("--version", default="", help="Version number, e.g. 1.0.78")
    ap.add_argument("--accent", default="手游分享", help="Large bottom emphasis, e.g. PC+安卓")
    ap.add_argument("--preset", choices=SIZE_PRESETS.keys(), default=None,
                    help="Output-size preset; default feed-4x5")
    ap.add_argument("--ratio", choices=RATIOS.keys(), default=None,
                    help="Backward-compatible ratio alias")
    ap.add_argument("--size", type=parse_size, default=None,
                    help="Custom exact size, e.g. 1242x1660; overrides preset/ratio")
    ap.add_argument("--font", default=None, help="Explicit Chinese TTF/TTC/OTF font path")
    ap.add_argument("--no-darken", action="store_true")
    ap.add_argument("--no-readability-layer", action="store_true")
    args = ap.parse_args()

    size = resolve_size(args.size, args.preset, args.ratio)
    font_path = find_font(args.font)
    render(
        args.input, args.output, args.title, args.tag, args.feature,
        args.version, args.accent, size, font_path,
        not args.no_darken, not args.no_readability_layer,
    )


if __name__ == "__main__":
    main()
