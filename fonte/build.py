"""Gera o resumão (PDF) e o baralho do Anki (.apkg) de um tema.

Uso: python3 build.py tema_a   ->  ../<slug>/Resumao - <título>.pdf  e  ../<slug>/Anki - <título>.apkg

Cada módulo de tema define TOPIC = dict(code, slug, title, source, sections, cards[, occ_img, readme]).
Blocos de seção (diagramados em HTML/CSS por html_build.py):
  ("p", txt) | ("h2", txt) | ("ul", [itens]) | ("box", titulo, [itens] ou txt) | ("tip", titulo, txt)
  | ("table", linhas, larguras_cm)
  | ("fig", imagem_web|None, figura_livro|None, legenda, largura_cm)   figura do livro tem prioridade
  | ("web", imagem_web, largura_cm[, legenda])
Cartões (cards):
  ("b", frente, verso[, imagem])                         básico; imagem opcional no verso
  ("c", texto_com_{{c1::lacuna}}[, extra[, imagem]])     cloze
  occ_img = [(figura_livro, (x0, y0, x1, y1), pergunta, resposta)] -> oclusão de imagem sobre a figura do livro.
"""
import hashlib
import importlib
import os
import shutil
import sys

import genanki

import html_build

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_ROOT = os.path.dirname(HERE)
FD = "/usr/share/fonts/truetype/dejavu/"


def paths(T):
    d = os.path.join(OUT_ROOT, T["slug"])
    names = (f"Resumao - {T['title']}.pdf", f"Anki - {T['title']}.apkg")
    os.makedirs(d, exist_ok=True)
    return [os.path.join(d, n) for n in names]



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


def build_anki(T):
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
        if rel and rel.startswith("fig/"):
            rel = None  # esquemas próprios foram abandonados: o cartão fica sem imagem
        src = html_build.book_ref(rel) if html_build.is_book(rel) else (html_build.credit_text(rel) if html_build.is_web(rel) else "")
        if kind == "b":
            deck.add_note(genanki.Note(model=BASIC, fields=[card[1], card[2], img_html(rel), tema, src],
                                       guid=genanki.guid_for(T["slug"], "b", card[1]), tags=tags))
        elif kind == "c":
            extra = card[2] if len(card) > 2 else ""
            deck.add_note(genanki.Note(model=CLOZE, fields=[card[1], extra, img_html(rel), tema, src],
                                       guid=genanki.guid_for(T["slug"], "c", card[1]), tags=tags + ["lacuna"]))
    # oclusão de imagem sobre figuras dos livros: o rótulo é dado pelo texto (achado por OCR) ou por uma caixa em pixels
    if T.get("occ_img"):
        import ocr
        from PIL import Image as PImage, ImageDraw, ImageFont
        os.makedirs(os.path.join(HERE, "fig_livro", "occ"), exist_ok=True)
        for i, (rel, bx, pergunta, resposta) in enumerate(T["occ_img"]):
            if isinstance(bx, str):
                bx = ocr.find_box(rel, bx)
            elif isinstance(bx[0], str):  # (rótulo, n-ésima ocorrência de cima para baixo[, (cresce x0, y0, x1, y1)])
                bx = ocr.find_box(rel, bx[0], nth=bx[1], grow=bx[2] if len(bx) > 2 else (0, 0, 0, 0))
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
    path = paths(T)[1]
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


if __name__ == "__main__":
    sys.path.insert(0, HERE)
    T = importlib.import_module(sys.argv[1]).TOPIC
    print(html_build.build_resumao_pdf(T, False, paths(T)[0]))
    print(build_anki(T))
