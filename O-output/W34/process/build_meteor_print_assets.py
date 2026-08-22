from pathlib import Path
import math
import re
import xml.etree.ElementTree as ET

from PIL import Image, ImageEnhance, ImageFilter
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
SOURCE_MOCKUP = Path(r"C:\Users\rant\AppData\Local\Temp\codex-clipboard-966f5802-ec45-45ce-b245-9ba1e4f1b6ba.png")
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
    """Crop the exact supplied watch from the user's reference and prepare CMYK print asset."""
    out = PROCESS / "meteor-watch-from-supplied-reference.jpg"
    im = Image.open(SOURCE_MOCKUP).convert("RGB")
    # Exact watch region from the supplied 1536 x 1024 reference.
    crop = im.crop((970, 378, 1206, 632))
    # Remove surrounding off-white while retaining the soft product shadow.
    bg = Image.new("RGB", crop.size, (255, 255, 255))
    px = crop.load()
    mask = Image.new("L", crop.size, 0)
    mp = mask.load()
    for y in range(crop.height):
        for x in range(crop.width):
            r, g, b = px[x, y]
            delta = max(abs(r-g), abs(g-b), abs(r-b))
            darkness = 255 - min(r, g, b)
            a = max(0, min(255, int((darkness - 5) * 5.8 + delta * 1.5)))
            mp[x, y] = a
    mask = mask.filter(ImageFilter.GaussianBlur(1.2))
    rgba = Image.new("RGBA", crop.size, (255, 255, 255, 0))
    rgba.paste(crop, (0, 0), mask)
    rgba = rgba.resize((1758, 1770), Image.Resampling.LANCZOS)
    sharp = ImageEnhance.Sharpness(rgba).enhance(1.35)
    # Composite onto white because rollup artwork is intentionally light.
    white = Image.new("RGB", sharp.size, "white")
    white.paste(sharp, mask=sharp.getchannel("A"))
    white.convert("CMYK").save(out, quality=96, dpi=(300, 300), subsampling=0)
    return out


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
    c.setStrokeColor(color); c.setLineWidth(2.5)
    p = c.beginPath(); p.moveTo(*pts[0])
    for pt in pts[1:]: p.lineTo(*pt)
    p.close(); c.drawPath(p, stroke=1, fill=0)
    c.setStrokeColor(WHITE); c.setLineWidth(2)
    if kind == 0:
        c.circle(cx, cy, r*.30, stroke=1, fill=0); c.line(cx+r*.2, cy-r*.22, cx+r*.44, cy-r*.47)
        c.line(cx-r*.18, cy-r*.08, cx-r*.05, cy+r*.07); c.line(cx-r*.05, cy+r*.07, cx+r*.08, cy-r*.02); c.line(cx+r*.08, cy-r*.02, cx+r*.22, cy+r*.22)
    elif kind == 1:
        for i, h in enumerate((.25,.45,.67)):
            c.rect(cx-r*.34+i*r*.25, cy-r*.33, r*.16, r*h, stroke=1, fill=0)
        c.line(cx-r*.38, cy-r*.38, cx+r*.38, cy-r*.38)
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


def draw_wall(c, pw, ph):
    background(c, 2000, 2200, True)
    b=BLEED*MM; w=2000*MM; h=2200*MM
    logo(c, b+120*MM, b+h-310*MM, 600*MM)
    c.setFillColor(WHITE); c.setFont("Arial-Bold", 128)
    c.drawString(b+120*MM, b+h-610*MM, "Connected Finance.")
    c.setFillColor(TEAL); c.drawString(b+120*MM, b+h-775*MM, "From Insight to Action.")
    c.setFillColor(WHITE); c.setFont("Arial", 52)
    c.drawString(b+120*MM, b+h-900*MM, "Treasury. Payments. Financial Operations.")
    wave(c, b, b+500*MM, w, 300*MM)
    labels=[("SEE","Real-time visibility",TEAL,0),("DECIDE","AI-supported insight",BLUE,1),("EXECUTE","From decision to action",RED,2)]
    for i,(title,sub,col,kind) in enumerate(labels):
        cx=b+(390+i*610)*MM; cy=b+920*MM
        hex_icon(c,cx,cy,125*MM,col,kind)
        c.setFillColor(col); c.setFont("Arial-Bold",58); c.drawCentredString(cx,cy-190*MM,title)
        c.setFillColor(WHITE); c.setFont("Arial",36); c.drawCentredString(cx,cy-255*MM,sub)
    c.setStrokeColor(TEAL); c.setDash(7,5); c.setLineWidth(2)
    c.line(b+300*MM,b+250*MM,b+1700*MM,b+250*MM)
    c.setDash(); c.setFillColor(WHITE); c.setFont("Arial-Bold",70)
    c.drawString(b+120*MM,b+215*MM,"ERP")
    c.drawCentredString(b+w/2,b+215*MM,"METEOR")
    c.drawRightString(b+w-120*MM,b+215*MM,"BANKS")


def draw_counter(c, pw, ph):
    background(c, 1200, 900, True)
    b=BLEED*MM; w=1200*MM; h=900*MM
    logo(c,b+90*MM,b+h-230*MM,470*MM)
    c.setFillColor(WHITE); c.setFont("Arial-Bold",72)
    c.drawString(b+90*MM,b+h-390*MM,"Connected Finance.")
    c.setFillColor(TEAL); c.drawString(b+90*MM,b+h-490*MM,"From Insight to Action.")
    wave(c,b-10*MM,b+205*MM,w+20*MM,180*MM,(TEAL,BLUE),22)
    c.setFillColor(WHITE); c.setFont("Arial",30)
    c.drawString(b+90*MM,b+95*MM,"Treasury. Payments. Financial Operations.")


def draw_rollup(c, pw, ph, watch_path):
    background(c, 850, 2000, False)
    b=BLEED*MM; w=850*MM; h=2000*MM
    # Dark logo panel preserves the official white/red vector mark.
    c.setFillColor(NAVY); c.roundRect(b+65*MM,b+h-330*MM,720*MM,230*MM,18*MM,stroke=0,fill=1)
    logo(c,b+115*MM,b+h-285*MM,620*MM)
    c.setFillColor(BLACK); c.setFont("Arial-Bold",105)
    c.drawString(b+70*MM,b+h-535*MM,"Treasury.")
    c.setFillColor(TEAL_DARK); c.drawString(b+70*MM,b+h-670*MM,"Anywhere.")
    c.setFillColor(BLACK); c.setFont("Arial",40)
    c.drawString(b+70*MM,b+h-770*MM,"Stay connected to your cash from anywhere.")
    c.drawImage(str(watch_path), b+145*MM, b+560*MM, width=560*MM, height=603*MM, preserveAspectRatio=True, mask='auto')
    c.setFillColor(BLACK); c.setFont("Arial-Bold",68)
    c.drawString(b+90*MM,b+590*MM,"Win an")
    c.setFillColor(TEAL_DARK); c.drawString(b+90*MM,b+505*MM,"Apple Watch")
    # Deliberately blank QR zone for later insertion.
    c.setStrokeColor(TEAL_DARK); c.setLineWidth(2); c.roundRect(b+235*MM,b+150*MM,380*MM,300*MM,15*MM,stroke=1,fill=0)
    c.setFillColor(MUTED); c.setFont("Arial",28)
    c.drawCentredString(b+w/2,b+110*MM,"Scan to enter")


def main():
    FINAL.mkdir(parents=True, exist_ok=True); PROCESS.mkdir(parents=True, exist_ok=True)
    watch = prepare_watch()
    make_pdf(FINAL / "W34-meteor-wall-200x220-print.pdf", 2000, 2200, draw_wall)
    make_pdf(FINAL / "W34-meteor-counter-120x90-print.pdf", 1200, 900, draw_counter)
    make_pdf(FINAL / "W34-meteor-rollup-85x200-print.pdf", 850, 2000, lambda c,pw,ph: draw_rollup(c,pw,ph,watch))
    print("Created 3 PDFs")


if __name__ == "__main__":
    main()
