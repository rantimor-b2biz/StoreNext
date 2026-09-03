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
    if track:
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
# =============================================================================
def s01_cover(c):
    bg(c, True)
    d, h = logo_drawing(300, True)
    renderPDF.draw(d, c, W / 2 - 150, y(150) - h)
    kicker(c, W / 2 - 60, 300, TEAL, 120)
    text(c, W / 2, 400, "Connected Treasury.", font="AB", size=T_HERO, color=WHITE, align="c")
    text(c, W / 2, 510, "From Insight to Action.", font="AB", size=T_HERO, color=TEAL, align="c")
    text(c, W / 2, 585, "Treasury. Payments. Financial Operations.", font="A",
         size=T_LEAD, color=MUTED_D, align="c")

    caps(c, W / 2, 690, "See  ·  Decide  ·  Execute", size=T_LABEL, color=TEAL, align="c", track=5)

    rule(c, MARGIN, W - MARGIN, 760, NAVY_3, 1.5)
    caps(c, MARGIN, 800, "Treasury Conference 2026", size=T_MIN, color=MUTED_D, track=3)
    text(c, W - MARGIN, 800, "Limor Carmeli   ·   Shiran Shapira", font="AB",
         size=T_MIN, color=WHITE, align="r")


def s02_who(c):
    bg(c, True)
    logo(c, MARGIN, 90, 170, True)
    kicker(c, MARGIN, 235, TEAL)
    text(c, MARGIN, 320, "Financial infrastructure", font="AB", size=T_H1, color=WHITE)
    text(c, MARGIN, 400, "for enterprise finance.", font="AB", size=T_H1, color=TEAL)
    wrap(c, MARGIN, 470, "Meteor centralises bank data, treasury, payments and lease "
                         "accounting in one system, integrated with your ERP.",
         W - 2 * MARGIN - 380, "A", T_LEAD, MUTED_D)

    stats = [("400+", "enterprise clients", TEAL),
             ("150+", "global banks, plus every Israeli bank", BLUE),
             ("1K+", "ERP integrations", TEAL),
             ("ISA", "licensed by the Israel Securities Authority", RED)]
    col = (W - 2 * MARGIN) / 4
    rule(c, MARGIN, W - MARGIN, 620, NAVY_3, 1.5)
    for i, (n, lab, col_c) in enumerate(stats):
        x = MARGIN + i * col
        text(c, x, 720, n, font="AB", size=76, color=col_c)
        wrap(c, x, 760, lab, col - 40, "A", T_MIN, MUTED_D, lead=30)


def s03_whynow(c):
    bg(c, False)
    logo(c, MARGIN, 90, 150, False)
    kicker(c, MARGIN, 235, RED)
    text(c, MARGIN, 320, "Why this matters in 2026.", font="AB", size=T_H1, color=INK)

    stats = [("63%", "of senior finance leaders expect FX volatility to rise in 2026.",
              "Alpha Group / Corpay, Countdown to 2026", BLUE),
             ("89%", "are not systematically stress-testing their FX forecasts.",
              "Alpha Group / Corpay, Countdown to 2026", RED),
             ("61%", "of finance leaders report finance and accounting talent shortages.",
              "Corporate Finance & Accounting Talent Study 2026", TEAL)]
    col = (W - 2 * MARGIN) / 3
    for i, (n, lab, src, col_c) in enumerate(stats):
        x = MARGIN + i * col
        text(c, x, 500, n, font="AB", size=T_STAT, color=col_c)
        wrap(c, x, 550, lab, col - 60, "A", T_BODY, INK, lead=38)
        wrap(c, x, 690, src, col - 60, "A", T_MIN, MUTED_L, lead=30)

    rule(c, MARGIN, W - MARGIN, 790, RULE_L)
    text(c, MARGIN, 838, "More volatility. Less certainty. No additional headcount.",
         font="AB", size=T_LEAD, color=INK)


def s04_challenge(c):
    bg(c, False)
    logo(c, MARGIN, 90, 150, False)
    kicker(c, MARGIN, 235, RED)
    text(c, MARGIN, 310, "The Treasury Challenge", font="AB", size=T_H1, color=INK)
    text(c, MARGIN, 375, "Decisions have to be faster. The information behind them is still apart.",
         font="A", size=T_LEAD, color=MUTED_L)

    # Deliberately broken: four islands at different heights, severed links.
    nodes = [(300, 500, "ERP", BLUE), (640, 560, "Spreadsheets", MUTED_L),
             (1000, 495, "Banks", TEAL), (1330, 565, "Treasury", RED)]
    for cx, cy, lab, col_c in nodes:
        hexagon(c, cx, cy, 58, stroke=col_c, fill=None, lw=4)
        caps(c, cx, cy + 105, lab, size=T_MIN, color=INK, align="c", track=2)
    # severed connectors with a visible red break
    for (x1, y1), (x2, y2) in (((358, 500), (582, 560)), ((698, 560), (942, 495)),
                               ((1058, 495), (1272, 565))):
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        c.setStrokeColor(RULE_L)
        c.setLineWidth(3)
        c.setDash(9, 11)
        c.line(x1, y(y1), mx - 26, y(my - 5))
        c.line(mx + 26, y(my + 5), x2, y(y2))
        c.setDash()
        c.setStrokeColor(RED)
        c.setLineWidth(5)
        c.line(mx - 14, y(my - 20), mx + 14, y(my + 20))
        c.line(mx - 14, y(my + 20), mx + 14, y(my - 20))

    rule(c, MARGIN, W - MARGIN, 690, RULE_L)
    pains = [("Fragmented information", "Balances and exposure live in banks, ERP and spreadsheets."),
             ("Limited foresight", "What is coming next still takes manual analysis."),
             ("Disconnected execution", "Acting on the decision is a separate process, in another system.")]
    col = (W - 2 * MARGIN) / 3
    for i, (t_, b_) in enumerate(pains):
        x = MARGIN + i * col
        caps(c, x, 740, t_, size=T_LABEL, color=INK, track=1.6)
        wrap(c, x, 790, b_, col - 50, "A", T_MIN, MUTED_L, lead=32)


def s05_connected(c):
    bg(c, True)
    logo(c, MARGIN, 90, 170, True)
    kicker(c, W / 2 - 60, 225, TEAL, 120)
    text(c, W / 2, 320, "Connected Treasury. End to end.", font="AB", size=T_H1,
         color=WHITE, align="c")

    nodes = [(330, "ERP", BLUE, "SAP · Oracle · Priority · NetSuite · Dynamics"),
             (800, "METEOR", TEAL, "Aggregation · Treasury · Payments · IFRS 16"),
             (1270, "BANKS", RED, "150+ global banks · every Israeli bank · SWIFT")]
    for cx, lab, col_c, sub in nodes:
        hexagon(c, cx, 500, 96, stroke=col_c, fill=None, lw=6)
        caps(c, cx, 512, lab, size=T_LABEL + 6, color=WHITE, align="c", track=3)
        wrap(c, cx, 640, sub, 400, "A", T_MIN, MUTED_D, lead=32, align="c")

    arrow(c, 440, 690, 495, TEAL, 5)
    arrow(c, 910, 1160, 495, TEAL, 5)
    caps(c, 565, 455, "real time", size=T_MIN, color=TEAL, align="c", track=2.6, font="A")
    caps(c, 1035, 455, "controlled", size=T_MIN, color=TEAL, align="c", track=2.6, font="A")

    rule(c, MARGIN, W - MARGIN, 780, NAVY_3, 1.5)
    text(c, W / 2, 838, "One system between your ERP and your banks. No re-keying in between.",
         font="AB", size=T_LEAD, color=WHITE, align="c")


def s06_sde(c):
    bg(c, False)
    logo(c, MARGIN, 90, 150, False)
    kicker(c, W / 2 - 60, 225, TEAL, 120)
    text(c, W / 2, 315, "See. Decide. Execute.", font="AB", size=T_H1, color=INK, align="c")
    text(c, W / 2, 378, "The same three steps the booth is built around.", font="A",
         size=T_LEAD, color=MUTED_L, align="c")

    cards = [(330, "See", TEAL, "Real-time visibility across cash, banks and ERP."),
             (800, "Decide", BLUE, "AI-supported insight to forecast, optimise and plan."),
             (1270, "Execute", RED, "From the decision to the payment, in one flow.")]
    for cx, lab, col_c, body in cards:
        hexagon(c, cx, 510, 82, stroke=col_c, fill=None, lw=6)
        caps(c, cx, 640, lab, size=T_LABEL + 8, color=col_c, align="c", track=3)
        wrap(c, cx, 700, body, 400, "A", T_BODY, INK, lead=38, align="c")

    rule(c, MARGIN, W - MARGIN, 800, RULE_L)
    text(c, W / 2, 848, "Approvals, controls and a full audit trail at every step.",
         font="AB", size=T_BODY, color=INK, align="c")


def s07_bankonnect(c):
    bg(c, False)
    logo(c, MARGIN, 90, 150, False)
    kicker(c, MARGIN, 235, RED)
    text(c, MARGIN, 315, "Execution runs on BANKONNECT.", font="AB", size=T_H1, color=INK)
    text(c, MARGIN, 380, "Meteor is the platform. BANKONNECT is the execution layer inside it.",
         font="A", size=T_LEAD, color=MUTED_L)

    boxes = [(MARGIN, "METEOR", "Decides", TEAL),
             (MARGIN + 470, "BANKONNECT", "Executes", RED),
             (MARGIN + 940, "BANKS", "Settle", BLUE)]
    for x, lab, sub, col_c in boxes:
        c.setStrokeColor(col_c)
        c.setLineWidth(4)
        c.rect(x, y(620), 440, 150, stroke=1, fill=0)
        caps(c, x + 34, 505, lab, size=T_LABEL + 4, color=INK, track=2.4)
        text(c, x + 34, 570, sub, font="A", size=T_BODY, color=col_c)
    arrow(c, MARGIN + 448, MARGIN + 462, 545, MUTED_L, 4)
    arrow(c, MARGIN + 918, MARGIN + 932, 545, MUTED_L, 4)

    rule(c, MARGIN, W - MARGIN, 700, RULE_L)
    text(c, MARGIN, 760, "One layer, three jobs: bank connectivity, payment initiation from the ERP, "
                         "and the approval trail behind both.", font="A", size=T_BODY, color=MUTED_L)
    text(c, MARGIN, 830, "You already know the name. It now sits inside a full treasury platform.",
         font="AB", size=T_LEAD, color=INK)


def s08_intelligence(c):
    bg(c, False)
    logo(c, MARGIN, 90, 150, False)
    kicker(c, W / 2 - 60, 225, BLUE, 120)
    text(c, W / 2, 312, "Intelligence where decisions happen.", font="AB", size=T_H1,
         color=INK, align="c")

    steps = [("DATA", MUTED_L), ("INSIGHT", BLUE), ("RECOMMENDATION", BLUE), ("ACTION", RED)]
    xs = [330, 640, 1010, 1330]
    for (lab, col_c), x in zip(steps, xs):
        caps(c, x, 410, lab, size=T_LABEL, color=col_c, align="c", track=2.4)
    for i in range(3):
        arrow(c, xs[i] + 120, xs[i + 1] - 120, 402, BLUE if i < 2 else RED, 3.5, 13)

    c.setFillColor(WHITE)
    c.rect(MARGIN + 40, y(640), W - 2 * MARGIN - 80, 180, stroke=0, fill=1)
    c.setStrokeColor(BLUE)
    c.setLineWidth(7)
    c.line(MARGIN + 40, y(640), MARGIN + 40, y(460))
    wrap(c, W / 2, 530, "Where will we face a liquidity gap in the next seven days, "
                        "and what should we do about it?", W - 2 * MARGIN - 220,
         "AB", 44, INK, lead=58, align="c")

    rule(c, MARGIN, W - MARGIN, 720, RULE_L)
    text(c, W / 2, 780, "AI is being built across forecasting, reconciliation and payments.",
         font="A", size=T_BODY, color=MUTED_L, align="c")
    text(c, W / 2, 840, "Meteor recommends. Your approvals still govern every action.",
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
        top = 410 + i * 78
        hexagon(c, 918, top - 8, 12, stroke=None, fill=TEAL)
        wrap(c, 960, top, it, 540, "A", T_BODY, WHITE, lead=36)

    rule(c, MARGIN, W - MARGIN, 780, NAVY_3, 1.5)
    caps(c, MARGIN, 838, "See  ·  Decide  ·  Execute", size=T_MIN, color=MUTED_D, track=4)


def s10_close(c):
    bg(c, True)
    d, h = logo_drawing(260, True)
    renderPDF.draw(d, c, W / 2 - 130, y(140) - h)
    kicker(c, W / 2 - 60, 265, TEAL, 120)
    text(c, W / 2, 370, "Connected Treasury.", font="AB", size=T_H1, color=WHITE, align="c")
    text(c, W / 2, 450, "From Insight to Action.", font="AB", size=T_H1, color=TEAL, align="c")

    # QR placeholder, matching the booth's "Scan to enter" mechanic
    c.setStrokeColor(TEAL)
    c.setLineWidth(3)
    c.rect(W / 2 - 90, y(700), 180, 180, stroke=1, fill=0)
    text(c, W / 2, 740, "QR", font="A", size=T_MIN, color=MUTED_D, align="c")
    caps(c, W / 2, 762, "Scan to enter  ·  Win an Apple Watch", size=T_MIN, color=TEAL,
         align="c", track=2.6)

    rule(c, MARGIN, W - MARGIN, 800, NAVY_3, 1.5)
    caps(c, MARGIN, 848, "Booth [ 00 ]", size=T_MIN, color=MUTED_D, track=3)
    text(c, W - MARGIN, 848, "Limor Carmeli   ·   Shiran Shapira", font="AB",
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
