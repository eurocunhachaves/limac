# LIMAC · Cardiologia

Material de estudo para a prova de entrada da **Liga Acadêmica de Cardiologia**: resumões enxutos em PDF e baralhos do Anki, tema a tema. Tudo foi refeito do zero com diagramação em **Typst** e figuras tiradas diretamente dos livros-texto, com o número de cada figura citado na legenda.

## Como estudar com este material

1. Leia o **resumão** do tema (cada um tem de 4 a 8 páginas). Comece pela caixa *Em 30 segundos*.
2. Faça os **flashcards** no mesmo dia e revise no Anki nos dias seguintes.
3. Antes da prova, releia só as seções *Valores para decorar*, *Correlações clínicas* e *Pegadinhas de prova* de cada tema.
4. Dúvida em um ponto? A tabela *Onde ler nas fontes* de cada tema aponta capítulo e página do PDF do livro.

## Temas

| | Tema | Área | O que cobre | Arquivos |
|---|---|---|---|---|
| **A** | [O músculo cardíaco e as valvas cardíacas](temas/a-musculo-cardiaco-e-valvas/README.md) | Fisiologia | Sincício, potencial de ação com platô, acoplamento excitação-contração, ciclo cardíaco (Wiggers), valvas, alça pressão-volume, Frank-Starling | [PDF](temas/a-musculo-cardiaco-e-valvas/resumao.pdf) · [Anki](temas/a-musculo-cardiaco-e-valvas/flashcards.apkg) |
| **B** | [Excitação rítmica do coração](temas/b-excitacao-ritmica/README.md) | Fisiologia | Nó sinusal e automatismo, nó AV e retardo, sistema de Purkinje, marca-passos ectópicos, controle autonômico | [PDF](temas/b-excitacao-ritmica/resumao.pdf) · [Anki](temas/b-excitacao-ritmica/flashcards.apkg) |

## Flashcards (Anki)

Cada tema tem um arquivo `.apkg` pronto para importar (*Arquivo → Importar*). Os baralhos ficam agrupados em **LIMAC Cardiologia** e trazem três tipos de cartão:

- **Básico:** pergunta e resposta, muitas vezes com a figura do livro no verso.
- **Lacuna:** frases com valores e conceitos para completar.
- **Oclusão de imagem:** um rótulo da figura do livro fica coberto e você precisa dizer qual é.

Os cartões têm modo noturno e funcionam no AnkiDroid e no AnkiMobile.

## Fontes

- **Guyton & Hall.** *Tratado de Fisiologia Médica*, 14ª ed. Caps. 9–11, 14–20 e 23.
- **Porto, C. C.** *Semiologia Médica*, 8ª ed. Caps. 46–51 e 55.
- **Moore.** *Anatomia Orientada para a Clínica* (consulta).

As figuras foram extraídas dos PDFs dos livros para uso pessoal de estudo. O repositório é privado; os PDFs dos livros não estão aqui.

## Estrutura do repositório

```
temas/<tema>/README.md       página do tema: essencial, valores, figuras, glossário, clínica, onde ler
temas/<tema>/resumao.pdf     resumão diagramado
temas/<tema>/flashcards.apkg baralho do Anki
fonte/modelo.typ             modelo tipográfico (Typst)
fonte/temas/<código>.py      conteúdo de cada tema (texto, tabelas, cartões)
fonte/build.py, anki.py      geração do PDF, do README e do baralho
fonte/figuras/               figuras dos livros usadas no material
fonte/fontes/                fontes tipográficas (Inter e Source Serif 4, licença OFL)
```

Para regenerar: `pip install typst pymupdf genanki pillow`, instalar `tesseract-ocr-por` e rodar `python3 fonte/build.py todos`.
