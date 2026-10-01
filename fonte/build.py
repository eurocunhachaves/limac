#!/usr/bin/env python3
"""Gera o resumão (PDF via Typst), o README do tema e o baralho Anki.

Uso:  python3 fonte/build.py a [b c ...]   (ou "todos")

Cada tema é um módulo em fonte/temas/<código>.py com:
  CODIGO, SLUG, TITULO, AREA, FONTES, ESSENCIAL, CORPO (Typst), VALORES,
  CLINICA, PEGADINHAS, GLOSSARIO, LEITURA, BASICOS, LACUNAS, OCLUSOES
As figuras vêm de fonte/figuras/{guyton,porto}/ (extraídas dos PDFs dos livros
por fonte/scripts/extrai_*.py) e são citadas pelo número no livro.
"""
import importlib.util, json, os, re, shutil, sys
from pathlib import Path

import pymupdf
import typst

FONTE = Path(__file__).resolve().parent
REPO = FONTE.parent
SAIDA_PROJETO = Path("/mnt/project-files/liga-cardio-v2")
EXTRAIDAS = Path(os.environ.get("LIMAC_FIG", "/tmp/claude-0/work/fig"))
PREVIA = Path(os.environ.get("LIMAC_PREVIA", "/tmp/claude-0/work/previa"))
ORDEM = ["a", "b", "c", "d", "e", "f", "g", "h", "s", "t", "u"]


# ---------------------------------------------------------------- utilidades
ESPECIAIS = set("\\#$@<>[]*_`~=")


def esc(s: str) -> str:
    out = []
    for i, ch in enumerate(s):
        if ch in ESPECIAIS:
            out.append("\\" + ch)
        elif ch == "/" and i + 1 < len(s) and s[i + 1] in "/*":
            out.append("\\/")
        elif ch == "-" and s[i:i + 2] == "--":
            out.append("\\-")
        else:
            out.append(ch)
    return "".join(out)


def md2typ(s: str) -> str:
    """Markdown mínimo (**negrito**, *itálico*, `x_y` como sub) -> Typst."""
    partes = re.split(r"(\*\*.+?\*\*|\*[^*]+?\*|\^\S+?\^)", s)
    out = []
    for p in partes:
        if p.startswith("**") and p.endswith("**") and len(p) > 4:
            out.append("#strong[" + esc(p[2:-2]) + "]")
        elif p.startswith("*") and p.endswith("*") and len(p) > 2:
            out.append("#emph[" + esc(p[1:-1]) + "]")
        elif p.startswith("^") and p.endswith("^") and len(p) > 2:
            out.append("#super[" + esc(p[1:-1]) + "]")
        elif out and p.startswith(";"):
            # ";" logo após #strong[...] encerraria a expressão e sumiria
            out.append("\\" + p[0] + esc(p[1:]))
        else:
            out.append(esc(p))
    return "".join(out)


def md2html(s: str) -> str:
    import html
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"\*([^*]+?)\*", r"<i>\1</i>", s)
    s = re.sub(r"\^(\S+?)\^", r"<sup>\1</sup>", s)
    return s


def md2md(s: str) -> str:
    s = re.sub(r"\^(\S+?)\^", r"<sup>\1</sup>", s)
    return s


def carrega(codigo: str):
    caminho = FONTE / "temas" / f"{codigo}.py"
    spec = importlib.util.spec_from_file_location(f"tema_{codigo}", caminho)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def figuras_usadas(t) -> list:
    chaves = set(re.findall(r'fig\("([gpw][0-9a-z_]+)"', t.CORPO))
    for b in getattr(t, "BASICOS", []):
        if len(b) > 2 and b[2]:
            chaves.add(b[2])
    for o in getattr(t, "OCLUSOES", []):
        chaves.add(o[0])
    return sorted(chaves)


def copia_figuras(chaves):
    for k in chaves:
        pasta = {"g": "guyton", "p": "porto", "w": "web"}[k[0]]
        destino = FONTE / "figuras" / pasta / f"{k}.png"
        if destino.exists():
            continue
        origem = EXTRAIDAS / pasta / f"{k}.png"
        destino.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(origem, destino)
    atualiza_tamanhos()


def atualiza_tamanhos():
    """figuras/tamanhos.json: chave -> [largura, altura] em pixels (lido pelo modelo)."""
    from PIL import Image
    tam = {}
    for f in sorted((FONTE / "figuras").glob("*/*.png")):
        with Image.open(f) as im:
            tam[f.stem] = list(im.size)
    (FONTE / "figuras" / "tamanhos.json").write_text(json.dumps(tam, indent=0), encoding="utf-8")


def legenda_livro(k: str) -> str:
    pasta = {"g": "guyton", "p": "porto"}.get(k[0])
    idx = EXTRAIDAS / pasta / "index.json" if pasta else None
    if idx and idx.exists():
        d = json.load(open(idx))
        if k in d:
            return d[k]["caption"]
    return ""


def ref_livro(k: str) -> str:
    cap, num = k[1:].split("_")
    num = re.sub(r"[a-z]$", "", num)
    livro = {"g": "Guyton & Hall", "p": "Porto"}[k[0]]
    return f"{livro}, Fig. {cap}.{int(num)}"


# ---------------------------------------------------------------- resumão
def gera_typst(t) -> str:
    L = []
    L.append('#import "../modelo.typ": *')
    fontes = ", ".join("[" + md2typ(f) + "]" for f in t.FONTES)
    L.append(f'#show: resumao.with(tema: "{t.CODIGO.upper()}", titulo: [{md2typ(t.TITULO)}], '
             f'area: "{t.AREA}", fontes: ({fontes},))')
    # Em 30 segundos
    itens = "\n".join("- " + md2typ(e) for e in t.ESSENCIAL)
    L.append(f'#essencial(titulo: "Em 30 segundos")[\n{itens}\n]')
    L.append(monta_corpo(t.CORPO, getattr(t, '_adiar', {})))
    R = []
    if t.VALORES:
        linhas = [", ".join("[" + md2typ(c) + "]" for c in v) for v in t.VALORES]
        R.append("== Valores para decorar\n\n" + '#tabela((1.3fr, 1.15fr, 1.45fr), ([Parâmetro], [Valor], [Observação]),\n  '
                 + ",\n  ".join(linhas) + ", tamanho: 8.9pt, pad: 3.9pt)")
    if t.PEGADINHAS:
        itens = "\n".join("- " + md2typ(p) for p in t.PEGADINHAS)
        R.append(f'#atencao(titulo: "Pegadinhas de prova")[\n{itens}\n]')
    if t.CLINICA:
        itens = "\n".join(f"- #strong[{esc(tit)}.] {md2typ(txt)}" for tit, txt in t.CLINICA)
        R.append(f'#clinica(titulo: "Correlações clínicas")[\n{itens}\n]')
    if getattr(t, "GLOSSARIO", None):
        linhas = [f"[*{md2typ(a)}*], [{md2typ(b)}]" for a, b in t.GLOSSARIO]
        R.append("== Glossário\n\n" + '#tabela((1fr, 2.6fr), ([Termo], [Significado]),\n  '
                 + ",\n  ".join(linhas) + ", tamanho: 8.9pt, pad: 3.9pt)")
    if t.LEITURA:
        linhas = [", ".join("[" + md2typ(c) + "]" for c in r) for r in t.LEITURA]
        R.append("== Onde ler nas fontes\n\n" + '#tabela((1fr, 1.25fr, 2.2fr), ([Livro], [Onde], [O que ler]),\n  '
                 + ",\n  ".join(linhas) + ", tamanho: 8.9pt)")
    ordem = getattr(t, "_ordem_rev", None)
    if ordem:   # Valores sempre primeiro e Onde ler sempre por último
        R = [R[0]] + [R[1:-1][i] for i in ordem] + [R[-1]]
    L.append("#revisao[\n" + "\n\n".join(R) + "\n]")
    return "\n\n".join(L) + "\n"


# ---------------------------------------------------------------- paginação
MOVEL = re.compile(r'#(?:fig|par-figs)\("([^"]+)"|#tabela\(rotulo: "([^"]+)"')


def blocos(corpo):
    return [b for b in re.split(r"\n\s*\n", corpo.strip("\n"))]


def chave_movel(bloco):
    m = MOVEL.match(bloco.strip())
    return (m.group(1) or m.group(2)) if m else None


def _barreira(bloco):
    b = bloco.lstrip()
    return b.startswith("=") or chave_movel(bloco) is not None


def monta_corpo(corpo, adiar):
    """Reposiciona figuras/tabelas: n > 0 desce n blocos, n < 0 sobe |n| blocos,
    sem atravessar título (= ou ==) nem outra figura/tabela."""
    bs = blocos(corpo)
    for k, n in adiar.items():
        i = next((j for j, b in enumerate(bs) if chave_movel(b) == k), None)
        if i is None or n == 0:
            continue
        b = bs.pop(i)
        j = i
        if n > 0:
            for _ in range(n):
                if j >= len(bs) or _barreira(bs[j]):
                    break
                j += 1
        else:
            for _ in range(-n):
                if j == 0 or _barreira(bs[j - 1]):
                    break
                j -= 1
        bs.insert(j, b)
    return "\n\n".join(bs)


def pode_mover(corpo, adiar, k, passo):
    antes = monta_corpo(corpo, adiar)
    depois = monta_corpo(corpo, {**adiar, k: adiar.get(k, 0) + passo})
    return antes != depois


AREA_TOPO, AREA_PE = 62, 72   # pt: cabeçalho e rodapé


def sobras(doc):
    """Para cada página: (pt livres no pé, lista de buracos internos em pt)."""
    res = []
    for pg in doc:
        r = pg.rect
        area = pymupdf.Rect(0, AREA_TOPO, r.width, r.height - AREA_PE)
        faixas = []
        for b in pg.get_text("blocks"):
            rb = pymupdf.Rect(b[:4])
            if rb.intersects(area):
                faixas.append((rb.y0, rb.y1))
        for img in pg.get_image_info():
            rb = pymupdf.Rect(img["bbox"])
            if rb.intersects(area):
                faixas.append((rb.y0, rb.y1))
        for d in pg.get_drawings():
            rb = d["rect"]
            if rb.intersects(area) and rb.height < area.height * 0.9:
                faixas.append((rb.y0, rb.y1))
        if not faixas:
            res.append((area.height, []))
            continue
        faixas.sort()
        fim, buracos = faixas[0][1], []
        for y0, y1 in faixas[1:]:
            if y0 - fim > 60:
                buracos.append(y0 - fim)
            fim = max(fim, y1)
        res.append((area.y1 - fim, buracos))
    return res


def _compila(src, pdf, escalas):
    entradas = {"escalas": json.dumps(escalas)}
    opts = dict(root=str(FONTE), font_paths=[str(FONTE / "fontes")], ignore_system_fonts=True,
                sys_inputs=entradas)
    typst.compile(str(src), output=str(pdf), **opts)
    marcas = json.loads(typst.query(str(src), "<marca>", field="value", **opts))
    return pymupdf.open(pdf), marcas


def _fim_do_texto(marcas):
    """Índice (0-based) da última página do texto, antes da Revisão rápida."""
    r = [m["pagina"] for m in marcas if m["tipo"] == "revisao"]
    return r[0] - 2 if r else None


def _custo(doc, marcas):
    """Sobra total (pt) no pé das páginas (exceto a última página do texto e a
    última do documento) e buracos internos."""
    sob = sobras(doc)
    fim_texto = _fim_do_texto(marcas)
    c = 0
    for i, (livre, buracos) in enumerate(sob):
        area = doc[i].rect.height - AREA_TOPO - AREA_PE
        if i < len(sob) - 1 and i != fim_texto and livre / area > 0.04:
            c += livre
        c += sum(buracos)
    # figura em página anterior à citação, ou duas páginas depois: proibido
    # e figura acima do texto que a cita, na mesma página
    ini = {m["chave"]: m for m in marcas if m["tipo"] == "ini"}
    refs = {}
    for m in marcas:
        if m["tipo"] == "ref":
            refs.setdefault(m["chave"], m)
    for k, f in ini.items():
        r = refs.get(k)
        if r is None:
            continue
        if not 0 <= f["pagina"] - r["pagina"] <= 1 or (f["pagina"] == r["pagina"] and f["y"] < r["y"]):
            c += 5000
    return c + 400 * len(sob)   # página a mais custa caro


def _candidatos(t, doc, marcas, escalas):
    """Mudanças possíveis para cada página com sobra no pé causada por uma
    figura/tabela que abriu a página seguinte."""
    ini = {m["chave"]: m for m in marcas if m["tipo"] == "ini"}
    fim = {m["chave"]: m for m in marcas if m["tipo"] == "fim"}
    fim_texto = _fim_do_texto(marcas)
    for i, (livre, _) in enumerate(sobras(doc)[:-1]):
        area = doc[i].rect.height - AREA_TOPO - AREA_PE
        if livre / area <= 0.06 or i == fim_texto:
            continue
        nxt = [m for m in ini.values() if m["pagina"] == i + 2]
        if not nxt:
            continue
        m = min(nxt, key=lambda m: m["y"])
        if m["y"] > AREA_TOPO + 45:
            continue
        k = m["chave"]
        alt = fim[k]["y"] - m["y"]
        folga = livre - 22
        if k[0] in "gpw" and alt * 0.8 <= folga:
            yield ("escala", {k: round(max(0.8, escalas.get(k, 1.0) * (folga / alt) * 0.97), 3)})
        aqui = [x["chave"] for x in ini.values() if x["pagina"] == i + 1 and x["chave"][0] in "gpw"
                and escalas.get(x["chave"], 1.0) > 0.8]
        for f in (0.9, 0.8):
            if aqui:
                yield ("escala", {x: f for x in aqui})
        for passo in (1, 2, 3, -1, -2):
            if pode_mover(t.CORPO, t._adiar, k, passo):
                yield ("move", {k: t._adiar.get(k, 0) + passo})
                if k[0] in "gpw":
                    for f in (0.9, 0.8):
                        yield ("ambos", ({k: t._adiar.get(k, 0) + passo}, {k: f}))


def pagina(t, src, pdf, max_voltas=80):
    """Paginação automática por busca local: tenta reduzir figuras (até 80%) ou
    mover figuras/tabelas alguns parágrafos (sem atravessar títulos) e fica com
    a mudança só se a sobra total nas páginas diminuir."""
    t._adiar, escalas = {}, {}

    def roda():
        src.write_text(gera_typst(t), encoding="utf-8")
        return _compila(src, pdf, escalas)

    doc, marcas = roda()
    custo = _custo(doc, marcas)
    voltas = 0
    melhorou = True
    while melhorou and voltas < max_voltas:
        melhorou = False
        for tipo, mud in list(_candidatos(t, doc, marcas, escalas)):
            voltas += 1
            antes_a, antes_e = dict(t._adiar), dict(escalas)
            if tipo == "ambos":
                t._adiar.update(mud[0]); escalas.update(mud[1])
            else:
                (t._adiar if tipo == "move" else escalas).update(mud)
            d2, m2 = roda()
            c2 = _custo(d2, m2)
            if c2 < custo - 5:
                doc, marcas, custo = d2, m2, c2
                melhorou = True
                break
            t._adiar, escalas = antes_a, antes_e
            if voltas >= max_voltas:
                break
    # ordem dos blocos da Revisão rápida (Valores sempre primeiro)
    import itertools
    n = len([x for x in (t.VALORES, t.PEGADINHAS, t.CLINICA, getattr(t, "GLOSSARIO", None), t.LEITURA) if x]) - 2
    melhor = (custo, None)
    for perm in itertools.permutations(range(n)):
        t._ordem_rev = list(perm)
        d2, m2 = roda()
        c2 = _custo(d2, m2)
        if c2 < melhor[0] - 5:
            melhor = (c2, list(perm))
    t._ordem_rev = melhor[1]
    doc, marcas = roda()
    return doc, escalas


def compila(t, destinos):
    build = FONTE / "_build"
    build.mkdir(exist_ok=True)
    src = build / f"{t.CODIGO}.typ"
    pdf = build / f"{t.CODIGO}.pdf"
    doc, escalas = pagina(t, src, pdf)
    if t._adiar or escalas:
        print(f"  paginação: adiados {t._adiar or '-'}; reduzidas {escalas or '-'}")
    for d in destinos:
        d.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(pdf, d)
    # prévias para conferência visual
    prev = PREVIA / t.CODIGO
    if prev.exists():
        shutil.rmtree(prev)
    prev.mkdir(parents=True)
    for i, pg in enumerate(doc):
        pg.get_pixmap(dpi=80).save(prev / f"p{i+1:02d}.png")
    verifica_preenchimento(doc, _fim_do_texto(json.loads(typst.query(str(src), '<marca>', field='value', root=str(FONTE), font_paths=[str(FONTE / 'fontes')], ignore_system_fonts=True, sys_inputs={'escalas': json.dumps(escalas)}))))
    verifica_figuras(src, escalas)
    return pdf, doc.page_count


def verifica_figuras(src, escalas):
    """Cada figura precisa ser citada (#vf) e ficar na mesma página da primeira
    citação ou, no máximo, na seguinte."""
    import json
    marcas = json.loads(typst.query(str(src), "<marca>", field="value", root=str(FONTE),
                                    font_paths=[str(FONTE / "fontes")], ignore_system_fonts=True,
                                    sys_inputs={"escalas": json.dumps(escalas)}))
    figs = {m["chave"]: m["pagina"] for m in marcas if m["tipo"] == "fig"}
    refs = {}
    for m in marcas:
        if m["tipo"] == "ref":
            refs.setdefault(m["chave"], m["pagina"])
    for k, pg in figs.items():
        if k not in refs:
            print(f"  ! figura {k} (p. {pg}) não é citada no texto")
        elif not 0 <= pg - refs[k] <= 1:
            print(f"  ! figura {k} está na p. {pg}, mas é citada na p. {refs[k]}")
    ini = {m["chave"]: m for m in marcas if m["tipo"] == "ini"}
    prim = {}
    for m in marcas:
        if m["tipo"] == "ref":
            prim.setdefault(m["chave"], m)
    for k, f in ini.items():
        r = prim.get(k)
        if r and f["pagina"] == r["pagina"] and f["y"] < r["y"]:
            print(f"  ! {k} aparece acima do texto que a cita (p. {f['pagina']})")


def verifica_preenchimento(doc, fim_texto=None):
    """Avisa sobre sobra no pé (exceto a última página e a última do texto,
    antes da Revisão rápida) e buracos no meio."""
    for i, (livre, buracos) in enumerate(sobras(doc)):
        area = doc[i].rect.height - AREA_TOPO - AREA_PE
        for bu in buracos:
            print(f"  ! página {i+1}: buraco de {bu / 28.35:.1f} cm no meio")
        if i < doc.page_count - 1 and i != fim_texto and livre / area > 0.09:
            print(f"  ! página {i+1}: {livre / area:.0%} vazia no fim")


# ---------------------------------------------------------------- README
def gera_readme(t, n_paginas, n_cards) -> str:
    L = [f"# Tema {t.CODIGO.upper()} · {t.TITULO}", ""]
    L.append(f"**Área:** {t.AREA} · **Resumão:** [resumao.pdf](resumao.pdf) ({n_paginas} páginas) · "
             f"**Anki:** [flashcards.apkg](flashcards.apkg) ({n_cards} cartões)")
    L.append("")
    L.append("**Fontes:** " + " · ".join(md2md(f) for f in t.FONTES))
    L += ["", "[← voltar ao índice](../../README.md)", "", "## O essencial", ""]
    L += ["- " + md2md(e) for e in t.ESSENCIAL]
    if t.VALORES:
        L += ["", "## Valores para decorar", "", "| Parâmetro | Valor | Observação |", "|---|---|---|"]
        L += [f"| {md2md(a)} | {md2md(b)} | {md2md(c)} |" for a, b, c in t.VALORES]
    figs = figuras_usadas(t)
    figs_corpo = [k for k in re.findall(r'fig\("([gpw][0-9a-z_]+)"', t.CORPO)]
    vistos = []
    for k in figs_corpo:
        if k not in vistos:
            vistos.append(k)
    if vistos:
        L += ["", "## Figuras-chave", ""]
        for k in vistos:
            pasta = {"g": "guyton", "p": "porto", "w": "web"}[k[0]]
            cap = legenda_livro(k)
            cap = re.sub(r"^Figura\s*\d+\.\d+\s*", "", cap)
            L += [f"**{ref_livro(k)}** — {cap}", "",
                  f'<img src="../../fonte/figuras/{pasta}/{k}.png" width="420">', ""]
    if t.GLOSSARIO:
        L += ["## Glossário", "", "| Termo | Significado |", "|---|---|"]
        L += [f"| **{md2md(a)}** | {md2md(b)} |" for a, b in t.GLOSSARIO]
    if t.CLINICA:
        L += ["", "## Correlações clínicas", ""]
        for tit, txt in t.CLINICA:
            L += [f"- **{tit}.** {md2md(txt)}"]
    if t.PEGADINHAS:
        L += ["", "## Pegadinhas de prova", ""]
        L += ["- " + md2md(p) for p in t.PEGADINHAS]
    if t.LEITURA:
        L += ["", "## Onde ler nas fontes", "", "| Livro | Onde | O que ler |", "|---|---|---|"]
        L += [f"| {md2md(a)} | {md2md(b)} | {md2md(c)} |" for a, b, c in t.LEITURA]
    L += ["", "---", "", "*Figuras reproduzidas dos livros-texto para uso pessoal de estudo; "
          "o número de cada figura no livro está indicado na legenda.*", ""]
    return "\n".join(L)


# ---------------------------------------------------------------- principal
def constroi(codigo):
    t = carrega(codigo)
    figs = figuras_usadas(t)
    copia_figuras(figs)
    pasta_repo = REPO / "temas" / t.SLUG
    pasta_proj = SAIDA_PROJETO / t.SLUG
    nome_pdf = f"Resumão {t.CODIGO.upper()} - {t.TITULO}.pdf"
    pdf, n = compila(t, [pasta_repo / "resumao.pdf", pasta_proj / nome_pdf])
    import anki
    apkg_repo = pasta_repo / "flashcards.apkg"
    n_cards = anki.gera_baralho(t, apkg_repo, FONTE)
    shutil.copy(apkg_repo, pasta_proj / f"Anki {t.CODIGO.upper()} - {t.TITULO}.apkg")
    (pasta_repo / "README.md").write_text(gera_readme(t, n, n_cards), encoding="utf-8")
    print(f"tema {codigo}: {n} páginas, {n_cards} cartões, figuras: {', '.join(figs)}")
    return t, n, n_cards


DESCRICAO = {
    "a": "Sincício, potencial de ação com platô, acoplamento excitação-contração, ciclo cardíaco (Wiggers), valvas, alça pressão-volume, Frank-Starling",
    "b": "Nó sinusal e automatismo, nó AV e retardo, sistema de Purkinje, marca-passos ectópicos, controle autonômico",
    "c": "Ondas, intervalos e segmentos, papel milimetrado, derivações (Einthoven, aumentadas, precordiais), eixo",
    "d": "Pressão, fluxo e resistência, Poiseuille, viscosidade, complacência, pulso arterial, medida da PA",
    "e": "Capilares, forças de Starling, interstício, edema, sistema linfático",
    "f": "Autorregulação, metabólitos, NO, angiogênese, hormônios vasoativos, barorreceptores, quimiorreceptores, reflexos",
    "g": "Débito cardíaco = retorno venoso, curvas de débito e de retorno, pressão média de enchimento, métodos de medida",
    "h": "Diurese e natriurese de pressão, curva de débito renal, sistema renina-angiotensina-aldosterona, sal e hipertensão",
    "s": "Anamnese, dor torácica, palpitações, dispneia, síncope, cianose, edema, arritmias ao exame clínico",
    "t": "Inspeção e palpação do precórdio, focos de ausculta, bulhas, ritmo de galope, estalidos, sopros, atrito",
    "u": "Pulso radial, tipos de pulso, pulso venoso jugular, medida da PA, Korotkoff, classificação da PA",
}


def gera_indice():
    linhas = []
    for c in ORDEM:
        if not (FONTE / "temas" / f"{c}.py").exists():
            continue
        t = carrega(c)
        linhas.append(f"| **{c.upper()}** | [{t.TITULO}](temas/{t.SLUG}/README.md) | {t.AREA} | {DESCRICAO.get(c, '')} | "
                      f"[PDF](temas/{t.SLUG}/resumao.pdf) · [Anki](temas/{t.SLUG}/flashcards.apkg) |")
    modelo = (REPO / "fonte" / "README-modelo.md").read_text(encoding="utf-8")
    (REPO / "README.md").write_text(modelo.replace("{{TABELA}}", "\n".join(linhas)), encoding="utf-8")


if __name__ == "__main__":
    sys.path.insert(0, str(FONTE))
    alvos = sys.argv[1:] or ["todos"]
    if alvos == ["todos"]:
        alvos = [c for c in ORDEM if (FONTE / "temas" / f"{c}.py").exists()]
    for c in alvos:
        constroi(c)
    gera_indice()
