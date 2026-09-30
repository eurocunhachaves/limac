"""Diagramas vetoriais do tema a (músculo cardíaco e valvas), com oclusões para o Anki."""
import math

from svgkit import (AMBER, AMBER_L, BLUE, BLUE_L, GREEN, GREEN_L, GREY_L, INK, LINE, MUTE, PURPLE, PURPLE_L, RED,
                    RED_L, SVG, TEAL, TEAL_L, export, sample)


def _smoothstep(a, b, x):
    t = min(1, max(0, (x - a) / (b - a)))
    return t * t * (3 - 2 * t)


# ---------------------------------------------------------------- potencial de ação ventricular
def potencial_acao(hide=None):
    s = SVG(780, 430, hide)
    m = s.axes(80, 50, 440, 240, (-40, 400), (-100, 40), xticks=(0, 100, 200, 300, 400), yticks=(-80, -40, 0, 40),
               xlabel="tempo (ms)", ylabel="potencial (mV)")

    def v(t):
        if t < 0:
            return -85
        if t < 2:
            return -85 + 105 * t / 2
        if t < 12:
            return 20 - 17 * (t - 2) / 10
        if t < 190:
            return 3 - 8 * (t - 12) / 178
        if t < 290:
            return -5 - 80 * _smoothstep(190, 290, t)
        return -85
    s.poly([m(t, v(t)) for t in [x / 2 for x in range(-80, 801)]], stroke=RED, sw=3)
    # períodos refratários
    x0, x1, x2 = m(0, 0)[0], m(250, 0)[0], m(300, 0)[0]
    s.rect(x0, 28, x1 - x0, 12, fill=RED_L, stroke=RED, r=6, sw=1)
    s.rect(x1, 28, x2 - x1, 12, fill="#fff", stroke=RED, r=6, sw=1, dash="3 2")
    s.label((x0 + x1) / 2, 22, "período refratário absoluto · 0,25–0,30 s", key="pra", size=10.5, weight=600, fill=RED,
            anchor="middle")
    s.label(x2 + 4, 38, "relativo\n+0,05 s", key="prr", size=9.5, fill=RED)
    # fases (círculos numerados)
    for n, (t, vv, dx, dy) in enumerate([(1, -30, -20, 0), (7, 14, 14, -14), (100, 3, 0, -20), (245, -40, 20, 0),
                                         (340, -85, 0, -20)]):
        px, py = m(t, vv)
        s.circle(px + dx, py + dy, 11, fill="#fff", stroke=INK, sw=1.4)
        s.text(px + dx, py + dy, str(n), size=11.5, weight=700, anchor="middle", valign="middle")
    # correntes iônicas
    rows = [("I Na (rápida)", BLUE, [(0, 3, 1)]), ("I Ca-L", AMBER, [(3, 20, .9), (20, 200, .75), (200, 260, .3)]),
            ("I K", TEAL, [(5, 15, .5), (15, 190, .25), (190, 290, .9)])]
    for i, (name, col, segs) in enumerate(rows):
        y = 330 + i * 26
        s.text(72, y + 12, name, size=10.5, fill=col, weight=600, anchor="end")
        s.line(80, y + 8, 520, y + 8, stroke="#eceef1", sw=8)
        for a, b, op in segs:
            s.rect(m(a, 0)[0], y + 2, max(3, m(b, 0)[0] - m(a, 0)[0]), 12, fill=col, r=6, opacity=op)
    # painel das fases
    px = 548
    s.rect(px, 50, 222, 344, fill="#fbfbfc", stroke=LINE, r=12)
    s.text(px + 14, 74, "Fases e íons", size=13, weight=700)
    items = [("0", "f0", "Despolarização:\n**entra Na⁺** (canais rápidos)", BLUE),
             ("1", "f1", "Repolarização inicial:\nNa⁺ fecha, **sai K⁺**", TEAL),
             ("2", "f2", "Platô: **entra Ca²⁺** (tipo L)\ne ↓ saída de K⁺", AMBER),
             ("3", "f3", "Repolarização:\nCa²⁺ fecha, **sai K⁺**", TEAL),
             ("4", "f4", "Repouso: **−85 a −90 mV**\n(permeável ao K⁺)", MUTE)]
    for i, (n, k, txt, col) in enumerate(items):
        y = 100 + i * 58
        s.circle(px + 24, y + 6, 11, fill=col)
        s.text(px + 24, y + 6, n, size=11.5, weight=700, fill="#fff", anchor="middle", valign="middle")
        s.label(px + 44, y - 2, txt, key=k, size=11, valign="top")
    return s.svg()


# ---------------------------------------------------------------- acoplamento excitação-contração
def acoplamento(hide=None):
    s = SVG(860, 470, hide)
    # meio extracelular e sarcolema com túbulo T
    s.rect(0, 0, 860, 62, fill=AMBER_L, r=0)
    s.text(16, 24, "Líquido extracelular", size=11, fill=AMBER, weight=600)
    memb = "M0,62 L220,62 Q232,62 232,74 L232,262 Q232,286 256,286 L264,286 Q288,286 288,262 L288,74 Q288,62 300,62 L860,62"
    s.path(memb, stroke=INK, sw=5, opacity=0.18)
    s.path(memb, stroke=INK, sw=1.6)
    s.path("M233,60 L233,262 Q233,285 256,285 L264,285 Q287,285 287,262 L287,60 Z", stroke="none", fill=AMBER_L)
    s.text(260, 250, "túbulo T", size=10.5, fill=AMBER, weight=600, anchor="middle", rotate=-90)
    # retículo sarcoplasmático (dos dois lados do túbulo = díade)
    for x0, x1 in ((40, 222), (298, 560)):
        s.rect(x0, 170, x1 - x0, 62, fill=PURPLE_L, stroke=PURPLE, r=26, sw=1.5)
    s.text(430, 206, "Retículo sarcoplasmático", size=12, weight=700, fill=PURPLE, anchor="middle")
    s.text(430, 222, "estoque de Ca²⁺", size=10.5, fill=PURPLE, anchor="middle")
    # canal tipo L (DHPR) na parede do túbulo e RyR2 no RS
    s.rect(282, 184, 14, 34, fill=AMBER, r=4)
    s.rect(300, 186, 12, 30, fill=PURPLE, r=4)
    s.label(218, 118, "canal de Ca²⁺\ntipo L (DHPR)", key="ltcc", size=10.5, fill=AMBER, weight=600, anchor="end")
    s.arrow([(200, 146), (278, 196)], color=AMBER, sw=1.2)
    s.label(330, 128, "RyR2 (receptor\nde rianodina)", key="ryr", size=10.5, fill=PURPLE, weight=600)
    s.arrow([(338, 150), (310, 184)], color=PURPLE, sw=1.2)
    # íons Ca²⁺
    def ca(x, y, r=5):
        s.circle(x, y, r, fill=AMBER, stroke="#fff", sw=1)
    for x, y in [(120, 36), (160, 44), (380, 30), (420, 44), (600, 36)]:
        ca(x, y, 4)
    # 1. entrada pelo tipo L
    s.arrow([(270, 40), (270, 120), (289, 196)], color=AMBER, sw=2.2, curve=True)
    # 2. liberação pelo RyR
    s.arrow([(312, 232), (360, 300), (420, 318)], color=PURPLE, sw=2.6, curve=True)
    for x, y in [(626, 316), (600, 330), (700, 318), (676, 332)]:
        ca(x, y, 4.5)
    for x, y in [(350, 290), (372, 304), (396, 312), (330, 276), (412, 326), (440, 322), (385, 330)]:
        ca(x, y)
    # miofilamentos
    y0 = 380
    s.rect(300, y0 - 26, 360, 76, fill="#fff", stroke=LINE, r=10)
    for k in range(2):
        yy = y0 - 10 + k * 40
        s.line(310, yy, 650, yy, stroke=RED, sw=3)
        for x in range(314, 650, 13):
            s.circle(x, yy, 3.4, fill=RED, opacity=0.8)
    s.line(360, y0 + 10, 600, y0 + 10, stroke=BLUE, sw=7)
    for x in range(372, 596, 22):
        s.line(x, y0 + 8, x + 8, y0 - 4, stroke=BLUE, sw=2.2)
        s.line(x, y0 + 12, x + 8, y0 + 24, stroke=BLUE, sw=2.2)
    s.text(668, y0 - 6, "actina +\ntroponina", size=10.5, fill=RED, weight=600)
    s.text(670, y0 + 22, "miosina", size=10.5, fill=BLUE, weight=600)
    s.arrow([(450, 330), (470, 352)], color=RED, sw=2)
    # 4. SERCA2 e 5. NCX
    s.circle(560, 170, 9, fill=TEAL, stroke="#fff", sw=1.5)
    s.arrow([(620, 300), (600, 220), (566, 180)], color=TEAL, sw=2.2, curve=True)
    s.label(592, 262, "SERCA2\n(↑ com fosfolambam\nfosforilado)", key="serca", size=10.5, fill=TEAL, weight=600, anchor="end")
    s.circle(700, 62, 10, fill=GREEN, stroke="#fff", sw=1.5)
    s.arrow([(690, 300), (706, 180), (700, 74)], color=GREEN, sw=2.2, curve=True)
    s.arrow([(740, 20), (712, 52)], color=GREEN, sw=1.6)
    s.label(722, 104, "trocador\nNa⁺/Ca²⁺\n(3 Na⁺ : 1 Ca²⁺)", key="ncx", size=10.5, fill=GREEN, weight=600)
    # passos numerados
    steps = [(262, 92, "1", AMBER), (352, 268, "2", PURPLE), (478, 344, "3", RED), (606, 212, "4", TEAL), (700, 214, "5", GREEN)]
    for x, y, n, c in steps:
        s.circle(x, y, 11, fill=c, stroke="#fff", sw=2)
        s.text(x, y, n, size=11.5, weight=800, fill="#fff", anchor="middle", valign="middle")
    # legenda
    s.rect(16, 300, 272, 160, fill="#fbfbfc", stroke=LINE, r=12)
    leg = [("1", AMBER, "Potencial desce pelo túbulo T:\nentra **Ca²⁺ pelo tipo L**", "p1"),
           ("2", PURPLE, "**Liberação de Ca²⁺ induzida\npor Ca²⁺** (RyR2)", "p2"),
           ("3", RED, "Ca²⁺ + **troponina C** →\npontes cruzadas → contração", "p3"),
           ("4", TEAL, "Relaxamento: **SERCA2**\nrecapta Ca²⁺ para o RS", "p4"),
           ("5", GREEN, "**NCX** expulsa Ca²⁺ da célula", "p5")]
    for i, (n, c, txt, k) in enumerate(leg):
        y = 318 + i * 29
        s.circle(32, y + 6, 8, fill=c)
        s.text(32, y + 6, n, size=9.5, weight=800, fill="#fff", anchor="middle", valign="middle")
        s.label(46, y - 2, txt, key=k, size=9.8, valign="top")
    return s.svg()


# ---------------------------------------------------------------- diagrama de Wiggers
T_EV = dict(fecha_m=0.15, abre_ao=0.19, fecha_ao=0.45, abre_m=0.53, fim_rapido=0.63, inicio_as=0.72)


def _lv_ej(t):
    x = min(1, max(0, (t - 0.19) / 0.26))
    return 80 + 42 * math.sin(math.pi * 0.8 * x ** 0.75)


def _lv(t):
    if t < 0.15:
        return _la(t) - 0.6
    if t < 0.19:
        return _la(0.15) - 0.6 + (80 - _la(0.15) + 0.6) * _smoothstep(0.15, 0.19, t)
    if t < 0.45:
        return _lv_ej(t)
    if t < 0.53:
        return 3 + (_lv_ej(0.45) - 3) * (1 - _smoothstep(0.45, 0.53, t))
    return 3 + 2 * _smoothstep(0.53, 0.8, t)


def _ao(t):
    if t < 0.19:
        return 84 - 4 * t / 0.19
    if t < 0.45:
        return _lv_ej(t) + 1.5
    top = _lv_ej(0.45) + 1.5
    if t < 0.47:
        return top - 5 * math.sin(math.pi * (t - 0.45) / 0.04)
    if t < 0.49:
        return top - 5 * math.sin(math.pi * (t - 0.45) / 0.04) * 0.4 + 1
    return top + 1 - (top + 1 - 84) * (t - 0.49) / 0.31


def _la(t):
    a = 5 * math.exp(-((t - 0.06) / 0.025) ** 2)
    c = 3 * math.exp(-((t - 0.17) / 0.015) ** 2)
    v = 6 * math.exp(-((t - 0.51) / 0.05) ** 2)
    base = 3 + 2.5 * _smoothstep(0.22, 0.48, t) * (1 - _smoothstep(0.53, 0.62, t))
    return base + a + c + v


def _vol(t):
    if t < 0.10:
        return 108 + 17 * _smoothstep(0.02, 0.10, t)
    if t < 0.19:
        return 125
    if t < 0.45:
        return 125 - 70 * (1 - (1 - (t - 0.19) / 0.26) ** 1.8)
    if t < 0.53:
        return 55
    if t < 0.63:
        return 55 + 42 * _smoothstep(0.53, 0.63, t)
    return 97 + 11 * (t - 0.63) / 0.17


def _ecg(t):
    g = lambda mu, sd, a: a * math.exp(-((t - mu) / sd) ** 2)
    return g(0.035, 0.018, 0.15) + g(0.115, 0.004, -0.12) + g(0.13, 0.007, 1.0) + g(0.145, 0.006, -0.25) + g(0.36, 0.035, 0.3)


def wiggers(hide=None):
    s = SVG(820, 600, hide)
    X0, W = 110, 560
    fx = lambda t: X0 + t / 0.8 * W
    # faixas de fase
    phases = [(0, .15, "SA", "sístole\natrial", GREY_L), (.15, .19, "CI", "contração\nisovolum.", RED_L),
              (.19, .45, "EJ", "ejeção", "#fff5f6"), (.45, .53, "RI", "relaxam.\nisovolum.", BLUE_L),
              (.53, .63, "ER", "enchimento\nrápido", "#f4f8fe"), (.63, .8, "DI", "diástase", "#fbfbfc")]
    for a, b, k, name, col in phases:
        s.rect(fx(a), 40, fx(b) - fx(a), 530, fill=col, r=0)
        s.label((fx(a) + fx(b)) / 2, 22, name, key="ph_" + k.lower(), size=9.6, weight=600, anchor="middle",
                valign="middle", fill=INK)
    for t in (.15, .19, .45, .53):
        s.line(fx(t), 40, fx(t), 570, stroke="#9aa1ab", sw=1, dash="4 3")
    s.text(fx(.3), 588, "SÍSTOLE", size=10.5, weight=800, fill=RED, anchor="middle")
    s.text(fx(.64), 588, "DIÁSTOLE", size=10.5, weight=800, fill=BLUE, anchor="middle")
    # pressões
    P = lambda p: 300 - p / 130 * 250
    for p in (0, 40, 80, 120):
        s.text(X0 - 8, P(p), str(p), size=10, fill=MUTE, anchor="end", valign="middle")
    s.text(X0 - 44, P(65), "pressão (mmHg)", size=11, fill=MUTE, anchor="middle", rotate=-90)
    N = 400
    ts = [i * 0.8 / N for i in range(N + 1)]
    s.poly([(fx(t), P(_ao(t))) for t in ts], stroke=RED, sw=2.6)
    s.poly([(fx(t), P(_lv(t))) for t in ts], stroke=BLUE, sw=2.6)
    s.poly([(fx(t), P(_la(t))) for t in ts], stroke=AMBER, sw=2.2)
    s.label(fx(.8) + 8, P(84), "aorta", size=11, weight=700, fill=RED, valign="middle")
    s.label(fx(.8) + 8, P(10), "átrio E", size=11, weight=700, fill=AMBER, valign="middle")
    s.label(fx(.8) + 8, P(-4), "ventrículo E", size=11, weight=700, fill=BLUE, valign="middle")
    # eventos valvares
    ev = [(.19, _ao(.19), "abre_ao", "abre a\naórtica", -8, -26, "end"), (.45, _ao(.45), "fecha_ao", "fecha a\naórtica", 10, -50, "start"),
          (.15, _lv(.15), "fecha_mi", "fecha a\nmitral", -6, -40, "end"), (.53, _lv(.53), "abre_mi", "abre a\nmitral", 8, -36, "start")]
    for t, p, k, txt, dx, dy, anc in ev:
        s.circle(fx(t), P(p), 4.5, fill="#fff", stroke=INK, sw=1.6)
        s.label(fx(t) + dx, P(p) + dy, txt, key=k, size=9.8, weight=600, anchor=anc, pill=("#ffffffd0", "none"), pad=(3, 2))
    s.label(fx(.49) + 8, P(_ao(.47)) + 22, "incisura", key="incisura", size=9.8, fill=RED, weight=600, pill=("#ffffffd0", "none"), pad=(3, 2))
    for t, k, txt, dx in ((.06, "onda_a", "a", 0), (.17, "onda_c", "c", 0), (.51, "onda_v", "v", 14)):
        s.label(fx(t) + dx, P(_la(t)) - 8, txt, key=k, size=11, weight=800, fill=AMBER, anchor="middle")
    # volume
    Vy = lambda v: 440 - (v - 40) / 100 * 100
    for v in (50, 90, 130):
        s.text(X0 - 8, Vy(v), str(v), size=10, fill=MUTE, anchor="end", valign="middle")
    s.text(X0 - 44, Vy(90), "volume VE (mℓ)", size=11, fill=MUTE, anchor="middle", rotate=-90)
    s.poly([(fx(t), Vy(_vol(t))) for t in ts], stroke=PURPLE, sw=2.6)
    s.label(fx(.19) + 4, Vy(125) - 8, "VDF ≈ 120", key="vdf", size=9.8, fill=PURPLE, weight=600)
    s.label(fx(.45) + 4, Vy(55) + 16, "VSF ≈ 50", key="vsf", size=9.8, fill=PURPLE, weight=600)
    # ECG
    E = lambda e: 500 - e * 38
    s.poly([(fx(t), E(_ecg(t))) for t in ts], stroke=GREEN, sw=2)
    s.label(fx(.8) + 8, E(0), "ECG", size=11, weight=700, fill=GREEN, valign="middle")
    for t, txt in ((.035, "P"), (.13, "QRS"), (.36, "T")):
        s.text(fx(t), E(_ecg(t)) - 8, txt, size=10, weight=700, fill=GREEN, anchor="middle")
    # bulhas
    for t, k, name, amp in ((.07, "B4", "B4", 5), (.15, "B1", "B1", 12), (.45, "B2", "B2", 10), (.595, "B3", "B3", 5)):
        pts = [(fx(t) - 10 + i * 1.2, 548 + amp * math.sin(i * 1.7) * math.exp(-((i - 8) / 6) ** 2)) for i in range(17)]
        s.poly(pts, stroke=INK, sw=1.4)
        s.label(fx(t), 536 - amp, name, key=k, size=10, weight=700, anchor="middle")
    s.label(fx(.8) + 8, 548, "bulhas", size=11, weight=700, fill=INK, valign="middle")
    return s.svg()


# ---------------------------------------------------------------- alça pressão-volume
def alca_pv(hide=None):
    s = SVG(700, 460, hide)
    m = s.axes(90, 30, 420, 340, (0, 160), (0, 140), xticks=(0, 40, 80, 120, 160), yticks=(0, 40, 80, 120),
               xlabel="volume do VE (mℓ)", ylabel="pressão do VE (mmHg)")
    # relação sistólica final e curva diastólica
    s.poly([m(v, 2.25 * (v - 10)) for v in (10, 70)], stroke=MUTE, sw=1.4, dash="5 4")
    s.text(*m(62, 137), "RPVSF (contratilidade)", size=10, fill=MUTE)
    s.poly([m(v, 3 + 0.00055 * (v - 40) ** 2.4 if v > 40 else 3) for v in range(30, 150, 4)], stroke=MUTE, sw=1.4, dash="5 4")
    s.text(*m(146, 64), "curva diastólica\n(complacência)", size=10, fill=MUTE, anchor="middle")
    A, B, C, D = (50, 5), (120, 10), (120, 80), (50, 100)
    fill_c = [(50 + 70 * i / 20, 5 + 5 * (i / 20) ** 2.2) for i in range(21)]
    ej = [(120 - 70 * i / 30, 80 + 40 * math.sin(math.pi * i / 30 * 0.8) - (i / 30) * 12) for i in range(31)]
    loop = [m(*p) for p in fill_c] + [m(*C)] + [m(*p) for p in ej] + [m(*D), m(*A)]
    s.poly(loop, stroke="none", fill=RED_L)
    s.poly(loop, stroke=RED, sw=3)
    for p, n in ((A, "A"), (B, "B"), (C, "C"), (D, "D")):
        s.circle(*m(*p), 6, fill="#fff", stroke=RED, sw=2.2)
    notes = [(A, "A · abre a mitral", -10, -4, "end", "pa"), (B, "B · fecha a mitral (VDF)", 8, 18, "start", "pb"),
             (C, "C · abre a aórtica", 10, 4, "start", "pc"), (D, "D · fecha a aórtica (VSF)", -10, -10, "end", "pd")]
    for p, txt, dx, dy, anc, k in notes:
        x, y = m(*p)
        s.label(x + dx, y + dy, txt, key=k, size=10.5, weight=600, anchor=anc)
    for (x, y), n, k in ((m(85, 3), "I", "I"), (m(128, 45), "II", "II"), (m(97, 124), "III", "III"), (m(40, 52), "IV", "IV")):
        s.circle(x, y, 13, fill=RED, stroke="#fff", sw=2)
        s.text(x, y, n, size=11, weight=800, fill="#fff", anchor="middle", valign="middle")
    s.label(*m(85, 60), "trabalho\nexterno (TE)", key="TE", size=12, weight=700, fill=RED, anchor="middle", valign="middle")
    y = m(0, 0)[1] + 58
    s.arrow([(m(50, 0)[0], y), (m(120, 0)[0], y)], color=PURPLE, both=True, sw=2)
    s.label(m(85, 0)[0], y + 18, "volume sistólico ≈ 70 mℓ", key="VS", size=10.5, weight=700, fill=PURPLE, anchor="middle")
    # legenda
    s.rect(530, 40, 160, 190, fill="#fbfbfc", stroke=LINE, r=12)
    s.text(544, 62, "Fases", size=12.5, weight=700)
    for i, (n, txt, k) in enumerate((("I", "enchimento", "lI"), ("II", "contração\nisovolumétrica", "lII"),
                                     ("III", "ejeção", "lIII"), ("IV", "relaxamento\nisovolumétrico", "lIV"))):
        y = 84 + i * 36
        s.circle(556, y + 7, 10, fill=RED)
        s.text(556, y + 7, n, size=9, weight=800, fill="#fff", anchor="middle", valign="middle")
        s.label(572, y, txt, key=k, size=10.5, valign="top")
    s.rect(530, 244, 160, 110, fill=BLUE_L, stroke=BLUE, r=12, sw=1)
    s.text(544, 264, "Pré-carga ↑", size=11, weight=700, fill=BLUE)
    s.text(544, 280, "alça mais larga à direita", size=10, fill=INK)
    s.text(544, 304, "Pós-carga ↑", size=11, weight=700, fill=RED)
    s.text(544, 320, "alça mais alta e estreita", size=10, fill=INK)
    s.text(544, 342, "(↓ volume sistólico)", size=10, fill=MUTE)
    return s.svg()


# ---------------------------------------------------------------- focos de ausculta
def focos(hide=None):
    s = SVG(640, 560, hide)
    cx = 300
    # tórax
    s.path(f"M{cx - 250},60 Q{cx - 270},300 {cx - 200},520 L{cx + 200},520 Q{cx + 270},300 {cx + 250},60 Z",
           stroke="#c9b8a6", sw=2, fill="#fbf6f1")
    s.path(f"M{cx - 230},66 Q{cx - 110},40 {cx - 14},70", stroke="#b9a58f", sw=6)
    s.path(f"M{cx + 230},66 Q{cx + 110},40 {cx + 14},70", stroke="#b9a58f", sw=6)
    s.rect(cx - 22, 64, 44, 300, fill="#efe4d6", stroke="#c9b8a6", r=14, sw=1.5)
    s.path(f"M{cx - 12},364 L{cx},398 L{cx + 12},364", stroke="#c9b8a6", sw=1.5, fill="#efe4d6")
    rib_y = [110, 160, 210, 260, 310, 360]
    for i, y in enumerate(rib_y):
        for sgn in (-1, 1):
            x1, x2 = cx + sgn * 26, cx + sgn * (190 + i * 6)
            s.path(f"M{x1},{y} Q{(x1 + x2) / 2},{y - 16 + i * 3} {x2},{y + 30 + i * 6}", stroke="#d8c7b4", sw=9)
            s.text(x1 + sgn * 6, y - 10 if sgn < 0 else y - 10, f"{i + 1}ª", size=8.5, fill="#a8927b",
                   anchor="end" if sgn < 0 else "start")
    s.line(cx + 118, 70, cx + 118, 480, stroke="#b9a58f", sw=1.2, dash="4 4")
    s.text(cx + 118, 494, "linha hemiclavicular E", size=9.5, fill="#a8927b", anchor="middle")
    s.ellipse(cx + 70, 290, 120, 95, fill=RED, opacity=0.07)
    # focos (EIC = entre costelas)
    foci = [("ao", cx - 42, 135, "Aórtico", "2º EIC D, justaesternal", RED),
            ("pu", cx + 42, 135, "Pulmonar", "2º EIC E, justaesternal", BLUE),
            ("ac", cx + 42, 210, "Aórtico acessório", "3º–4º EIC E, junto ao esterno", PURPLE),
            ("tr", cx + 16, 392, "Tricúspide", "base do apêndice xifoide, à E", AMBER),
            ("mi", cx + 118, 312, "Mitral (ictus)", "5º EIC E, linha hemiclavicular", GREEN)]
    lab_pos = {"ao": (20, 150, "start"), "pu": (430, 110, "start"), "ac": (430, 190, "start"), "tr": (20, 440, "start"),
               "mi": (430, 330, "start")}
    for k, x, y, name, where, col in foci:
        s.circle(x, y, 13, fill=col, opacity=0.25)
        s.circle(x, y, 7, fill=col, stroke="#fff", sw=2)
        lx, ly, anc = lab_pos[k]
        s.line(x, y, lx + (0 if anc == "start" else 0) + (150 if lx < cx else -6), ly - 4, stroke=col, sw=1)
        s.label(lx, ly - 8, f"**{name}**\n{where}", key=k, size=10.5, fill=col, valign="top")
    return s.svg()


FIGS = {"a_potencial_acao": potencial_acao, "a_acoplamento": acoplamento, "a_wiggers": wiggers, "a_alca_pv": alca_pv,
        "a_focos": focos}

OCLUSOES = [
    ("a_potencial_acao", "f0", "Fase 0 do potencial ventricular: qual íon?", "Entrada de <b>Na⁺</b> (canais rápidos)."),
    ("a_potencial_acao", "f1", "Fase 1: o que acontece?", "Canais de Na⁺ fecham; <b>sai K⁺</b> (transitório)."),
    ("a_potencial_acao", "f2", "Fase 2: por que existe o platô?", "<b>Entra Ca²⁺</b> pelos canais tipo L e <b>cai a saída de K⁺</b>."),
    ("a_potencial_acao", "f3", "Fase 3: o que repolariza a fibra?", "Canais de Ca²⁺ fecham e <b>sai K⁺</b>."),
    ("a_potencial_acao", "f4", "Fase 4: qual o potencial de repouso?", "<b>−85 a −90 mV</b> (alta permeabilidade ao K⁺)."),
    ("a_potencial_acao", "pra", "O que representa essa faixa e quanto dura?", "<b>Período refratário absoluto</b> do ventrículo: 0,25 a 0,30 s."),
    ("a_acoplamento", "p1", "Passo 1 do acoplamento?", "Potencial desce pelo túbulo T e <b>entra Ca²⁺ pelos canais tipo L</b>."),
    ("a_acoplamento", "p2", "Passo 2 do acoplamento?", "<b>Liberação de Ca²⁺ induzida por Ca²⁺</b> pelos receptores de rianodina (RyR2)."),
    ("a_acoplamento", "p3", "Passo 3 do acoplamento?", "Ca²⁺ liga-se à <b>troponina C</b> → pontes cruzadas → contração."),
    ("a_acoplamento", "p4", "Passo 4: como o Ca²⁺ volta ao RS?", "<b>SERCA2</b> (bomba de Ca²⁺ do RS), estimulada quando o fosfolambam é fosforilado."),
    ("a_acoplamento", "p5", "Passo 5: como o Ca²⁺ sai da célula?", "<b>Trocador Na⁺/Ca²⁺</b> (NCX), 3 Na⁺ entram para 1 Ca²⁺ sair."),
    ("a_acoplamento", "ryr", "Qual canal libera o Ca²⁺ do RS?", "<b>RyR2</b> (receptor de rianodina)."),
    ("a_acoplamento", "ltcc", "Qual canal está na parede do túbulo T?", "<b>Canal de Ca²⁺ tipo L</b> (receptor de di-hidropiridina)."),
    ("a_wiggers", "ph_ci", "Nome da fase?", "<b>Contração isovolumétrica</b> (todas as valvas fechadas)."),
    ("a_wiggers", "ph_ri", "Nome da fase?", "<b>Relaxamento isovolumétrico</b>."),
    ("a_wiggers", "ph_er", "Nome da fase?", "<b>Enchimento rápido</b> (1º terço da diástole)."),
    ("a_wiggers", "abre_ao", "Qual evento valvar?", "<b>Abertura da valva aórtica</b> (PVE supera ≈ 80 mmHg)."),
    ("a_wiggers", "fecha_mi", "Qual evento valvar?", "<b>Fechamento da mitral</b> (início da sístole, B1)."),
    ("a_wiggers", "abre_mi", "Qual evento valvar?", "<b>Abertura da mitral</b> (fim do relaxamento isovolumétrico)."),
    ("a_wiggers", "incisura", "Nome desse entalhe na curva aórtica?", "<b>Incisura</b>: refluxo breve e fechamento da valva aórtica."),
    ("a_wiggers", "onda_a", "Qual onda de pressão atrial e sua causa?", "Onda <b>a</b>: contração atrial."),
    ("a_wiggers", "onda_c", "Qual onda de pressão atrial e sua causa?", "Onda <b>c</b>: abaulamento das valvas AV no início da sístole."),
    ("a_wiggers", "onda_v", "Qual onda de pressão atrial e sua causa?", "Onda <b>v</b>: enchimento atrial com as AV fechadas."),
    ("a_wiggers", "B4", "Qual bulha ocorre aqui?", "<b>B4</b>: contração atrial contra ventrículo rígido."),
    ("a_wiggers", "B3", "Qual bulha ocorre aqui?", "<b>B3</b>: enchimento rápido; normal em jovens, IC em idosos."),
    ("a_wiggers", "vdf", "Volume nesse ponto?", "<b>Volume diastólico final ≈ 110 a 120 mℓ</b>."),
    ("a_alca_pv", "II", "Qual fase da alça (B → C)?", "<b>Contração isovolumétrica</b>."),
    ("a_alca_pv", "IV", "Qual fase da alça (D → A)?", "<b>Relaxamento isovolumétrico</b>."),
    ("a_alca_pv", "pc", "O que acontece no ponto C?", "<b>Abre a valva aórtica</b>: começa a ejeção."),
    ("a_alca_pv", "pa", "O que acontece no ponto A?", "<b>Abre a valva mitral</b>: começa o enchimento."),
    ("a_alca_pv", "TE", "O que representa a área da alça?", "<b>Trabalho sistólico externo</b>."),
    ("a_alca_pv", "VS", "Qual grandeza é a largura da alça?", "<b>Volume sistólico</b> = VDF − VSF ≈ 70 mℓ."),
    ("a_focos", "ao", "Qual foco de ausculta?", "<b>Aórtico</b>: 2º EIC direito, justaesternal."),
    ("a_focos", "pu", "Qual foco de ausculta?", "<b>Pulmonar</b>: 2º EIC esquerdo, junto ao esterno."),
    ("a_focos", "ac", "Qual foco de ausculta?", "<b>Aórtico acessório</b>: 3º-4º EIC esquerdo, junto ao esterno."),
    ("a_focos", "tr", "Qual foco de ausculta?", "<b>Tricúspide</b>: base do apêndice xifoide, ligeiramente à esquerda."),
    ("a_focos", "mi", "Qual foco de ausculta?", "<b>Mitral</b>: 5º EIC esquerdo na linha hemiclavicular (ictus cordis)."),
]

if __name__ == "__main__":
    print("ok", export("dia_a", FIGS, OCLUSOES))
