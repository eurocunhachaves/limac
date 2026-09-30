# LIMAC · Estudos para a Liga Acadêmica de Cardiologia

Material de estudo que montei para a prova de seleção da Liga Acadêmica de Cardiologia: resumões em PDF,
listas de questões com gabarito comentado, baralhos do Anki e um quiz on-line, organizados por tema.

**▶ Quiz on-line: [https://eurocunhachaves.github.io/limac/](https://eurocunhachaves.github.io/limac/)** (correção na hora, modo prova com cronômetro e simulados)

## Temas

| | Tema | Base | Resumão | Questões | Anki |
|---|---|---|---|---|---|
| a | O músculo cardíaco e as valvas cardíacas | Guyton cap. 9 (e 23) | [resumão](temas/a-musculo-cardiaco-e-valvas/resumao.pdf) | [27 objetivas + 9 abertas](temas/a-musculo-cardiaco-e-valvas/questoes.pdf) | [baralho](temas/a-musculo-cardiaco-e-valvas/flashcards.apkg) |
| b | Excitação rítmica do coração | Guyton cap. 10 | [resumão](temas/b-excitacao-ritmica/resumao.pdf) | [23 objetivas + 8 abertas](temas/b-excitacao-ritmica/questoes.pdf) | [baralho](temas/b-excitacao-ritmica/flashcards.apkg) |
| c | O eletrocardiograma normal | Guyton caps. 11 e 12 | [resumão](temas/c-ecg-normal/resumao.pdf) | [25 objetivas + 9 abertas](temas/c-ecg-normal/questoes.pdf) | [baralho](temas/c-ecg-normal/flashcards.apkg) |
| d | Biofísica da circulação | Guyton caps. 14 e 15 | [resumão](temas/d-biofisica-circulacao/resumao.pdf) | [28 objetivas + 9 abertas](temas/d-biofisica-circulacao/questoes.pdf) | [baralho](temas/d-biofisica-circulacao/flashcards.apkg) |
| e | Fisiologia vascular e da microcirculação | Guyton cap. 16 | em preparação | | |
| f | Controle local, humoral e nervoso da circulação | Guyton caps. 17 e 18 | em preparação | | |
| g | Débito cardíaco e retorno venoso | Guyton cap. 20 | em preparação | | |
| h | Regulação da pressão arterial pelo sistema renal | Guyton cap. 19 | em preparação | | |
| s | Semiologia cardiovascular | Porto, Semiologia Médica | em preparação | | |

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
