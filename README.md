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
| **C** | [Eletrocardiograma normal](temas/c-ecg-normal/README.md) | Fisiologia | Ondas, intervalos e segmentos, papel milimetrado, derivações (Einthoven, aumentadas, precordiais), eixo | [PDF](temas/c-ecg-normal/resumao.pdf) · [Anki](temas/c-ecg-normal/flashcards.apkg) |
| **D** | [Biofísica da circulação](temas/d-biofisica-da-circulacao/README.md) | Fisiologia | Pressão, fluxo e resistência, Poiseuille, viscosidade, complacência, pulso arterial, medida da PA | [PDF](temas/d-biofisica-da-circulacao/resumao.pdf) · [Anki](temas/d-biofisica-da-circulacao/flashcards.apkg) |
| **E** | [Vasos, pulso e microcirculação](temas/e-vasos-e-microcirculacao/README.md) | Fisiologia | Capilares, forças de Starling, interstício, edema, sistema linfático | [PDF](temas/e-vasos-e-microcirculacao/resumao.pdf) · [Anki](temas/e-vasos-e-microcirculacao/flashcards.apkg) |
| **F** | [Controle local, humoral e nervoso da circulação](temas/f-controle-da-circulacao/README.md) | Fisiologia | Autorregulação, metabólitos, NO, angiogênese, hormônios vasoativos, barorreceptores, quimiorreceptores, reflexos | [PDF](temas/f-controle-da-circulacao/resumao.pdf) · [Anki](temas/f-controle-da-circulacao/flashcards.apkg) |
| **G** | [Débito cardíaco e retorno venoso](temas/g-debito-cardiaco-e-retorno-venoso/README.md) | Fisiologia | Débito cardíaco = retorno venoso, curvas de débito e de retorno, pressão média de enchimento, métodos de medida | [PDF](temas/g-debito-cardiaco-e-retorno-venoso/resumao.pdf) · [Anki](temas/g-debito-cardiaco-e-retorno-venoso/flashcards.apkg) |
| **H** | [Regulação renal da pressão arterial](temas/h-regulacao-renal-da-pa/README.md) | Fisiologia | Diurese e natriurese de pressão, curva de débito renal, sistema renina-angiotensina-aldosterona, sal e hipertensão | [PDF](temas/h-regulacao-renal-da-pa/resumao.pdf) · [Anki](temas/h-regulacao-renal-da-pa/flashcards.apkg) |

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
