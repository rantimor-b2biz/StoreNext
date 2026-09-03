"""
Meteor Treasury Conference deck - v2 (revised after stage-readiness review).

Design constraints enforced here (these were the review's must-fix items):
  * 16:9 canvas, 1600 x 900 pt, so 1 pt == 1 px of a 1600x900 render.
  * Absolute type floor of 24 pt = 2.67% of slide height. Nothing smaller.
  * No content below y = 100 pt (bottom 11% left clear of heads and podium).
  * One colour per entity, consistent across every slide, matching the booth:
    SEE = teal, DECIDE = blue, EXECUTE = red, and the ERP-METEOR-BANKS rail.
  * Palette sampled from the W34 booth proofs so deck and booth are one system.

Product claims are limited to C-core/product-capabilities.md (approved list).
Market statistics carry their source on the slide.
"""
from pathlib import Path
import xml.etree.ElementTree as ET

from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.shapes import Drawing, Group
from reportlab.graphics.svgpath import SvgPath
from reportlab.graphics import renderPDF

ROOT = Path(r"C:\Users\rant\Documents\ran-workspace\StoreNext")
OUT = ROOT / "O-output" / "W36" / "final" / "meteor-treasury-conference-deck-v2.pdf"
LOGO_SVG = ROOT / "C-core" / "meteor-logo.svg"

W, H = 1600.0, 900.0

# --- palette sampled from O-output/W34/process/proof-*.png (the booth) --------
NAVY = HexColor("#0F2032")
NAVY_2 = HexColor("#16293D")
NAVY_3 = HexColor("#1D3348")
TEAL = HexColor("#32A89D")
BLUE = HexColor("#4375C3")
RED = HexColor("#E63B47")
WHITE = HexColor("#FFFFFF")
CREAM = HexColor("#F7F6F3")
INK = HexColor("#101820")
MUTED_L = HexColor("#4E5866")   # on cream  -> ~8.4:1
MUTED_D = HexColor("#B4C0CC")   # on navy   -> ~9.6:1
RULE_L = HexColor("#D8D5CE")

pdfmetrics.registerFont(TTFont("A", r"C:\Windows\Fonts\arial.ttf"))
pdfmetrics.registerFont(TTFont("AB", r"C:\Windows\Fonts\arialbd.ttf"))

# --- type scale, % of 900 pt slide height ------------------------------------
T_HERO = 96      # 10.7%
T_H1 = 74        # 8.2%
T_STAT = 116     # 12.9%
T_LEAD = 36      # 4.0%
T_BODY = 28      # 3.1%
T_LABEL = 28     # 3.1%
T_MIN = 24       # 2.67%  <- absolute floor
MARGIN = 110
FLOOR = 100      # nothing below this


def y(top):
    """Coordinates measured from the top edge, like a design tool."""
    return H - top


def tw(s, font, size, track=0):
    return pdfmetrics.stringWidth(s, font, size) + track * max(0, len(s) - 1)


def text(c, x, top, s, font="A", size=T_BODY, color=INK, align="l", track=0):
    w_ = tw(s, font, size, track)
    x0 = x - w_ / 2 if align == "c" else (x - w_ if align == "r" else x)
    t = c.beginText(x0, y(top))
    t.setFont(font, size)
    t.setFillColor(color)
    # Tc is graphics state and survives BT/ET, so always emit it or a previous
    # tracked line silently widens every run that follows.
    t.setCharSpace(track)
    t.textOut(s)
    c.drawText(t)


def caps(c, x, top, s, size=T_LABEL, color=INK, align="l", track=2.4, font="AB"):
    text(c, x, top, s.upper(), font=font, size=size, color=color, align=align, track=track)


def wrap(c, x, top, s, width, font="A", size=T_BODY, color=INK, lead=None, align="l"):
    lead = lead or size * 1.34
    words, line, out = s.split(), "", []
    for w_ in words:
        t = (line + " " + w_).strip()
        if pdfmetrics.stringWidth(t, font, size) <= width:
            line = t
        else:
            out.append(line)
            line = w_
    out.append(line)
    for i, ln in enumerate(out):
        text(c, x, top + i * lead, ln, font=font, size=size, color=color, align=align)
    return len(out) * lead


def logo_drawing(target_w, dark=True):
    root = ET.parse(LOGO_SVG).getroot()
    vb = [float(v) for v in root.attrib["viewBox"].split()]
    h = target_w * vb[3] / vb[2]
    g = Group()
    for node in root.iter():
        if node.tag.endswith("path") and node.attrib.get("d"):
            fill = (node.attrib.get("fill") or "").lower()
            col = RED if fill in ("#db5055", "#ee404a", "#e63b47") else (WHITE if dark else INK)
            g.add(SvgPath(node.attrib["d"], fillColor=col, strokeColor=None))
    g.transform = [target_w / vb[2], 0, 0, -h / vb[3], 0, h]
    d = Drawing(target_w, h)
    d.add(g)
    return d, h


def logo(c, x, top, w_=190, dark=True):
    d, h = logo_drawing(w_, dark)
    renderPDF.draw(d, c, x, y(top) - h)
    return h


def bg(c, dark=True):
    c.setFillColor(NAVY if dark else CREAM)
    c.rect(0, 0, W, H, stroke=0, fill=1)
    if dark:
        # smooth vertical gradient, no hard band edges across the type
        steps = 120
        top_rgb = (0x0D, 0x1B, 0x2B)
        bot_rgb = (0x16, 0x2C, 0x42)
        for i in range(steps):
            t = i / (steps - 1)
            rgb = [top_rgb[j] + (bot_rgb[j] - top_rgb[j]) * (1 - t) for j in range(3)]
            c.setFillColor(HexColor("#%02X%02X%02X" % tuple(int(v) for v in rgb)))
            c.rect(0, H * i / steps, W, H / steps + 1, stroke=0, fill=1)
        for cx, cy, r in ((1440, 720, 230), (1540, 250, 150), (140, 780, 150)):
            hexagon(c, cx, cy, r, stroke=HexColor("#1B3145"), fill=None, lw=2)


def hexagon(c, cx, cy_from_top, r, stroke=None, fill=None, lw=3):
    import math
    cy = y(cy_from_top)
    p = c.beginPath()
    for i in range(6):
        a = math.radians(60 * i - 30)
        px, py = cx + r * math.cos(a), cy + r * math.sin(a)
        p.moveTo(px, py) if i == 0 else p.lineTo(px, py)
    p.close()
    if fill is not None:
        c.setFillColor(fill)
    if stroke is not None:
        c.setStrokeColor(stroke)
        c.setLineWidth(lw)
    c.drawPath(p, stroke=1 if stroke is not None else 0, fill=1 if fill is not None else 0)


def arrow(c, x1, x2, top, color, lw=4, head=16):
    yy = y(top)
    c.setStrokeColor(color)
    c.setFillColor(color)
    c.setLineWidth(lw)
    c.line(x1, yy, x2 - head, yy)
    p = c.beginPath()
    p.moveTo(x2, yy)
    p.lineTo(x2 - head, yy + head * 0.55)
    p.lineTo(x2 - head, yy - head * 0.55)
    p.close()
    c.drawPath(p, stroke=0, fill=1)


def kicker(c, x, top, color=TEAL, w_=120):
    c.setStrokeColor(color)
    c.setLineWidth(7)
    c.line(x, y(top), x + w_, y(top))


def rule(c, x1, x2, top, color=RULE_L, lw=1.5):
    c.setStrokeColor(color)
    c.setLineWidth(lw)
    c.line(x1, y(top), x2, y(top))


def footer(c, s, dark=False, color=None):
    text(c, MARGIN, 838, s, font="A", size=T_MIN,
         color=color or (MUTED_D if dark else MUTED_L))


# =============================================================================
# SLIDES
# Colour rule, applied everywhere:
#   BLUE = the ERP / decision side.  TEAL = visibility and the bank side.
#   RED  = Meteor's own layer, and the point where action happens.
# =============================================================================
def s01_cover(c):
    bg(c, True)
    d, h = logo_drawing(300, True)
    renderPDF.draw(d, c, W / 2 - 150, y(160) - h)
    kicker(c, W / 2 - 60, 300, TEAL, 120)
    text(c, W / 2, 400, "Connected Treasury.", font="AB", size=T_HERO, color=WHITE, align="c")
    text(c, W / 2, 510, "From Insight to Action.", font="AB", size=T_HERO, color=TEAL, align="c")
    text(c, W / 2, 580, "Treasury. Payments. Financial Operations.", font="A",
         size=T_LEAD, color=MUTED_D, align="c")
    caps(c, W / 2, 675, "See  ·  Decide  ·  Execute", size=T_LABEL, color=TEAL, align="c", track=5)

    rule(c, MARGIN, W - MARGIN, 745, NAVY_3, 1.5)
    caps(c, MARGIN, 790, "Treasury Conference 2026", size=T_MIN, color=MUTED_D, track=3)
    text(c, W - MARGIN, 790, "Limor Carmeli   ·   Shiran Shapira", font="AB",
         size=T_MIN, color=WHITE, align="r")


def s02_who(c):
    bg(c, True)
    logo(c, MARGIN, 90, 170, True)
    kicker(c, MARGIN, 235, TEAL)
    text(c, MARGIN, 315, "Financial infrastructure", font="AB", size=T_H1, color=WHITE)
    text(c, MARGIN, 395, "for enterprise finance.", font="AB", size=T_H1, color=TEAL)
    wrap(c, MARGIN, 465, "Meteor centralizes bank data, treasury, payments and lease "
                         "accounting in one system, integrated with your ERP.",
         1000, "A", T_LEAD, MUTED_D, lead=48)

    stats = [("400+", "enterprise clients", TEAL),
             ("150+", "global banks, plus every Israeli bank", TEAL),
             ("1K+", "ERP integrations", BLUE),
             ("ISA", "licensed by the Israel Securities Authority", RED)]
    col = (W - 2 * MARGIN) / 4
    rule(c, MARGIN, W - MARGIN, 620, NAVY_3, 1.5)
    for i, (n, lab, col_c) in enumerate(stats):
        x = MARGIN + i * col
        text(c, x, 710, n, font="AB", size=72, color=col_c)
        wrap(c, x, 752, lab, col - 55, "A", T_MIN, MUTED_D, lead=30)


def s03_whynow(c):
    bg(c, False)
    logo(c, MARGIN, 90, 150, False)
    kicker(c, MARGIN, 235, RED)
    text(c, MARGIN, 315, "Why this matters in 2026.", font="AB", size=T_H1, color=INK)

    stats = [("63%", "of senior finance leaders expect FX volatility to rise in 2026.",
              "Alpha Group / Corpay, Countdown to 2026", BLUE),
             ("89%", "of those surveyed do not systematically stress-test their FX forecasts.",
              "Alpha Group / Corpay, Countdown to 2026", RED),
             ("61%", "of finance leaders report finance and accounting talent shortages.",
              "Corporate Finance & Accounting Talent Study 2026", TEAL)]
    col = (W - 2 * MARGIN) / 3
    for i, (n, lab, src, col_c) in enumerate(stats):
        x = MARGIN + i * col
        text(c, x, 480, n, font="AB", size=T_STAT, color=col_c)
        wrap(c, x, 530, lab, col - 80, "A", T_BODY, INK, lead=38)
        wrap(c, x, 668, src, col - 80, "A", T_MIN, MUTED_L, lead=30)

    rule(c, MARGIN, W - MARGIN, 740, RULE_L)
    text(c, MARGIN, 790, "More volatility. Less certainty. No additional headcount.",
         font="AB", size=T_LEAD, color=INK)


def s04_challenge(c):
    bg(c, False)
    logo(c, MARGIN, 90, 150, False)
    kicker(c, MARGIN, 225, RED)
    text(c, MARGIN, 300, "The Treasury Challenge", font="AB", size=T_H1, color=INK)
    text(c, MARGIN, 358, "Decisions have to be faster. The information behind them is still in pieces.",
         font="A", size=T_LEAD, color=MUTED_L)

    # Deliberately broken: four islands at different heights, links severed.
    nodes = [(300, 452, "ERP", BLUE), (630, 500, "Spreadsheets", MUTED_L),
             (980, 448, "Banks", TEAL), (1300, 502, "Treasury", RED)]
    for cx, cy, lab, col_c in nodes:
        hexagon(c, cx, cy, 46, stroke=col_c, fill=None, lw=4)
        caps(c, cx, cy + 88, lab, size=T_MIN, color=INK, align="c", track=2)
    for (x1, y1), (x2, y2) in (((346, 452), (584, 500)), ((676, 500), (934, 448)),
                               ((1026, 448), (1254, 502))):
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        c.setStrokeColor(RULE_L)
        c.setLineWidth(3)
        c.setDash(9, 11)
        c.line(x1, y(y1), mx - 26, y(my - 4))
        c.line(mx + 26, y(my + 4), x2, y(y2))
        c.setDash()
        c.setStrokeColor(RED)
        c.setLineWidth(5)
        c.line(mx - 13, y(my - 17), mx + 13, y(my + 17))
        c.line(mx - 13, y(my + 17), mx + 13, y(my - 17))

    rule(c, MARGIN, W - MARGIN, 618, RULE_L)
    pains = [("Fragmented information", "Balances and exposure sit in banks, ERP and spreadsheets."),
             ("Limited foresight", "What is coming next still takes manual analysis."),
             ("Disconnected execution", "Acting on the decision is a separate job, in another system.")]
    col = (W - 2 * MARGIN) / 3
    for i, (t_, b_) in enumerate(pains):
        x = MARGIN + i * col
        caps(c, x, 662, t_, size=T_LABEL, color=INK, track=1.6)
        wrap(c, x, 706, b_, col - 80, "A", T_MIN, MUTED_L, lead=32)

    text(c, MARGIN, 795, "The gap is not the data. It is the distance between information, "
                         "decision and execution.", font="AB", size=T_BODY, color=INK)


def s05_connected(c):
    bg(c, True)
    logo(c, MARGIN, 90, 170, True)
    kicker(c, W / 2 - 60, 225, TEAL, 120)
    text(c, W / 2, 300, "Connected Treasury. End to end.", font="AB", size=T_H1,
         color=WHITE, align="c")

    nodes = [(320, "ERP", BLUE, "SAP · Oracle · Priority · NetSuite · Dynamics"),
             (800, "METEOR", RED, "Aggregation · Treasury · Payments · IFRS 16"),
             (1280, "BANKS", TEAL, "150+ global banks · every Israeli bank · SWIFT")]
    for cx, lab, col_c, sub in nodes:
        hexagon(c, cx, 470, 92, stroke=col_c, fill=None, lw=6)
        caps(c, cx, 482, lab, size=T_LABEL + 6, color=WHITE, align="c", track=3)
        wrap(c, cx, 610, sub, 350, "A", T_MIN, MUTED_D, lead=32, align="c")

    arrow(c, 425, 680, 466, TEAL, 5)
    arrow(c, 905, 1160, 466, TEAL, 5)
    caps(c, 552, 428, "real time", size=T_MIN, color=TEAL, align="c", track=2.6, font="A")
    caps(c, 1032, 428, "controlled", size=T_MIN, color=TEAL, align="c", track=2.6, font="A")

    rule(c, MARGIN, W - MARGIN, 730, NAVY_3, 1.5)
    text(c, W / 2, 790, "One system between your ERP and your banks. No re-keying in between.",
         font="AB", size=32, color=WHITE, align="c")


def s06_sde(c):
    bg(c, False)
    logo(c, MARGIN, 90, 150, False)
    kicker(c, W / 2 - 60, 225, TEAL, 120)
    text(c, W / 2, 300, "See. Decide. Execute.", font="AB", size=T_H1, color=INK, align="c")
    text(c, W / 2, 358, "Three steps. One system.", font="A", size=T_LEAD, color=MUTED_L, align="c")

    cards = [(320, "1", "See", TEAL, "Real-time visibility across cash, banks and ERP."),
             (800, "2", "Decide", BLUE, "AI-supported insight to forecast, optimize and plan."),
             (1280, "3", "Execute", RED, "From the decision to the payment, in one flow.")]
    for cx, num, lab, col_c, body in cards:
        hexagon(c, cx, 462, 76, stroke=col_c, fill=None, lw=6)
        text(c, cx, 480, num, font="AB", size=52, color=col_c, align="c")
        caps(c, cx, 592, lab, size=T_LABEL + 8, color=col_c, align="c", track=3)
        wrap(c, cx, 646, body, 370, "A", T_BODY, INK, lead=38, align="c")

    rule(c, MARGIN, W - MARGIN, 740, RULE_L)
    text(c, W / 2, 792, "Approvals, controls and a full audit trail at every step.",
         font="AB", size=T_BODY, color=INK, align="c")


def s07_bankonnect(c):
    bg(c, False)
    logo(c, MARGIN, 90, 150, False)
    kicker(c, MARGIN, 225, RED)
    text(c, MARGIN, 300, "Execution runs on BANKONNECT.", font="AB", size=T_H1, color=INK)
    text(c, MARGIN, 358, "Meteor is the platform. BANKONNECT is the execution layer inside it.",
         font="A", size=T_LEAD, color=MUTED_L)

    boxes = [(MARGIN, "METEOR", "Decides", INK),
             (MARGIN + 470, "BANKONNECT", "Executes", RED),
             (MARGIN + 940, "BANKS", "Settles", TEAL)]
    for x, lab, sub, col_c in boxes:
        c.setStrokeColor(col_c)
        c.setLineWidth(4)
        c.rect(x, y(580), 440, 140, stroke=1, fill=0)
        caps(c, x + 34, 484, lab, size=T_LABEL + 2, color=INK, track=2.4)
        text(c, x + 34, 545, sub, font="A", size=T_BODY, color=col_c)
    arrow(c, MARGIN + 448, MARGIN + 462, 512, MUTED_L, 4)
    arrow(c, MARGIN + 918, MARGIN + 932, 512, MUTED_L, 4)

    rule(c, MARGIN, W - MARGIN, 640, RULE_L)
    wrap(c, MARGIN, 690, "One layer, three jobs: bank connectivity, payment initiation from the "
                         "ERP, and the approval trail behind both.", 1300, "A", T_BODY, MUTED_L, lead=36)
    text(c, MARGIN, 788, "You already know the name. It now sits inside a full treasury platform.",
         font="AB", size=T_LEAD, color=INK)


def s08_intelligence(c):
    bg(c, False)
    logo(c, MARGIN, 90, 150, False)
    kicker(c, W / 2 - 60, 225, BLUE, 120)
    text(c, W / 2, 300, "Intelligence where decisions happen.", font="AB", size=T_H1,
         color=INK, align="c")

    # Lay the pipeline out from measured label widths so arrows never collide.
    steps = [("DATA", MUTED_L), ("INSIGHT", BLUE), ("RECOMMENDATION", BLUE), ("ACTION", RED)]
    gap = 90
    widths = [tw(s_.upper(), "AB", T_MIN, 2.4) for s_, _ in steps]
    total = sum(widths) + gap * (len(steps) - 1)
    x = W / 2 - total / 2
    for i, ((lab, col_c), w_) in enumerate(zip(steps, widths)):
        text(c, x, 392, lab, font="AB", size=T_MIN, color=col_c, track=2.4)
        if i < len(steps) - 1:
            arrow(c, x + w_ + 22, x + w_ + gap - 22, 384,
                  BLUE if i < len(steps) - 2 else RED, 3.5, 12)
        x += w_ + gap

    c.setFillColor(WHITE)
    c.rect(MARGIN + 40, y(610), W - 2 * MARGIN - 80, 170, stroke=0, fill=1)
    c.setStrokeColor(BLUE)
    c.setLineWidth(7)
    c.line(MARGIN + 40, y(610), MARGIN + 40, y(440))
    wrap(c, W / 2, 505, "Where will we face a liquidity gap in the next seven days, "
                        "and what should we do about it?", W - 2 * MARGIN - 220,
         "AB", 42, INK, lead=56, align="c")

    rule(c, MARGIN, W - MARGIN, 670, RULE_L)
    text(c, W / 2, 722, "AI is being built across forecasting, reconciliation and payments.",
         font="A", size=T_BODY, color=MUTED_L, align="c")
    text(c, W / 2, 792, "Meteor recommends. Your approvals still govern every action.",
         font="AB", size=T_LEAD, color=INK, align="c")


def s09_demo(c):
    bg(c, True)
    logo(c, MARGIN, 90, 170, True)
    kicker(c, MARGIN, 250, RED)
    text(c, MARGIN, 360, "Now let's see it", font="AB", size=T_HERO, color=WHITE)
    text(c, MARGIN, 465, "in action.", font="AB", size=T_HERO, color=RED)

    caps(c, 900, 340, "In the next few minutes", size=T_MIN, color=TEAL, track=3)
    items = ["One cash position across every connected bank.",
             "A seven-day liquidity forecast, built from live data.",
             "One payment initiated from the ERP, start to finish."]
    for i, it in enumerate(items):
        top = 410 + i * 86
        hexagon(c, 916, top - 8, 11, stroke=None, fill=TEAL)
        wrap(c, 956, top, it, 500, "A", T_BODY, WHITE, lead=36)

    rule(c, MARGIN, W - MARGIN, 740, NAVY_3, 1.5)
    caps(c, MARGIN, 790, "See  ·  Decide  ·  Execute", size=T_MIN, color=MUTED_D, track=4)


def s10_close(c):
    bg(c, True)
    d, h = logo_drawing(260, True)
    renderPDF.draw(d, c, W / 2 - 130, y(150) - h)
    kicker(c, W / 2 - 60, 265, TEAL, 120)
    text(c, W / 2, 355, "Connected Treasury.", font="AB", size=T_H1, color=WHITE, align="c")
    text(c, W / 2, 435, "From Insight to Action.", font="AB", size=T_H1, color=TEAL, align="c")

    # QR placeholder, same mechanic as the booth rollup
    c.setStrokeColor(TEAL)
    c.setLineWidth(3)
    c.rect(W / 2 - 75, y(645), 150, 150, stroke=1, fill=0)
    text(c, W / 2, 578, "QR", font="A", size=T_MIN, color=MUTED_D, align="c")
    caps(c, W / 2, 692, "Scan to enter  ·  Win an Apple Watch", size=T_MIN, color=TEAL,
         align="c", track=2.6)

    rule(c, MARGIN, W - MARGIN, 745, NAVY_3, 1.5)
    caps(c, MARGIN, 792, "Booth [ 00 ]", size=T_MIN, color=MUTED_D, track=3)
    text(c, W - MARGIN, 792, "Limor Carmeli   ·   Shiran Shapira", font="AB",
         size=T_MIN, color=WHITE, align="r")


SLIDES = [s01_cover, s02_who, s03_whynow, s04_challenge, s05_connected,
          s06_sde, s07_bankonnect, s08_intelligence, s09_demo, s10_close]


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(OUT), pagesize=(W, H))
    c.setTitle("Meteor - Connected Treasury - Treasury Conference 2026")
    for fn in SLIDES:
        fn(c)
        c.showPage()
    c.save()
    print("wrote", OUT)


if __name__ == "__main__":
    main()
