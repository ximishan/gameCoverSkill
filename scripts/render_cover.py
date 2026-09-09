#!/usr/bin/env python3
import argparse
import os
from pathlib import Path
from typing import List, Tuple

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

RATIOS = {
    "4:5": (1080, 1350),
    "3:4": (1080, 1440),
    "9:16": (1080, 1920),
    "1:1": (1080, 1080),
    "16:9": (1920, 1080),
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
YELLOW = (255, 214, 0, 255)
BLACK = (0, 0, 0, 255)
TAG_BG = (0, 0, 0, 185)


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
    lines = []
    remaining = text
    while remaining:
        if len(remaining) <= max_chars:
            lines.append(remaining)
            break
        # Try to split near max_chars on common separators.
        cut = max_chars
        for i in range(max_chars, max(2, max_chars - 3), -1):
            if i < len(remaining) and remaining[i - 1] in " ·|/-—：:，,":
                cut = i
                break
        lines.append(remaining[:cut].strip(" ·|/-—：:，,"))
        remaining = remaining[cut:].strip(" ·|/-—：:，,")
    return [x for x in lines if x]


def fit_font(draw: ImageDraw.ImageDraw, lines: List[str], font_path: str,
             max_width: int, start_size: int, min_size: int = 42, stroke: int = 8) -> ImageFont.FreeTypeFont:
    size = start_size
    while size >= min_size:
        font = ImageFont.truetype(font_path, size=size)
        widest = 0
        for line in lines or [" "]:
            box = draw.textbbox((0, 0), line, font=font, stroke_width=stroke)
            widest = max(widest, box[2] - box[0])
        if widest <= max_width:
            return font
        size -= 4
    return ImageFont.truetype(font_path, size=min_size)


def line_height(draw: ImageDraw.ImageDraw, font: ImageFont.FreeTypeFont, stroke: int) -> int:
    box = draw.textbbox((0, 0), "国Ag", font=font, stroke_width=stroke)
    return box[3] - box[1]


def draw_centered_lines(draw: ImageDraw.ImageDraw, lines: List[str], center_x: int, y: int,
                        font: ImageFont.FreeTypeFont, fill, stroke_width: int,
                        spacing: int = 10) -> int:
    h = line_height(draw, font, stroke_width)
    for line in lines:
        box = draw.textbbox((0, 0), line, font=font, stroke_width=stroke_width)
        w = box[2] - box[0]
        draw.text((center_x - w / 2, y), line, font=font, fill=fill,
                  stroke_width=stroke_width, stroke_fill=BLACK)
        y += h + spacing
    return y


def add_bottom_gradient(img: Image.Image, height_ratio: float = 0.52) -> Image.Image:
    w, h = img.size
    gh = int(h * height_ratio)
    overlay = Image.new("RGBA", (w, gh), (0, 0, 0, 0))
    px = overlay.load()
    for y in range(gh):
        t = y / max(1, gh - 1)
        alpha = int(12 + 170 * (t ** 1.7))
        for x in range(w):
            px[x, y] = (0, 0, 0, alpha)
    img.alpha_composite(overlay, (0, h - gh))
    return img


def draw_tag(draw: ImageDraw.ImageDraw, text: str, font_path: str, canvas_w: int, canvas_h: int):
    if not text:
        return
    size = max(34, int(canvas_w * 0.050))
    font = ImageFont.truetype(font_path, size=size)
    stroke = max(3, int(canvas_w * 0.003))
    box = draw.textbbox((0, 0), text, font=font, stroke_width=stroke)
    tw, th = box[2] - box[0], box[3] - box[1]
    pad_x, pad_y = int(size * 0.38), int(size * 0.22)
    x = int(canvas_w * 0.055)
    y = int(canvas_h * 0.055)
    rect = (x, y, x + tw + pad_x * 2, y + th + pad_y * 2)
    radius = int(size * 0.26)
    draw.rounded_rectangle(rect, radius=radius, fill=TAG_BG)
    draw.text((x + pad_x, y + pad_y - 2), text, font=font, fill=WHITE,
              stroke_width=stroke, stroke_fill=BLACK)


def render(input_path: str, output_path: str, title: str, tag: str, accent: str,
           ratio: str, position: str, font_path: str, darken: bool, gradient: bool):
    if ratio not in RATIOS:
        raise ValueError(f"Unsupported ratio {ratio}. Choose from: {', '.join(RATIOS)}")
    size = RATIOS[ratio]
    img = Image.open(input_path).convert("RGB")
    img = cover_crop(img, size)

    if darken:
        img = ImageEnhance.Brightness(img).enhance(0.82)
        img = ImageEnhance.Contrast(img).enhance(1.07)
        img = ImageEnhance.Color(img).enhance(1.08)

    img = img.convert("RGBA")
    if gradient:
        img = add_bottom_gradient(img)

    draw = ImageDraw.Draw(img)
    w, h = img.size
    side_margin = int(w * 0.065)
    max_width = w - 2 * side_margin
    stroke = max(6, int(w * 0.0105))

    draw_tag(draw, tag, font_path, w, h)

    title_lines = split_text(title, max_chars=8)
    accent_lines = split_text(accent, max_chars=7)

    title_font = fit_font(draw, title_lines, font_path, max_width,
                          start_size=int(w * 0.105), min_size=int(w * 0.055), stroke=stroke)
    accent_font = fit_font(draw, accent_lines, font_path, max_width,
                           start_size=int(w * 0.135), min_size=int(w * 0.065), stroke=stroke)

    title_h = line_height(draw, title_font, stroke)
    accent_h = line_height(draw, accent_font, stroke)
    title_block_h = len(title_lines) * title_h + max(0, len(title_lines)-1) * int(w*0.008)
    accent_block_h = len(accent_lines) * accent_h + max(0, len(accent_lines)-1) * int(w*0.007)

    if position == "bottom":
        accent_y = h - int(h * 0.065) - accent_block_h
        title_y = accent_y - int(h * 0.040) - title_block_h
    elif position == "center":
        total = title_block_h + accent_block_h + int(h * 0.045)
        title_y = int(h * 0.54 - total / 2)
        accent_y = title_y + title_block_h + int(h * 0.045)
    elif position == "split":
        title_y = int(h * 0.37)
        accent_y = h - int(h * 0.08) - accent_block_h
    else:
        raise ValueError("position must be bottom, center, or split")

    if title_lines:
        draw_centered_lines(draw, title_lines, w // 2, title_y, title_font, WHITE, stroke,
                            spacing=int(w * 0.008))
    if accent_lines:
        draw_centered_lines(draw, accent_lines, w // 2, accent_y, accent_font, YELLOW, stroke,
                            spacing=int(w * 0.007))

    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.suffix.lower() in {".jpg", ".jpeg"}:
        img.convert("RGB").save(out, quality=95, optimize=True)
    else:
        img.save(out, optimize=True)
    print(str(out.resolve()))


def main():
    ap = argparse.ArgumentParser(description="Render a bold Chinese game-sharing cover from an existing image.")
    ap.add_argument("input", help="Input screenshot/key art image")
    ap.add_argument("--output", "-o", default="game-cover.png")
    ap.add_argument("--title", required=True, help="Game title or main hook")
    ap.add_argument("--tag", default="游戏分享", help="Small top tag")
    ap.add_argument("--accent", default="手游分享", help="Large yellow emphasis text")
    ap.add_argument("--ratio", choices=RATIOS.keys(), default="4:5")
    ap.add_argument("--position", choices=["bottom", "center", "split"], default="bottom")
    ap.add_argument("--font", default=None, help="Explicit Chinese TTF/TTC/OTF font path")
    ap.add_argument("--no-darken", action="store_true")
    ap.add_argument("--no-gradient", action="store_true")
    args = ap.parse_args()

    font_path = find_font(args.font)
    render(
        input_path=args.input,
        output_path=args.output,
        title=args.title,
        tag=args.tag,
        accent=args.accent,
        ratio=args.ratio,
        position=args.position,
        font_path=font_path,
        darken=not args.no_darken,
        gradient=not args.no_gradient,
    )


if __name__ == "__main__":
    main()
