"""Diagramas vetoriais do tema e (microcirculação e sistema linfático; Guyton cap. 16), com oclusões para o Anki."""
import math

from svgkit import (AMBER, AMBER_L, BLUE, BLUE_L, GREEN, GREEN_L, GREY_L, INK, LINE, MUTE, PURPLE, PURPLE_L, RED,
                    RED_L, SVG, TEAL, TEAL_L, export)

PILL = ("#ffffffe8", "none")
ART, VEN = "#c43a4b", "#3b5bb5"


def _mix(t):
    """Cor do sangue do lado arterial (t = 0) ao venoso (t = 1)."""
    a, b = (0xc4, 0x3a, 0x4b), (0x3b, 0x5b, 0xb5)
    return "#" + "".join(f"{round(x + (y - x) * t):02x}" for x, y in zip(a, b))


# ---------------------------------------------------------------- leito microcirculatório
def microcirculacao(hide=None):
    s = SVG(860, 440, hide)
    s.rect(20, 20, 820, 380, fill="#fbf8f4", r=16)
    # arteríola (entra à esquerda, alto) e vênula (sai à direita, baixo)
    s.path("M20,110 C120,110 160,110 240,118", stroke=ART, sw=26)
    for x in range(40, 236, 16):   # anéis de músculo liso contínuos
        s.path(f"M{x},96 L{x + 4},124", stroke="#7a1d2a", sw=3, opacity=0.55)
    s.path("M620,330 C700,336 760,336 840,336", stroke=VEN, sw=34)
    # metarteríola (canal preferencial)
    s.path("M240,118 C340,130 420,200 500,262 C540,294 580,320 620,330", stroke=_mix(0.4), sw=14)
    for t in (0.18, 0.42, 0.66):   # músculo intermitente
        x = 240 + 380 * t
        y = 118 + 212 * t ** 1.3
        s.circle(x, y, 10, fill="none", stroke="#7a1d2a", sw=3)
    # capilares verdadeiros com esfíncteres
    caps = [("M270,124 C300,200 360,220 420,210 C480,200 520,230 560,300", 272, 130),
            ("M330,146 C340,250 420,300 470,310 C520,320 560,330 600,332", 332, 152),
            ("M300,128 C360,60 480,70 560,120 C620,160 640,240 630,320", 302, 130)]
    for d, ex, ey in caps:
        s.path(d, stroke=_mix(0.6), sw=7)
        s.circle(ex, ey + 4, 8, fill="none", stroke=AMBER, sw=3.2)
    # células teciduais
    for x, y in ((420, 150), (520, 180), (380, 260), (470, 250), (560, 240), (430, 100)):
        s.ellipse(x, y, 20, 13, fill="#efe2d4", stroke="#d8c7b4", sw=1)
    # rótulos
    s.label(40, 50, "Arteríola\nmúsculo liso contínuo · 10–15 µm", key="arteriola", size=12, weight=700, fill=ART,
            valign="top")
    s.label(390, 368, "Metarteríola\nmúsculo em pontos intermitentes", key="metart", size=12, weight=700, fill=_mix(0.4),
            anchor="end", valign="top")
    s.arrow([(330, 368), (420, 222)], color=_mix(0.4), sw=1.2)
    s.label(96, 190, "Esfíncter\npré-capilar\n(abre/fecha a entrada)", key="esfincter", size=12, weight=700, fill=AMBER,
            valign="top")
    s.arrow([(190, 206), (262, 138)], color=AMBER, sw=1.4)
    s.label(660, 60, "Capilar verdadeiro\n1 camada de endotélio\nparede 0,5 µm · luz 4–9 µm", key="capilar", size=12,
            weight=700, fill=_mix(0.6), valign="top")
    s.arrow([(660, 96), (598, 132)], color=_mix(0.6), sw=1.2)
    s.label(840, 382, "Vênula\nmaior que a arteríola, músculo fraco", key="venula", size=12, weight=700, fill=VEN,
            anchor="end", valign="top")
    s.text(840, 430, "Vasomotricidade: fluxo intermitente; o principal regulador é o O₂ tecidual.", size=11, fill=MUTE,
           anchor="end")
    return s.svg()


# ---------------------------------------------------------------- parede capilar e vias de passagem
def parede(hide=None):
    s = SVG(860, 430, hide)
    # luz (plasma) em cima, interstício embaixo
    s.rect(20, 20, 820, 120, fill=RED_L, r=12)
    s.text(40, 48, "LUZ DO CAPILAR (plasma)", size=12, weight=800, fill=RED)
    s.rect(20, 262, 820, 130, fill="#f4f7fb", r=12)
    s.text(40, 380, "INTERSTÍCIO", size=12, weight=800, fill=BLUE)
    # duas células endoteliais e a fenda
    s.rect(20, 150, 400, 90, fill="#f6d9c8", stroke="#d59c7e", r=14, sw=1.5)
    s.rect(440, 150, 400, 90, fill="#f6d9c8", stroke="#d59c7e", r=14, sw=1.5)
    s.ellipse(200, 195, 48, 22, fill="#e3b49a")
    s.ellipse(680, 195, 48, 22, fill="#e3b49a")
    s.rect(20, 244, 820, 8, fill="#b9c2cc", r=4)   # membrana basal
    s.text(836, 262, "membrana basal", size=10, fill=MUTE, anchor="end")
    for y in (170, 196, 222):   # proteínas juncionais
        s.line(420, y, 440, y, stroke="#a15d3e", sw=3)
    # cavéolas / canal vesicular
    for x, y in ((520, 162), (560, 190), (600, 222)):
        s.circle(x, y, 9, fill="#fff", stroke="#a15d3e", sw=1.6)
    s.label(560, 110, "cavéolas / canal vesicular\n(transcitose de macromoléculas)", key="cav", size=11, weight=600,
            fill="#8a4b30", anchor="middle", valign="top", pill=PILL, pad=(4, 2))
    # vias
    s.arrow([(330, 80), (330, 300)], color=TEAL, sw=3)
    s.label(260, 300, "O₂, CO₂ (lipossolúveis):\natravessam a membrana\ninteira, muito rápido", key="lipo", size=11.5,
            weight=700, fill=TEAL, anchor="middle", valign="top")
    s.arrow([(430, 80), (430, 300)], color=BLUE, sw=3)
    s.label(430, 300, "água, Na⁺, Cl⁻, glicose:\npela fenda intercelular", key="hidro", size=11.5, weight=700, fill=BLUE,
            anchor="middle", valign="top")
    s.circle(740, 90, 16, fill=PURPLE, opacity=0.9)
    s.text(740, 95, "Alb", size=10, weight=800, fill="#fff", anchor="middle")
    s.arrow([(740, 110), (740, 140)], color=PURPLE, sw=2.5)
    s.line(724, 146, 756, 130, stroke=RED, sw=3)
    s.line(724, 130, 756, 146, stroke=RED, sw=3)
    s.label(740, 300, "proteínas plasmáticas:\nquase não passam", key="prot", size=11.5, weight=700, fill=PURPLE,
            anchor="middle", valign="top")
    s.label(452, 36, "fenda intercelular 6–7 nm\n≈ 1/1.000 da área da parede", key="fenda", size=11.5, weight=700,
            fill=INK, valign="top", pill=PILL, pad=(4, 2))
    s.arrow([(452, 70), (434, 150)], color=INK, sw=1.2)
    return s.svg()


# ---------------------------------------------------------------- tipos de capilar
def tipos(hide=None):
    s = SVG(860, 300, hide)
    cards = [("cer", "Cérebro", "junções oclusivas:\nsó água, O₂, CO₂", PURPLE, PURPLE_L, 0),
             ("mus", "Músculo, pele", "fendas de 6–7 nm\n(contínuo)", RED, RED_L, 1),
             ("glom", "Glomérulo renal", "fenestrações: filtra\nmuito, mas não proteína", AMBER, AMBER_L, 2),
             ("fig", "Fígado (sinusoide)", "fendas quase abertas:\npassam até proteínas", GREEN, GREEN_L, 3)]
    for k, name, sub, c, cl, i in cards:
        x = 20 + i * 212
        s.rect(x, 20, 196, 260, fill=cl, r=14)
        s.text(x + 98, 48, name, size=13, weight=800, fill=c, anchor="middle")
        y0 = 80
        # parede com o tipo de poro
        if k == "cer":
            s.rect(x + 18, y0, 160, 60, fill="#f6d9c8", stroke="#d59c7e", r=8)
            for yy in range(y0 + 6, y0 + 60, 8):
                s.line(x + 94, yy, x + 102, yy, stroke=c, sw=3)
        elif k == "mus":
            s.rect(x + 18, y0, 74, 60, fill="#f6d9c8", stroke="#d59c7e", r=8)
            s.rect(x + 104, y0, 74, 60, fill="#f6d9c8", stroke="#d59c7e", r=8)
        elif k == "glom":
            s.rect(x + 18, y0, 160, 60, fill="#f6d9c8", stroke="#d59c7e", r=8)
            for xx in range(x + 36, x + 170, 26):
                s.rect(xx, y0 + 2, 10, 56, fill=cl, r=5)
        else:
            for xx in (x + 18, x + 84, x + 150):
                s.rect(xx, y0, 30, 60, fill="#f6d9c8", stroke="#d59c7e", r=8)
        s.arrow([(x + 98, y0 - 20), (x + 98, y0 + 86)], color=c, sw=2, dash=None if k != "cer" else "3 3")
        s.label(x + 98, 190, sub, key=k, size=11.5, weight=600, anchor="middle", valign="top")
    s.text(430, 296, "permeabilidade crescente →", size=11, fill=MUTE, anchor="middle")
    return s.svg()


# ---------------------------------------------------------------- forças de Starling ao longo do capilar
def starling(hide=None):
    s = SVG(980, 470, hide)
    # capilar
    for i in range(60):
        x = 120 + i * 11
        s.rect(x, 190, 12, 70, fill=_mix(i / 59), r=0)
    s.rect(120, 190, 660, 70, fill="none", stroke="#8b95a1", r=4, sw=2)
    s.text(110, 221, "extremidade\narterial", size=11, weight=700, fill=ART, anchor="end", valign="middle")
    s.text(790, 221, "extremidade\nvenosa", size=11, weight=700, fill=VEN, valign="middle")
    s.label(450, 232, "Pc 30 → 10 mmHg (média funcional 17)", key="pc", size=12, weight=800, fill="#fff",
            anchor="middle")

    def col(x, pc, key_pc, net, key_net, out):
        s.arrow([(x, 188), (x, 132)], color=RED, sw=3)
        s.label(x, 124, f"Pc {pc}", key=key_pc, size=12, weight=800, fill=RED, anchor="middle")
        s.arrow([(x + 60, 188), (x + 60, 132)], color=AMBER, sw=3)
        s.label(x + 60, 124, "Πi 8", key=None, size=12, weight=800, fill=AMBER, anchor="middle")
        s.arrow([(x - 60, 188), (x - 60, 132)], color=TEAL, sw=3)
        s.label(x - 60, 124, "−Pi 3", key=None, size=12, weight=800, fill=TEAL, anchor="middle")
        s.arrow([(x, 330), (x, 262)], color=PURPLE, sw=3)
        s.label(x, 350, "Πp 28", key=None, size=12, weight=800, fill=PURPLE, anchor="middle")
        c = RED if out else BLUE
        s.rect(x - 96, 20, 192, 62, fill=RED_L if out else BLUE_L, r=10)
        s.label(x, 42, net, key=key_net, size=13, weight=800, fill=c, anchor="middle", valign="top")
    col(230, 30, "pc_a", "para fora: 41 − 28\n= 13 mmHg (filtra)", "pef_a", True)
    col(670, 10, "pc_v", "para dentro: 28 − 21\n= 7 mmHg (reabsorve)", "pef_v", False)
    # setas de fluxo de líquido
    s.arrow([(300, 264), (450, 340), (600, 264)], color=BLUE, sw=2, curve=True, dash="5 4")
    s.label(450, 306, "9/10 reabsorvidos", key="nove", size=11.5, weight=700, fill=BLUE, anchor="middle", pill=PILL, pad=(4, 2))
    s.label(450, 400, "1/10 → linfáticos (2–3 ℓ/dia)", key="linfa", size=12, weight=800, fill=GREEN, anchor="middle",
            pill=("#fff", GREEN), pad=(8, 4))
    s.arrow([(450, 314), (450, 382)], color=GREEN, sw=2)
    # legenda das forças
    lx = 880
    items = [(RED, "Pc", "pressão capilar\n(para fora)"), (TEAL, "Pi", "intersticial −3\n(negativa: puxa\npara fora)"),
             (AMBER, "Πi", "oncótica\nintersticial (fora)"), (PURPLE, "Πp", "oncótica do\nplasma (dentro)")]
    y = 110
    for c, n, t in items:
        s.text(lx, y, n, size=13, weight=800, fill=c)
        s.text(lx, y + 16, t, size=9.5, fill=MUTE)
        y += 64 if t.count("\n") < 2 else 76
    s.rect(120, 420, 660, 40, fill=GREY_L, r=10)
    s.label(450, 446, "PEF = Pc − Pi − Πp + Πi · média: 28,3 − 28 = **0,3 mmHg** → filtração efetiva ≈ 2 mℓ/min",
            key="media", size=12, anchor="middle")
    return s.svg()


# ---------------------------------------------------------------- capilar linfático terminal
def linfatico(hide=None):
    s = SVG(860, 380, hide)
    s.rect(20, 20, 820, 340, fill="#f4f7fb", r=16)
    # capilar linfático (tubo) com células sobrepostas
    s.rect(120, 140, 600, 100, fill="#e8f5ec", r=50)
    for i, x in enumerate(range(130, 700, 90)):
        s.path(f"M{x},140 L{x + 100},140", stroke=GREEN, sw=6)
        s.path(f"M{x + 100},140 L{x + 92},158", stroke=GREEN, sw=5)   # borda livre (válvula) para dentro
        s.path(f"M{x},240 L{x + 100},240", stroke=GREEN, sw=6)
        s.path(f"M{x + 100},240 L{x + 92},222", stroke=GREEN, sw=5)
    # filamentos de ancoragem
    for x in range(160, 700, 90):
        s.line(x, 140, x - 20, 70, stroke=MUTE, sw=1.4, dash="2 3")
        s.line(x, 240, x - 20, 310, stroke=MUTE, sw=1.4, dash="2 3")
    # líquido e proteínas entrando
    for x in (205, 385, 565):
        s.arrow([(x + 40, 88), (x + 24, 150)], color=BLUE, sw=2)
        s.circle(x + 48, 80, 5, fill=PURPLE)
    s.arrow([(700, 190), (800, 190)], color=GREEN, sw=4)
    s.text(806, 186, "linfa", size=12, weight=800, fill=GREEN)
    s.label(40, 40, "filamentos de ancoragem: tecido incha → puxam a parede e abrem as junções", key="fil", size=12,
            weight=700, fill=INK)
    s.label(420, 272, "bordas sobrepostas = válvulas que só abrem para dentro", key="valv", size=12, weight=700,
            fill=GREEN, anchor="middle", valign="top", pill=PILL, pad=(4, 2))
    s.label(40, 344, "entra líquido **e proteína** (que não volta pelo capilar sanguíneo)", key="prot", size=12,
            fill=PURPLE)
    return s.svg()


# ---------------------------------------------------------------- fluxo linfático × pressão intersticial
def fluxo_linfa(hide=None):
    s = SVG(760, 380, hide)
    m = s.axes(80, 30, 480, 270, (-8, 4), (0, 22), xticks=(-8, -6, -4, -2, 0, 2, 4), yticks=(0, 5, 10, 15, 20),
               xlabel="pressão do líquido intersticial (mmHg)", ylabel="fluxo linfático (× normal)")

    def f(p):
        if p < -6:
            return 1
        if p < 1:
            return 1 + 19 * ((p + 6) / 7) ** 2.2
        return 20
    pts = [m(p / 10, f(p / 10)) for p in range(-80, 41)]
    s.poly(pts, stroke=GREEN, sw=3.4)
    s.line(*m(0, 0), *m(0, 22), stroke=MUTE, sw=1, dash="4 4")
    s.label(*m(-7.8, 3.2), "normal (Pi negativa):\nfluxo pequeno", key="normal", size=11, weight=700, fill=GREEN)
    s.label(m(-3.2, 0)[0], m(0, 14)[1], "Pi −6 → 0:\nfluxo ↑ mais de 20×", key="x20", size=11.5, weight=800, fill=INK,
            anchor="end", pill=PILL, pad=(4, 2))
    s.label(m(1.3, 0)[0], m(0, 17.5)[1], "platô: Pi > +1–2\ncomprime os linfáticos", key="plato", size=11, weight=700,
            fill=RED, pill=PILL, pad=(4, 2))
    px = 580
    s.rect(px, 40, 170, 240, fill=GREEN_L, r=12)
    s.text(px + 12, 64, "Fluxo linfático =", size=12, weight=800, fill=GREEN)
    s.label(px + 12, 76, "**Pi × atividade da\nbomba linfática**", key="formula", size=11.5, valign="top")
    s.text(px + 12, 138, "Bomba: músculo liso\nentre válvulas (ducto\ntorácico 50–100 mmHg)\n+ músculos, movimento,\n"
           "pulso arterial.\nExercício: 10–30×.", size=10.5, fill=INK)
    return s.svg()


FIGS = {"e_microcirculacao": microcirculacao, "e_parede": parede, "e_tipos": tipos, "e_starling": starling,
        "e_linfatico": linfatico, "e_fluxo_linfa": fluxo_linfa}

OCLUSOES = [
    ("e_microcirculacao", "metart", "Vaso com músculo liso só em pontos intermitentes, entre arteríola e vênula?", "<b>Metarteríola</b>."),
    ("e_microcirculacao", "esfincter", "Estrutura muscular na origem de cada capilar verdadeiro?", "<b>Esfíncter pré-capilar</b>: abre e fecha a entrada do capilar."),
    ("e_microcirculacao", "capilar", "Espessura da parede e diâmetro do capilar?", "Parede ≈ <b>0,5 µm</b> (1 camada de endotélio); luz <b>4 a 9 µm</b>."),
    ("e_microcirculacao", "arteriola", "Vaso muito muscular que controla o fluxo de cada tecido (10 a 15 µm)?", "<b>Arteríola</b>."),
    ("e_parede", "fenda", "Largura da fenda intercelular e fração da área?", "<b>6 a 7 nm</b> (pouco menor que a albumina); ≈ <b>1/1.000</b> da área."),
    ("e_parede", "lipo", "Como passam O₂ e CO₂?", "São <b>lipossolúveis</b>: atravessam a membrana do endotélio em toda a área, muito rápido."),
    ("e_parede", "hidro", "Por onde passam água, Na⁺, Cl⁻ e glicose?", "Pelas <b>fendas intercelulares</b> (poros)."),
    ("e_parede", "cav", "Estrutura do endotélio ligada à transcitose de macromoléculas?", "<b>Cavéolas</b> (vesículas plasmalêmicas, com caveolina)."),
    ("e_tipos", "cer", "Como são as junções dos capilares cerebrais?", "<b>Oclusivas</b>: só moléculas muito pequenas (água, O₂, CO₂)."),
    ("e_tipos", "glom", "Estrutura típica do capilar glomerular?", "<b>Fenestrações</b>: filtra muito líquido e íons, mas não proteínas."),
    ("e_tipos", "fig", "Como é o capilar do fígado?", "<b>Sinusoide</b> com fendas quase abertas: passam até proteínas plasmáticas."),
    ("e_starling", "pc_a", "Pressão capilar na extremidade arterial (Guyton)?", "≈ <b>30 mmHg</b>."),
    ("e_starling", "pc_v", "Pressão capilar na extremidade venosa?", "≈ <b>10 mmHg</b>."),
    ("e_starling", "pef_a", "Pressão efetiva na extremidade arterial?", "<b>13 mmHg para fora</b> (41 − 28): filtração."),
    ("e_starling", "pef_v", "Pressão efetiva na extremidade venosa?", "<b>7 mmHg para dentro</b> (28 − 21): reabsorção."),
    ("e_starling", "linfa", "Que fração do filtrado volta pela linfa e quanto por dia?", "≈ <b>1/10</b>; <b>2 a 3 ℓ/dia</b>."),
    ("e_starling", "media", "Pressão efetiva média em todo o capilar e filtração efetiva?", "<b>0,3 mmHg</b> (28,3 − 28) → ≈ <b>2 mℓ/min</b> no corpo (sem os rins)."),
    ("e_linfatico", "fil", "Qual a função dos filamentos de ancoragem?", "Quando o tecido incha, <b>puxam a parede</b> e abrem as junções: o líquido entra."),
    ("e_linfatico", "valv", "Por que a linfa não reflui para o interstício?", "As <b>bordas sobrepostas</b> das células endoteliais funcionam como válvulas que só abrem para dentro."),
    ("e_fluxo_linfa", "x20", "O que acontece com o fluxo linfático quando Pi sobe de −6 para 0 mmHg?", "Aumenta <b>mais de 20×</b>."),
    ("e_fluxo_linfa", "plato", "Por que o fluxo linfático para de subir quando Pi passa de +1 a +2 mmHg?", "A pressão tecidual <b>comprime os linfáticos maiores</b>: entrada e compressão se equilibram (platô)."),
    ("e_fluxo_linfa", "formula", "Os dois determinantes do fluxo linfático?", "<b>Pressão do líquido intersticial × atividade da bomba linfática</b>."),
]

if __name__ == "__main__":
    print("ok", export("dia_e", FIGS, OCLUSOES))
