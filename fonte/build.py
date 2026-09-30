"""Gera resumão (PDF), lista de questões (PDF) e baralho Anki (.apkg) de um tema.

Uso: python3 build.py tema_a   (carrega tema_a.py deste diretório)
Cada módulo de tema define TOPIC = dict(code, slug, title, source, sections, mcq, open, cards).
Blocos de seção: ("p", txt) | ("ul", [itens]) | ("box", titulo, [itens] ou txt)
                 | ("table", linhas, larguras_cm) | ("fig", caminho_png, legenda, largura_cm)
Texto aceita a marcação inline do reportlab (<b>, <i>, <sub>, <sup>).
"""
import hashlib
import importlib
import os
import random
import sys

import genanki
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (CondPageBreak, Image, KeepTogether, ListFlowable, ListItem, PageBreak,
                                Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_ROOT = os.path.dirname(HERE)

FD = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DV", FD + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DV-B", FD + "DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DVS", FD + "DejaVuSerif.ttf"))
pdfmetrics.registerFont(TTFont("DVS-B", FD + "DejaVuSerif-Bold.ttf"))
from reportlab.pdfbase.pdfmetrics import registerFontFamily
registerFontFamily("DV", normal="DV", bold="DV-B", italic="DV", boldItalic="DV-B")
registerFontFamily("DVS", normal="DVS", bold="DVS-B", italic="DVS", boldItalic="DVS-B")

RED = colors.HexColor("#9b1c2c")
RED_L = colors.HexColor("#fbeaec")
BLUE_L = colors.HexColor("#eaf1fb")
GREY = colors.HexColor("#555555")

ST = {
    "title": ParagraphStyle("title", fontName="DV-B", fontSize=20, leading=24, textColor=RED, spaceAfter=4),
    "sub": ParagraphStyle("sub", fontName="DV", fontSize=9.5, leading=12, textColor=GREY, spaceAfter=10),
    "h1": ParagraphStyle("h1", fontName="DV-B", fontSize=13.5, leading=17, textColor=RED, spaceBefore=10, spaceAfter=4, keepWithNext=1),
    "h2": ParagraphStyle("h2", fontName="DV-B", fontSize=11, leading=14, spaceBefore=6, spaceAfter=2, keepWithNext=1),
    "p": ParagraphStyle("p", fontName="DV", fontSize=9.6, leading=13.2, alignment=TA_JUSTIFY, spaceAfter=4),
    "li": ParagraphStyle("li", fontName="DV", fontSize=9.6, leading=13),
    "box_t": ParagraphStyle("box_t", fontName="DV-B", fontSize=9.8, leading=13, textColor=RED),
    "cell": ParagraphStyle("cell", fontName="DV", fontSize=8.6, leading=11),
    "cellh": ParagraphStyle("cellh", fontName="DV-B", fontSize=8.8, leading=11, textColor=colors.white),
    "cap": ParagraphStyle("cap", fontName="DV", fontSize=8.3, leading=10.5, textColor=GREY, alignment=TA_CENTER, spaceAfter=6),
    "q": ParagraphStyle("q", fontName="DV", fontSize=9.8, leading=13.4, spaceBefore=6, spaceAfter=2, alignment=TA_JUSTIFY),
    "opt": ParagraphStyle("opt", fontName="DV", fontSize=9.6, leading=12.6, leftIndent=14),
    "ans": ParagraphStyle("ans", fontName="DV", fontSize=9.3, leading=12.6, alignment=TA_JUSTIFY, spaceAfter=5),
}
PAGE_W = A4[0] - 3.6 * cm


def footer(title):
    def draw(canv, doc):
        canv.saveState()
        canv.setFont("DV", 7.5)
        canv.setFillColor(GREY)
        canv.drawString(1.8 * cm, 1.1 * cm, title)
        canv.drawRightString(A4[0] - 1.8 * cm, 1.1 * cm, f"{doc.page}")
        canv.restoreState()
    return draw


def bullets(items, style="li"):
    return ListFlowable(
        [ListItem(Paragraph(i, ST[style]), leftIndent=12, value="•") for i in items],
        bulletType="bullet", start="•", leftIndent=12, bulletFontName="DV", bulletFontSize=8)


def box(title, content, bg=RED_L, border=RED):
    inner = [Paragraph(title, ST["box_t"])] if title else []
    if isinstance(content, str):
        inner.append(Paragraph(content, ST["li"]))
    else:
        inner.append(bullets(content))
    t = Table([[inner]], colWidths=[PAGE_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("LINEBEFORE", (0, 0), (0, -1), 3, border),
        ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return KeepTogether([Spacer(1, 3), t, Spacer(1, 5)])


def table(rows, widths):
    data = [[Paragraph(c, ST["cellh"] if r == 0 else ST["cell"]) for c in row] for r, row in enumerate(rows)]
    t = Table(data, colWidths=[w * cm for w in widths], repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), RED),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f6f6f6")]),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#cccccc")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ]))
    return KeepTogether([Spacer(1, 3), t, Spacer(1, 6)])


def render_block(b):
    kind = b[0]
    if kind == "p":
        return [Paragraph(b[1], ST["p"])]
    if kind == "h2":
        return [CondPageBreak(3 * cm), Paragraph(b[1], ST["h2"])]
    if kind == "ul":
        return [bullets(b[1]), Spacer(1, 4)]
    if kind == "box":
        return [box(b[1], b[2])]
    if kind == "tip":
        return [box(b[1], b[2], bg=BLUE_L, border=colors.HexColor("#2a5ca8"))]
    if kind == "table":
        return [table(b[1], b[2])]
    if kind == "fig":
        path = os.path.join(HERE, b[1])
        w = b[3] * cm
        img = Image(path)
        img.drawHeight = w * img.imageHeight / img.imageWidth
        img.drawWidth = w
        return [KeepTogether([img, Paragraph(b[2], ST["cap"])])]
    raise ValueError(kind)


def out_dir(T):
    d = os.path.join(OUT_ROOT, T["slug"])
    os.makedirs(d, exist_ok=True)
    return d


def build_resumao(T):
    path = os.path.join(out_dir(T), f"Resumao - {T['title']}.pdf")
    doc = SimpleDocTemplate(path, pagesize=A4, leftMargin=1.8 * cm, rightMargin=1.8 * cm,
                            topMargin=1.6 * cm, bottomMargin=1.7 * cm, title=f"Resumão: {T['title']}")
    story = [Paragraph(f"Tema {T['code']}. {T['title']}", ST["title"]),
             Paragraph(f"Resumão para a prova da Liga de Cardiologia · Fonte: {T['source']}", ST["sub"])]
    for heading, blocks in T["sections"]:
        story += [CondPageBreak(3.5 * cm), Paragraph(heading, ST["h1"])]
        for b in blocks:
            story += render_block(b)
    doc.build(story, onFirstPage=footer(T["title"]), onLaterPages=footer(T["title"]))
    return path


def build_questoes(T):
    path = os.path.join(out_dir(T), f"Questoes - {T['title']}.pdf")
    doc = SimpleDocTemplate(path, pagesize=A4, leftMargin=1.8 * cm, rightMargin=1.8 * cm,
                            topMargin=1.6 * cm, bottomMargin=1.7 * cm, title=f"Questões: {T['title']}")
    story = [Paragraph(f"Questões · Tema {T['code']}. {T['title']}", ST["title"]),
             Paragraph(f"{len(T['mcq'])} questões de múltipla escolha e {len(T['open'])} questões abertas "
                       f"(casos clínicos). Gabarito comentado no final. Fonte: {T['source']}", ST["sub"]),
             Paragraph("Parte 1. Múltipla escolha", ST["h1"])]
    L = "ABCDE"
    for i, q in enumerate(T["mcq"], 1):
        items = [Paragraph(f"<b>{i}.</b> {q['q']}", ST["q"])]
        items += [Paragraph(f"{L[j]}) {o}", ST["opt"]) for j, o in enumerate(q["opts"])]
        story.append(KeepTogether(items))
    story.append(Paragraph("Parte 2. Questões abertas", ST["h1"]))
    for i, q in enumerate(T["open"], 1):
        story.append(Paragraph(f"<b>Caso {i}.</b> {q['q']}", ST["q"]))
        story.append(Spacer(1, 8))
    story.append(PageBreak())
    story.append(Paragraph("Gabarito comentado", ST["title"]))
    story.append(Paragraph(" · ".join(f"{i}-{L[q['a']]}" for i, q in enumerate(T["mcq"], 1)), ST["sub"]))
    for i, q in enumerate(T["mcq"], 1):
        story.append(Paragraph(f"<b>{i}. {L[q['a']]}.</b> {q['c']}", ST["ans"]))
    story.append(Paragraph("Respostas esperadas das questões abertas", ST["h1"]))
    for i, q in enumerate(T["open"], 1):
        story.append(Paragraph(f"<b>Caso {i}.</b>", ST["h2"]))
        ans = q["a"]
        story += [bullets(ans), Spacer(1, 4)] if isinstance(ans, list) else [Paragraph(ans, ST["ans"])]
    doc.build(story, onFirstPage=footer(T["title"]), onLaterPages=footer(T["title"]))
    return path


def stable_id(s):
    return int(hashlib.md5(s.encode()).hexdigest()[:8], 16) + (1 << 30)


CSS = """.card{font-family:Arial,Helvetica,sans-serif;font-size:20px;text-align:center;color:#222;background:#fff}
.back{margin-top:8px;font-size:18px;text-align:left;display:inline-block;max-width:680px}
.tag{font-size:12px;color:#9b1c2c;margin-bottom:10px}"""

MODEL = genanki.Model(
    stable_id("liga-cardio-basic-v1"), "Liga Cardio · Básico",
    fields=[{"name": "Frente"}, {"name": "Verso"}, {"name": "Tema"}],
    templates=[{
        "name": "Cartão",
        "qfmt": '<div class="tag">{{Tema}}</div>{{Frente}}',
        "afmt": '{{FrontSide}}<hr id="answer"><div class="back">{{Verso}}</div>',
    }],
    css=CSS)


def build_anki(T):
    deck = genanki.Deck(stable_id("liga-cardio::" + T["slug"]),
                        f"Liga de Cardiologia::{T['code']}. {T['title']}")
    tag = f"Tema {T['code']}. {T['title']}"
    for front, back in T["cards"]:
        deck.add_note(genanki.Note(model=MODEL, fields=[front, back, tag],
                                   guid=genanki.guid_for(T["slug"], front),
                                   tags=["liga_cardio", f"tema_{T['code']}"]))
    path = os.path.join(out_dir(T), f"Anki - {T['title']}.apkg")
    genanki.Package(deck).write_to_file(path)
    return path


if __name__ == "__main__":
    sys.path.insert(0, HERE)
    T = importlib.import_module(sys.argv[1]).TOPIC
    free = [q for q in T["mcq"] if not q.get("keep")]
    targets = [i % 5 for i in range(len(free))]
    random.Random(T["slug"]).shuffle(targets)
    for q, tgt in zip(free, targets):  # posição do gabarito equilibrada e estável entre execuções
        assert len(q["opts"]) == 5 and 0 <= q["a"] < 5, q["q"]
        right = q["opts"][q["a"]]
        others = [o for j, o in enumerate(q["opts"]) if j != q["a"]]
        random.Random(q["q"]).shuffle(others)
        others.insert(tgt, right)
        q["opts"], q["a"] = others, tgt
    for fn in (build_resumao, build_questoes, build_anki):
        print(fn(T))
    from collections import Counter
    print("gabarito:", Counter("ABCDE"[q["a"]] for q in T["mcq"]), "cards:", len(T["cards"]))
