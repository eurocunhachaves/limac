"""Copia o material gerado para o repositório GitHub (eurocunhachaves/limac) e reescreve o README.

Uso: python3 sync_repo.py /caminho/do/clone   (depois: git add -A && git commit && git push)
Não copia os livros-fonte (direitos autorais).
"""
import importlib
import json
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

# ordem e títulos dos temas da prova; entram no índice como "em preparação" até existir tema_X.py
PLANO = [
    ("a", "O músculo cardíaco e as valvas cardíacas", "Guyton cap. 9 (e 23)"),
    ("b", "Excitação rítmica do coração", "Guyton cap. 10"),
    ("c", "O eletrocardiograma normal", "Guyton caps. 11 e 12"),
    ("d", "Biofísica da circulação", "Guyton caps. 14 e 15"),
    ("e", "Fisiologia vascular e da microcirculação", "Guyton cap. 16"),
    ("f", "Controle local, humoral e nervoso da circulação", "Guyton caps. 17 e 18"),
    ("g", "Débito cardíaco e retorno venoso", "Guyton cap. 20"),
    ("h", "Regulação da pressão arterial pelo sistema renal", "Guyton cap. 19"),
    ("s", "Semiologia cardiovascular", "Porto, Semiologia Médica"),
]


QUIZ_URL = "https://eurocunhachaves.github.io/limac/"


def sync_quiz(repo, temas):
    """Publica o quiz web em docs/ (GitHub Pages): página, fontes e um JSON por tema."""
    docs = os.path.join(repo, "docs")
    os.makedirs(os.path.join(docs, "data"), exist_ok=True)
    os.makedirs(os.path.join(docs, "fonts"), exist_ok=True)
    shutil.copy(os.path.join(HERE, "web", "quiz", "index.html"), os.path.join(docs, "index.html"))
    for f in os.listdir(os.path.join(HERE, "web", "fonts")):
        shutil.copy(os.path.join(HERE, "web", "fonts", f), os.path.join(docs, "fonts", f))
    open(os.path.join(docs, ".nojekyll"), "w").close()
    index = []
    for T in temas:
        src = os.path.join(OUT_ROOT, "_publico", T["slug"], "quiz.json")
        if not os.path.exists(src):
            continue
        shutil.copy(src, os.path.join(docs, "data", f"{T['code']}.json"))
        index.append({"code": T["code"], "title": T["title"], "kind": "tema", "n": len(T["mcq"]),
                      "open": len(T["open"]) + len(T.get("open_extra", []))})
    sims = os.path.join(OUT_ROOT, "_publico", "simulados")
    if os.path.isdir(sims):
        for f in sorted(os.listdir(sims)):
            if f.endswith(".json"):
                d = json.load(open(os.path.join(sims, f)))
                shutil.copy(os.path.join(sims, f), os.path.join(docs, "data", f))
                index.append({"code": d["code"], "title": d["title"], "kind": "simulado", "n": len(d["mcq"]),
                              "open": len(d["open"]), "minutes": d.get("minutes")})
    with open(os.path.join(docs, "data", "index.json"), "w") as fh:
        json.dump(index, fh, ensure_ascii=False)


def main(repo):
    linhas = []
    temas = []
    for code, titulo, fonte in PLANO:
        mod = f"tema_{code}"
        if not os.path.exists(os.path.join(HERE, mod + ".py")):
            linhas.append(f"| {code} | {titulo} | {fonte} | em preparação | | |")
            continue
        T = importlib.import_module(mod).TOPIC
        temas.append(T)
        src = os.path.join(OUT_ROOT, "_publico", T["slug"])  # versão pública: sem figuras dos livros
        dst = os.path.join(repo, "temas", T["slug"])
        os.makedirs(dst, exist_ok=True)
        for n in ("resumao.pdf", "questoes.pdf", "flashcards.apkg"):
            shutil.copy(os.path.join(src, n), os.path.join(dst, n))
        d = f"temas/{T['slug']}"
        linhas.append(f"| {code} | {titulo} | {fonte} | [resumão]({d}/resumao.pdf) | "
                      f"[{len(T['mcq'])} objetivas + {len(T['open']) + len(T.get('open_extra', []))} abertas]({d}/questoes.pdf) | "
                      f"[baralho]({d}/flashcards.apkg) |")

    fonte_dst = os.path.join(repo, "fonte")
    os.makedirs(os.path.join(fonte_dst, "fig"), exist_ok=True)
    for f in os.listdir(HERE):
        if f.endswith(".py"):
            shutil.copy(os.path.join(HERE, f), os.path.join(fonte_dst, f))
    for f in os.listdir(os.path.join(HERE, "fig")):
        shutil.copy(os.path.join(HERE, "fig", f), os.path.join(fonte_dst, "fig", f))
    os.makedirs(os.path.join(fonte_dst, "web"), exist_ok=True)
    shutil.copy(os.path.join(HERE, "web", "pdf.js"), os.path.join(fonte_dst, "web", "pdf.js"))
    shutil.copytree(os.path.join(HERE, "web", "fonts"), os.path.join(fonte_dst, "web", "fonts"), dirs_exist_ok=True)
    if os.path.isdir(os.path.join(HERE, "fig_web")):  # imagens de licença aberta (Wikimedia Commons), com créditos
        shutil.copytree(os.path.join(HERE, "fig_web"), os.path.join(fonte_dst, "fig_web"), dirs_exist_ok=True)
    sync_quiz(repo, temas)
    with open(os.path.join(fonte_dst, "requirements.txt"), "w") as fh:
        fh.write("genanki\nreportlab\nmatplotlib\nnumpy\n")
    with open(os.path.join(repo, ".gitignore"), "w") as fh:
        fh.write("__pycache__/\n*.pyc\n")

    readme = f"""# LIMAC · Estudos para a Liga Acadêmica de Cardiologia

Material de estudo que montei para a prova de seleção da Liga Acadêmica de Cardiologia: resumões em PDF,
listas de questões com gabarito comentado, baralhos do Anki e um quiz on-line, organizados por tema.

**▶ Quiz on-line: [{QUIZ_URL}]({QUIZ_URL})** (correção na hora, modo prova com cronômetro e simulados)

## Temas

| | Tema | Base | Resumão | Questões | Anki |
|---|---|---|---|---|---|
{chr(10).join(linhas)}

## Como usar

- **Resumão**: leitura rápida do tema, com esquemas e uma tabela final de números para decorar.
- **Quiz on-line**: as mesmas questões objetivas no navegador, com correção e comentário na hora (modo estudo)
  ou com cronômetro e correção no fim (modo prova). Guarda o seu melhor resultado por tema no próprio navegador.
- **Questões**: múltipla escolha no formato da prova e casos clínicos abertos. O gabarito comentado fica no final do PDF.
- **Anki**: no Anki, `Arquivo → Importar` e escolha o `.apkg`. Cada tema entra como subbaralho de
  *Liga de Cardiologia*, com cartões de pergunta e resposta, de lacuna (cloze) e de oclusão de imagem.
  Reimportar uma versão nova atualiza os cartões sem duplicar.

## Estrutura

```
temas/<tema>/resumao.pdf      resumo do tema
temas/<tema>/questoes.pdf     questões + gabarito comentado
temas/<tema>/flashcards.apkg  baralho do Anki
docs/                         quiz on-line (GitHub Pages)
fonte/                        scripts que geram tudo (Python + HTML/CSS)
```

Para regerar um tema: `pip install -r fonte/requirements.txt`, `npm install playwright` (o resumão é diagramado em
HTML/CSS e impresso em PDF pelo Chromium) e `python3 fonte/build.py tema_a` (os arquivos saem na pasta acima de `fonte/`).

## Referências

- Hall JE, Hall ME. *Guyton & Hall · Tratado de Fisiologia Médica*. 14ª ed. Rio de Janeiro: GEN Guanabara Koogan.
- Porto CC, Porto AL. *Semiologia Médica*. 8ª ed. Rio de Janeiro: Guanabara Koogan; 2019.

Os livros não estão neste repositório, e esta versão pública não inclui figuras deles: os esquemas foram
desenhados a partir dos valores descritos no texto, e as demais imagens são de licença aberta (Wikimedia Commons),
com autor e licença indicados na legenda e em `fonte/fig_web/*/creditos.json`. A fonte Inter é distribuída sob a
SIL Open Font License. (Os scripts referenciam uma pasta `fig_livro/` que só existe na
minha cópia pessoal.) Material de estudo pessoal, sem fins comerciais.
"""
    with open(os.path.join(repo, "README.md"), "w") as fh:
        fh.write(readme)
    print("\n".join(linhas))


if __name__ == "__main__":
    main(sys.argv[1])
