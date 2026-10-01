// Modelo tipográfico dos resumões LIMAC (Typst).
// Corpo em Source Serif 4, títulos e elementos de interface em Inter.

#let cores = (
  prim: rgb("#8a1b2b"),      // vinho (identidade)
  prim-claro: rgb("#f7ecee"),
  azul: rgb("#1f4e79"),
  azul-claro: rgb("#eaf1f8"),
  verde: rgb("#2d6a4f"),
  verde-claro: rgb("#eaf4ee"),
  ambar: rgb("#9a6200"),
  ambar-claro: rgb("#fdf4e3"),
  cinza: rgb("#5b5f66"),
  linha: rgb("#d9dce1"),
  zebra: rgb("#f6f7f9"),
)

#let sans = "Inter"
#let serif = "Source Serif 4"

// ---------- caixas ----------
#let caixa(titulo, cor, fundo, corpo, quebra: false, icone: none) = block(
  width: 100%,
  breakable: quebra,
  fill: fundo,
  inset: (left: 11pt, right: 11pt, top: 8pt, bottom: 9pt),
  radius: (right: 3pt),
  stroke: (left: 2.6pt + cor),
  above: 1.1em,
  below: 1.1em,
)[
  #set par(justify: false)
  #text(font: sans, weight: "bold", size: 7.6pt, fill: cor, tracking: 0.06em, upper(titulo))
  #v(3pt, weak: true)
  #set text(size: 9.4pt)
  #corpo
]

#let essencial(corpo, titulo: "O essencial", quebra: false) = caixa(titulo, cores.prim, cores.prim-claro, corpo, quebra: quebra)
#let decore(corpo, titulo: "Para decorar", quebra: false) = caixa(titulo, cores.azul, cores.azul-claro, corpo, quebra: quebra)
#let clinica(corpo, titulo: "Correlação clínica", quebra: false) = caixa(titulo, cores.verde, cores.verde-claro, corpo, quebra: quebra)
#let atencao(corpo, titulo: "Pegadinha de prova", quebra: false) = caixa(titulo, cores.ambar, cores.ambar-claro, corpo, quebra: quebra)

// ---------- figuras dos livros ----------
// fonte: "g" = Guyton & Hall (14ª ed.), "p" = Porto (8ª ed.), "w" = internet
#let livros = (
  g: "Guyton & Hall, Tratado de Fisiologia Médica, 14ª ed.",
  p: "Porto, Semiologia Médica, 8ª ed.",
)

#let ref-livro(chave) = {
  // "g9_08" -> "Guyton & Hall, Fig. 9.8"
  let tipo = chave.at(0)
  let partes = chave.slice(1).split("_")
  let num = partes.at(0) + "." + str(int(partes.at(1).replace(regex("[a-z]$"), "")))
  if tipo == "g" { "Guyton & Hall, Fig. " + num } else if tipo == "p" { "Porto, Fig. " + num } else { chave }
}

#let fig(chave, legenda, largura: 100%, altura: auto, credito: auto, flutua: none) = {
  let pasta = if chave.at(0) == "g" { "guyton" } else if chave.at(0) == "p" { "porto" } else { "web" }
  let cred = if credito == auto { ref-livro(chave) } else { credito }
  figure(
    if altura == auto { image("figuras/" + pasta + "/" + chave + ".png", width: largura) } else { image("figuras/" + pasta + "/" + chave + ".png", height: altura) },
    caption: [#legenda #h(0.3em) #text(fill: cores.cinza, style: "italic")[(#cred)]],
    placement: flutua,
    gap: 6pt,
  )
}

// Figura ao lado do texto. `lado` = "esq" ou "dir".
#let ao-lado(figura, corpo, prop: 42%, lado: "dir", gutter: 14pt, flutua: none) = {
  let cols = if lado == "dir" { (1fr, prop) } else { (prop, 1fr) }
  let cel = if lado == "dir" { (corpo, figura) } else { (figura, corpo) }
  let b = block(breakable: false, above: 1em, below: 1em,
    grid(columns: cols, column-gutter: gutter, align: (top, top), ..cel))
  if flutua == none { b } else { place(flutua, float: true, clearance: 1.2em, b) }
}

// ---------- tabelas ----------
#let tabela(colunas, cabecalho, ..linhas, quebra: false, alinhar: auto, tamanho: 8.9pt, pad: 5pt) = {
  let n = cabecalho.len()
  block(breakable: quebra, above: 1em, below: 1.1em)[
    #set text(size: tamanho, hyphenate: false)
    #set par(justify: false, leading: 0.5em)
    #table(
      columns: colunas,
      align: if alinhar == auto { (x, y) => left + horizon } else { alinhar },
      inset: (x: 6pt, y: pad),
      stroke: (x, y) => (
        top: if y == 0 { 0.9pt + cores.prim } else if y == 1 { 0.6pt + cores.prim } else { 0.4pt + cores.linha },
        bottom: 0.9pt + cores.prim,
      ),
      fill: (x, y) => if y > 0 and calc.even(y) { cores.zebra } else { none },
      table.header(..cabecalho.map(c => text(font: sans, weight: "semibold", size: tamanho - 0.6pt, fill: cores.prim, c))),
      ..linhas,
    )
  ]
}

// ---------- miudezas ----------
#let termo(t) = text(font: sans, weight: "semibold", size: 0.92em, fill: cores.prim, t)
#let seta = sym.arrow.r
#let sobe = text(fill: cores.verde, weight: "bold", sym.arrow.t)
#let desce = text(fill: cores.prim, weight: "bold", sym.arrow.b)

// ---------- documento ----------
#let resumao(tema: "", titulo: "", area: "Fisiologia", fontes: (), corpo) = {
  set document(title: "Resumão " + tema + " · " + titulo, author: "LIMAC")
  set page(
    paper: "a4",
    margin: (x: 1.9cm, top: 2.1cm, bottom: 2cm),
    header: context {
      if counter(page).get().first() > 1 [
        #set text(font: sans, size: 7.4pt, fill: cores.cinza)
        #grid(columns: (1fr, auto),
          [Tema #tema · #titulo],
          [Liga de Cardiologia · resumão])
        #v(-4pt)
        #line(length: 100%, stroke: 0.4pt + cores.linha)
      ]
    },
    footer: context [
      #set text(font: sans, size: 7.6pt, fill: cores.cinza)
      #h(1fr) #counter(page).display() / #counter(page).final().first() #h(1fr)
    ],
  )
  set text(font: serif, size: 10pt, lang: "pt", region: "br", hyphenate: true)
  set par(justify: true, leading: 0.6em, spacing: 0.85em)
  set list(indent: 0.4em, body-indent: 0.45em, spacing: 0.55em, marker: text(fill: cores.prim, sym.bullet))
  set enum(indent: 0.4em, body-indent: 0.45em, spacing: 0.55em)
  set strong(delta: 250)
  show strong: set text(weight: 600)

  set heading(numbering: "1.")
  show heading: set text(font: sans)
  show heading.where(level: 1): it => block(above: 1.5em, below: 0.75em, sticky: true)[
    #set text(size: 12.5pt, weight: "bold", fill: cores.prim)
    #if it.numbering != none [#counter(heading).display(it.numbering) #h(0.35em)]
    #it.body
    #v(-6pt)
    #line(length: 100%, stroke: 0.6pt + cores.prim.lighten(55%))
  ]
  show heading.where(level: 2): it => block(above: 1.15em, below: 0.6em, sticky: true)[
    #set text(size: 10.3pt, weight: "semibold", fill: cores.azul)
    #it.body
  ]
  show figure.caption: it => {
    set text(size: 8.2pt)
    set par(justify: false, leading: 0.45em)
    block(width: 100%, inset: (x: 2pt))[
      #text(font: sans, weight: "semibold", fill: cores.prim)[#it.supplement #context it.counter.display(it.numbering)] #h(0.2em) #it.body
    ]
  }
  set figure(supplement: "Fig.")
  show figure: set block(above: 1.1em, below: 1.1em, breakable: false)

  // capa (cabeçalho da primeira página)
  block(width: 100%, fill: cores.prim, inset: (x: 16pt, top: 14pt, bottom: 14pt), radius: 3pt, below: 1.2em)[
    #set text(font: sans, fill: white)
    #text(size: 8pt, weight: "semibold", tracking: 0.1em)[#upper(area) · TEMA #tema]
    #v(2pt)
    #text(size: 19pt, weight: "bold")[#titulo]
    #v(1pt)
    #text(size: 8.4pt)[Resumão enxuto para a prova da Liga Acadêmica de Cardiologia]
  ]
  if fontes.len() > 0 {
    block(width: 100%, below: 1.2em)[
      #set text(font: sans, size: 7.8pt, fill: cores.cinza)
      #set par(justify: false)
      *Fontes:* #fontes.join(" · ")
    ]
  }
  corpo
}
