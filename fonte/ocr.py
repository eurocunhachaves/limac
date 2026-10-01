"""Localiza rótulos dentro das figuras dos livros (OCR com tesseract) para gerar oclusões de imagem.

find_box("fig_livro/g16_05.png", "Pressão capilar") -> (x0, y0, x1, y1) em pixels da figura original.
Os resultados do OCR ficam em fig_livro/ocr_cache.json (não precisa rodar o tesseract de novo).
"""
import difflib
import json
import os
import re
import subprocess
import tempfile
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "fig_livro", "ocr_cache.json")
SCALE = 3
_cache = None


def _norm(s):
    s = unicodedata.normalize("NFKD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9+−-]", "", s)


def words(rel):
    """Palavras reconhecidas na figura: [(texto, x0, y0, x1, y1)] em ordem de leitura."""
    global _cache
    if _cache is None:
        _cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
    if rel in _cache:
        return _cache[rel]
    from PIL import Image
    im = Image.open(os.path.join(HERE, rel)).convert("L")
    im = im.resize((im.width * SCALE, im.height * SCALE), Image.LANCZOS)
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "x.png")
        im.save(p)
        out = subprocess.run(["tesseract", p, "-", "-l", "por", "--psm", "11", "tsv"], capture_output=True,
                             text=True).stdout
    res = []
    for line in out.splitlines()[1:]:
        f = line.split("\t")
        if len(f) < 12 or not f[11].strip() or float(f[10]) < 30:
            continue
        x, y, w, h = (int(v) / SCALE for v in f[6:10])
        res.append([f[11].strip(), x, y, x + w, y + h])
    _cache[rel] = res
    json.dump(_cache, open(CACHE, "w"), ensure_ascii=False)
    return res


def _sim(a, b):
    return difflib.SequenceMatcher(None, _norm(a), _norm(b)).ratio()


def _dist(box, w):
    dx = max(box[0] - w[3], w[1] - box[2], 0)
    dy = max(box[1] - w[4], w[2] - box[3], 0)
    return (dx * dx + 9 * dy * dy) ** 0.5  # prefere a mesma linha


def find_box(rel, text, pad=3, nth=0, near=45, grow=(0, 0, 0, 0)):
    """Caixa que cobre o rótulo `text`: as palavras podem estar em linhas diferentes, desde que próximas."""
    ws = words(rel)
    q = [t for t in text.split() if _norm(t)]
    hits = []
    for w0 in ws:
        if _sim(w0[0], q[0]) < 0.75:
            continue
        box, used, score, miss = list(w0[1:]), {id(w0)}, _sim(w0[0], q[0]), 0
        for t in q[1:]:
            cands = [w for w in ws if id(w) not in used and _sim(w[0], t) >= 0.8 and _dist(box, w) < near]
            if not cands:
                miss += 1
                continue
            w = min(cands, key=lambda w: _dist(box, w))
            used.add(id(w))
            score += _sim(w[0], t)
            box = [min(box[0], w[1]), min(box[1], w[2]), max(box[2], w[3]), max(box[3], w[4])]
        if miss <= len(q) // 3:
            hits.append((score / len(q), box))
    hits.sort(key=lambda h: (-h[0], h[1][1], h[1][0]))
    hits = [h for h in hits if h[0] >= hits[0][0] - 0.08] if hits else []  # só as ocorrências tão boas quanto a melhor
    uniq = []
    for _, b in hits:
        if all(abs(b[0] - u[0]) > 8 or abs(b[1] - u[1]) > 8 for u in uniq):
            uniq.append(b)
    uniq.sort(key=lambda b: (b[1], b[0]))  # nth conta de cima para baixo
    if len(uniq) <= nth:
        raise KeyError(f"rótulo não encontrado em {rel}: {text!r}")
    b = uniq[nth]
    return (int(b[0] - pad - grow[0]), int(b[1] - pad - grow[1]), int(b[2] + pad + grow[2]), int(b[3] + pad + grow[3]))
