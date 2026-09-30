"""Diagramas vetoriais do tema c (ECG normal; Guyton caps. 11 e 12), com oclusões para o Anki."""
import math

from svgkit import (AMBER, AMBER_L, BLUE, BLUE_L, GREEN, GREEN_L, GREY_L, INK, LINE, MUTE, PURPLE, PURPLE_L, RED,
                    RED_L, SVG, TEAL, TEAL_L, export)

PINK_MIN, PINK_MAJ = "#f8d5da", "#eca7b1"
PILL = ("#ffffffe8", "none")


def _g(x, mu, sd, amp):
    return amp * math.exp(-0.5 * ((x - mu) / sd) ** 2)


def batimento(t, t0=0.0):
    """ECG sintético (mV): P 0,10 s, PR 0,16 s, QRS 0,08 s, QT 0,35 s."""
    x = t - t0
    return (_g(x, 0.145, 0.022, 0.18) + _g(x, 0.272, 0.006, -0.10) + _g(x, 0.295, 0.010, 1.20)
            + _g(x, 0.318, 0.007, -0.30) + _g(x, 0.50, 0.045, 0.30))


def _papel(s, x0, y0, nx, ny, mm):
    """Papel milimetrado do ECG com nx × ny quadradinhos de mm px."""
    s.rect(x0, y0, nx * mm, ny * mm, fill="#fff8f9", r=0)
    for i in range(nx + 1):
        maj = i % 5 == 0
        s.line(x0 + i * mm, y0, x0 + i * mm, y0 + ny * mm, stroke=PINK_MAJ if maj else PINK_MIN, sw=1.1 if maj else 0.6)
    for j in range(ny + 1):
        maj = (ny - j) % 5 == 0
        s.line(x0, y0 + j * mm, x0 + nx * mm, y0 + j * mm, stroke=PINK_MAJ if maj else PINK_MIN, sw=1.1 if maj else 0.6)


# ---------------------------------------------------------------- ECG normal
def ecg_normal(hide=None):
    s = SVG(840, 470, hide)
    mm, X0, Y0 = 18, 30, 40
    nx, ny = 44, 22                       # 44 mm = 1,76 s; 22 mm = −0,6 a +1,6 mV
    _papel(s, X0, Y0, nx, ny, mm)
    fx = lambda t: X0 + t * 25 * mm       # 25 mm/s
    fy = lambda v: Y0 + (1.6 - v) * 10 * mm
    # faixas das ondas (1º batimento)
    for a, b, c in ((0.10, 0.19, AMBER), (0.26, 0.34, RED), (0.40, 0.61, BLUE)):
        s.rect(fx(a), Y0, fx(b) - fx(a), ny * mm, fill=c, r=0, opacity=0.07)
    pts = [(fx(t / 1000), fy(batimento(t / 1000) + batimento(t / 1000, 0.83))) for t in range(0, 1480, 2)]
    s.poly(pts, stroke=INK, sw=2.4)
    s.line(fx(0.34), fy(0.02), fx(0.42), fy(0.02), stroke=GREEN, sw=4, opacity=0.8)
    # ondas
    for k, t, v, c in (("P", 0.145, 0.33, AMBER), ("Q", 0.25, -0.2, RED), ("R", 0.295, 1.36, RED), ("S", 0.33, -0.48, RED),
                       ("T", 0.50, 0.45, BLUE)):
        s.label(fx(t), fy(v), k, key=k, size=17, weight=800, fill=c, anchor="middle", valign="middle")

    def bracket(a, b, v, txt, key, c=PURPLE, dy=-10, lx=None):
        y = fy(v)
        s.line(fx(a), y - 7, fx(a), y + 7, stroke=c, sw=1.6)
        s.line(fx(b), y - 7, fx(b), y + 7, stroke=c, sw=1.6)
        s.arrow([(fx(a) + 2, y), (fx(b) - 2, y)], color=c, sw=1.6, both=True)
        s.label(fx(lx) if lx else (fx(a) + fx(b)) / 2, y + dy, txt, key=key, size=12, weight=700, fill=c, anchor="middle", pill=PILL,
                pad=(4, 2))
    bracket(0.10, 0.26, -0.45, "PR ≈ 0,16 s", "PR", lx=0.12)
    bracket(0.26, 0.61, 1.0, "QT ≈ 0,35 s", "QT")
    bracket(0.26, 0.34, 0.66, "QRS 0,08 s", "QRS")
    bracket(0.295, 1.125, 1.48, "RR ≈ 0,83 s → FC = 60 / 0,83 ≈ 72 bpm", "RR")
    s.label(fx(0.38), fy(-0.22), "segmento ST", key="ST", size=11.5, weight=700, fill=GREEN, anchor="middle", pill=PILL,
            pad=(4, 2))
    # calibração 1 mV
    c0 = 1.52
    s.poly([(fx(c0), fy(0)), (fx(c0 + 0.02), fy(0)), (fx(c0 + 0.02), fy(1)), (fx(c0 + 0.10), fy(1)), (fx(c0 + 0.10), fy(0)),
            (fx(c0 + 0.13), fy(0))], stroke=INK, sw=2.2, smooth=False)
    s.label(fx(c0 + 0.06), fy(1.1), "1 mV = 10 mm", key="cal", size=11, weight=700, anchor="middle", pill=PILL, pad=(4, 2))
    # legenda das faixas
    y = Y0 + ny * mm + 26
    for i, (c, t) in enumerate(((AMBER, "P: despolarização atrial"), (RED, "QRS: despolarização ventricular"),
                                (BLUE, "T: repolarização ventricular"), (GREEN, "ST: ventrículo todo despolarizado"))):
        x = X0 + i * 200
        s.rect(x, y - 10, 14, 14, fill=c, r=3, opacity=0.85)
        s.text(x + 20, y + 1, t, size=11, fill=INK)
    return s.svg()


# ---------------------------------------------------------------- papel
def papel(hide=None):
    s = SVG(620, 420, hide)
    mm, X0, Y0 = 30, 150, 70
    _papel(s, X0, Y0, 10, 10, mm)
    # destaque de 1 quadradinho e 1 quadrado grande
    s.rect(X0, Y0 + 9 * mm, mm, mm, fill=RED, r=0, opacity=0.25)
    s.rect(X0 + 5 * mm, Y0 + 5 * mm, 5 * mm, 5 * mm, fill="none", stroke=RED, r=0, sw=2.4)
    y = Y0 - 18
    s.arrow([(X0, y), (X0 + mm, y)], color=INK, sw=1.4, both=True)
    s.label(X0 + mm / 2, y - 10, "1 mm = 0,04 s", key="peq_t", size=11, weight=600, anchor="middle")
    s.arrow([(X0 + 5 * mm, y), (X0 + 10 * mm, y)], color=INK, sw=1.4, both=True)
    s.label(X0 + 7.5 * mm, y - 10, "5 mm = 0,20 s", key="grd_t", size=11, weight=600, anchor="middle")
    x = X0 - 16
    s.arrow([(x, Y0 + 9 * mm), (x, Y0 + 10 * mm)], color=INK, sw=1.4, both=True)
    s.label(x - 8, Y0 + 9.5 * mm, "1 mm = 0,1 mV", key="peq_v", size=11, weight=600, anchor="end", valign="middle")
    xr = X0 + 10 * mm + 16
    s.arrow([(xr, Y0 + 5 * mm), (xr, Y0 + 10 * mm)], color=INK, sw=1.4, both=True)
    s.label(xr + 8, Y0 + 7.5 * mm, "5 mm = 0,5 mV", key="grd_v", size=11, weight=600, valign="middle")
    s.label(X0 + 5 * mm, Y0 + 10 * mm + 30, "velocidade padrão: 25 mm/s (25 mm = 1 s)", key="vel", size=11.5, weight=700,
            fill=RED, anchor="middle")
    return s.svg()


# ---------------------------------------------------------------- sistema hexaxial
def _pol(cx, cy, r, ang):
    a = math.radians(ang)
    return cx + r * math.cos(a), cy + r * math.sin(a)   # 0° à esquerda do paciente, +90° para baixo


def hexaxial(hide=None):
    s = SVG(560, 545, hide)
    cx, cy, R = 250, 250, 175
    # setor normal (Guyton: 20° a 100°)
    a0, a1 = _pol(cx, cy, R, 20), _pol(cx, cy, R, 100)
    s.path(f"M{cx},{cy} L{a0[0]:.1f},{a0[1]:.1f} A{R},{R} 0 0 1 {a1[0]:.1f},{a1[1]:.1f} Z", stroke="none", fill=GREEN_L)
    s.circle(cx, cy, R, fill="none", stroke=LINE, sw=1.4)
    leads = [("I", 0, RED), ("II", 60, RED), ("III", 120, RED), ("aVR", -150, BLUE), ("aVL", -30, BLUE), ("aVF", 90, BLUE)]
    for name, ang, c in leads:
        p, q = _pol(cx, cy, R, ang), _pol(cx, cy, R, ang + 180)
        s.line(*q, cx, cy, stroke=c, sw=1.2, dash="4 4", opacity=0.5)
        s.arrow([(cx, cy), p], color=c, sw=2.4)
        lx, ly = _pol(cx, cy, R + 26, ang)
        s.label(lx, ly, name, key="L_" + name, size=15, weight=800, fill=c, anchor="middle", valign="middle")
        dx, dy = _pol(0, 0, 1, ang + 90)
        tx, ty = _pol(cx, cy, R - 34, ang)
        sign = "+" if ang > 0 else ("−" if ang < 0 else "")
        s.label(tx + 13 * dx, ty + 13 * dy, f"{sign}{abs(ang)}°", key="A_" + name, size=10.5, weight=600, fill=MUTE,
                anchor="middle", valign="middle", pill=PILL, pad=(3, 1))
    e = _pol(cx, cy, R - 30, 59)
    s.arrow([(cx, cy), e], color=GREEN, sw=4.5)
    s.circle(cx, cy, 5, fill=INK)
    s.label(20, 470, "Eixo médio do QRS **+59°** (seta verde)\nnormal ≈ 20° a 100° (Guyton; setor verde)", key="eixo",
            size=11.5, fill=GREEN, valign="top")
    s.text(cx, 20, "−90°", size=10, fill=MUTE, anchor="middle")
    s.text(20, cy + 4, "±180°", size=10, fill=MUTE)
    s.text(cx, 536, "direita do paciente ←      → esquerda do paciente", size=9.5, fill=MUTE, anchor="middle")
    return s.svg()


# ---------------------------------------------------------------- regra dos quadrantes (DI e aVF)
def quadrantes(hide=None):
    s = SVG(520, 480, hide)
    cx, cy, R = 250, 235, 175
    quads = [("q_norm", 0, 90, GREEN_L, GREEN, "NORMAL", "DI + · aVF +", (1, 1)),
             ("q_esq", -90, 0, AMBER_L, AMBER, "DESVIO À\nESQUERDA", "DI + · aVF −", (1, -1)),
             ("q_dir", 90, 180, BLUE_L, BLUE, "DESVIO À\nDIREITA", "DI − · aVF +", (-1, 1)),
             ("q_ext", 180, 270, RED_L, RED, "EXTREMO", "DI − · aVF −", (-1, -1))]
    for k, a, b, cl, c, t, sub, (sx, sy) in quads:
        p, q = _pol(cx, cy, R, a), _pol(cx, cy, R, b)
        s.path(f"M{cx},{cy} L{p[0]:.1f},{p[1]:.1f} A{R},{R} 0 0 1 {q[0]:.1f},{q[1]:.1f} Z", stroke="#fff", sw=3, fill=cl)
        x, y = cx + sx * 88, cy + sy * 80
        s.label(x, y - 8, t, key=k, size=13, weight=800, fill=c, anchor="middle", valign="middle")
        s.text(x, y + 30, sub, size=11, weight=600, fill=INK, anchor="middle")
    s.arrow([(cx - R - 14, cy), (cx + R + 20, cy)], color=INK, sw=1.6)
    s.arrow([(cx, cy - R - 14), (cx, cy + R + 20)], color=INK, sw=1.6)
    s.text(cx + R + 22, cy - 8, "DI (0°)", size=11, weight=700, anchor="end")
    s.text(cx + 8, cy + R + 22, "aVF (+90°)", size=11, weight=700)
    s.text(20, 468, "Se DI + e aVF −, olhe DII: DII + → ainda normal (até −30°).", size=10, fill=MUTE)
    return s.svg()


# ---------------------------------------------------------------- triângulo de Einthoven
def einthoven(hide=None):
    s = SVG(620, 460, hide)
    # silhueta simples
    s.circle(250, 60, 30, fill="#f1e7dc", stroke="#d8c7b4", sw=1.5)
    s.path("M170,110 C200,96 300,96 330,110 L372,250 L346,258 L314,160 L312,300 L330,440 L290,440 L252,320 L212,440 "
           "L172,440 L190,300 L188,160 L156,258 L130,250 Z", stroke="#d8c7b4", sw=1.5, fill="#f7f0e8")
    RA, LA, LL = (140, 250), (360, 250), (300, 430)   # braço D (à esquerda da figura), braço E, perna E
    s.poly([RA, LA, LL, RA], stroke=MUTE, sw=1, dash="4 4", smooth=False)
    s.arrow([(RA[0] + 16, RA[1]), (LA[0] - 16, LA[1])], color=RED, sw=3)
    s.arrow([(RA[0] + 10, RA[1] + 14), (LL[0] - 8, LL[1] - 16)], color=BLUE, sw=3)
    s.arrow([(LA[0] - 6, LA[1] + 16), (LL[0] + 4, LL[1] - 18)], color=GREEN, sw=3)
    s.label(250, 238, "I", key="E_I", size=16, weight=800, fill=RED, anchor="middle")
    s.label(196, 356, "II", key="E_II", size=16, weight=800, fill=BLUE, anchor="middle")
    s.label(348, 350, "III", key="E_III", size=16, weight=800, fill=GREEN, anchor="middle")
    for (x, y), t in ((RA, "BD"), (LA, "BE"), (LL, "PE")):
        s.circle(x, y, 14, fill=INK, stroke="#fff", sw=2)
        s.text(x, y, t, size=9.5, weight=800, fill="#fff", anchor="middle", valign="middle")
    # painel
    px = 420
    s.rect(px, 60, 186, 250, fill="#fff", stroke=LINE, r=12, shadow=True)
    s.text(px + 14, 86, "Polo − → polo +", size=12, weight=700)
    for i, (c, n, t) in enumerate(((RED, "I", "BD → BE"), (BLUE, "II", "BD → PE"), (GREEN, "III", "BE → PE"))):
        y = 114 + i * 30
        s.text(px + 14, y, n, size=13, weight=800, fill=c)
        s.text(px + 48, y, t, size=11.5)
    s.rect(px + 12, 212, 162, 82, fill=RED_L, r=8)
    s.text(px + 22, 234, "Lei de Einthoven", size=11.5, weight=700, fill=RED)
    s.label(px + 22, 246, "**I + III = II**\n(somas no mesmo\ninstante)", key="lei", size=11, valign="top")
    s.text(px, 340, "BD = braço direito\nBE = braço esquerdo\nPE = perna esquerda", size=10, fill=MUTE)
    return s.svg()


# ---------------------------------------------------------------- precordiais
def precordiais(hide=None):
    s = SVG(700, 500, hide)
    cx = 250
    s.path(f"M{cx - 220},40 Q{cx - 240},260 {cx - 180},470 L{cx + 180},470 Q{cx + 240},260 {cx + 220},40 Z",
           stroke="#c9b8a6", sw=2, fill="#fbf6f1")
    s.rect(cx - 20, 44, 40, 270, fill="#efe4d6", stroke="#c9b8a6", r=12, sw=1.5)
    for i, y in enumerate([80, 125, 170, 215, 260, 305, 350]):
        for sg in (-1, 1):
            x1, x2 = cx + sg * 24, cx + sg * (180 + i * 5)
            s.path(f"M{x1},{y} Q{(x1 + x2) / 2},{y - 14 + i * 3} {x2},{y + 28 + i * 5}", stroke="#dccbb8", sw=8)
    s.ellipse(cx + 55, 290, 105, 80, fill=RED, opacity=0.07)
    for x, n in ((cx + 110, "LHC"), (cx + 170, "LAA"), (cx + 215, "LAM")):
        s.line(x, 48, x, 460, stroke="#b9a58f", sw=1.1, dash="4 4")
        s.text(x, 482, n, size=9.5, fill="#a8927b", anchor="middle")
    pts = [("V1", cx - 32, 238), ("V2", cx + 32, 238), ("V3", cx + 72, 262), ("V4", cx + 110, 286), ("V5", cx + 170, 290),
           ("V6", cx + 215, 294)]
    for n, x, y in pts:
        s.circle(x, y, 13, fill=RED, stroke="#fff", sw=2)
        s.text(x, y, n[1], size=11, weight=800, fill="#fff", anchor="middle", valign="middle")
    px = 490
    s.rect(px, 60, 200, 290, fill="#fff", stroke=LINE, r=12, shadow=True)
    s.text(px + 14, 86, "Posição dos eletrodos", size=12, weight=700)
    legend = [("V1", "4º EIC D, paraesternal"), ("V2", "4º EIC E, paraesternal"), ("V3", "entre V2 e V4"),
              ("V4", "5º EIC E, linha hemiclavicular"), ("V5", "linha axilar anterior,\nnível de V4"),
              ("V6", "linha axilar média,\nnível de V4")]
    y = 106
    for n, t in legend:
        s.text(px + 14, y + 12, n, size=12, weight=800, fill=RED)
        s.label(px + 46, y, t, key="P_" + n, size=10.5, valign="top")
        y += 36 + (14 if "\n" in t else 0)
    s.text(px, 380, "V1–V2: QRS negativo\n(longe da base, perto do\nventrículo direito)\nV4–V6: QRS positivo", size=10,
           fill=MUTE)
    return s.svg()


FIGS = {"c_ecg_normal": ecg_normal, "c_papel": papel, "c_hexaxial": hexaxial, "c_quadrantes": quadrantes,
        "c_precordiais": precordiais, "c_einthoven": einthoven}

OCLUSOES = [
    ("c_ecg_normal", "P", "Qual onda e o que representa?", "Onda <b>P</b>: despolarização atrial."),
    ("c_ecg_normal", "Q", "Qual onda e o que representa?", "Onda <b>Q</b>: despolarização do septo da esquerda para a direita."),
    ("c_ecg_normal", "T", "Qual onda e o que representa?", "Onda <b>T</b>: repolarização ventricular."),
    ("c_ecg_normal", "PR", "Nome e valor normal deste intervalo?", "Intervalo <b>PR (PQ)</b> ≈ <b>0,16 s</b> (início da P ao início do QRS)."),
    ("c_ecg_normal", "QT", "Nome e valor normal deste intervalo?", "Intervalo <b>QT</b> ≈ <b>0,35 s</b> (contração ventricular)."),
    ("c_ecg_normal", "QRS", "Duração normal do QRS?", "≈ <b>0,06 a 0,10 s</b> (aqui 0,08 s)."),
    ("c_ecg_normal", "RR", "Qual intervalo e qual FC corresponde a 0,83 s?", "<b>RR</b>; FC = 60/0,83 ≈ <b>72 bpm</b>."),
    ("c_ecg_normal", "ST", "Nome deste trecho?", "<b>Segmento ST</b> (ventrículo todo despolarizado: sem corrente, linha de base)."),
    ("c_ecg_normal", "cal", "Qual o sinal de calibração padrão?", "<b>1 mV = 10 mm</b> (10 quadradinhos)."),
    ("c_papel", "peq_t", "Quanto vale 1 quadradinho na horizontal?", "<b>0,04 s</b> (a 25 mm/s)."),
    ("c_papel", "grd_t", "Quanto vale 1 quadrado grande na horizontal?", "<b>0,20 s</b>."),
    ("c_papel", "peq_v", "Quanto vale 1 quadradinho na vertical?", "<b>0,1 mV</b>."),
    ("c_papel", "vel", "Velocidade padrão do papel?", "<b>25 mm/s</b>."),
    ("c_hexaxial", "L_II", "Qual derivação tem eixo em +60°?", "<b>DII</b>."),
    ("c_hexaxial", "L_III", "Qual derivação tem eixo em +120°?", "<b>DIII</b>."),
    ("c_hexaxial", "L_aVL", "Qual derivação tem eixo em −30°?", "<b>aVL</b>."),
    ("c_hexaxial", "L_aVR", "Qual derivação tem eixo em −150° (210°)?", "<b>aVR</b>."),
    ("c_hexaxial", "L_aVF", "Qual derivação tem eixo em +90°?", "<b>aVF</b>."),
    ("c_hexaxial", "eixo", "Eixo elétrico médio do QRS normal (Guyton)?", "<b>+59°</b>; varia de ≈ 20° a 100° em corações normais."),
    ("c_quadrantes", "q_norm", "DI positivo e aVF positivo: qual eixo?", "<b>Normal</b> (0° a +90°)."),
    ("c_quadrantes", "q_esq", "DI positivo e aVF negativo: qual eixo?", "<b>Desvio à esquerda</b> (confirmar com DII: se DII positivo, ainda pode ser normal até −30°)."),
    ("c_quadrantes", "q_dir", "DI negativo e aVF positivo: qual eixo?", "<b>Desvio à direita</b>."),
    ("c_quadrantes", "q_ext", "DI negativo e aVF negativo: qual eixo?", "<b>Desvio extremo</b> (−90° a ±180°)."),
    ("c_precordiais", "P_V1", "Onde fica V1?", "<b>4º EIC direito</b>, borda esternal."),
    ("c_precordiais", "P_V2", "Onde fica V2?", "<b>4º EIC esquerdo</b>, borda esternal."),
    ("c_precordiais", "P_V4", "Onde fica V4?", "<b>5º EIC esquerdo</b>, linha hemiclavicular."),
    ("c_precordiais", "P_V6", "Onde fica V6?", "<b>Linha axilar média</b>, no nível de V4."),
    ("c_einthoven", "E_I", "Qual derivação vai do braço direito (−) ao braço esquerdo (+)?", "<b>DI</b> (eixo 0°)."),
    ("c_einthoven", "E_II", "Qual derivação vai do braço direito (−) à perna esquerda (+)?", "<b>DII</b> (eixo +60°)."),
    ("c_einthoven", "E_III", "Qual derivação vai do braço esquerdo (−) à perna esquerda (+)?", "<b>DIII</b> (eixo +120°)."),
    ("c_einthoven", "lei", "Enuncie a lei de Einthoven.", "<b>I + III = II</b> (potenciais no mesmo instante)."),
]

if __name__ == "__main__":
    print("ok", export("dia_c", FIGS, OCLUSOES))
