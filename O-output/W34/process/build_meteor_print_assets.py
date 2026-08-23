from pathlib import Path
import math
import re
import xml.etree.ElementTree as ET

from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageDraw
from reportlab.pdfgen import canvas
from reportlab.lib.colors import PCMYKColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics.shapes import Drawing, Group
from reportlab.graphics.svgpath import SvgPath
from reportlab.graphics import renderPDF
from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject

ROOT = Path(r"C:\Users\rant\Documents\ran-workspace\StoreNext")
WEEK = ROOT / "O-output" / "W34"
FINAL = WEEK / "final"
PROCESS = WEEK / "process"
SOURCE_WATCH = Path(r"C:\Users\rant\Downloads\apple watch.png")
SOURCE_CITY = PROCESS / "meteor-city-data-background-v2.png"
LOGO_SVG = Path(r"C:\Users\rant\Downloads\Meteor logo-white.svg")

MM = 72 / 25.4
BLEED = 5
SAFE = 30

NAVY = PCMYKColor(100, 78, 42, 62)
NAVY_2 = PCMYKColor(95, 67, 38, 45)
BLACK = PCMYKColor(75, 68, 67, 90)
WHITE = PCMYKColor(0, 0, 0, 0)
TEAL = PCMYKColor(78, 0, 37, 12)
TEAL_DARK = PCMYKColor(83, 18, 48, 5)
BLUE = PCMYKColor(80, 48, 0, 0)
RED = PCMYKColor(0, 81, 66, 5)
MUTED = PCMYKColor(17, 8, 0, 18)

pdfmetrics.registerFont(TTFont("Arial", r"C:\Windows\Fonts\arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", r"C:\Windows\Fonts\arialbd.ttf"))


def prepare_watch():
    """Prepare the user's standalone transparent watch as a CMYK print asset."""
    out = PROCESS / "meteor-apple-watch-print-cmyk.jpg"
    rgba = Image.open(SOURCE_WATCH).convert("RGBA")
    rgba = rgba.resize((2768, 2880), Image.Resampling.LANCZOS)
    sharp = ImageEnhance.Sharpness(rgba).enhance(1.18)
    white = Image.new("RGB", sharp.size, "white")
    white.paste(sharp.convert("RGB"), mask=sharp.getchannel("A"))
    white.convert("CMYK").save(out, quality=96, dpi=(300, 300), subsampling=0)
    return out


def prepare_city_backgrounds():
    """Prepare dark, high-resolution CMYK city compositions for wall and counter."""
    source = Image.open(SOURCE_CITY).convert("RGB")
    outputs = {}
    for name, size, city_top in (
        ("wall", (4000, 4400), 1550),
        ("counter", (4000, 3000), 470),
    ):
        base = Image.new("RGB", size, (7, 24, 39))
        city_h = size[1] - city_top
        fitted = ImageOps.fit(source, (size[0], city_h), method=Image.Resampling.LANCZOS, centering=(0.57, 0.56))
        fitted = ImageEnhance.Contrast(fitted).enhance(1.05)
        base.paste(fitted, (0, city_top))
        # Smooth navy fade protects the headline and logo area.
        overlay = Image.new("RGBA", size, (4, 18, 31, 0))
        od = ImageDraw.Draw(overlay)
        fade_end = city_top + int(city_h * .30)
        for y in range(max(0, city_top-200), fade_end):
            t = (y - (city_top-200)) / max(1, fade_end-(city_top-200))
            alpha = int(235 * (1-t))
            od.line((0, y, size[0], y), fill=(4, 18, 31, alpha))
        base = Image.alpha_composite(base.convert("RGBA"), overlay).convert("RGB")
        out = PROCESS / f"meteor-{name}-background-cmyk-v2.jpg"
        base.convert("CMYK").save(out, quality=95, dpi=(150,150), subsampling=0)
        outputs[name] = out
    return outputs


def load_logo_drawing(target_w, target_h):
    root = ET.parse(LOGO_SVG).getroot()
    vb = [float(v) for v in root.attrib["viewBox"].split()]
    group = Group()
    for node in root.iter():
        if node.tag.endswith("path") and node.attrib.get("d"):
            fill = node.attrib.get("fill", "white")
            if fill.lower() == "#db5055":
                color = RED
            else:
                color = WHITE
            group.add(SvgPath(node.attrib["d"], fillColor=color, strokeColor=None))
    sx, sy = target_w / vb[2], target_h / vb[3]
    group.transform = [sx, 0, 0, -sy, 0, target_h]
    drawing = Drawing(target_w, target_h)
    drawing.add(group)
    return drawing


def logo(c, x, y, w):
    h = w * 52 / 213
    renderPDF.draw(load_logo_drawing(w, h), c, x, y)
    return h


def trim_marks(c, trim_w, trim_h):
    b = BLEED * MM
    tw, th = trim_w * MM, trim_h * MM
    c.saveState()
    c.setStrokeColor(PCMYKColor(0, 0, 0, 100))
    c.setLineWidth(0.25)
    gap, length = 2 * MM, 6 * MM
    for x in (b, b + tw):
        c.line(x, b-gap, x, b-gap-length)
        c.line(x, b+th+gap, x, b+th+gap+length)
    for y in (b, b + th):
        c.line(b-gap, y, b-gap-length, y)
        c.line(b+tw+gap, y, b+tw+gap+length, y)
    c.restoreState()


def background(c, trim_w, trim_h, dark=True):
    pw, ph = (trim_w + 2*BLEED) * MM, (trim_h + 2*BLEED) * MM
    c.setFillColor(NAVY if dark else WHITE)
    c.rect(0, 0, pw, ph, stroke=0, fill=1)
    if dark:
        # Layered translucent-like skyline/data grid using CMYK solids.
        c.setFillColor(NAVY_2)
        c.rect(0, 0, pw, ph * .50, stroke=0, fill=1)
        c.setStrokeColor(PCMYKColor(75, 34, 5, 55))
        c.setLineWidth(.3)
        for i in range(18):
            x = pw * (.05 + i*.055)
            h = ph * (.12 + ((i*37) % 17)/100)
            c.rect(x, ph*.23, pw*.035, h, stroke=1, fill=0)
            for j in range(3):
                c.line(x+pw*.008, ph*.25+j*ph*.035, x+pw*.027, ph*.25+j*ph*.035)


def wave(c, x0, y0, width, amp, colors=(TEAL, BLUE, RED), count=18):
    for j in range(count):
        c.setStrokeColor(colors[j % len(colors)])
        c.setLineWidth(0.45 if j % 3 else 0.8)
        p = c.beginPath()
        y = y0 + (j-count/2) * amp / count
        p.moveTo(x0, y)
        p.curveTo(x0+width*.22, y+amp*(.65-j/count), x0+width*.32, y-amp*.8, x0+width*.52, y)
        p.curveTo(x0+width*.70, y+amp*.85, x0+width*.82, y-amp*(.45+j/count*.2), x0+width, y+amp*.08)
        c.drawPath(p, stroke=1, fill=0)


def hex_icon(c, cx, cy, r, color, kind):
    pts = [(cx+r*math.cos(math.radians(60*i+30)), cy+r*math.sin(math.radians(60*i+30))) for i in range(6)]
    # Soft vector glow and dark hexagonal tile, matching the supplied sketch.
    for grow, width in ((1.10, 7), (1.05, 4)):
        glow = [(cx+r*grow*math.cos(math.radians(60*i+30)), cy+r*grow*math.sin(math.radians(60*i+30))) for i in range(6)]
        c.setStrokeColor(color); c.setLineWidth(width)
        gp = c.beginPath(); gp.moveTo(*glow[0])
        for pt in glow[1:]: gp.lineTo(*pt)
        gp.close(); c.drawPath(gp, stroke=1, fill=0)
    c.setFillColor(PCMYKColor(100,76,45,68)); c.setStrokeColor(color); c.setLineWidth(7)
    p = c.beginPath(); p.moveTo(*pts[0])
    for pt in pts[1:]: p.lineTo(*pt)
    p.close(); c.drawPath(p, stroke=1, fill=1)
    c.setStrokeColor(WHITE); c.setFillColor(WHITE); c.setLineWidth(7)
    if kind == 0:
        c.circle(cx, cy, r*.30, stroke=1, fill=0); c.line(cx+r*.2, cy-r*.22, cx+r*.44, cy-r*.47)
        c.line(cx-r*.18, cy-r*.08, cx-r*.05, cy+r*.07); c.line(cx-r*.05, cy+r*.07, cx+r*.08, cy-r*.02); c.line(cx+r*.08, cy-r*.02, cx+r*.22, cy+r*.22)
        c.circle(cx-r*.18,cy-r*.08,r*.025,stroke=0,fill=1); c.circle(cx+r*.22,cy+r*.22,r*.025,stroke=0,fill=1)
    elif kind == 1:
        # AI spark: a four-point primary sparkle plus two supporting sparks.
        def spark(sx, sy, rr):
            sp=c.beginPath(); sp.moveTo(sx,sy+rr); sp.lineTo(sx+rr*.22,sy+rr*.22); sp.lineTo(sx+rr,sy)
            sp.lineTo(sx+rr*.22,sy-rr*.22); sp.lineTo(sx,sy-rr); sp.lineTo(sx-rr*.22,sy-rr*.22)
            sp.lineTo(sx-rr,sy); sp.lineTo(sx-rr*.22,sy+rr*.22); sp.close(); c.drawPath(sp,stroke=1,fill=0)
        spark(cx,cy,r*.38); spark(cx+r*.42,cy+r*.39,r*.14); spark(cx-r*.43,cy-r*.32,r*.10)
    else:
        p=c.beginPath(); p.moveTo(cx-r*.34,cy+r*.22); p.lineTo(cx+r*.36,cy+r*.40); p.lineTo(cx+r*.06,cy-r*.38); p.lineTo(cx-r*.03,cy-r*.05); p.close(); c.drawPath(p,stroke=1,fill=0)


def make_pdf(path, trim_w, trim_h, draw_fn):
    page = ((trim_w + 2*BLEED)*MM, (trim_h + 2*BLEED)*MM)
    c = canvas.Canvas(str(path), pagesize=page, pageCompression=1, pdfVersion=(1, 7))
    c.setTitle(path.stem)
    c.setAuthor("Meteor, A StoreNext Company")
    draw_fn(c, page[0], page[1])
    trim_marks(c, trim_w, trim_h)
    c.showPage(); c.save()
    # Add explicit press boxes: media/bleed box includes 5 mm; trim box is final size.
    reader = PdfReader(str(path))
    writer = PdfWriter()
    p = reader.pages[0]
    p.bleedbox = RectangleObject([0, 0, page[0], page[1]])
    p.cropbox = RectangleObject([0, 0, page[0], page[1]])
    p.trimbox = RectangleObject([BLEED*MM, BLEED*MM, (BLEED+trim_w)*MM, (BLEED+trim_h)*MM])
    p.artbox = RectangleObject([(BLEED+SAFE)*MM, (BLEED+SAFE)*MM, (BLEED+trim_w-SAFE)*MM, (BLEED+trim_h-SAFE)*MM])
    writer.add_page(p)
    writer.add_metadata({"/Title": path.stem, "/Author": "Meteor, A StoreNext Company", "/Subject": "Print artwork with 5 mm bleed"})
    temp = path.with_suffix(".tmp.pdf")
    with temp.open("wb") as stream: writer.write(stream)
    temp.replace(path)
    reader = PdfReader(str(path))
    page0 = reader.pages[0]
    assert abs(float(page0.mediabox.width) / MM - (trim_w + 2*BLEED)) < .1
    assert abs(float(page0.mediabox.height) / MM - (trim_h + 2*BLEED)) < .1


def draw_wall(c, pw, ph, city_path):
    b=BLEED*MM; w=2000*MM; h=2200*MM
    c.drawImage(str(city_path),0,0,width=pw,height=ph,preserveAspectRatio=False)
    logo(c, b+135*MM, b+h-300*MM, 600*MM)
    c.setFillColor(WHITE); c.setFont("Arial-Bold", 130*MM)
    c.drawString(b+135*MM, b+h-585*MM, "Connected Finance.")
    c.setFillColor(TEAL); c.setFont("Arial-Bold", 125*MM)
    c.drawString(b+135*MM, b+h-755*MM, "From Insight to Action.")
    c.setFillColor(WHITE); c.setFont("Arial", 38*MM)
    c.drawString(b+140*MM, b+h-865*MM, "Treasury. Payments. Financial Operations.")
    labels=[("SEE",("Real-time visibility","across cash and banks"),TEAL,0),("DECIDE",("AI-powered insights","to optimize and plan"),BLUE,1),("EXECUTE",("From decisions","to financial action"),RED,2)]
    for i,(title,subs,col,kind) in enumerate(labels):
        cx=b+(390+i*610)*MM; cy=b+850*MM
        hex_icon(c,cx,cy,125*MM,col,kind)
        c.setFillColor(col); c.setFont("Arial-Bold",46*MM); c.drawCentredString(cx,cy-190*MM,title)
        c.setFillColor(WHITE); c.setFont("Arial",24*MM); c.drawCentredString(cx,cy-250*MM,subs[0]); c.drawCentredString(cx,cy-290*MM,subs[1])
    c.setStrokeColor(TEAL); c.setDash(7,5); c.setLineWidth(2)
    c.line(b+320*MM,b+210*MM,b+1680*MM,b+210*MM)
    c.setDash(); c.setFillColor(WHITE); c.setFont("Arial-Bold",42*MM)
    c.drawString(b+120*MM,b+175*MM,"ERP")
    c.drawCentredString(b+w/2,b+175*MM,"METEOR")
    c.drawRightString(b+w-120*MM,b+175*MM,"BANKS")


def draw_counter(c, pw, ph, city_path):
    b=BLEED*MM; w=1200*MM; h=900*MM
    c.drawImage(str(city_path),0,0,width=pw,height=ph,preserveAspectRatio=False)
    logo(c,b+365*MM,b+h-220*MM,470*MM)
    c.setFillColor(WHITE); c.setFont("Arial-Bold",60*MM)
    c.drawCentredString(b+w/2,b+h-390*MM,"Connected Finance.")
    c.setFillColor(TEAL); c.setFont("Arial-Bold",58*MM)
    c.drawCentredString(b+w/2,b+h-485*MM,"From Insight to Action.")
    c.setFillColor(WHITE); c.setFont("Arial",22*MM)
    c.drawCentredString(b+w/2,b+65*MM,"Treasury. Payments. Financial Operations.")


def draw_rollup(c, pw, ph, watch_path):
    background(c, 850, 2000, False)
    b=BLEED*MM; w=850*MM; h=2000*MM
    c.setFillColor(NAVY); c.rect(0,b+h-330*MM,pw,335*MM,stroke=0,fill=1)
    logo(c,b+175*MM,b+h-245*MM,500*MM)
    c.setFillColor(TEAL); c.rect(b+70*MM,b+h-410*MM,180*MM,9*MM,stroke=0,fill=1)
    c.setFillColor(BLACK); c.setFont("Arial-Bold",88*MM)
    c.drawString(b+70*MM,b+h-545*MM,"Treasury.")
    c.setFillColor(TEAL_DARK); c.setFont("Arial-Bold",88*MM)
    c.drawString(b+70*MM,b+h-670*MM,"Anywhere.")
    c.setFillColor(BLACK); c.setFont("Arial",25*MM)
    c.drawString(b+72*MM,b+h-790*MM,"Stay connected to your cash from anywhere.")
    c.setFillColor(PCMYKColor(0,0,0,16)); c.ellipse(b+165*MM,b+500*MM,b+700*MM,b+590*MM,stroke=0,fill=1)
    c.drawImage(str(watch_path), b+115*MM, b+525*MM, width=620*MM, height=646*MM, preserveAspectRatio=True, mask='auto')
    c.setFillColor(NAVY); c.roundRect(b+65*MM,b+385*MM,720*MM,150*MM,18*MM,stroke=0,fill=1)
    c.setFillColor(WHITE); c.setFont("Arial-Bold",38*MM)
    c.drawString(b+105*MM,b+455*MM,"Win an")
    c.setFillColor(TEAL); c.setFont("Arial-Bold",38*MM); c.drawString(b+310*MM,b+455*MM,"Apple Watch")
    # Deliberately blank QR zone for later insertion.
    c.setStrokeColor(TEAL_DARK); c.setLineWidth(2); c.roundRect(b+275*MM,b+95*MM,300*MM,250*MM,15*MM,stroke=1,fill=0)
    c.setFillColor(MUTED); c.setFont("Arial",18*MM)
    c.drawCentredString(b+w/2,b+55*MM,"Scan to enter")


def main():
    FINAL.mkdir(parents=True, exist_ok=True); PROCESS.mkdir(parents=True, exist_ok=True)
    watch = prepare_watch()
    city = prepare_city_backgrounds()
    make_pdf(FINAL / "W34-meteor-wall-200x220-print.pdf", 2000, 2200, lambda c,pw,ph: draw_wall(c,pw,ph,city["wall"]))
    make_pdf(FINAL / "W34-meteor-counter-120x90-print.pdf", 1200, 900, lambda c,pw,ph: draw_counter(c,pw,ph,city["counter"]))
    make_pdf(FINAL / "W34-meteor-rollup-85x200-print.pdf", 850, 2000, lambda c,pw,ph: draw_rollup(c,pw,ph,watch))
    print("Created 3 PDFs")


if __name__ == "__main__":
    main()
