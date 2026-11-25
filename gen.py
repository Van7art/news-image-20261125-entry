#!/usr/bin/env python3
"""Variant A: classic broadsheet front page — 'THE WORLD',
Wednesday 25 November 2026.

Lead story: Zelenskyy confirms Ukraine struck the Russian cargo ship
Sparta II in the Gulf of Finland. Draws a 1024x1024 newspaper front
page with PIL only. All illustration is drawn with shapes; no photos,
no real people depicted.
"""
import math
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (17, 17, 17)
RED = (166, 25, 46)
BLUE = (31, 78, 121)
GREY = (90, 86, 78)
LIGHT = (226, 220, 208)
OCEAN = (58, 120, 178)
STEEL = (120, 130, 140)

FD = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FD, name), size)


F_MAST = font("DejaVuSerif-Bold.ttf", 66)
F_HEAD = font("DejaVuSerif-Bold.ttf", 38)
F_CELL_HEAD = font("DejaVuSans-Bold.ttf", 17)
F_KICK = font("DejaVuSans-Bold.ttf", 15)
F_DECK = font("DejaVuSans.ttf", 18)
F_CELL_DECK = font("DejaVuSans.ttf", 13)
F_TINY = font("DejaVuSans.ttf", 12)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_text_block(d, x, y, text, fnt, max_w, fill=INK, spacing=4):
    for line in wrap(d, text, fnt, max_w):
        d.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + spacing
    return y


# ---------------- small drawn icons (46x46 box) ----------------
def icon_scales(d, x, y, c=BLUE):
    d.line([(x + 23, y + 4), (x + 23, y + 38)], fill=c, width=3)
    d.line([(x + 6, y + 10), (x + 40, y + 10)], fill=c, width=3)
    d.line([(x + 6, y + 10), (x + 2, y + 24)], fill=c, width=2)
    d.line([(x + 6, y + 10), (x + 10, y + 24)], fill=c, width=2)
    d.line([(x + 40, y + 10), (x + 36, y + 24)], fill=c, width=2)
    d.line([(x + 40, y + 10), (x + 44, y + 24)], fill=c, width=2)
    d.arc([x + 1, y + 22, x + 11, y + 30], 0, 180, fill=c, width=2)
    d.arc([x + 35, y + 22, x + 45, y + 30], 0, 180, fill=c, width=2)
    d.rectangle([x + 12, y + 38, x + 34, y + 43], fill=c)


def icon_lock(d, x, y, c=INK):
    d.rectangle([x + 10, y + 20, x + 36, y + 43], outline=c, width=2)
    d.arc([x + 14, y + 6, x + 32, y + 26], 180, 360, fill=c, width=3)
    d.ellipse([x + 20, y + 27, x + 26, y + 33], fill=RED)
    d.rectangle([x + 21, y + 32, x + 25, y + 38], fill=RED)


def icon_plane(d, x, y, c=BLUE):
    d.polygon([(x + 4, y + 26), (x + 30, y + 12), (x + 44, y + 14),
               (x + 28, y + 26), (x + 20, y + 26)], fill=c)
    d.polygon([(x + 16, y + 26), (x + 22, y + 36), (x + 26, y + 26)], fill=c)
    d.polygon([(x + 30, y + 20), (x + 36, y + 30), (x + 30, y + 30)], fill=c)
    d.arc([x + 2, y + 34, x + 44, y + 46], 180, 360, fill=GREY, width=1)


def icon_medal(d, x, y, c=RED):
    d.ellipse([x + 12, y + 16, x + 34, y + 38], outline=c, width=3)
    pts = []
    for i in range(10):
        r = 7 if i % 2 == 0 else 3
        a = math.pi / 2 + i * math.pi / 5
        pts.append((x + 23 + r * math.cos(a), y + 27 - r * math.sin(a)))
    d.polygon(pts, fill=c)
    d.line([(x + 16, y + 16), (x + 10, y + 4)], fill=BLUE, width=3)
    d.line([(x + 30, y + 16), (x + 36, y + 4)], fill=BLUE, width=3)


def icon_chart(d, x, y, c=INK):
    d.line([(x + 6, y + 42), (x + 44, y + 42)], fill=c, width=2)
    d.line([(x + 6, y + 42), (x + 6, y + 4)], fill=c, width=2)
    pts = [(x + 8, y + 34), (x + 18, y + 26), (x + 26, y + 30),
           (x + 34, y + 16), (x + 42, y + 8)]
    d.line(pts, fill=RED, width=3)
    for px, py in pts[1:]:
        d.ellipse([px - 2, py - 2, px + 2, py + 2], fill=RED)


def icon_cross(d, x, y, c=RED):
    d.rectangle([x + 18, y + 4, x + 28, y + 42], fill=c)
    d.rectangle([x + 4, y + 16, x + 42, y + 26], fill=c)


def icon_drone(d, x, y, c=INK):
    d.rectangle([x + 16, y + 18, x + 30, y + 28], fill=c)
    for cx in (x + 6, x + 40):
        d.ellipse([cx - 6, y + 4, cx + 6, y + 16], outline=c, width=2)
        d.line([(cx - 8, y + 10), (cx + 8, y + 10)], fill=c, width=2)
    d.line([(x + 12, y + 14), (x + 18, y + 20)], fill=c, width=2)
    d.line([(x + 34, y + 14), (x + 28, y + 20)], fill=c, width=2)
    d.line([(x + 23, y + 28), (x + 23, y + 38)], fill=RED, width=2)
    d.ellipse([x + 19, y + 38, x + 27, y + 44], fill=RED)


def icon_bat(d, x, y, c=(196, 154, 92)):
    d.polygon([(x + 12, y + 4), (x + 22, y + 4), (x + 18, y + 32),
               (x + 8, y + 32)], fill=c)
    d.rectangle([x + 13, y + 32, x + 17, y + 44], fill=INK)
    d.ellipse([x + 28, y + 28, x + 42, y + 42], fill=RED)
    d.arc([x + 28, y + 28, x + 42, y + 42], 200, 340,
          fill=(255, 255, 255), width=2)


def icon_burst(d, x, y, c=RED):
    pts = []
    for i in range(16):
        r = 21 if i % 2 == 0 else 9
        a = i * math.pi / 8
        pts.append((x + 23 + r * math.cos(a), y + 22 - r * math.sin(a)))
    d.polygon(pts, fill=c)
    d.ellipse([x + 17, y + 16, x + 29, y + 28], fill=(255, 210, 60))


# ---------------- page ----------------
img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
d.rectangle([14, 14, W - 15, H - 15], outline=INK, width=2)

# Masthead
d.text((W // 2, 30), "THE WORLD", font=F_MAST, fill=INK, anchor="ma")
d.line([(36, 112), (W - 36, 112)], fill=INK, width=2)
d.text((36, 120), "WEDNESDAY 25 NOVEMBER 2026", font=F_KICK, fill=RED)
d.text((W - 36, 120), "WORLD NEWS IN ONE PAGE", font=F_KICK, fill=INK, anchor="ra")
d.line([(36, 146), (W - 36, 146)], fill=INK, width=1)

# ---- Lead story: Zelenskyy / Sparta II ----
d.text((36, 162), "UKRAINE  •  GULF OF FINLAND", font=F_KICK, fill=RED)
d.text((36, 188), "ZELENSKYY: WE HIT", font=F_HEAD, fill=INK)
d.text((36, 234), "THE RUSSIAN SHIP", font=F_HEAD, fill=INK)
d.text((36, 286),
       "Kyiv claims the drone strike on the",
       font=F_DECK, fill=INK)
d.text((36, 312),
       "cargo vessel Sparta II — a “legitimate",
       font=F_DECK, fill=INK)
d.text((36, 338),
       "target” carrying weapons.",
       font=F_DECK, fill=INK)
d.text((36, 374),
       "Norway, a staunch ally, urges caution",
       font=F_DECK, fill=GREY)
d.text((36, 400),
       "as the sea war widens.",
       font=F_DECK, fill=GREY)

# Lead illustration: burning cargo ship at sea (drawn shapes)
# sky + sea panel
d.rectangle([560, 162, 988, 452], fill=(214, 231, 242))
d.rectangle([560, 162, 988, 452], outline=INK, width=2)
# sun haze
d.ellipse([900, 176, 962, 238], fill=(255, 226, 150))
# smoke columns
for sx, sy, r in [(640, 210, 26), (668, 188, 32), (700, 210, 24),
                  (726, 186, 28)]:
    d.ellipse([sx - r, sy - r, sx + r, sy + r], fill=(120, 118, 112))
# fire at the funnel
d.polygon([(636, 250), (656, 218), (668, 246), (684, 214),
           (700, 250)], fill=(230, 90, 20))
d.polygon([(648, 250), (662, 230), (676, 250)], fill=(255, 200, 60))
# hull
d.polygon([(586, 330), (962, 330), (930, 392), (618, 392)], fill=STEEL)
d.rectangle([586, 330, 962, 342], fill=RED)
# containers
for i, cc in enumerate([BLUE, (60, 120, 60), (200, 120, 40), BLUE]):
    d.rectangle([610 + i * 86, 268, 688 + i * 86, 330], fill=cc)
    d.rectangle([610 + i * 86, 268, 688 + i * 86, 330], outline=INK, width=1)
# bridge tower
d.rectangle([880, 236, 948, 330], fill=(240, 240, 236))
d.rectangle([880, 236, 948, 330], outline=INK, width=1)
for wy in (252, 276, 300):
    d.rectangle([890, wy, 938, wy + 12], fill=BLUE)
# sea waves
for wy in (400, 414, 428):
    for wx in range(566, 980, 46):
        d.arc([wx, wy, wx + 44, wy + 16], 0, 180, fill=OCEAN, width=2)
d.text((560, 458), "The Sparta II, struck by a Ukrainian drone on 21 November.",
       font=F_TINY, fill=GREY)

d.line([(36, 490), (W - 36, 490)], fill=INK, width=2)
d.text((36, 502), "THE DAY IN BRIEF", font=F_KICK, fill=RED)

# ---- Grid: 3 x 3 stories ----
stories = [
    ("Huawei found guilty in US trial",
     "Jury convicts the Chinese tech giant of stealing trade secrets; acquitted of racketeering.",
     icon_scales),
    ("CIA and spy chief's office hit by cyberattack",
     "Intrusion affects classified systems, sources say; the latest in a run of US breaches.",
     icon_lock),
    ("NATO jets to watch Poland's skies",
     "Early-warning aircraft to deploy after missiles landed in Poland during an attack on Ukraine.",
     icon_plane),
    ("Trump gives Giuliani the Medal of Freedom",
     "The former New York mayor receives America's highest civilian honour at the White House.",
     icon_medal),
    ("New US tariffs set to land",
     "Trump administration poised to unveil duties after a probe into excess factory capacity.",
     icon_chart),
    ("WHO flees Ebola hospital in Congo",
     "Staff evacuated after three days sheltering from fighting; outbreak toll: 5,775 dead.",
     icon_cross),
    ("Houthi drone hits tower in Riyadh",
     "Eleven people injured in a drone attack on a tower in the Saudi capital, officials say.",
     icon_drone),
    ("England level T20 series in Australia",
     "Eight-wicket win in the second T20I, chasing 185, squares the five-match series.",
     icon_bat),
    ("Putin: retaliation 'inevitable'",
     "Russia's president vows a response after Ukraine struck Russian oil plants.",
     icon_burst),
]

gx, gy = 36, 532
cw, ch, gap = 304, 112, 8
for i, (head, deck, icon) in enumerate(stories):
    col, row = i % 3, i // 3
    x = gx + col * (cw + gap)
    y = gy + row * (ch + gap)
    d.rectangle([x, y, x + cw, y + ch], outline=LIGHT, width=1)
    icon(d, x + 8, y + 8)
    tx = x + 62
    yy = draw_text_block(d, tx, y + 8, head, F_CELL_HEAD, cw - 70, spacing=2)
    draw_text_block(d, tx, yy + 2, deck, F_CELL_DECK, cw - 70, fill=GREY, spacing=1)

# ---- Also today strip (three columns) ----
ay = 532 + 3 * ch + 2 * gap + 12
d.line([(36, ay), (W - 36, ay)], fill=INK, width=1)
d.text((36, ay + 8), "ALSO TODAY", font=F_KICK, fill=RED)
F_STRIP_B = font("DejaVuSans-Bold.ttf", 13)
F_STRIP = font("DejaVuSans.ttf", 13)
cols = [
    (36, "Quake shakes Nepal",
     "A 5.6-magnitude earthquake hits Koshi Province near the Chinese border."),
    (360, "Sarkozy case goes to trial",
     "France orders the ex-president's corruption case to trial; first hearing 1 April 2027."),
    (684, "US confidence at two-year high",
     "Highest in nearly two years."),
]
for cx, h, t in cols:
    yy = ay + 30
    yy = draw_text_block(d, cx, yy, h, F_STRIP_B, 300, spacing=1)
    draw_text_block(d, cx, yy + 1, t, F_STRIP, 300, fill=GREY, spacing=1)

d.line([(36, H - 42), (W - 36, H - 42)], fill=INK, width=1)
d.text((W // 2, H - 34),
       "THE WORLD  •  All stories from Wednesday 25 November 2026  •  "
       "25 Nov is the International Day for the Elimination of Violence against Women",
       font=F_TINY, fill=GREY, anchor="ma")

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
img.save(out, "PNG", optimize=True)
print("saved", out, os.path.getsize(out), "bytes")
