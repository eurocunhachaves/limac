"""Diagramas vetoriais do tema b (excitação rítmica do coração), com oclusões para o Anki."""
from svgkit import (AMBER, AMBER_L, BLUE, BLUE_L, GREEN, GREEN_L, GREY_L, INK, LINE, MUTE, PURPLE, PURPLE_L, RED,
                    RED_L, SVG, TEAL, TEAL_L, export)

PILL = ("#ffffffe0", "none")


def sa_ciclo(t0, periodo, v_min=-60, limiar=-40):
    """Pontos de um ciclo nodal: vale em t0, rampa até o limiar, subida por Ca²⁺, repolarização."""
    r = periodo - 0.30
    return [(t0, v_min), (t0 + r, limiar), (t0 + r + 0.07, 2), (t0 + r + 0.13, -4), (t0 + periodo, v_min)]


def _nodal(periodo, v_min, t_end, limiar=-40):
    """Curva nodal amostrada (rampa levemente côncava, subida arredondada)."""
    pts, t = [], 0.0
    while t < t_end:
        r = periodo - 0.30
        for i in range(24):  # rampa (fase 4)
            u = i / 24
            pts.append((t + r * u, v_min + (limiar - v_min) * (u ** 1.25)))
        for i in range(10):  # subida lenta (Ca²⁺ L)
            u = i / 10
            pts.append((t + r + 0.07 * u, limiar + 42 * (1 - (1 - u) ** 2)))
        for i in range(16):  # repolarização
            u = i / 16
            pts.append((t + r + 0.07 + 0.23 * u, 2 - (2 - v_min) * (3 * u * u - 2 * u ** 3)))
        t += periodo
    pts.append((t, v_min))
    return [(x, y) for x, y in pts if x <= t_end]


# ---------------------------------------------------------------- potencial do nó sinusal
def potencial_sa(hide=None):
    s = SVG(800, 400, hide)
    m = s.axes(80, 40, 560, 280, (0, 2.5), (-100, 30), xticks=(0, 0.5, 1, 1.5, 2, 2.5), yticks=(-80, -60, -40, -20, 0, 20),
               xlabel="tempo (s)", ylabel="potencial (mV)", tick_fmt=lambda v: f"{v:g}".replace(".", ","))
    # faixa da fase 4 (rampa) no 2º ciclo
    x0, x1 = m(0.8, 0)[0], m(1.3, 0)[0]
    s.rect(x0, 40, x1 - x0, 280, fill=AMBER_L, r=0, opacity=0.8)
    s.line(m(0, -40)[0], m(0, -40)[1], m(2.5, -40)[0], m(2.5, -40)[1], stroke=MUTE, sw=1.2, dash="5 4")
    s.label(m(1.9, -40)[0], m(0, -40)[1] - 6, "limiar ≈ −40 mV", key="limiar", size=10.5, weight=600, fill=MUTE,
            anchor="end", pill=PILL, pad=(3, 2))
    # fibra ventricular para comparação
    tv = [(1.9, -88), (1.95, -88), (1.953, 20), (1.97, 5), (2.0, 2), (2.13, -4), (2.2, -40), (2.25, -82), (2.3, -88), (2.5, -88)]
    s.poly([m(*p) for p in tv], stroke=TEAL, sw=2, opacity=0.9)
    s.poly([m(*p) for p in _nodal(0.8, -60, 1.62)], stroke=RED, sw=3)
    # rótulos com setas
    s.label(m(0.06, 0)[0], m(0, -78)[1], "repouso\n−55 a −60 mV", key="repouso", size=10.5,
            weight=600, fill=RED, valign="top", pill=PILL, pad=(4, 3))
    s.arrow([m(0.2, -73), m(0.07, -62)], color=RED, sw=1.4)
    s.label(m(1.12, 0)[0], m(0, -86)[1], "fase 4 · despolarização diastólica lenta\ncorrente funny (Na⁺) + Ca²⁺",
            key="funny", size=10.5, weight=600, fill=AMBER, anchor="middle", valign="top", pill=PILL, pad=(4, 3))
    s.arrow([m(1.05, -76), m(1.05, -52)], color=AMBER, sw=1.6)
    s.label(m(0.18, 0)[0], m(0, 25)[1], "subida lenta:\ncanais de Ca²⁺ tipo L", key="subida", size=10.5, weight=600,
            fill=INK, valign="top", pill=PILL, pad=(4, 3))
    s.arrow([m(0.46, 12), m(0.53, -6)], color=INK, sw=1.4)
    s.label(m(0.9, 0)[0], m(0, 25)[1], "repolarização:\nCa²⁺ inativa, abre K⁺", key="repol", size=10.5, weight=600,
            fill=INK, valign="top", pill=PILL, pad=(4, 3))
    s.arrow([m(0.88, 10), m(0.72, -20)], color=INK, sw=1.4)
    # legenda
    lx = 660
    s.rect(lx - 10, 60, 150, 96, fill="#fff", stroke=LINE, r=10, shadow=True)
    s.line(lx + 2, 86, lx + 26, 86, stroke=RED, sw=3)
    s.text(lx + 34, 90, "nó sinusal", size=11, weight=600)
    s.line(lx + 2, 116, lx + 26, 116, stroke=TEAL, sw=2)
    s.text(lx + 34, 112, "músculo\nventricular", size=11, weight=600, valign="middle")
    s.text(lx + 2, 146, "sem platô · sem fase 0 rápida", size=9, fill=MUTE)
    s.text(lx - 10, 190, "Por que não há\ncanais rápidos de Na⁺?", size=10.5, weight=700, fill=INK)
    s.text(lx - 10, 226, "a −55 mV eles ficam\ninativados (comportas\nde inativação fechadas).", size=10, fill=MUTE)
    return s.svg()


# ---------------------------------------------------------------- sistema de condução
def conducao(hide=None):
    s = SVG(860, 520, hide)
    # coração estilizado (vista anterior, 4 câmaras)
    s.path("M150,112 C150,62 228,50 262,88 C292,54 378,58 390,110 C446,150 454,262 404,342 C364,404 304,452 262,474 "
           "C218,444 150,392 120,330 C88,258 98,158 150,112 Z", stroke="#e0b3b9", sw=2.2, fill="#fdf1f2")
    s.path("M112,204 C180,214 340,214 424,202", stroke="#cfd3d8", sw=5, opacity=0.9)          # anel fibroso
    s.path("M262,90 L262,206", stroke="#e0b3b9", sw=2, dash="4 3")                         # septo interatrial
    s.path("M262,212 C268,300 270,390 262,468", stroke="#e0b3b9", sw=10, opacity=0.5)      # septo interventricular
    for x, y, t in ((160, 188, "AD"), (340, 160, "AE"), (180, 318, "VD"), (345, 318, "VE")):
        s.text(x, y, t, size=15, weight=800, fill="#e3b7bd", anchor="middle")
    # vias internodais e Bachmann
    for c in ("M168,112 C150,150 200,188 240,198", "M170,114 C205,140 222,170 242,196", "M172,110 C240,110 250,160 246,194"):
        s.path(c, stroke=AMBER, sw=2, dash="2 3")
    s.path("M174,104 C230,84 300,90 350,118", stroke=AMBER, sw=2.4)
    s.text(300, 82, "feixe de Bachmann", size=9.5, fill=AMBER, anchor="middle", italic=True)
    # nós
    s.ellipse(164, 108, 16, 10, fill=AMBER, stroke="#fff", sw=2)
    s.ellipse(246, 198, 13, 9, fill=AMBER, stroke="#fff", sw=2)
    # feixe AV, ramos e Purkinje
    s.path("M250,204 L262,240", stroke=PURPLE, sw=5)
    s.path("M262,240 C252,300 246,360 246,420", stroke=PURPLE, sw=3.4)   # ramo direito
    s.path("M264,240 C278,300 282,360 280,424", stroke=PURPLE, sw=3.4)   # ramo esquerdo
    for d in ("M246,420 C220,452 170,420 140,350", "M246,420 C210,420 170,380 150,300",
              "M280,424 C320,450 380,400 400,330", "M280,424 C330,420 370,360 392,280", "M280,330 C320,330 350,300 370,250",
              "M248,340 C220,330 190,300 176,250"):
        s.path(d, stroke=GREEN, sw=1.6)
    # tempos de chegada
    t = [(118, 88, "0 s", "t_sa", "end"), (206, 234, "0,03 s", "t_av", "end"), (300, 238, "0,12 s", "t_fp", "start"),
         (292, 280, "0,16 s", "t_ramos", "start"), (250, 496, "≈ 0,19 s", "t_purk", "middle"),
         (424, 380, "≈ 0,22 s\n(epicárdio)", "t_epi", "start")]
    for x, y, txt, k, anc in t:
        s.label(x, y, txt, key=k, size=11, weight=700, fill=RED, anchor=anc, pill=("#fff", RED), pad=(6, 3))
    for x, y, txt, anc in ((140, 128, "nó sinusal", "end"), (222, 176, "nó AV", "end"), (270, 216, "feixe AV", "start")):
        s.text(x, y, txt, size=10, weight=700, fill=INK, anchor=anc)
    s.text(240, 300, "ramo D", size=9.5, fill=PURPLE, anchor="end", weight=600)
    s.text(286, 300, "ramo E", size=9.5, fill=PURPLE, weight=600)
    s.text(360, 438, "Purkinje", size=9.5, fill=GREEN, weight=600)
    # painel: velocidades e atrasos
    px = 500
    s.rect(px, 30, 340, 300, fill="#fff", stroke=LINE, r=12, shadow=True)
    s.text(px + 18, 58, "Velocidades e atrasos", size=13, weight=700)
    rows = [(AMBER, "vias internodais", "≈ 1 m/s (músculo atrial 0,3)", "v_intern"),
            (AMBER, "nó AV (atraso nodal)", "0,09 s", "d_av"),
            (PURPLE, "feixe AV penetrante", "+0,04 s", "d_fp"),
            (GREEN, "fibras de Purkinje", "1,5 a 4 m/s (+0,03 s)", "v_purk"),
            (RED, "músculo ventricular", "0,3 a 0,5 m/s · endo → epi +0,03 s", "v_musc")]
    for i, (c, name, val, k) in enumerate(rows):
        y = 84 + i * 48
        s.circle(px + 26, y + 10, 7, fill=c)
        s.text(px + 42, y + 6, name, size=11, weight=600)
        s.label(px + 42, y + 24, val, key=k, size=10.5, fill=MUTE)
    # caixa do atraso total
    s.rect(px, 350, 340, 124, fill=RED_L, stroke=RED, r=12, sw=1.4)
    s.text(px + 18, 378, "Atraso total AV", size=13, weight=700, fill=RED)
    s.label(px + 18, 392, "**0,16 s** = 0,03 + 0,09 + 0,04\nCausa: **poucas junções comunicantes**\nno nó AV "
            "→ dá tempo de o átrio esvaziar\nantes da contração ventricular.", key="atraso_total", size=10.5, valign="top")
    return s.svg()


# ---------------------------------------------------------------- hierarquia de marcapassos
def marcapassos(hide=None):
    s = SVG(760, 300, hide)
    m = s.axes(150, 50, 460, 180, (0, 100), (0, 3), xticks=(0, 20, 40, 60, 80, 100), yticks=(),
               xlabel="frequência intrínseca (disparos/min)", grid=False)
    for x in (20, 40, 60, 80, 100):
        s.line(m(x, 0)[0], 50, m(x, 0)[0], 230, stroke="#eceef1", sw=1)
    items = [("Nó sinusal", 70, 80, RED, RED_L, "sa"), ("Nó AV", 40, 60, AMBER, AMBER_L, "av"),
             ("Purkinje", 15, 40, BLUE, BLUE_L, "pk")]
    for i, (name, lo, hi, c, cl, k) in enumerate(items):
        y = 72 + i * 56
        s.text(140, y + 17, name, size=12, weight=700, anchor="end")
        s.rect(m(lo, 0)[0], y, m(hi, 0)[0] - m(lo, 0)[0], 30, fill=c, r=8, shadow=True)
        s.label(m(hi, 0)[0] + 8, y + 20, f"{lo} a {hi} bpm", key=k, size=11.5, weight=700, fill=c)
    s.rect(630, 60, 118, 150, fill=GREY_L, r=10)
    s.text(642, 84, "O mais rápido\ncomanda", size=11.5, weight=700, fill=RED)
    s.text(642, 124, "e suprime os\noutros por\nsobrecarga.\nSe o sinusal\nfalha, o AV\nassume.", size=10, fill=INK)
    s.text(380, 30, "Hierarquia dos marcapassos", size=13, weight=700, anchor="middle")
    return s.svg()


# ---------------------------------------------------------------- efeito autonômico
def autonomo(hide=None):
    s = SVG(840, 400, hide)
    x0, w, T = 90, 470, 2.4
    fx = lambda t: x0 + t / T * w
    rows = [(AMBER, AMBER_L, "Simpático (noradrenalina, β1)", "↑ Na⁺ e Ca²⁺ → rampa mais\níngreme → **FC ↑** (e força ↑)",
             "simp", 0.5, -57),
            (INK, GREY_L, "Normal", "≈ 70 a 80 bpm", "norm", 0.8, -60),
            (BLUE, BLUE_L, "Vago (acetilcolina)", "↑ K⁺ → **hiperpolariza**\n(−65 a −75 mV) → FC ↓", "vago", 1.25, -72)]
    for i, (c, cl, title, body, k, per, vmin) in enumerate(rows):
        y0, h = 24 + i * 112, 96
        fy = lambda v: y0 + h - (v + 80) / 105 * h
        s.rect(x0 - 8, y0 - 6, w + 16, h + 12, fill="#fafbfc", r=8)
        s.line(x0, fy(-40), x0 + w, fy(-40), stroke=MUTE, sw=1, dash="4 4")
        s.line(x0, fy(-60), x0 + w, fy(-60), stroke="#dfe2e6", sw=1)
        s.text(x0 - 12, fy(-40), "−40", size=9.5, fill=MUTE, anchor="end", valign="middle")
        s.text(x0 - 12, fy(-60), "−60", size=9.5, fill=MUTE, anchor="end", valign="middle")
        s.poly([(fx(t), fy(v)) for t, v in _nodal(per, vmin, T)], stroke=c, sw=2.6)
        n = int(60 / per)
        s.text(x0 + w + 4, y0 + 10, f"≈ {n} bpm", size=10.5, weight=700, fill=c, anchor="end", )
        px = 600
        s.rect(px, y0 - 6, 226, h + 12, fill=cl, r=10)
        s.rect(px, y0 - 6, 5, h + 12, fill=c, r=2)
        s.text(px + 16, y0 + 18, title, size=11.5, weight=700, fill=c)
        s.label(px + 16, y0 + 30, body, key=k, size=10.5, valign="top")
    for t in (0, 0.6, 1.2, 1.8, 2.4):
        s.text(fx(t), 372, f"{t:g}".replace(".", ","), size=10.5, fill=MUTE, anchor="middle")
    s.text(x0 + w / 2, 392, "tempo (s)", size=11, fill=MUTE, anchor="middle")
    s.text(600, 380, "Vago forte pode parar o sinusal por 5 a 20 s\n(até surgir o escape ventricular).", size=9.5, fill=MUTE)
    return s.svg()


FIGS = {"b_potencial_sa": potencial_sa, "b_conducao": conducao, "b_marcapassos": marcapassos, "b_autonomo": autonomo}

OCLUSOES = [
    ("b_potencial_sa", "repouso", "Potencial de \"repouso\" do nó sinusal e por que é menos negativo?",
     "<b>−55 a −60 mV</b>: a membrana é naturalmente permeável a Na⁺ e Ca²⁺."),
    ("b_potencial_sa", "funny", "O que causa a subida lenta entre os batimentos?",
     "<b>Corrente funny</b> (vazamento de Na⁺) + Ca²⁺: despolarização diastólica lenta."),
    ("b_potencial_sa", "limiar", "Qual o limiar de disparo do nó sinusal?", "≈ <b>−40 mV</b>, quando abrem os canais de Ca²⁺ tipo L."),
    ("b_potencial_sa", "subida", "Qual canal faz a fase de subida no nó sinusal?",
     "<b>Canais de Ca²⁺ tipo L</b> (os rápidos de Na⁺ estão inativados a −55 mV)."),
    ("b_potencial_sa", "repol", "O que encerra o potencial nodal?",
     "Canais de Ca²⁺ inativam (100 a 150 ms) e <b>abrem canais de K⁺</b>."),
    ("b_conducao", "t_av", "Quando o impulso chega ao nó AV?", "≈ <b>0,03 s</b> após o nó sinusal."),
    ("b_conducao", "t_fp", "Quando o impulso sai do nó AV e entra no feixe AV penetrante?", "≈ <b>0,12 s</b> (0,03 + 0,09)."),
    ("b_conducao", "d_av", "Quanto é o atraso dentro do nó AV?", "<b>0,09 s</b>."),
    ("b_conducao", "d_fp", "Atraso adicional no feixe AV penetrante?", "<b>0,04 s</b>."),
    ("b_conducao", "t_ramos", "Quando o impulso chega aos ramos no septo?", "≈ <b>0,16 s</b> (atraso total)."),
    ("b_conducao", "t_epi", "Quando a última fibra ventricular (epicárdio) é despolarizada?", "≈ <b>0,22 s</b> após o nó sinusal."),
    ("b_conducao", "v_purk", "Velocidade de condução nas fibras de Purkinje?", "<b>1,5 a 4 m/s</b> (≈ 6× o músculo, 150× o nó AV)."),
    ("b_conducao", "v_musc", "Velocidade no músculo ventricular?", "<b>0,3 a 0,5 m/s</b>; endocárdio → epicárdio leva +0,03 s."),
    ("b_conducao", "v_intern", "Velocidade nas vias internodais e no feixe de Bachmann?", "≈ <b>1 m/s</b> (músculo atrial comum ≈ 0,3 m/s)."),
    ("b_conducao", "atraso_total", "Atraso total até o ventrículo e sua causa?",
     "<b>0,16 s</b>; causa: <b>poucas junções comunicantes</b> no nó AV."),
    ("b_marcapassos", "sa", "Frequência intrínseca do nó sinusal?", "<b>70 a 80</b> disparos/min."),
    ("b_marcapassos", "av", "Frequência intrínseca do nó AV?", "<b>40 a 60</b> disparos/min."),
    ("b_marcapassos", "pk", "Frequência intrínseca das fibras de Purkinje?", "<b>15 a 40</b> disparos/min."),
    ("b_autonomo", "vago", "Efeito da acetilcolina no nó sinusal?",
     "↑ permeabilidade ao <b>K⁺</b> → <b>hiperpolariza</b> (−65 a −75 mV) → demora mais para chegar ao limiar."),
    ("b_autonomo", "simp", "Efeito da noradrenalina (β1) no nó sinusal?",
     "↑ permeabilidade a <b>Na⁺ e Ca²⁺</b> → rampa mais íngreme → FC ↑."),
]

if __name__ == "__main__":
    print("ok", export("dia_b", FIGS, OCLUSOES))
