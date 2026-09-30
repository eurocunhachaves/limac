"""Copia o material gerado para o repositório GitHub (eurocunhachaves/limac) e reescreve o README.

Uso: python3 sync_repo.py /caminho/do/clone   (depois: git add -A && git commit && git push)
Não copia os livros-fonte (direitos autorais).
"""
import importlib
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
    ("e", "Fisiologia vascular e da microcirculação", "Guyton caps. 15 e 16"),
    ("f", "Controle local, humoral e nervoso da circulação", "Guyton caps. 17 e 18"),
    ("g", "Débito cardíaco e retorno venoso", "Guyton cap. 20"),
    ("h", "Regulação da pressão arterial pelo sistema renal", "Guyton cap. 19"),
    ("s", "Semiologia cardiovascular", "Porto, Semiologia Médica"),
]


def main(repo):
    linhas = []
    for code, titulo, fonte in PLANO:
        mod = f"tema_{code}"
        if not os.path.exists(os.path.join(HERE, mod + ".py")):
            linhas.append(f"| {code} | {titulo} | {fonte} | em preparação | | |")
            continue
        T = importlib.import_module(mod).TOPIC
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
    with open(os.path.join(fonte_dst, "requirements.txt"), "w") as fh:
        fh.write("genanki\nreportlab\nmatplotlib\nnumpy\n")
    with open(os.path.join(repo, ".gitignore"), "w") as fh:
        fh.write("__pycache__/\n*.pyc\n")

    readme = f"""# LIMAC · Estudos para a Liga Acadêmica de Cardiologia

Material de estudo que montei para a prova de seleção da Liga Acadêmica de Cardiologia: resumões em PDF,
listas de questões com gabarito comentado e baralhos do Anki, organizados por tema.

## Temas

| | Tema | Base | Resumão | Questões | Anki |
|---|---|---|---|---|---|
{chr(10).join(linhas)}

## Como usar

- **Resumão**: leitura rápida do tema, com esquemas e uma tabela final de números para decorar.
- **Questões**: múltipla escolha no formato da prova e casos clínicos abertos. O gabarito comentado fica no final do PDF.
- **Anki**: no Anki, `Arquivo → Importar` e escolha o `.apkg`. Cada tema entra como subbaralho de
  *Liga de Cardiologia*, com cartões de pergunta e resposta, de lacuna (cloze) e de oclusão de imagem.
  Reimportar uma versão nova atualiza os cartões sem duplicar.

## Estrutura

```
temas/<tema>/resumao.pdf      resumo do tema
temas/<tema>/questoes.pdf     questões + gabarito comentado
temas/<tema>/flashcards.apkg  baralho do Anki
fonte/                        scripts que geram tudo (Python)
```

Para regerar um tema: `pip install -r fonte/requirements.txt` e `python3 fonte/build.py tema_a`
(os arquivos saem na pasta acima de `fonte/`).

## Referências

- Hall JE, Hall ME. *Guyton & Hall · Tratado de Fisiologia Médica*. 14ª ed. Rio de Janeiro: GEN Guanabara Koogan.
- Porto CC, Porto AL. *Semiologia Médica*. 8ª ed. Rio de Janeiro: Guanabara Koogan; 2019.

Os livros não estão neste repositório, e esta versão pública não inclui figuras deles: os esquemas foram
desenhados a partir dos valores descritos no texto. (Os scripts referenciam uma pasta `fig_livro/` que só existe na
minha cópia pessoal.) Material de estudo pessoal, sem fins comerciais.
"""
    with open(os.path.join(repo, "README.md"), "w") as fh:
        fh.write(readme)
    print("\n".join(linhas))


if __name__ == "__main__":
    main(sys.argv[1])
