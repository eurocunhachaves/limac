"""Diagramas vetoriais do tema d (biofísica da circulação; Guyton caps. 14 e 15), com oclusões para o Anki."""
import math

from svgkit import (AMBER, AMBER_L, BLUE, BLUE_L, GREEN, GREEN_L, GREY_L, INK, LINE, MUTE, PURPLE, PURPLE_L, RED,
                    RED_L, SVG, TEAL, TEAL_L, export)

PILL = ("#ffffffe8", "none")


def _arc(cx, cy, r0, r1, a0, a1):
    """Setor de anel (graus, 0 = topo, sentido horário)."""
    p = lambda r, a: (cx + r * math.sin(math.radians(a)), cy - r * math.cos(math.radians(a)))
    large = 1 if a1 - a0 > 180 else 0
    (x0, y0), (x1, y1), (x2, y2), (x3, y3) = p(r1, a0), p(r1, a1), p(r0, a1), p(r0, a0)
    return (f"M{x0:.1f},{y0:.1f} A{r1},{r1} 0 {large} 1 {x1:.1f},{y1:.1f} L{x2:.1f},{y2:.1f} "
            f"A{r0},{r0} 0 {large} 0 {x3:.1f},{y3:.1f} Z")


# ---------------------------------------------------------------- distribuição do volume
def volumes(hide=None):
    s = SVG(560, 330, hide)
    cx, cy = 160, 165
    parts = [("Veias sistêmicas", 64, BLUE, "veias"), ("Artérias sistêmicas", 13, RED, "arterias"),
             ("Arteríolas + capilares", 7, AMBER, "cap"), ("Circulação pulmonar", 9, PURPLE, "pulm"),
             ("Coração", 7, TEAL, "cor")]
    a = 0
    for name, pct, c, k in parts:
        b = a + pct * 3.6
        s.path(_arc(cx, cy, 72, 135, a + 0.6, b - 0.6), stroke="none", fill=c)
        a = b
    s.text(cx, cy - 6, "84%", size=26, weight=800, fill=INK, anchor="middle", valign="middle")
    s.text(cx, cy + 22, "sistêmica", size=11, fill=MUTE, anchor="middle")
    for i, (name, pct, c, k) in enumerate(parts):
        y = 58 + i * 50
        s.rect(330, y - 12, 16, 16, fill=c, r=4)
        s.text(356, y + 1, name, size=12, weight=600)
        s.label(356, y + 20, f"{pct}%", key=k, size=12, weight=800, fill=c)
    return s.svg()


# ---------------------------------------------------------------- pressões ao longo da circulação
def pressoes(hide=None):
    s = SVG(900, 430, hide)
    m = s.axes(70, 40, 800, 280, (-0.6, 11.6), (0, 130), yticks=(0, 20, 40, 60, 80, 100, 120), ylabel="pressão (mmHg)")
    segs = ["Aorta", "Grandes\nartérias", "Pequenas\nartérias", "Arteríolas", "Capilares", "Vênulas", "Veias", "Veias\ncavas",
            None, "Artéria\npulmonar", "Capilar\npulmonar", "Veias\npulmonares"]
    s.rect(m(-0.5, 0)[0], 40, m(7.5, 0)[0] - m(-0.5, 0)[0], 280, fill=RED_L, r=0, opacity=0.35)
    s.rect(m(8.5, 0)[0], 40, m(11.5, 0)[0] - m(8.5, 0)[0], 280, fill=BLUE_L, r=0, opacity=0.6)
    s.rect(m(2.6, 0)[0], 40, m(3.4, 0)[0] - m(2.6, 0)[0], 280, fill=AMBER_L, r=0)
    sis, dia = [120, 120, 110, 70], [80, 78, 75, 45]
    top = [m(i, v) for i, v in enumerate(sis)]
    bot = [m(i, v) for i, v in enumerate(dia)]
    s.poly(top + bot[::-1] + [top[0]], stroke="none", fill=RED, opacity=0.18)
    media = [100, 97, 90, 60, 17, 12, 8, 0]
    s.poly([m(i, v) for i, v in enumerate(media)], stroke=RED, sw=3)
    for i, v in enumerate(media):
        s.circle(*m(i, v), 5, fill=RED, stroke="#fff", sw=1.5)
    s.poly([m(9, 25), m(10, 10), m(11, 6), m(11, 3), m(10, 5), m(9, 8), m(9, 25)], stroke="none", fill=BLUE, opacity=0.18)
    pm = [16, 7, 4]
    s.poly([m(9 + i, v) for i, v in enumerate(pm)], stroke=BLUE, sw=3)
    for i, v in enumerate(pm):
        s.circle(*m(9 + i, v), 5, fill=BLUE, stroke="#fff", sw=1.5)
    for i, n in enumerate(segs):
        if n:
            s.text(m(i, 0)[0], 340, n, size=10, fill=INK, anchor="middle", weight=600)
    s.line(m(8, 0)[0], 40, m(8, 0)[0], 320, stroke=MUTE, sw=1, dash="3 4")
    s.text(m(3.5, 0)[0], 400, "CIRCULAÇÃO SISTÊMICA", size=12, weight=800, fill=RED, anchor="middle")
    s.text(m(10, 0)[0], 400, "PULMONAR", size=12, weight=800, fill=BLUE, anchor="middle")
    s.label(m(0.15, 124)[0], m(0, 124)[1], "120/80 · média 100", key="aorta", size=11, weight=700, fill=RED, pill=PILL, pad=(4, 2))
    s.label(m(3.25, 0)[0], m(0, 92)[1], "maior queda:\narteríolas", key="arteriola", size=11, weight=700, fill=AMBER,
            pill=PILL, pad=(4, 2))
    s.label(m(4.2, 0)[0], m(0, 36)[1], "35 → 10\n(média 17)", key="capilar", size=11, weight=700, pill=PILL, pad=(4, 2))
    s.label(m(7, 0)[0], m(0, 14)[1], "átrio D ≈ 0", key="ad", size=11, weight=700, anchor="middle", pill=PILL, pad=(4, 2))
    s.label(m(9, 0)[0], m(0, 40)[1], "25/8\nmédia 16", key="ap", size=11, weight=700, fill=BLUE, anchor="middle", pill=PILL,
            pad=(4, 2))
    s.label(m(10, 0)[0], m(0, 20)[1], "≈ 7", key="cp", size=11, weight=700, fill=BLUE, anchor="middle", pill=PILL, pad=(4, 2))
    return s.svg()


# ---------------------------------------------------------------- Poiseuille
def poiseuille(hide=None):
    s = SVG(760, 380, hide)
    s.text(300, 30, "mesma ΔP = 100 mmHg", size=11.5, fill=MUTE, anchor="middle")
    for r, f, y, k in ((1, 1, 70, "f1"), (2, 16, 142, "f2"), (4, 256, 240, "f4")):
        h = 9 * r
        s.rect(90, y - h, 420, 2 * h, fill=RED_L, stroke=RED, r=h, sw=1.6)
        for j in range(-r + 1, r):   # linhas de corrente
            yy = y + j * h / r * 0.8
            s.line(110, yy, 490, yy, stroke=RED, sw=1, opacity=0.35)
        s.text(78, y + 5, f"r = {r}", size=12, weight=700, anchor="end")
        s.arrow([(520, y), (580, y)], color=RED, sw=1 + r * 1.3)
        s.label(592, y + 6, f"{f} mℓ/min", key=k, size=14, weight=800, fill=RED)
    s.text(592, 262, "fluxo ∝ r⁴", size=11, fill=MUTE)
    s.rect(30, 300, 400, 52, fill=RED_L, stroke=RED, r=10, sw=1.2)
    s.label(46, 332, "Poiseuille:  **F = π·ΔP·r⁴ / (8·η·ℓ)**", key="lei", size=13)
    s.rect(450, 300, 290, 52, fill=BLUE_L, stroke=BLUE, r=10, sw=1.2)
    s.label(466, 332, "Ohm:  **F = ΔP / R**", key="ohm", size=13)
    return s.svg()


# ---------------------------------------------------------------- laminar × turbulento
def fluxo(hide=None):
    s = SVG(760, 300, hide)
    for x0, title, k, sub, k2 in ((20, "LAMINAR: perfil parabólico", "laminar", "centro rápido, parede ≈ 0", "centro"),
                                  (400, "TURBULENTO: redemoinhos", "turb", "Re > 2.000 → turbulência", "re")):
        s.label(x0 + 170, 40, title, key=k, size=13, weight=800, fill=INK, anchor="middle")
        s.rect(x0, 70, 340, 150, fill="#fff", stroke=LINE, r=0)
        s.line(x0, 70, x0 + 340, 70, stroke=RED, sw=4)
        s.line(x0, 220, x0 + 340, 220, stroke=RED, sw=4)
        s.label(x0 + 170, 256, sub, key=k2, size=11.5, fill=MUTE, anchor="middle")
    # laminar: setas de comprimento parabólico
    for j in range(9):
        y = 82 + j * 16.5
        u = 1 - ((y - 145) / 75) ** 2
        s.arrow([(60, y), (60 + 8 + 220 * u, y)], color=BLUE, sw=1.8)
    s.poly([(60 + 8 + 220 * (1 - ((y - 145) / 75) ** 2), y) for y in range(71, 220, 3)], stroke=BLUE, sw=1.2, dash="3 3")
    # turbulento: redemoinhos
    for cx, cy, r in ((470, 110, 22), (540, 170, 26), (610, 115, 20), (680, 175, 22), (500, 185, 14), (650, 140, 12)):
        s.path(f"M{cx + r},{cy} A{r},{r} 0 1 1 {cx},{cy - r} A{r * 0.6},{r * 0.6} 0 1 1 {cx + r * 0.3},{cy + r * 0.2}",
               stroke=BLUE, sw=1.8)
    s.arrow([(420, 145), (460, 145)], color=BLUE, sw=2)
    s.text(380, 292, "Re = v · d · ρ / η   (velocidade, diâmetro, densidade / viscosidade)", size=11, fill=MUTE,
           anchor="middle")
    return s.svg()


# ---------------------------------------------------------------- complacência
def complacencia(hide=None):
    s = SVG(760, 380, hide)
    m = s.axes(80, 30, 620, 270, (0, 3600), (0, 140), xticks=(0, 1000, 2000, 3000), yticks=(0, 40, 80, 120),
               xlabel="volume (mℓ)", ylabel="pressão (mmHg)", tick_fmt=lambda v: f"{v:,}".replace(",", "."))
    s.poly([m(v, (v - 400) / 3) for v in range(400, 811, 10)], stroke=RED, sw=3.2)
    s.poly([m(v, max(0, (v - 1800) / 170)) for v in range(1500, 3501, 20)], stroke=BLUE, sw=3.2)
    s.circle(*m(700, 100), 6, fill=RED, stroke="#fff", sw=2)
    s.circle(*m(2500, 4.1), 6, fill=BLUE, stroke="#fff", sw=2)
    s.label(m(760, 0)[0], m(0, 112)[1], "arterial: 700 mℓ → 100 mmHg\n(com 400 mℓ → 0)", key="art", size=11.5, weight=700,
            fill=RED, pill=PILL, pad=(4, 2))
    s.label(m(1900, 0)[0], m(0, 34)[1], "venoso: 2.000–3.500 mℓ\ncentenas de mℓ mudam só 3–5 mmHg", key="ven", size=11.5,
            weight=700, fill=BLUE, pill=PILL, pad=(4, 2))
    s.rect(m(1500, 0)[0], m(0, 94)[1], 290, 58, fill=GREY_L, stroke=LINE, r=10)
    s.label(m(1500, 0)[0] + 12, m(0, 94)[1] + 10, "complacência venosa **≈ 24×** a arterial\n(8× mais distensível × 3× o volume)",
            key="x24", size=11, valign="top")
    return s.svg()


# ---------------------------------------------------------------- pulso de pressão aórtico
def _onda(t):
    x = t % 0.8
    if x < 0.30:
        return 80 + 40 * math.sin(x / 0.3 * math.pi / 2) ** 1.5
    if x < 0.33:
        return 120 - (x - 0.3) / 0.03 * 12
    y = 80 + 32 * (math.exp(-(x - 0.33) / 0.25) - math.exp(-0.47 / 0.25) * (x - 0.33) / 0.47)
    if x < 0.36:
        y += 3 * math.sin((x - 0.33) / 0.03 * math.pi)
    return y


def pulso(hide=None):
    s = SVG(780, 340, hide)
    m = s.axes(70, 30, 520, 250, (0, 1.6), (70, 130), xticks=(0, 0.4, 0.8, 1.2, 1.6), yticks=(80, 96, 120),
               xlabel="tempo (s)", ylabel="mmHg", tick_fmt=lambda v: f"{v:g}".replace(".", ","), grid=False)
    for v, c, d in ((120, MUTE, "5 4"), (80, MUTE, "5 4"), (96, GREEN, "8 4")):
        s.line(*m(0, v), *m(1.6, v), stroke=c, sw=1.3 if c == GREEN else 1, dash=d)
    s.poly([m(t / 1000, _onda(t / 1000)) for t in range(0, 1600, 2)], stroke=RED, sw=3)
    x = m(0.66, 0)[0]
    s.arrow([(x, m(0, 80)[1] - 2), (x, m(0, 120)[1] + 2)], color=INK, sw=1.6, both=True)
    s.label(x - 8, m(0, 104)[1], "pressão de\npulso = 40", key="pp", size=11, weight=700, anchor="end", valign="middle", pill=PILL, pad=(3, 2))
    s.arrow([(m(0.5, 0)[0], m(0, 125)[1]), (m(0.345, 0)[0] + 3, m(0, 111)[1] - 3)], color=INK, sw=1.2)
    s.label(m(0.5, 0)[0], m(0, 125)[1] - 2, "incisura (fecha a valva aórtica)", key="incisura", size=11, weight=600)
    s.label(606, m(0, 120)[1], "sistólica 120", key="ps", size=12, weight=700, valign="middle")
    s.label(606, m(0, 80)[1], "diastólica 80", key="pd", size=12, weight=700, valign="middle")
    s.label(606, m(0, 96)[1], "PAM ≈ 96\n(60% PD + 40% PS)", key="pam", size=11.5, weight=700, fill=GREEN, valign="middle")
    return s.svg()


# ---------------------------------------------------------------- Korotkoff
def korotkoff(hide=None):
    s = SVG(780, 380, hide)
    m = s.axes(70, 30, 560, 250, (0, 8), (55, 160), xticks=(0, 2, 4, 6, 8), yticks=(60, 80, 100, 120, 140, 160),
               xlabel="tempo (s)", ylabel="mmHg", grid=False)
    art = lambda t: 80 + 40 * math.sin(math.pi * min(1, (t % 0.8) / 0.5)) ** 2
    cuff = lambda t: 145 - 9 * t
    t1, t2 = 25 / 9, 65 / 9
    # jato (onde arterial > manguito, entre sistólica e diastólica)
    ts = [i / 400 for i in range(0, 3201)]
    for i in range(len(ts) - 1):
        t = ts[i]
        if t1 <= t <= t2 and art(t) > cuff(t):
            s.line(*m(t, cuff(t)), *m(t, art(t)), stroke=RED, sw=1.6, opacity=0.25)
    s.poly([m(t, art(t)) for t in ts[::2]], stroke=RED, sw=2)
    s.poly([m(0, 145), m(8, 73)], stroke=INK, sw=2.6, smooth=False)
    for t in (t1, t2):
        s.line(m(t, 0)[0], 30, m(t, 0)[0], 280, stroke=MUTE, sw=1.1, dash="4 4")
    s.rect(m(t1, 0)[0], 332, m(t2, 0)[0] - m(t1, 0)[0], 8, fill=RED, r=4, opacity=0.8)
    s.text((m(t1, 0)[0] + m(t2, 0)[0]) / 2, 358, "sons audíveis", size=10.5, weight=700, fill=RED, anchor="middle")
    s.label(m(t1, 0)[0] + 6, 46, "1º som\n= sistólica (120)", key="sis", size=11, weight=700, valign="top", pill=PILL,
            pad=(3, 2))
    s.label(m(t2, 0)[0] - 6, 46, "abafa/some\n= diastólica (80)", key="dia", size=11, weight=700, anchor="end", valign="top",
            pill=PILL, pad=(3, 2))
    s.label(m(0.15, 0)[0], m(0, 150)[1] - 2, "pressão do manguito", key="cuff", size=11, weight=700, pill=PILL, pad=(3, 2))
    s.rect(646, 60, 126, 170, fill=RED_L, r=10)
    s.label(656, 72, "Sons de\nKorotkoff:\njato turbulento\npela artéria\nparcialmente\nocluída.", key="origem", size=10.5,
            valign="top")
    return s.svg()


# ---------------------------------------------------------------- gravidade
def gravidade(hide=None):
    s = SVG(560, 520, hide)
    skin, edge = "#f4e3d7", "#d4b5a2"
    s.circle(160, 58, 34, fill=skin, stroke=edge, sw=1.5)
    s.path("M118,100 C140,92 180,92 202,100 L214,280 L192,284 L186,300 L180,500 L146,500 L140,300 L134,284 L106,280 Z",
           stroke=edge, sw=1.5, fill=skin)
    s.path("M202,104 L236,120 L250,300 L228,302 L214,140", stroke=edge, sw=1.5, fill=skin)   # braço pendente
    # veias
    s.path("M160,40 L160,92 L162,190 C162,240 160,300 154,496", stroke=BLUE, sw=3.5)
    s.path("M164,108 C200,112 226,130 238,290", stroke=BLUE, sw=2.5)
    s.ellipse(168, 170, 16, 18, fill=RED)
    items = [("seio", 40, "seio sagital −10 mmHg", RED), ("pescoco", 100, "veias do pescoço 0 (colapsam)", MUTE),
             ("ad", 170, "átrio direito 0", INK), ("mao", 290, "veias da mão +35", BLUE),
             ("pe", 490, "pés +90 parado\n< +20 caminhando", BLUE)]
    for k, y, text, c in items:
        s.line(250 if k == "mao" else 200, y, 300, y, stroke=MUTE, sw=1)
        s.circle(300, y, 3, fill=MUTE)
        s.label(310, y, text, key=k, size=12, weight=700, fill=c, valign="middle")
    s.arrow([(460, 200), (460, 420)], color=BLUE, sw=2.5)
    s.text(470, 312, "+1 mmHg\na cada 13,6 mm\nabaixo do\ncoração", size=10, fill=MUTE, valign="middle")
    return s.svg()


FIGS = {"d_volumes": volumes, "d_pressoes": pressoes, "d_poiseuille": poiseuille, "d_fluxo": fluxo,
        "d_complacencia": complacencia, "d_pulso": pulso, "d_korotkoff": korotkoff, "d_gravidade": gravidade}

OCLUSOES = [
    ("d_volumes", "veias", "Que fração do sangue está nas veias sistêmicas?", "≈ <b>64%</b> (reservatório de volume)."),
    ("d_volumes", "pulm", "Que fração do sangue está na circulação pulmonar?", "≈ <b>9%</b>."),
    ("d_pressoes", "aorta", "Pressão na aorta (sistólica/diastólica/média)?", "<b>120/80</b>, média <b>100 mmHg</b>."),
    ("d_pressoes", "arteriola", "Onde ocorre a maior queda de pressão?", "Nas <b>arteríolas</b> (≈ 2/3 da resistência sistêmica)."),
    ("d_pressoes", "capilar", "Pressão capilar sistêmica?", "<b>35</b> (arterial) → <b>10</b> (venosa); média funcional ≈ <b>17 mmHg</b>."),
    ("d_pressoes", "ad", "Pressão no átrio direito?", "≈ <b>0 mmHg</b>."),
    ("d_pressoes", "ap", "Pressão na artéria pulmonar?", "<b>25/8</b>, média <b>16 mmHg</b>."),
    ("d_pressoes", "cp", "Pressão capilar pulmonar?", "≈ <b>7 mmHg</b>."),
    ("d_poiseuille", "f2", "Raio 2× maior: qual o fluxo?", "<b>16×</b> (2⁴)."),
    ("d_poiseuille", "f4", "Raio 4× maior: qual o fluxo?", "<b>256×</b> (4⁴)."),
    ("d_poiseuille", "lei", "Qual é a lei de Poiseuille?", "<b>F = π·ΔP·r⁴ / (8·η·ℓ)</b>."),
    ("d_poiseuille", "ohm", "Relação entre fluxo, pressão e resistência?", "<b>F = ΔP / R</b> (lei de Ohm)."),
    ("d_fluxo", "laminar", "Que tipo de fluxo e perfil de velocidade?", "<b>Laminar</b>, perfil <b>parabólico</b>."),
    ("d_fluxo", "re", "Acima de qual Reynolds há turbulência mesmo em vaso liso?", "Re &gt; <b>2.000</b> (200 a 400: turbulência nos ramos)."),
    ("d_complacencia", "art", "Volume e pressão do sistema arterial?", "<b>700 mℓ → 100 mmHg</b>; com 400 mℓ a pressão cai a 0."),
    ("d_complacencia", "ven", "Volume do sistema venoso?", "<b>2.000 a 3.500 mℓ</b>; centenas de mℓ mudam só 3 a 5 mmHg."),
    ("d_complacencia", "x24", "Complacência venosa × arterial?", "≈ <b>24×</b> (8× mais distensível × 3× o volume)."),
    ("d_pulso", "pp", "Como se chama SIS − DIA e quanto vale?", "<b>Pressão de pulso</b> ≈ <b>40 mmHg</b>."),
    ("d_pulso", "pam", "PAM e como estimá-la?", "≈ <b>60% diastólica + 40% sistólica</b> (≈ 96 com 120/80): fica mais perto da diastólica. Na clínica: PD + PP/3 ≈ 93."),
    ("d_pulso", "incisura", "O que causa esta marca?", "<b>Incisura</b>: fechamento da <b>valva aórtica</b>."),
    ("d_korotkoff", "sis", "O que marca o 1º som de Korotkoff?", "A <b>pressão sistólica</b>."),
    ("d_korotkoff", "dia", "O que marca o abafamento/desaparecimento?", "A <b>pressão diastólica</b>."),
    ("d_korotkoff", "origem", "Qual a origem dos sons de Korotkoff?", "<b>Jato turbulento</b> pela artéria parcialmente ocluída e vibração da parede."),
    ("d_gravidade", "pe", "Pressão venosa nos pés em pé?", "<b>+90 mmHg</b> parado; <b>&lt; +20</b> caminhando (bomba venosa)."),
    ("d_gravidade", "seio", "Pressão no seio sagital em pé?", "≈ <b>−10 mmHg</b> (risco de embolia gasosa)."),
    ("d_gravidade", "pescoco", "Pressão nas veias do pescoço em pé?", "<b>0</b>: colapsam pela pressão atmosférica."),
    ("d_gravidade", "mao", "Pressão nas veias da mão (braço pendente)?", "≈ <b>+35 mmHg</b> (+6 da 1ª costela + 29 gravitacional)."),
]

if __name__ == "__main__":
    print("ok", export("dia_d", FIGS, OCLUSOES))
