"""Baralhos Anki (.apkg) dos temas: cartões básicos, de lacuna e de oclusão
de imagem sobre figuras dos livros."""
import hashlib, json, re, subprocess
from pathlib import Path

import genanki
from PIL import Image, ImageDraw, ImageFont

from build import md2html, ref_livro

CSS = """
.card { font-family: "Inter", "Segoe UI", system-ui, sans-serif; font-size: 19px;
  line-height: 1.45; color: #1d2026; background: #fbfaf8; text-align: left;
  max-width: 680px; margin: 0 auto; padding: 18px 20px; }
.nightMode.card, .night_mode .card { color: #eceef1; background: #1e2024; }
.tag { display: inline-block; font-size: 11px; letter-spacing: .08em; text-transform: uppercase;
  font-weight: 700; color: #fff; background: #8a1b2b; padding: 3px 9px; border-radius: 10px; }
.q { font-size: 21px; font-weight: 600; margin: 14px 0 6px; }
.a { margin-top: 10px; padding: 12px 14px; border-left: 4px solid #1f4e79;
  background: #eaf1f8; border-radius: 0 6px 6px 0; }
.nightMode .a, .night_mode .a { background: #24303d; }
.extra { margin-top: 12px; font-size: 15px; color: #4a4f57; }
.nightMode .extra, .night_mode .extra { color: #b6bcc5; }
.fonte { margin-top: 14px; font-size: 12px; color: #7a7f88; font-style: italic; }
img { max-width: 100%; height: auto; display: block; margin: 10px auto; border-radius: 4px; }
.cloze { font-weight: 700; color: #8a1b2b; }
.nightMode .cloze, .night_mode .cloze { color: #ff9aa8; }
hr#answer { border: none; border-top: 1px solid #d9dce1; margin: 14px 0; }
b { color: #8a1b2b; } .nightMode b, .night_mode b { color: #ff9aa8; }
"""


def _id(txt: str) -> int:
    return int(hashlib.sha1(txt.encode()).hexdigest()[:8], 16)


BASICO = genanki.Model(
    _id("limac-basico-v2"), "LIMAC · Básico",
    fields=[{"name": "Tema"}, {"name": "Frente"}, {"name": "Verso"}, {"name": "Imagem"}, {"name": "Fonte"}],
    templates=[{
        "name": "Cartão",
        "qfmt": '<span class="tag">{{Tema}}</span><div class="q">{{Frente}}</div>',
        "afmt": '{{FrontSide}}<hr id="answer"><div class="a">{{Verso}}</div>{{#Imagem}}{{Imagem}}{{/Imagem}}'
                '{{#Fonte}}<div class="fonte">{{Fonte}}</div>{{/Fonte}}',
    }], css=CSS)

LACUNA = genanki.Model(
    _id("limac-lacuna-v2"), "LIMAC · Lacuna",
    fields=[{"name": "Texto"}, {"name": "Tema"}, {"name": "Extra"}, {"name": "Fonte"}],
    templates=[{
        "name": "Lacuna",
        "qfmt": '<span class="tag">{{Tema}}</span><div class="q">{{cloze:Texto}}</div>',
        "afmt": '<span class="tag">{{Tema}}</span><div class="q">{{cloze:Texto}}</div>'
                '{{#Extra}}<div class="extra">{{Extra}}</div>{{/Extra}}'
                '{{#Fonte}}<div class="fonte">{{Fonte}}</div>{{/Fonte}}',
    }], css=CSS, model_type=genanki.Model.CLOZE)

OCLUSAO = genanki.Model(
    _id("limac-oclusao-v2"), "LIMAC · Oclusão de imagem",
    fields=[{"name": "Tema"}, {"name": "Pergunta"}, {"name": "ImagemPergunta"}, {"name": "ImagemResposta"},
            {"name": "Resposta"}, {"name": "Fonte"}],
    templates=[{
        "name": "Oclusão",
        "qfmt": '<span class="tag">{{Tema}}</span><div class="q">{{Pergunta}}</div>{{ImagemPergunta}}',
        "afmt": '<span class="tag">{{Tema}}</span><div class="q">{{Pergunta}}</div>'
                '<div class="a">{{Resposta}}</div>{{ImagemResposta}}<div class="fonte">{{Fonte}}</div>',
    }], css=CSS)


# ------------------------------------------------------------ oclusão
OCR_CACHE = {}


def _ocr(caminho: Path):
    """Caixas de palavras (tesseract, português) na imagem ampliada 3x."""
    chave = str(caminho)
    if chave in OCR_CACHE:
        return OCR_CACHE[chave]
    img = Image.open(caminho).convert("L")
    f = 3
    big = img.resize((img.width * f, img.height * f), Image.LANCZOS)
    tmp = Path("/tmp/claude-0/ocr_tmp.png")
    tmp.parent.mkdir(parents=True, exist_ok=True)
    big.save(tmp)
    out = subprocess.run(["tesseract", str(tmp), "-", "-l", "por", "--psm", "11", "tsv"],
                         capture_output=True, text=True).stdout
    palavras = []
    for ln in out.splitlines()[1:]:
        c = ln.split("\t")
        if len(c) < 12 or not c[11].strip():
            continue
        x, y, w, h = (int(v) // f for v in c[6:10])
        palavras.append((c[11].strip(), x, y, w, h))
    OCR_CACHE[chave] = palavras
    return palavras


def _norm(s):
    import unicodedata
    s = unicodedata.normalize("NFD", s.lower())
    return "".join(ch for ch in s if ch.isalnum())


def localiza(caminho: Path, alvo):
    """alvo: tupla (x0,y0,x1,y1) em pixels, ou texto do rótulo (uma ou mais palavras
    em sequência), opcionalmente ("texto", n) para a n-ésima ocorrência."""
    if isinstance(alvo, tuple) and len(alvo) == 4 and all(isinstance(v, int) for v in alvo):
        return alvo
    n = 0
    if isinstance(alvo, tuple):
        alvo, n = alvo
    toks = [_norm(t) for t in alvo.split()]
    pal = _ocr(caminho)
    achados = []
    for i in range(len(pal)):
        if _norm(pal[i][0]) != toks[0] and not (len(toks[0]) > 3 and _norm(pal[i][0]).startswith(toks[0])):
            continue
        grupo = [pal[i]]
        ok = True
        for j, tk in enumerate(toks[1:], 1):
            # próxima palavra do rótulo: mais próxima à direita ou logo abaixo
            cands = [p for p in pal if _norm(p[0]) == tk or (len(tk) > 3 and _norm(p[0]).startswith(tk))]
            ult = grupo[-1]
            cands = [p for p in cands if abs(p[2] - ult[2]) < 3 * ult[4] + 6 and abs(p[1] - ult[1]) < 260]
            if not cands:
                ok = False
                break
            grupo.append(min(cands, key=lambda p: abs(p[2] - ult[2]) * 3 + abs(p[1] - (ult[1] + ult[3]))))
        if ok:
            x0 = min(p[1] for p in grupo); y0 = min(p[2] for p in grupo)
            x1 = max(p[1] + p[3] for p in grupo); y1 = max(p[2] + p[4] for p in grupo)
            achados.append((x0, y0, x1, y1))
    if len(achados) <= n:
        raise ValueError(f"rótulo não encontrado: {alvo!r} em {caminho.name}")
    return achados[n]


def imagens_oclusao(fig: Path, caixa, destino: Path, nome: str):
    x0, y0, x1, y1 = caixa
    pad = 3
    x0, y0, x1, y1 = x0 - pad, y0 - pad, x1 + pad, y1 + pad
    img = Image.open(fig).convert("RGB")
    esc = 2 if img.width < 700 else 1
    img = img.resize((img.width * esc, img.height * esc), Image.LANCZOS)
    b = [v * esc for v in (x0, y0, x1, y1)]
    q = img.copy(); d = ImageDraw.Draw(q)
    d.rounded_rectangle(b, radius=4 * esc, fill=(138, 27, 43), outline=(90, 10, 20), width=2)
    try:
        fonte = ImageFont.truetype(str(Path(__file__).parent / "fontes" / "Inter-Bold.ttf"), int(min(b[3] - b[1], 30) * 0.8))
        d.text(((b[0] + b[2]) / 2, (b[1] + b[3]) / 2), "?", fill="white", font=fonte, anchor="mm")
    except Exception:
        pass
    r = img.copy(); d = ImageDraw.Draw(r)
    d.rounded_rectangle(b, radius=4 * esc, outline=(31, 78, 121), width=3 * esc // 2 + 1)
    pq = destino / f"{nome}_q.jpg"; pr = destino / f"{nome}_r.jpg"
    q.save(pq, quality=86, optimize=True); r.save(pr, quality=86, optimize=True)
    return pq, pr


# ------------------------------------------------------------ baralho
def monta_deck(t, fonte_dir: Path):
    """Deck do tema, lista de arquivos de mídia e número de cartões."""
    tema = f"Tema {t.CODIGO.upper()} · {t.TITULO}"
    deck = genanki.Deck(_id("limac-deck-" + t.CODIGO), f"LIMAC Cardiologia::{t.CODIGO.upper()} · {t.TITULO}")
    midia = []
    tmp = fonte_dir / "_build" / "anki" / t.CODIGO
    tmp.mkdir(parents=True, exist_ok=True)
    for f in list(tmp.glob("*.png")) + list(tmp.glob("*.jpg")):
        f.unlink()

    def img_html(k):
        pasta = {"g": "guyton", "p": "porto", "w": "web"}[k[0]]
        orig = fonte_dir / "figuras" / pasta / f"{k}.png"
        nome = f"limac_{k}.png"
        dst = tmp / nome
        dst.write_bytes(orig.read_bytes())
        if str(dst) not in midia:
            midia.append(str(dst))
        return f'<img src="{nome}">'

    n = 0
    for c in getattr(t, "BASICOS", []):
        frente, verso = c[0], c[1]
        k = c[2] if len(c) > 2 else None
        nota = genanki.Note(model=BASICO, fields=[tema, md2html(frente), md2html(verso),
                                                   img_html(k) if k else "", ref_livro(k) if k else ""],
                            guid=genanki.guid_for("b", t.CODIGO, frente), tags=[f"tema_{t.CODIGO}", "basico"])
        deck.add_note(nota); n += 1
    for c in getattr(t, "LACUNAS", []):
        texto, extra = c[0], (c[1] if len(c) > 1 else "")
        html = md2html(texto)
        nota = genanki.Note(model=LACUNA, fields=[html, tema, md2html(extra), ""],
                            guid=genanki.guid_for("c", t.CODIGO, texto), tags=[f"tema_{t.CODIGO}", "lacuna"])
        deck.add_note(nota)
        n += len(set(re.findall(r"\{\{c(\d+)::", texto)))
    for i, o in enumerate(getattr(t, "OCLUSOES", [])):
        k, alvo, pergunta, resposta = o
        pasta = {"g": "guyton", "p": "porto"}[k[0]]
        fig = fonte_dir / "figuras" / pasta / f"{k}.png"
        caixa = localiza(fig, alvo)
        pq, pr = imagens_oclusao(fig, caixa, tmp, f"limac_occ_{t.CODIGO}_{i:02d}_{k}")
        midia += [str(pq), str(pr)]
        nota = genanki.Note(model=OCLUSAO, fields=[tema, md2html(pergunta), f'<img src="{pq.name}">',
                                                    f'<img src="{pr.name}">', md2html(resposta), ref_livro(k)],
                            guid=genanki.guid_for("o", t.CODIGO, k, str(alvo)), tags=[f"tema_{t.CODIGO}", "oclusao"])
        deck.add_note(nota); n += 1
    return deck, midia, n


def gera_baralho(t, saida: Path, fonte_dir: Path) -> int:
    deck, midia, n = monta_deck(t, fonte_dir)
    saida.parent.mkdir(parents=True, exist_ok=True)
    pacote = genanki.Package(deck)
    pacote.media_files = midia
    pacote.write_to_file(str(saida))
    return n


def gera_completo(temas, saida: Path, fonte_dir: Path) -> int:
    """Um único .apkg com todos os temas como subbaralhos de LIMAC Cardiologia."""
    decks, midia, total = [], [], 0
    for t in temas:
        d, m, n = monta_deck(t, fonte_dir)
        decks.append(d); midia += [x for x in m if x not in midia]; total += n
    saida.parent.mkdir(parents=True, exist_ok=True)
    pacote = genanki.Package(decks)
    pacote.media_files = midia
    pacote.write_to_file(str(saida))
    return total
