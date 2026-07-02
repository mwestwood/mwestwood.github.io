#!/usr/bin/env python3
"""
make-touch-icon.py — generate assets/images/apple-touch-icon.png (180x180).

Raw PNG writer (struct + zlib only — PIL is not available in this environment).

Design: "night study" mark — deep violet-charcoal vertical gradient with a
faint amber corner glow, three rounded "note lines" in an amber→ember
gradient (long, long, short — a note being written), and a small amber gem.
Fully opaque (apple-touch-icons should not have transparency).

Usage: python3 _tools/make-touch-icon.py
"""

import os
import struct
import zlib

W = H = 180

# Palette (matches _sass/custom/custom.scss tokens)
BG_TOP = (42, 41, 51)      # #2a2933
BG_BOT = (30, 29, 36)      # #1e1d24
ACCENT = (226, 176, 74)    # #e2b04a amber
EMBER = (226, 118, 74)     # #e2764a


def lerp(a, b, t):
    return tuple(a[i] + (b[i] - a[i]) * t for i in range(3))


def capsule_dist(px, py, x0, y0, x1, y1):
    """Distance from point to the segment (x0,y0)-(x1,y1)."""
    dx, dy = x1 - x0, y1 - y0
    ln2 = dx * dx + dy * dy
    t = 0.0 if ln2 == 0 else max(0.0, min(1.0, ((px - x0) * dx + (py - y0) * dy) / ln2))
    cx, cy = x0 + dx * t, y0 + dy * t
    return ((px - cx) ** 2 + (py - cy) ** 2) ** 0.5, t


# Note lines: (x0, x1, y, half-thickness)
LINES = [
    (46, 134, 66, 7),
    (46, 134, 92, 7),
    (46, 100, 118, 7),
]
GEM = (117, 118, 9)  # small amber gem at the end of the short line (x, y, r)


def pixel(x, y):
    fx, fy = x + 0.5, y + 0.5

    # Background: vertical gradient + faint amber glow from the top right.
    t = fy / H
    r, g, b = lerp(BG_TOP, BG_BOT, t)
    glow = max(0.0, 1 - ((fx - 165) ** 2 + (fy - 12) ** 2) ** 0.5 / 150)
    glow = glow * glow * 0.10
    r += (ACCENT[0] - r) * glow
    g += (ACCENT[1] - g) * glow
    b += (ACCENT[2] - b) * glow

    # Note lines with soft (1px antialiased) capsule edges.
    for (x0, x1, yy, ht) in LINES:
        d, along = capsule_dist(fx, fy, x0, yy, x1, yy)
        a = max(0.0, min(1.0, ht - d + 0.5))  # coverage
        if a > 0:
            lr, lg, lb = lerp(ACCENT, EMBER, along)
            r += (lr - r) * a
            g += (lg - g) * a
            b += (lb - b) * a

    # Gem: rotated square (diamond) after the short line.
    gx, gy, gr = GEM
    dd = abs(fx - gx) + abs(fy - gy)  # L1 metric = diamond
    a = max(0.0, min(1.0, gr - dd + 0.5))
    if a > 0:
        r += (ACCENT[0] - r) * a
        g += (ACCENT[1] - g) * a
        b += (ACCENT[2] - b) * a

    return int(round(r)), int(round(g)), int(round(b))


def make_png(path):
    rows = bytearray()
    for y in range(H):
        rows.append(0)  # filter: none
        for x in range(W):
            rows.extend(pixel(x, y))

    def chunk(tag, data):
        return (struct.pack(">I", len(data)) + tag + data +
                struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF))

    ihdr = struct.pack(">IIBBBBB", W, H, 8, 2, 0, 0, 0)  # 8-bit RGB
    png = (b"\x89PNG\r\n\x1a\n" +
           chunk(b"IHDR", ihdr) +
           chunk(b"IDAT", zlib.compress(bytes(rows), 9)) +
           chunk(b"IEND", b""))
    with open(path, "wb") as f:
        f.write(png)
    print(f"✅  Wrote {path} ({len(png)} bytes)")


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(os.path.dirname(here), "assets", "images",
                       "apple-touch-icon.png")
    make_png(out)
