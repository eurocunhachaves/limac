"""Copia o material para o repositório GitHub (eurocunhachaves/limac, privado) e escreve os READMEs.

Uso: python3 sync_repo.py /caminho/do/clone   (depois: git add -A && git commit && git push)
Para cada tema: temas/<slug>/README.md (resumo navegável com as figuras do livro, valores, glossário, clínica e
onde ler), resumao.pdf, flashcards.apkg e figuras/. Os PDFs dos livros não vão para o repositório.
"""
import html as H
import importlib
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import html_build  # noqa: E402
from extras import EXTRAS  # noqa: E402

PLANO = [
    ("a", "O músculo cardíaco e as valvas cardíacas", "Guyton cap. 9 (e 23)"),
    ("b", "Excitação rítmica do coração", "Guyton cap. 10"),
    ("c", "O eletrocardiograma normal", "Guyton caps. 11 e 12"),
    ("d", "Biofísica da circulação", "Guyton caps. 14 e 15"),
    ("e", "Microcirculação e sistema linfático", "Guyton cap. 16"),
    ("f", "Controle local, humoral e nervoso da circulação", "Guyton caps. 17 e 18"),
    ("g", "Débito cardíaco e retorno venoso", "Guyton cap. 20"),
    ("h", "Regulação da pressão arterial pelo sistema renal", "Guyton cap. 19"),
    ("s", "Semiologia cardiovascular", "Porto, Semiologia Médica"),
]


def md_table(rows):
    cell = lambda c: c.replace("|", "\\|")
    out = ["| " + " | ".join(cell(c) for c in rows[0]) + " |", "|" + "---|" * len(rows[0])]
    out += ["| " + " | ".join(cell(c) for c in r) + " |" for r in rows[1:]]
    return "\n".join(out)


def md_figure(rel, caption, width_cm, figs):
    figs.add(rel)
    px = min(700, int(width_cm * 48))
    src = html_build.book_ref(rel) if html_build.is_book(rel) else html_build.credit_text(rel)
    alt = H.escape(re.sub("<[^>]+>", "", caption))
    return (f'<p align="center"><img src="figuras/{os.path.basename(rel)}" width="{px}" alt="{alt}">'
            f"<br><sub>{caption} <i>({src})</i></sub></p>")


def md_block(b, figs):
    k = b[0]
    if k == "p":
        return b[1]
    if k == "h2":
        return f"#### {b[1]}"
    if k == "ul":
        return "\n".join(f"- {i}" for i in b[1])
    if k in ("box", "tip"):
        icon = "📌" if k == "box" else "💡"
        body = "> " + b[2] if isinstance(b[2], str) else "\n".join(f"> - {i}" for i in b[2])
        return f"> {icon} **{b[1]}**\n>\n{body}"
    if k == "table":
        return md_table(b[1])
    if k == "fig":
        rel = html_build.pick(b[1], b[2])
        return md_figure(rel, b[3], b[4], figs) if rel else ""
    if k == "web":
        return md_figure(b[1], b[3] if len(b) > 3 else "", b[2], figs)
    raise ValueError(k)


def anchor(h):
    return re.sub(r"[^\w\- ]", "", h.lower()).strip().replace(" ", "-")


def topic_readme(T, n_cards, n_occ):
    figs = set()
    X = EXTRAS.get(T["code"], {})
    d = [f"# {T['code'].upper()} · {T['title']}\n",
         f"Fonte: {T['source']}.  ",
         f"📄 [Resumão em PDF](resumao.pdf) · 🗂️ [Baralho do Anki](flashcards.apkg) "
         f"({n_cards} cartões, {n_occ} de oclusão de imagem) · ⬅️ [Todos os temas](../../README.md)\n"]
    if X.get("essencial"):
        d.append("## O essencial\n")
        d.append("\n".join(f"{i}. {s}" for i, s in enumerate(X["essencial"], 1)) + "\n")
    d.append("## Sumário\n")
    d += [f"- [{h}](#{anchor(h)})" for h, _ in T["sections"]]
    extra_sec = [("valores", "Valores para decorar"), ("glossario", "Glossário"), ("clinica", "Correlações clínicas"),
                 ("leitura", "Onde ler na fonte")]
    d += [f"- [{name}](#{anchor(name)})" for key, name in extra_sec if X.get(key)]
    d.append("")
    for h, blocks in T["sections"]:
        d.append(f"## {h}\n")
        for b in blocks:
            s = md_block(b, figs)
            if s:
                d.append(s + "\n")
    if X.get("valores"):
        d += ["## Valores para decorar\n", md_table([["Item", "Valor"]] + [list(v) for v in X["valores"]]) + "\n"]
    if X.get("glossario"):
        d += ["## Glossário\n", "\n".join(f"- **{t}**: {s}" for t, s in X["glossario"]) + "\n"]
    if X.get("clinica"):
        d += ["## Correlações clínicas\n", "\n".join(f"- **{t}**: {s}" for t, s in X["clinica"]) + "\n"]
    if X.get("leitura"):
        d += ["## Onde ler na fonte\n", md_table([["Fonte", "O que ler"]] + [list(v) for v in X["leitura"]]) + "\n"]
    d.append("---\n<sub>Figuras reproduzidas das fontes indicadas, para estudo pessoal. Repositório privado.</sub>\n")
    return "\n".join(d), figs


def main(repo):
    linhas = []
    for code, titulo, fonte in PLANO:
        mod = f"tema_{code}"
        if not os.path.exists(os.path.join(HERE, mod + ".py")):
            linhas.append(f"| {code.upper()} | {titulo} | {fonte} | em preparação | | |")
            continue
        T = importlib.import_module(mod).TOPIC
        src = os.path.join(OUT_ROOT, T["slug"])
        dst = os.path.join(repo, "temas", T["slug"])
        os.makedirs(os.path.join(dst, "figuras"), exist_ok=True)
        shutil.copy(os.path.join(src, f"Resumao - {T['title']}.pdf"), os.path.join(dst, "resumao.pdf"))
        shutil.copy(os.path.join(src, f"Anki - {T['title']}.apkg"), os.path.join(dst, "flashcards.apkg"))
        n_occ = len(T.get("occ_img", []))
        readme, figs = topic_readme(T, len(T["cards"]) + n_occ, n_occ)
        for rel in figs:
            shutil.copy(os.path.join(HERE, rel), os.path.join(dst, "figuras", os.path.basename(rel)))
        with open(os.path.join(dst, "README.md"), "w") as fh:
            fh.write(readme)
        dd = f"temas/{T['slug']}"
        linhas.append(f"| {code.upper()} | [{T['title']}]({dd}/README.md) | {fonte} | [PDF]({dd}/resumao.pdf) | "
                      f"[{len(T['cards']) + n_occ} cartões]({dd}/flashcards.apkg) | {len(figs)} |")

    fonte_dst = os.path.join(repo, "fonte")
    os.makedirs(os.path.join(fonte_dst, "web"), exist_ok=True)
    for f in os.listdir(HERE):
        if f.endswith(".py"):
            shutil.copy(os.path.join(HERE, f), os.path.join(fonte_dst, f))
    shutil.copy(os.path.join(HERE, "web", "pdf.js"), os.path.join(fonte_dst, "web", "pdf.js"))
    shutil.copytree(os.path.join(HERE, "web", "fonts"), os.path.join(fonte_dst, "web", "fonts"), dirs_exist_ok=True)
    os.makedirs(os.path.join(fonte_dst, "fig_livro"), exist_ok=True)
    for f in os.listdir(os.path.join(HERE, "fig_livro")):
        if f.endswith(".png") or f == "ocr_cache.json":
            shutil.copy(os.path.join(HERE, "fig_livro", f), os.path.join(fonte_dst, "fig_livro", f))
    with open(os.path.join(fonte_dst, "requirements.txt"), "w") as fh:
        fh.write("genanki\npillow\n")
    with open(os.path.join(repo, ".gitignore"), "w") as fh:
        fh.write("__pycache__/\n*.pyc\n")
    with open(os.path.join(repo, "README.md"), "w") as fh:
        fh.write(ROOT.replace("{linhas}", "\n".join(linhas)))
    print("\n".join(linhas))


ROOT = """# LIMAC · Estudos para a Liga Acadêmica de Cardiologia

Material para a prova de seleção da Liga Acadêmica de Cardiologia: um **resumão em PDF** e um **baralho do Anki**
por tema, com as figuras do Guyton (e do Porto, na Semiologia). Cada tema tem também uma página aqui no GitHub com
o resumo completo, as figuras, os números para decorar, um glossário, correlações clínicas e onde ler na fonte.

## Temas

| | Tema (página de estudo) | Base | Resumão | Anki | Figuras |
|---|---|---|---|---|---|
{linhas}

## Como estudar

1. **Leia a página do tema** (link na tabela) ou o resumão em PDF. Comece pelo *O essencial*: é o que a prova mais cobra.
2. **Faça os flashcards no mesmo dia.** No Anki: `Arquivo → Importar` e escolha o `.apkg`. Cada tema entra como
   subbaralho de *Liga de Cardiologia*. Há cartões de pergunta e resposta, de lacuna (cloze) e de **oclusão de imagem**
   sobre as figuras do livro (um rótulo coberto por um **?** laranja). Reimportar uma versão nova atualiza os cartões
   sem duplicar e sem perder o seu progresso.
3. **Revise os *Valores para decorar*** de cada tema na véspera da prova.
4. Para as **questões abertas** (casos clínicos), use as *Correlações clínicas*: elas ligam a fisiologia ao quadro
   do paciente, que é o que as perguntas abertas costumam pedir.

## Ordem sugerida

A → B → C (o coração como bomba e como sistema elétrico) → D → E → F → G → H (a circulação e o controle da pressão)
→ S (a semiologia, que usa tudo o que veio antes).

## Estrutura

```
temas/<tema>/README.md        página de estudo do tema (abre direto no GitHub)
temas/<tema>/resumao.pdf      resumão diagramado para imprimir ou ler no celular
temas/<tema>/flashcards.apkg  baralho do Anki
temas/<tema>/figuras/         figuras do livro usadas no tema
fonte/                        scripts que geram tudo (Python + HTML/CSS) e as figuras extraídas dos livros
```

Para regerar um tema: `pip install -r fonte/requirements.txt`, `npm install playwright` e
`python3 fonte/build.py tema_a` (os arquivos saem na pasta acima de `fonte/`). As oclusões de imagem acham o
rótulo na figura por OCR (tesseract, em português); o resultado fica em `fonte/fig_livro/ocr_cache.json`.

## Referências

- Hall JE, Hall ME. *Guyton & Hall · Tratado de Fisiologia Médica*. 14ª ed. Rio de Janeiro: GEN Guanabara Koogan.
- Porto CC, Porto AL. *Semiologia Médica*. 8ª ed. Rio de Janeiro: Guanabara Koogan; 2019.
- Moore KL, Dalley AF, Agur AMR. *Anatomia Orientada para a Clínica*. Rio de Janeiro: Guanabara Koogan.

Repositório privado, para estudo pessoal. As figuras pertencem aos respectivos livros.
"""


if __name__ == "__main__":
    main(sys.argv[1])
