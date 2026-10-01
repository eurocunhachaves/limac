# LIMAC · Estudos para a Liga Acadêmica de Cardiologia

Material para a prova de seleção da Liga Acadêmica de Cardiologia: um **resumão em PDF** e um **baralho do Anki**
por tema, com as figuras do Guyton (e do Porto, na Semiologia). Cada tema tem também uma página aqui no GitHub com
o resumo completo, as figuras, os números para decorar, um glossário, correlações clínicas e onde ler na fonte.

## Temas

| | Tema (página de estudo) | Base | Resumão | Anki | Figuras |
|---|---|---|---|---|---|
| A | [Músculo cardíaco e valvas cardíacas](temas/a-musculo-cardiaco-e-valvas/README.md) | Guyton cap. 9 (e 23) | [PDF](temas/a-musculo-cardiaco-e-valvas/resumao.pdf) | [76 cartões](temas/a-musculo-cardiaco-e-valvas/flashcards.apkg) | 7 |
| B | [Excitação rítmica do coração](temas/b-excitacao-ritmica/README.md) | Guyton cap. 10 | [PDF](temas/b-excitacao-ritmica/resumao.pdf) | [48 cartões](temas/b-excitacao-ritmica/flashcards.apkg) | 4 |
| C | [O eletrocardiograma normal](temas/c-ecg-normal/README.md) | Guyton caps. 11 e 12 | [PDF](temas/c-ecg-normal/resumao.pdf) | [48 cartões](temas/c-ecg-normal/flashcards.apkg) | 7 |
| D | [Biofísica da circulação](temas/d-biofisica-circulacao/README.md) | Guyton caps. 14 e 15 | [PDF](temas/d-biofisica-circulacao/resumao.pdf) | [73 cartões](temas/d-biofisica-circulacao/flashcards.apkg) | 11 |
| E | [Microcirculação e sistema linfático](temas/e-microcirculacao-linfatico/README.md) | Guyton cap. 16 | [PDF](temas/e-microcirculacao-linfatico/resumao.pdf) | [50 cartões](temas/e-microcirculacao-linfatico/flashcards.apkg) | 8 |
| F | [Controle local, humoral e nervoso da circulação](temas/f-controle-circulacao/README.md) | Guyton caps. 17 e 18 | [PDF](temas/f-controle-circulacao/resumao.pdf) | [70 cartões](temas/f-controle-circulacao/flashcards.apkg) | 11 |
| G | Débito cardíaco e retorno venoso | Guyton cap. 20 | em preparação | | |
| H | Regulação da pressão arterial pelo sistema renal | Guyton cap. 19 | em preparação | | |
| S | Semiologia cardiovascular | Porto, Semiologia Médica | em preparação | | |

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
