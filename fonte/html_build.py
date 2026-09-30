"""Resumão diagramado em HTML/CSS e convertido em PDF pelo Chromium (Playwright).

Usa os mesmos blocos de seção de build.py, mais:
  ("web", "fig_web/<letra>/<arquivo>", largura_cm[, legenda])   imagem de licença aberta (entra nas duas versões)
Figuras com largura até FLOAT_MAX cm ficam à direita do texto; as maiores ocupam a largura toda.
"""
import html
import json
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
WEB = os.path.join(HERE, "web")
FLOAT_MAX = 9

_CRED = {}


def credit(rel):
    """Metadados de crédito de uma imagem em fig_web/ (lidos do creditos.json da pasta)."""
    folder = os.path.dirname(rel)
    if folder not in _CRED:
        p = os.path.join(HERE, folder, "creditos.json")
        _CRED[folder] = {c["arquivo"]: c for c in json.load(open(p))} if os.path.exists(p) else {}
    return _CRED[folder].get(os.path.basename(rel), {})


def credit_text(rel):
    c = credit(rel)
    return f"{c.get('autor', 'autor desconhecido')}, {c.get('licenca', 'licença aberta')}, via Wikimedia Commons"


def is_book(rel):
    return bool(rel) and rel.startswith("fig_livro/")


def is_web(rel):
    return bool(rel) and rel.startswith("fig_web/")


def book_source(rel):
    return "Guyton & Hall" if "fig_livro/g" in rel else "Porto, Semiologia Médica"


def src_url(rel):
    return "file://" + os.path.join(HERE, rel)


CSS = """
@font-face{font-family:Inter;font-weight:400;src:url(web/fonts/inter-latin-400-normal.woff2),url(web/fonts/inter-latin-ext-400-normal.woff2)}
@font-face{font-family:Inter;font-weight:500;src:url(web/fonts/inter-latin-500-normal.woff2)}
@font-face{font-family:Inter;font-weight:600;src:url(web/fonts/inter-latin-600-normal.woff2)}
@font-face{font-family:Inter;font-weight:700;src:url(web/fonts/inter-latin-700-normal.woff2)}
@font-face{font-family:Inter;font-weight:800;src:url(web/fonts/inter-latin-800-normal.woff2)}
:root{--red:#9b1c2c;--red2:#c2415a;--redl:#fbeaec;--blue:#2a5ca8;--bluel:#eaf1fb;--ink:#1f2328;--mute:#5f6670;--line:#e3e5e8}
*{box-sizing:border-box}
html{font-family:Inter,"DejaVu Sans",sans-serif;font-size:9.4pt;line-height:1.42;color:var(--ink)}
body{margin:0}
b{color:var(--red);font-weight:700}
.cover{background:linear-gradient(120deg,var(--red),var(--red2));color:#fff;border-radius:10px;padding:14px 18px 14px;
       display:flex;gap:16px;align-items:center;margin-bottom:10px}
.cover .badge{flex:0 0 58px;height:58px;border-radius:50%;background:#fff;color:var(--red);font-weight:800;font-size:30pt;
       display:flex;align-items:center;justify-content:center}
.cover .kicker{font-size:7.5pt;letter-spacing:.12em;text-transform:uppercase;opacity:.85}
.cover h1{margin:1px 0 3px;font-size:19pt;line-height:1.1;font-weight:800}
.cover .src{font-size:8pt;opacity:.9}
.toc{display:flex;flex-wrap:wrap;gap:5px;margin:0 0 10px}
.toc span{border:1px solid var(--line);border-radius:20px;padding:2px 9px;font-size:7.6pt;color:var(--mute);background:#fafafa}
.toc span i{font-style:normal;font-weight:700;color:var(--red)}
h2.sec{clear:both;margin:14px 0 6px;font-size:13pt;font-weight:800;color:var(--red);display:flex;align-items:center;gap:8px;
       break-after:avoid;border-bottom:2px solid var(--redl);padding-bottom:3px}
h2.sec .n{background:var(--red);color:#fff;border-radius:6px;font-size:10pt;min-width:22px;height:22px;display:inline-flex;
       align-items:center;justify-content:center}
h3{clear:both;margin:10px 0 4px;font-size:10.5pt;font-weight:700;break-after:avoid}
p{margin:0 0 6px;text-align:justify}
ul{margin:0 0 7px;padding-left:15px}
li{margin:0 0 3px}
li::marker{color:var(--red)}
.box{clear:both;background:var(--redl);border-left:4px solid var(--red);border-radius:8px;padding:8px 12px 6px;margin:8px 0 9px;
       break-inside:avoid}
.box.tip{background:var(--bluel);border-color:var(--blue)}
.box .t{font-weight:800;color:var(--red);margin-bottom:3px;font-size:9.6pt}
.box.tip .t{color:var(--blue)}
.box .t::before{content:"★ ";font-size:8.5pt}
.box.tip .t::before{content:"💡 "}
.box ul{margin-bottom:2px}
table{clear:both;width:100%;border-collapse:separate;border-spacing:0;margin:6px 0 9px;font-size:8.4pt;
       border:1px solid var(--line);border-radius:8px;overflow:hidden;break-inside:avoid}
th{background:var(--red);color:#fff;text-align:left;padding:5px 7px;font-weight:700}
th b{color:#fff}
td{padding:4px 7px;vertical-align:top;border-top:1px solid var(--line)}
tr:nth-child(even) td{background:#f7f7f8}
figure{margin:4px 0 8px;break-inside:avoid;text-align:center}
.pair{display:flex;gap:12px;align-items:flex-start;margin-bottom:4px;break-inside:avoid}
.pair .txt{flex:1;min-width:0}
.pair figure{flex:0 0 auto;margin-top:2px}
figure img{max-width:100%;border-radius:6px}
figcaption{font-size:7.6pt;color:var(--mute);margin-top:2px;line-height:1.3;text-align:center}
figcaption .cr{display:block;font-size:6.8pt;color:#9aa0a6}
.credits{clear:both;margin-top:14px;border-top:1px solid var(--line);padding-top:6px;font-size:7pt;color:var(--mute)}
.credits a{color:var(--mute)}
"""


def esc(s):
    return html.escape(s, quote=True)


def figure(rel, caption, width, cred=""):
    cls = ' class="side"' if width <= FLOAT_MAX else ""
    cr = f'<span class="cr">{cred}</span>' if cred else ""
    return (f'<figure{cls} style="width:{width}cm"><img src="{src_url(rel)}">'
            f'<figcaption>{caption}{cr}</figcaption></figure>')


def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def block(b, publico, used_web):
    kind = b[0]
    if kind == "pair":
        return (f'<div class="pair"><div class="txt">{block(b[2], publico, used_web)}</div>'
                f'{block(b[1], publico, used_web)}</div>')
    if kind == "p":
        return f"<p>{b[1]}</p>"
    if kind == "h2":
        return f"<h3>{b[1]}</h3>"
    if kind == "ul":
        return ul(b[1])
    if kind in ("box", "tip"):
        body = f"<div>{b[2]}</div>" if isinstance(b[2], str) else ul(b[2])
        return f'<div class="box{" tip" if kind == "tip" else ""}"><div class="t">{b[1]}</div>{body}</div>'
    if kind == "table":
        rows, widths = b[1], b[2]
        tot = sum(widths)
        cols = "".join(f'<col style="width:{w / tot * 100:.1f}%">' for w in widths)
        head = "".join(f"<th>{c}</th>" for c in rows[0])
        body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows[1:])
        return f"<table><colgroup>{cols}</colgroup><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>"
    if kind == "fig":
        _, own, book, caption, width = b
        rel = own if publico else (book or own)
        if not rel:
            return ""
        cred = f"Fonte: {book_source(rel)}." if is_book(rel) else ""
        return figure(rel, caption, width, cred)
    if kind == "web":
        rel, width = b[1], b[2]
        c = credit(rel)
        caption = b[3] if len(b) > 3 else c.get("legenda", "")
        used_web.append(rel)
        return figure(rel, caption, width, f"Imagem: {esc(credit_text(rel))}.")
    raise ValueError(kind)


def fig_width(b, publico):
    if b[0] == "web":
        return b[2]
    if b[0] == "fig" and (b[1] if publico else (b[2] or b[1])):
        return b[4]
    return None


def arrange(blocks, publico):
    """Figura estreita vira par lado a lado com o bloco de texto seguinte (tabela seguinte passa para antes)."""
    out = list(blocks)
    i = 0
    while i < len(out):
        w = fig_width(out[i], publico)
        if w is not None and w <= FLOAT_MAX:
            if i + 1 < len(out) and out[i + 1][0] == "table":
                out[i], out[i + 1] = out[i + 1], out[i]
                i += 1
            if i + 1 < len(out) and out[i + 1][0] in ("ul", "p", "box", "tip"):
                out[i:i + 2] = [("pair", out[i], out[i + 1])]
        i += 1
    return out


def resumao_html(T, publico):
    used_web = []
    secs = []
    for heading, blocks in T["sections"]:
        num, _, name = heading.partition(". ")
        inner = "".join(block(b, publico, used_web) for b in arrange(blocks, publico))
        secs.append(f'<section><h2 class="sec"><span class="n">{num}</span>{name}</h2>{inner}</section>')
    toc = "".join(f'<span><i>{h.partition(". ")[0]}</i> {h.partition(". ")[2]}</span>' for h, _ in T["sections"])
    creds = ""
    if used_web:
        items = []
        for rel in dict.fromkeys(used_web):
            c = credit(rel)
            items.append(f'{esc(c.get("titulo", os.path.basename(rel)))}: {esc(c.get("autor", ""))}, '
                         f'<a href="{esc(c.get("licenca_url", ""))}">{esc(c.get("licenca", ""))}</a>, '
                         f'<a href="{esc(c.get("url", ""))}">{esc(c.get("url", ""))}</a>')
        creds = '<div class="credits"><b>Créditos das imagens de licença aberta.</b> ' + " · ".join(items) + "</div>"
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Resumão: {esc(T['title'])}</title>
<style>{CSS}</style></head><body>
<div class="cover"><div class="badge">{T['code']}</div><div><div class="kicker">LIMAC · Resumão para a prova da Liga de Cardiologia</div>
<h1>{T['title']}</h1><div class="src">Fonte: {T['source']}</div></div></div>
<div class="toc">{toc}</div>
{''.join(secs)}
{creds}
</body></html>"""


def build_resumao_pdf(T, publico, out_pdf):
    html_path = os.path.join(HERE, f".resumao_{T['code']}_{'pub' if publico else 'pes'}.html")
    with open(html_path, "w") as f:
        f.write(resumao_html(T, publico))
    subprocess.run(["node", os.path.join(WEB, "pdf.js"), html_path, out_pdf, T["title"]], check=True)
    os.remove(html_path)
    return out_pdf


def quiz_json(T):
    """Questões objetivas no formato do quiz web (versão pública)."""
    return {
        "code": T["code"], "title": T["title"], "source": T["source"],
        "mcq": [{"q": q["q"], "opts": q["opts"], "a": q["a"], "c": q["c"]} for q in T["mcq"]],
        "open": [{"q": q["q"], "a": q["a"] if isinstance(q["a"], list) else [q["a"]]} for q in T["open"]]
               + [{"q": q, "a": [a]} for q, a in T.get("open_extra", [])],
    }
