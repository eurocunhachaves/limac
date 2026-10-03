# LIMAC · Cardiologia

Material de estudo para a prova de entrada da **Liga Acadêmica de Cardiologia**: resumões enxutos em PDF e baralhos do Anki, tema a tema. Tudo foi refeito do zero com diagramação em **Typst** e figuras tiradas diretamente dos livros-texto, com o número de cada figura citado na legenda.

## Como estudar com este material

1. Leia o **resumão** do tema (cada um tem de 7 a 10 páginas, contando a revisão final). Comece pela caixa *Em 30 segundos*.
2. Faça os **flashcards** no mesmo dia e revise no Anki nos dias seguintes.
3. Antes da prova, releia só as seções *Valores para decorar*, *Correlações clínicas* e *Pegadinhas de prova* de cada tema.
4. Dúvida em um ponto? A tabela *Onde ler nas fontes* de cada tema aponta capítulo e página do PDF do livro.

### Semiologia (temas S, T e U)

A Semiologia é conteúdo novo e prático, então vale estudar com os olhos, os ouvidos e as mãos:

- **Veja antes de ler.** A página de cada tema tem vídeos por subtema, curtos e longos, em português e inglês. Assista ao do subtema e só depois leia a parte correspondente do resumão.
- **Treine o ouvido.** Ausculta é som: faça o [baralho de sons](anki/LIMAC-Sons-cardiacos.apkg) com fone de ouvido e use as [bibliotecas de sons](temas/t-semiologia-precordio-bulhas-sopros/README.md#sons-cardíacos) indicadas no tema T.
- **Pratique em alguém de casa.** Ache o ictus e os focos de ausculta, palpe os pulsos, olhe a jugular a 45° e meça a pressão arterial seguindo o resumão U.
- **Explique em voz alta.** Depois do Anki, explique um sintoma do tema S (a dispneia, por exemplo) como se estivesse falando com um paciente.

## Temas

| | Tema | Área | O que cobre | Arquivos |
|---|---|---|---|---|
{{TABELA}}

## Flashcards (Anki)

Cada tema tem um arquivo `.apkg` pronto para importar (*Arquivo → Importar*). Os baralhos ficam agrupados em **LIMAC Cardiologia** e trazem três tipos de cartão:

- **Básico:** pergunta e resposta, muitas vezes com a figura do livro no verso.
- **Lacuna:** frases com valores e conceitos para completar.
- **Oclusão de imagem:** um rótulo da figura do livro fica coberto e você precisa dizer qual é.

Os cartões têm modo noturno e funcionam no AnkiDroid e no AnkiMobile.

Para importar tudo de uma vez, use [`anki/LIMAC-Cardiologia-completo.apkg`](anki/LIMAC-Cardiologia-completo.apkg): um único arquivo com todos os temas como subbaralhos. Ele usa os mesmos identificadores dos arquivos por tema, então importar os dois não duplica cartões.

### Baralho de sons (ausculta)

[`anki/LIMAC-Sons-cardiacos.apkg`](anki/LIMAC-Sons-cardiacos.apkg) é um baralho **separado, só de áudio**, com 17 gravações reais: bulhas normais, frequência e ritmo, taquicardias, fibrilação atrial, B3, B4, clique sistólico, sopros de ejeção e de regurgitação, sopro inocente, reforço pré-sistólico e sopro carotídeo. Na frente o som toca com uma pergunta; no verso vêm a resposta e a parte **Para associar**, que liga o som a outro tema (fisiologia A–H ou semiologia S–U). Ele não faz parte do baralho completo: importe-o à parte e use fone de ouvido. Autoria e licença de cada gravação estão em [`fonte/sons/CREDITOS.md`](fonte/sons/CREDITOS.md).

Ficaram de fora os sons sem gravação de licença livre que desse para conferir com segurança: desdobramentos da B2, estalido de abertura, sopro da insuficiência aórtica, atrito pericárdico, extrassístoles, BAVT e sons de Korotkoff. Os quatro primeiros estão nas [bibliotecas de sons](temas/t-semiologia-precordio-bulhas-sopros/README.md#sons-cardíacos) do tema T, e os sons de Korotkoff, no [vídeo da MedTV](temas/u-semiologia-pulsos-pulso-venoso-pa/README.md#pressão-arterial-e-sons-de-korotkoff) do tema U. Para extrassístoles e BAVT, as Fig. 47.8 e 47.10 do Porto, no [tema S](temas/s-semiologia-anamnese-sintomas-arritmias/README.md), descrevem o que se ouve.

## Fontes

- **Guyton & Hall.** *Tratado de Fisiologia Médica*, 14ª ed. Caps. 9–12 e 14–20.
- **Porto, C. C.** *Semiologia Médica*, 8ª ed. Caps. 46 e 47.
- **Moore.** *Anatomia Orientada para a Clínica* (consulta).
- **Gravações de sons cardíacos:** Wikimedia Commons e os bancos HLS-CMDS e CirCor DigiScope (PhysioNet), todos com licença livre ([créditos](fonte/sons/CREDITOS.md)).

As figuras foram extraídas dos PDFs dos livros para uso pessoal de estudo. O repositório é privado; os PDFs dos livros não estão aqui.

## Estrutura do repositório

```
temas/<tema>/README.md       página do tema: essencial, valores, figuras, glossário, clínica, onde ler (e vídeos, em S, T e U)
temas/<tema>/resumao.pdf     resumão diagramado
temas/<tema>/flashcards.apkg baralho do Anki
anki/LIMAC-Cardiologia-completo.apkg  todos os baralhos num arquivo só
anki/LIMAC-Sons-cardiacos.apkg        baralho de sons (ausculta), separado
fonte/modelo.typ             modelo tipográfico (Typst)
fonte/temas/<código>.py      conteúdo de cada tema (texto, tabelas, cartões)
fonte/build.py, anki.py      geração do PDF, do README e do baralho
fonte/videos.py              vídeos recomendados de S, T e U e bibliotecas de sons
fonte/anki_sons.py           cartões e geração do baralho de sons
fonte/sons/                  gravações (MP3) e CREDITOS.md, com autoria e licenças
fonte/figuras/               figuras dos livros usadas no material e legendas.json (legendas completas)
fonte/scripts/               extração das figuras e das legendas a partir dos PDFs dos livros
fonte/fontes/                fontes tipográficas (Inter e Source Serif 4, licença OFL)
```

Para regenerar tudo: `pip install typst pymupdf genanki pillow`, instalar `tesseract-ocr-por` e rodar `python3 fonte/build.py todos`. Para mexer só nas páginas do GitHub, sem tocar nos PDFs nem nos baralhos: `python3 fonte/build.py readme`. Baralho de sons: `python3 fonte/anki_sons.py`.
