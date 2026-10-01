// Modelo tipográfico dos resumões LIMAC (Typst), versão 3.
//
// Regras de diagramação (valem para todos os temas):
// - Uma coluna só. Nada de texto ao lado de figura ou tabela.
// - Figura sempre logo depois do parágrafo que a cita (#vf), centralizada,
//   com a legenda da mesma largura da figura. Nunca flutua.
// - Figura, tabela e caixa são blocos inteiros: nunca se partem.
// - Títulos ficam presos ao bloco seguinte (não ficam órfãos no pé da página).
// - O fim de cada tema é uma "Revisão rápida" que começa em página nova.
// - O build confere: página com sobra no pé, figura longe da citação e
//   figura sem citação.

#let cores = (
  prim: rgb("#8a1b2b"),      // vinho (identidade)
  prim-claro: rgb("#f8eef0"),
  azul: rgb("#1f4e79"),
  azul-claro: rgb("#edf3f9"),
  verde: rgb("#2d6a4f"),
  verde-claro: rgb("#edf5f0"),
  ambar: rgb("#8a5a00"),
  ambar-claro: rgb("#fcf5e6"),
  texto: rgb("#1d2026"),
  cinza: rgb("#5b5f66"),
  linha: rgb("#d5d9de"),
  zebra: rgb("#f5f6f8"),
)

#let sans = "Inter"
#let serif = "Source Serif 4"
#let espaco = 1.15em   // espaço padrão acima e abaixo de figuras, tabelas e caixas

// ---------- caixas ----------
#let caixa(titulo, cor, fundo, corpo) = block(
  width: 100%,
  breakable: false,
  fill: fundo,
  inset: (x: 12pt, top: 9pt, bottom: 10pt),
  radius: 3pt,
  stroke: (left: 3pt + cor),
  above: espaco,
  below: espaco,
)[
  #set par(justify: false, leading: 0.62em, spacing: 0.7em)
  #set list(spacing: 0.62em)
  #text(font: sans, weight: "bold", size: 7.8pt, fill: cor, tracking: 0.07em, upper(titulo))
  #v(4pt, weak: true)
  #set text(size: 9.8pt)
  #corpo
]

#let essencial(corpo, titulo: "O essencial") = caixa(titulo, cores.prim, cores.prim-claro, corpo)
#let decore(corpo, titulo: "Para decorar") = caixa(titulo, cores.azul, cores.azul-claro, corpo)
#let clinica(corpo, titulo: "Correlação clínica") = caixa(titulo, cores.verde, cores.verde-claro, corpo)
#let atencao(corpo, titulo: "Pegadinha de prova") = caixa(titulo, cores.ambar, cores.ambar-claro, corpo)

// ---------- figuras dos livros ----------
#let ref-livro(chave) = {
  // "g9_08" -> "Guyton & Hall, Fig. 9.8"
  let tipo = chave.at(0)
  let partes = chave.slice(1).split("_")
  let num = partes.at(0) + "." + str(int(partes.at(1).replace(regex("[a-z]$"), "")))
  if tipo == "g" { "Guyton & Hall, Fig. " + num } else if tipo == "p" { "Porto, Fig. " + num } else { chave }
}

#let caminho(chave) = {
  let pasta = if chave.at(0) == "g" { "guyton" } else if chave.at(0) == "p" { "porto" } else { "web" }
  "figuras/" + pasta + "/" + chave + ".png"
}

#let legenda-fig(legenda, chaves) = [#legenda #text(fill: cores.cinza, style: "italic")[(#chaves.map(ref-livro).join("; "))]]

// Tamanhos em pixels das figuras (gerado pelo build). A largura padrão segue uma
// escala única (px por cm), para que os rótulos de todas as figuras tenham o
// mesmo tamanho de letra que no livro.
#let tamanhos = json("figuras/tamanhos.json")
#let px-por-cm = 54
#let largura-padrao(chave, max-alt: 9cm) = {
  let t = tamanhos.at(chave)
  let w = t.at(0) / px-por-cm * 1cm
  let h = t.at(1) / px-por-cm * 1cm
  if h > max-alt { w = w * (max-alt / h) }
  w
}

// Paginação. Figuras e tabelas numeradas entram SEMPRE no fluxo do texto
// (nunca flutuam). O build ajusta a página: quando um bloco não cabe e deixaria
// sobra no pé, ele reduz a figura (até 80%) ou adia o bloco por um ou mais
// parágrafos, dentro da mesma seção. As escalas chegam por sys.inputs.
#let largura-texto = 21cm - 4.6cm
#let escalas = json(bytes(sys.inputs.at("escalas", default: "{}")))
#let bloco-movel(chave, conteudo) = block(width: 100%, breakable: false, above: espaco, below: espaco)[
  #context [#metadata((tipo: "ini", chave: chave, pagina: here().page(), y: here().position().y.pt()))<marca>]
  #conteudo
  #context [#metadata((tipo: "fim", chave: chave, pagina: here().page(), y: here().position().y.pt()))<marca>]
]

// Figura do livro, na escala única, logo após o parágrafo que a cita.
#let fig(chave, legenda, largura: auto, flutua: auto) = {
  let esc = escalas.at(chave, default: 1.0)
  let w0 = if largura == auto { calc.min(largura-padrao(chave).cm(), largura-texto.cm()) * 1cm } else if type(largura) == ratio { largura-texto * largura } else { largura }
  let w = w0 * esc
  let w-leg = calc.min(calc.max(w.cm(), 9), largura-texto.cm()) * 1cm
  bloco-movel(chave, align(center, block(width: w-leg)[
    #figure(
      image(caminho(chave), width: w),
      caption: legenda-fig(legenda, (chave,)),
      gap: 7pt,
    ) #label(chave)
    #context [#metadata((tipo: "fig", chave: chave, pagina: here().page()))<marca>]
  ]))
}

// Duas figuras lado a lado com a MESMA altura e uma legenda única.
#let par-figs(a, b, legenda, altura: 5.5cm, flutua: auto) = {
  let corpo = align(center)[
    #figure(
      grid(columns: 2, column-gutter: 18pt, align: bottom,
        image(caminho(a), height: altura), image(caminho(b), height: altura)),
      caption: legenda-fig(legenda, (a, b)),
      gap: 7pt,
    ) #label(a)
    #context [#metadata((tipo: "fig", chave: a, pagina: here().page()))<marca>]
  ]
  if flutua == none {
    block(width: 100%, breakable: false, above: espaco, below: espaco, corpo)
  } else {
    place(flutua, float: true, clearance: 1.5em, block(width: 100%, breakable: false, corpo))
  }
}

// Citação de figura no texto: #vf("g9_08") -> "Fig. 5" (com verificação de página)
#let vf(chave) = {
  context [#metadata((tipo: "ref", chave: chave, pagina: here().page()))<marca>]
  ref(label(chave))
}

// ---------- tabelas ----------
#let tabela(colunas, cabecalho, ..linhas, alinhar: auto, tamanho: 9.2pt, pad: 4.6pt, rotulo: none, titulo: none, flutua: auto) = {
  let t = {
    set text(size: tamanho, hyphenate: false)
    set par(justify: false, leading: 0.5em)
    table(
      columns: colunas,
      align: if alinhar == auto { (x, y) => left + horizon } else { alinhar },
      inset: (x: 7pt, y: pad),
      stroke: (x, y) => (
        top: if y == 0 { 1pt + cores.prim } else if y == 1 { 0.6pt + cores.prim } else { 0.4pt + cores.linha },
        bottom: 1pt + cores.prim,
      ),
      fill: (x, y) => if y > 0 and calc.even(y) { cores.zebra } else { none },
      table.header(..cabecalho.map(c => text(font: sans, weight: "semibold", size: tamanho - 0.7pt, fill: cores.prim, c))),
      ..linhas,
    )
  }
  if rotulo == none {
    block(breakable: false, above: espaco, below: espaco, width: 100%, t)
  } else {
    // tabela numerada que flutua como as figuras (citar com #vf(rotulo))
    bloco-movel(rotulo)[
      #figure(t, caption: titulo, kind: table, supplement: "Tabela", gap: 6pt) #label(rotulo)
      #context [#metadata((tipo: "fig", chave: rotulo, pagina: here().page()))<marca>]
    ]
  }
}

// ---------- miudezas ----------
#let seta = sym.arrow.r
#let quebra = pagebreak(weak: true)

// ---------- documento ----------
#let resumao(tema: "", titulo: "", area: "Fisiologia", fontes: (), corpo) = {
  set document(title: "Resumão " + tema + " · " + titulo, author: "LIMAC")
  set page(
    paper: "a4",
    margin: (x: 2.3cm, top: 2.2cm, bottom: 2.5cm),
    footer-descent: 40%,
    header: context {
      if counter(page).get().first() > 1 [
        #set text(font: sans, size: 7.5pt, fill: cores.cinza)
        #grid(columns: (1fr, auto), [Tema #tema · #titulo], [Liga de Cardiologia])
        #v(-4pt)
        #line(length: 100%, stroke: 0.4pt + cores.linha)
      ]
    },
    footer: context [
      #set text(font: sans, size: 7.6pt, fill: cores.cinza)
      #h(1fr) #counter(page).display() / #counter(page).final().first() #h(1fr)
    ],
  )
  set text(font: serif, size: 10.5pt, lang: "pt", region: "br", hyphenate: true, fill: cores.texto)
  set par(justify: true, leading: 0.66em, spacing: 1em)
  set list(indent: 0.3em, body-indent: 0.5em, spacing: 0.7em, marker: text(fill: cores.prim, sym.bullet))
  set enum(indent: 0.3em, body-indent: 0.5em, spacing: 0.7em)
  show strong: set text(weight: 600)
  set sub(typographic: false)

  set heading(numbering: "1.")
  show heading: set text(font: sans)
  show heading.where(level: 1): it => block(above: 1.9em, below: 0.9em, sticky: true, width: 100%)[
    #set text(size: 13pt, weight: "bold", fill: cores.prim)
    #if it.numbering != none {
      box(fill: cores.prim, inset: (x: 5pt, y: 3pt), radius: 2pt, baseline: 3pt,
        text(fill: white, size: 10.5pt, counter(heading).display("1")))
      h(0.5em)
    }
    #it.body
    #v(-5pt)
    #line(length: 100%, stroke: 0.7pt + cores.prim.lighten(50%))
  ]
  show heading.where(level: 2): it => block(above: 1.4em, below: 0.7em, sticky: true)[
    #set text(size: 10.8pt, weight: "semibold", fill: cores.azul)
    #it.body
  ]
  set figure(supplement: "Fig.")
  show figure.where(kind: table): set figure.caption(position: top)
  show figure.caption: it => {
    set text(size: 8.6pt)
    set par(justify: false, leading: 0.5em)
    align(left)[#text(font: sans, weight: "semibold", fill: cores.prim)[#it.supplement #context it.counter.display(it.numbering)] #h(0.25em) #it.body]
  }
  show ref: it => text(font: sans, size: 0.9em, weight: "semibold", fill: cores.prim, it)

  // cabeçalho da primeira página
  block(width: 100%, fill: cores.prim, inset: (x: 18pt, top: 16pt, bottom: 16pt), radius: 3pt, below: 1em)[
    #set text(font: sans, fill: white)
    #text(size: 8pt, weight: "semibold", tracking: 0.1em)[#upper(area) · TEMA #tema]
    #v(3pt)
    #text(size: 20pt, weight: "bold")[#titulo]
    #v(2pt)
    #text(size: 8.6pt)[Resumão enxuto para a prova da Liga Acadêmica de Cardiologia]
  ]
  if fontes.len() > 0 {
    block(width: 100%, below: 1.3em)[
      #set text(font: sans, size: 8pt, fill: cores.cinza)
      #set par(justify: false)
      *Fontes:* #fontes.join(" · ")
    ]
  }
  corpo
}

// Revisão rápida: começa em página nova e não é numerada.
#let revisao(corpo) = {
  pagebreak(weak: true)
  context [#metadata((tipo: "revisao", chave: "", pagina: here().page()))<marca>]
  heading(numbering: none, level: 1)[Revisão rápida]
  corpo
}
