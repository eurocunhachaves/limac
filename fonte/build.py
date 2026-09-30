"""Gera resumão (PDF), lista de questões (PDF) e baralho Anki (.apkg) de um tema, em duas versões.

Uso: python3 build.py tema_a
  - versão pessoal (com figuras dos livros): ../<slug>/
  - versão pública (só esquemas próprios, vai para o GitHub): ../_publico/<slug>/

Cada módulo de tema define TOPIC = dict(code, slug, title, source, sections, mcq, open, open_extra, cards, occ).
Blocos de seção:
  ("p", txt) | ("h2", txt) | ("ul", [itens]) | ("box", titulo, [itens] ou txt) | ("tip", titulo, txt)
  | ("table", linhas, larguras_cm)
  | ("fig", figura_propria|None, figura_livro|None, legenda, largura_cm)
    figura_propria fica em fig/, figura_livro em fig_livro/ (esta só entra na versão pessoal).
Cartões (cards):
  ("b", frente, verso[, imagem])                         básico; imagem opcional no verso
  ("c", texto_com_{{c1::lacuna}}[, extra[, imagem]])     cloze
  Na versão pública, cartões com imagem de fig_livro/ saem sem a imagem.
  occ = nome do módulo de figuras com OCLUSOES -> cartões de oclusão de imagem.
  occ_img = [(figura_livro, (x0, y0, x1, y1), pergunta, resposta)] -> oclusão sobre figura do livro (só versão pessoal).
Texto aceita a marcação inline do reportlab (<b>, <i>, <sub>, <sup>).
"""
import hashlib
import importlib
import os
import random
import shutil
import sys

import genanki

import html_build
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (CondPageBreak, Image, KeepTogether, ListFlowable, ListItem, PageBreak,
                                Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle)

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_ROOT = os.path.dirname(HERE)

FD = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DV", FD + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DV-B", FD + "DejaVuSans-Bold.ttf"))
registerFontFamily("DV", normal="DV", bold="DV-B", italic="DV", boldItalic="DV-B")

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
    inner.append(Paragraph(content, ST["li"]) if isinstance(content, str) else bullets(content))
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


def is_book(rel):
    return bool(rel) and rel.startswith("fig_livro/")


def book_source(rel):
    return "Guyton & Hall" if "fig_livro/g" in rel else "Porto, Semiologia Médica"


def render_block(b, publico):
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
        _, own, book, caption, width = b
        rel = own if publico else (book or own)  # pessoal prefere o livro; público só esquema próprio
        if not rel:
            return []
        if is_book(rel):
            caption += f" (Fonte: {book_source(rel)}.)"
        img = Image(os.path.join(HERE, rel))
        w = width * cm
        img.drawHeight = w * img.imageHeight / img.imageWidth
        img.drawWidth = w
        return [KeepTogether([img, Paragraph(caption, ST["cap"])])]
    raise ValueError(kind)


def paths(T, publico):
    if publico:
        d = os.path.join(OUT_ROOT, "_publico", T["slug"])
        names = ("resumao.pdf", "questoes.pdf", "flashcards.apkg")
    else:
        d = os.path.join(OUT_ROOT, T["slug"])
        names = (f"Resumao - {T['title']}.pdf", f"Questoes - {T['title']}.pdf", f"Anki - {T['title']}.apkg")
    os.makedirs(d, exist_ok=True)
    return [os.path.join(d, n) for n in names]


def doc_for(path, title):
    return SimpleDocTemplate(path, pagesize=A4, leftMargin=1.8 * cm, rightMargin=1.8 * cm,
                             topMargin=1.6 * cm, bottomMargin=1.7 * cm, title=title)


def build_resumao(T, publico):
    path = paths(T, publico)[0]
    story = [Paragraph(f"Tema {T['code']}. {T['title']}", ST["title"]),
             Paragraph(f"Resumão para a prova da Liga de Cardiologia · Fonte: {T['source']}", ST["sub"])]
    for heading, blocks in T["sections"]:
        need = 3.5 * cm
        if blocks and blocks[0][0] == "fig":  # título + figura de abertura não se separam
            rel = blocks[0][1] if publico else (blocks[0][2] or blocks[0][1])
            if rel:
                img = Image(os.path.join(HERE, rel))
                need = blocks[0][4] * cm * img.imageHeight / img.imageWidth + 2.5 * cm
        story += [CondPageBreak(need), Paragraph(heading, ST["h1"])]
        for b in blocks:
            story += render_block(b, publico)
    doc_for(path, f"Resumão: {T['title']}").build(story, onFirstPage=footer(T["title"]), onLaterPages=footer(T["title"]))
    return path


def answer_flow(ans):
    return [bullets(ans), Spacer(1, 4)] if isinstance(ans, list) else [Paragraph(ans, ST["ans"])]


def build_questoes(T, publico):
    path = paths(T, publico)[1]
    extra = T.get("open_extra", [])
    story = [Paragraph(f"Questões · Tema {T['code']}. {T['title']}", ST["title"]),
             Paragraph(f"{len(T['mcq'])} questões de múltipla escolha, {len(T['open'])} casos clínicos abertos e "
                       f"{len(extra)} perguntas abertas prováveis. Gabarito comentado e respostas-modelo no final. "
                       f"Fonte: {T['source']}", ST["sub"]),
             Paragraph("Parte 1. Múltipla escolha", ST["h1"])]
    L = "ABCDE"
    for i, q in enumerate(T["mcq"], 1):
        items = [Paragraph(f"<b>{i}.</b> {q['q']}", ST["q"])]
        items += [Paragraph(f"{L[j]}) {o}", ST["opt"]) for j, o in enumerate(q["opts"])]
        story.append(KeepTogether(items))
    story.append(Paragraph("Parte 2. Casos clínicos (questões abertas)", ST["h1"]))
    for i, q in enumerate(T["open"], 1):
        story += [Paragraph(f"<b>Caso {i}.</b> {q['q']}", ST["q"]), Spacer(1, 6)]
    if extra:
        story.append(Paragraph("Parte 3. Outras perguntas abertas prováveis", ST["h1"]))
        for i, (q, _) in enumerate(extra, 1):
            story.append(Paragraph(f"<b>{i}.</b> {q}", ST["q"]))
    story.append(PageBreak())
    story.append(Paragraph("Gabarito comentado", ST["title"]))
    story.append(Paragraph(" · ".join(f"{i}-{L[q['a']]}" for i, q in enumerate(T["mcq"], 1)), ST["sub"]))
    for i, q in enumerate(T["mcq"], 1):
        story.append(Paragraph(f"<b>{i}. {L[q['a']]}.</b> {q['c']}", ST["ans"]))
    story.append(Paragraph("Respostas esperadas dos casos clínicos", ST["h1"]))
    for i, q in enumerate(T["open"], 1):
        story.append(Paragraph(f"<b>Caso {i}.</b>", ST["h2"]))
        story += answer_flow(q["a"])
    if extra:
        story.append(Paragraph("Respostas-modelo das perguntas abertas prováveis", ST["h1"]))
        for i, (q, a) in enumerate(extra, 1):
            story.append(Paragraph(f"<b>{i}. {q}</b>", ST["ans"]))
            story += answer_flow(a)
    doc_for(path, f"Questões: {T['title']}").build(story, onFirstPage=footer(T["title"]), onLaterPages=footer(T["title"]))
    return path


# ---------------------------------------------------------------- Anki
def stable_id(s):
    return int(hashlib.md5(s.encode()).hexdigest()[:8], 16) + (1 << 30)


CSS = """
.card{font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif;font-size:19px;line-height:1.45;color:#1f2328;
      background:#f4f1ee;text-align:left;margin:0}
.wrap{max-width:720px;margin:14px auto;background:#fff;border-radius:14px;box-shadow:0 2px 10px rgba(0,0,0,.08);overflow:hidden}
.head{background:linear-gradient(90deg,#9b1c2c,#c2415a);color:#fff;font-size:12px;letter-spacing:.04em;
      text-transform:uppercase;padding:7px 16px}
.body{padding:16px 20px 18px}
.q{font-size:21px;font-weight:600}
.a{margin-top:12px;padding:12px 14px;background:#fbeaec;border-left:4px solid #9b1c2c;border-radius:6px}
.extra{margin-top:10px;font-size:15px;color:#555}
.src{margin-top:12px;font-size:11px;color:#999;text-align:right}
img{max-width:100%;height:auto;border-radius:8px;margin:10px auto 0;display:block}
b{color:#9b1c2c}
.cloze{font-weight:700;color:#fff;background:#9b1c2c;padding:0 6px;border-radius:5px}
.hint{font-size:13px;color:#e8590c;font-weight:600;margin-bottom:4px}
.qm{background:#e8590c;color:#fff;padding:0 5px;border-radius:4px}
.nightMode .card,.night_mode .card{background:#1e1e1e}
.nightMode .wrap,.night_mode .wrap{background:#2a2a2a;color:#eee;box-shadow:none}
.nightMode .a,.night_mode .a{background:#3a2328;color:#eee}
.nightMode .extra,.night_mode .extra{color:#bbb}
.nightMode b,.night_mode b{color:#ff8fa3}
.nightMode img,.night_mode img{background:#fff;padding:4px}
"""

HEAD = '<div class="wrap"><div class="head">{{Tema}}</div><div class="body">'
SRC = '{{#Fonte}}<div class="src">Imagem: {{Fonte}}</div>{{/Fonte}}'
END = '</div></div>'

BASIC = genanki.Model(
    stable_id("limac-basic-v2"), "LIMAC · Básico",
    fields=[{"name": n} for n in ("Frente", "Verso", "Imagem", "Tema", "Fonte")],
    templates=[{"name": "Cartão",
                "qfmt": HEAD + '<div class="q">{{Frente}}</div>' + END,
                "afmt": HEAD + '<div class="q">{{Frente}}</div><div class="a">{{Verso}}</div>{{Imagem}}' + SRC + END}],
    css=CSS)

CLOZE = genanki.Model(
    stable_id("limac-cloze-v2"), "LIMAC · Lacuna",
    fields=[{"name": n} for n in ("Texto", "Extra", "Imagem", "Tema", "Fonte")],
    templates=[{"name": "Lacuna",
                "qfmt": HEAD + '<div class="q">{{cloze:Texto}}</div>' + END,
                "afmt": HEAD + '<div class="q">{{cloze:Texto}}</div>{{#Extra}}<div class="extra">{{Extra}}</div>{{/Extra}}'
                               '{{Imagem}}' + SRC + END}],
    css=CSS, model_type=genanki.Model.CLOZE)

OCC = genanki.Model(
    stable_id("limac-oclusao-v2"), "LIMAC · Oclusão de imagem",
    fields=[{"name": n} for n in ("Pergunta", "ImagemOculta", "ImagemCompleta", "Resposta", "Tema")],
    templates=[{"name": "Oclusão",
                "qfmt": HEAD + '<div class="hint">O que está sob o <span class="qm">?</span></div>'
                               '<div class="q">{{Pergunta}}</div>{{ImagemOculta}}' + END,
                "afmt": HEAD + '<div class="q">{{Pergunta}}</div><div class="a">{{Resposta}}</div>{{ImagemCompleta}}' + END}],
    css=CSS)


def build_anki(T, publico):
    deck = genanki.Deck(stable_id("liga-cardio::" + T["slug"]), f"Liga de Cardiologia::{T['code']}. {T['title']}")
    tema = f"Tema {T['code']} · {T['title']}"
    tags = ["limac", f"tema_{T['code']}"]
    media = {}

    def img_html(rel):
        if not rel:
            return ""
        name = f"limac_{T['code']}_{os.path.basename(rel)}"
        media[name] = os.path.join(HERE, rel)
        return f'<img src="{name}">'

    for card in T["cards"]:
        kind = card[0]
        rel = card[3] if len(card) > 3 else None
        if publico and is_book(rel):
            rel = None  # versão pública: mantém o cartão, sem a figura do livro
        src = book_source(rel) if is_book(rel) else (html_build.credit_text(rel) if html_build.is_web(rel) else "")
        if kind == "b":
            deck.add_note(genanki.Note(model=BASIC, fields=[card[1], card[2], img_html(rel), tema, src],
                                       guid=genanki.guid_for(T["slug"], "b", card[1]), tags=tags))
        elif kind == "c":
            extra = card[2] if len(card) > 2 else ""
            deck.add_note(genanki.Note(model=CLOZE, fields=[card[1], extra, img_html(rel), tema, src],
                                       guid=genanki.guid_for(T["slug"], "c", card[1]), tags=tags + ["lacuna"]))
    if T.get("occ"):
        for fig, key, pergunta, resposta in importlib.import_module(T["occ"]).OCLUSOES:
            deck.add_note(genanki.Note(
                model=OCC,
                fields=[pergunta, img_html(f"fig/{fig}__occ_{key}.png"), img_html(f"fig/{fig}.png"), resposta, tema],
                guid=genanki.guid_for(T["slug"], "occ", fig, key), tags=tags + ["oclusao"]))
    if not publico:  # oclusão sobre figuras dos livros (só na versão pessoal)
        from PIL import Image as PImage, ImageDraw, ImageFont
        os.makedirs(os.path.join(HERE, "fig_livro", "occ"), exist_ok=True)
        for i, (rel, bx, pergunta, resposta) in enumerate(T.get("occ_img", [])):
            im = PImage.open(os.path.join(HERE, rel)).convert("RGB")
            dr = ImageDraw.Draw(im)
            dr.rounded_rectangle(bx, radius=5, fill="#e8590c")
            font = ImageFont.truetype(FD + "DejaVuSans-Bold.ttf", max(12, int((bx[3] - bx[1]) * 0.7)))
            dr.text(((bx[0] + bx[2]) / 2, (bx[1] + bx[3]) / 2), "?", fill="white", font=font, anchor="mm")
            occ_rel = f"fig_livro/occ/{os.path.splitext(os.path.basename(rel))[0]}_{i}.png"
            im.save(os.path.join(HERE, occ_rel))
            deck.add_note(genanki.Note(
                model=OCC, fields=[pergunta, img_html(occ_rel), img_html(rel), resposta, tema],
                guid=genanki.guid_for(T["slug"], "occimg", rel, str(bx)), tags=tags + ["oclusao"]))
    path = paths(T, publico)[2]
    # o genanki usa o nome do arquivo como nome da mídia: copia com o prefixo do tema para uma pasta temporária
    tmp = os.path.join(os.path.dirname(path), ".media")
    os.makedirs(tmp, exist_ok=True)
    files = []
    for name, src in media.items():
        shutil.copy(src, os.path.join(tmp, name))
        files.append(os.path.join(tmp, name))
    pkg = genanki.Package(deck)
    pkg.media_files = files
    pkg.write_to_file(path)
    shutil.rmtree(tmp)
    return path, len(deck.notes)


def balance(T):
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


if __name__ == "__main__":
    sys.path.insert(0, HERE)
    T = importlib.import_module(sys.argv[1]).TOPIC
    balance(T)
    for publico in (False, True):
        print(html_build.build_resumao_pdf(T, publico, paths(T, publico)[0]))
        print(build_questoes(T, publico))
        print(build_anki(T, publico))
    import json
    with open(os.path.join(OUT_ROOT, "_publico", T["slug"], "quiz.json"), "w") as f:
        json.dump(html_build.quiz_json(T), f, ensure_ascii=False)
    from collections import Counter
    print("gabarito:", dict(Counter("ABCDE"[q["a"]] for q in T["mcq"])), "MCQ:", len(T["mcq"]))
