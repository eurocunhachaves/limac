"""Diagramas vetoriais do tema f (controle local, humoral e nervoso da circulação; Guyton caps. 17 e 18)."""
import math

from svgkit import (AMBER, AMBER_L, BLUE, BLUE_L, GREEN, GREEN_L, GREY_L, INK, LINE, MUTE, PURPLE, PURPLE_L, RED,
                    RED_L, SVG, TEAL, TEAL_L, export)

PILL = ("#ffffffe8", "none")


def _step(a, b, x):
    t = min(1, max(0, (x - a) / (b - a)))
    return t * t * (3 - 2 * t)


# ---------------------------------------------------------------- hiperemia reativa e ativa
def hiperemia(hide=None):
    s = SVG(860, 330, hide)
    for x0, title, key in ((70, "Hiperemia REATIVA", "reativa"), (500, "Hiperemia ATIVA", "ativa")):
        m = s.axes(x0, 60, 320, 190, (0, 10), (0, 7), yticks=(0, 1, 4, 7), grid=True,
                   ylabel="fluxo (× normal)" if x0 == 70 else "", xlabel="tempo")
        if x0 == 70:
            s.rect(m(2, 0)[0], 60, m(4, 0)[0] - m(2, 0)[0], 190, fill=GREY_L, r=0)
            s.text(m(3, 0)[0], 76, "artéria\nocluída", size=10.5, weight=700, fill=MUTE, anchor="middle")

            def f(t):
                if t < 2:
                    return 1
                if t < 4:
                    return 0
                return 1 + 4.5 * math.exp(-(t - 4) / 1.3) * _step(4, 4.15, t)
            s.poly([m(t / 50, f(t / 50)) for t in range(0, 501)], stroke=RED, sw=3)
            s.label(m(4.6, 0)[0], m(0, 6.2)[1], "fluxo ↑ 4 a 7×\npaga a \"dívida\" de O₂", key=key, size=11, weight=700,
                    fill=RED, pill=PILL, pad=(4, 2))
        else:
            s.rect(m(2, 0)[0], 60, m(7, 0)[0] - m(2, 0)[0], 190, fill=AMBER_L, r=0)
            s.text(m(4.5, 0)[0], 76, "metabolismo ↑ (exercício)", size=10.5, weight=700, fill=AMBER, anchor="middle")
            f = lambda t: 1 + 3.2 * _step(2, 3, t) * (1 - _step(7, 8.2, t))
            s.poly([m(t / 50, f(t / 50)) for t in range(0, 501)], stroke=GREEN, sw=3)
            s.label(m(2.4, 0)[0], m(0, 5.6)[1], "vasodilatadores locais\n→ fluxo ↑ (músculo até 20×)", key=key, size=11,
                    weight=700, fill=GREEN, pill=PILL, pad=(4, 2))
        s.text(x0, 34, title, size=13.5, weight=800)
    return s.svg()


# ---------------------------------------------------------------- autorregulação
def autorregulacao(hide=None):
    s = SVG(820, 390, hide)
    m = s.axes(80, 30, 500, 280, (0, 250), (0, 2.5), xticks=(0, 50, 100, 150, 200, 250), yticks=(0, 0.5, 1, 1.5, 2, 2.5),
               xlabel="pressão arterial (mmHg)", ylabel="fluxo (× normal)",
               tick_fmt=lambda v: f"{v:g}".replace(".", ","))
    s.rect(m(70, 0)[0], 30, m(175, 0)[0] - m(70, 0)[0], 280, fill=GREEN_L, r=0, opacity=0.7)
    s.poly([m(p, p / 100) for p in range(0, 251, 5)], stroke=MUTE, sw=1.4, dash="6 5")
    s.text(*m(212, 2.3), "sem autorregulação", size=10.5, fill=MUTE, anchor="end")

    def agudo(p):
        if p < 70:
            return 0.9 * p / 70
        if p < 175:
            return 0.9 + 0.25 * (p - 70) / 105
        return 1.15 + 0.012 * (p - 175) ** 1.25
    s.poly([m(p, min(2.5, agudo(p))) for p in range(0, 236, 3) if agudo(p) <= 2.55], stroke=RED, sw=3.2)

    def cronico(p):
        if p < 50:
            return p / 50
        if p < 200:
            return 1 + 0.08 * (p - 50) / 150
        return 1.08 + 0.02 * (p - 200)
    s.poly([m(p, cronico(p)) for p in range(0, 236, 3)], stroke=GREEN, sw=3, dash="8 5")
    s.label(m(122, 0)[0], m(0, 2.1)[1], "70 a 175 mmHg:\nfluxo varia só 20–30%", key="faixa", size=12, weight=800, fill=INK,
            anchor="middle", pill=PILL, pad=(4, 2))
    px = 600
    s.rect(px, 50, 210, 240, fill="#fff", stroke=LINE, r=12, shadow=True)
    s.line(px + 14, 76, px + 44, 76, stroke=RED, sw=3)
    s.label(px + 52, 70, "agudo (minutos)\nmetabólico + miogênico", key="agudo", size=10.5, weight=600, valign="top")
    s.line(px + 14, 132, px + 44, 132, stroke=GREEN, sw=3, dash="8 5")
    s.label(px + 52, 126, "longo prazo (semanas):\nquase plano de 50 a 200\n(muda a vascularização)", key="longo",
            size=10.5, weight=600, valign="top")
    s.text(px + 14, 214, "Cérebro e coração:\nautorregulação ainda\nmais precisa.", size=10.5, fill=MUTE)
    return s.svg()


# ---------------------------------------------------------------- endotélio: NO e endotelina
def endotelio(hide=None):
    s = SVG(880, 440, hide)
    s.rect(20, 20, 840, 60, fill=RED_L, r=10)
    s.text(40, 56, "LUZ: fluxo → tensão de cisalhamento; acetilcolina, bradicinina, angiotensina II", size=12, weight=600,
           fill=RED)
    s.rect(20, 92, 840, 110, fill="#f6e3d3", stroke="#d9b79c", r=12)
    s.text(40, 116, "CÉLULA ENDOTELIAL", size=11.5, weight=800, fill="#8a5a3b")
    s.rect(20, 214, 840, 206, fill="#eef3e9", stroke="#c3d3b6", r=12)
    s.text(40, 402, "MÚSCULO LISO VASCULAR", size=11.5, weight=800, fill=GREEN)
    # via do NO
    s.box(60, 128, 250, 60, title=None, body="arginina + O₂", color="#8a5a3b", size=12)
    s.arrow([(310, 158), (380, 158)], color=INK, sw=2)
    s.label(345, 146, "eNOS", key="enos", size=12, weight=800, fill=PURPLE, anchor="middle")
    s.circle(420, 158, 26, fill=PURPLE)
    s.text(420, 158, "NO", size=15, weight=800, fill="#fff", anchor="middle", valign="middle")
    s.text(460, 140, "gás lipofílico\nmeia-vida ≈ 6 s", size=10, fill=MUTE)
    s.arrow([(420, 186), (420, 250)], color=PURPLE, sw=2.6)
    s.box(330, 256, 180, 46, body="guanilato ciclase\nsolúvel", color=PURPLE, size=11.5, key="gc")
    s.arrow([(510, 280), (570, 280)], color=INK, sw=2)
    s.text(540, 270, "GTP →", size=10, fill=MUTE, anchor="middle")
    s.circle(610, 280, 30, fill=GREEN)
    s.label(610, 280, "GMPc", key="gmpc", size=12.5, weight=800, fill="#fff", anchor="middle", valign="middle")
    s.arrow([(640, 280), (700, 280)], color=INK, sw=2)
    s.box(700, 252, 140, 56, title="PKG", body="relaxamento", color=GREEN, size=11.5)
    # PDE-5
    s.arrow([(610, 312), (610, 356)], color=RED, sw=2)
    s.label(560, 380, "PDE-5 degrada o GMPc\n(sildenafila bloqueia)", key="pde5", size=11, weight=700, fill=RED, anchor="middle",
            valign="top")
    s.label(90, 250, "nitratos (nitroglicerina)\nliberam NO → angina", key="nitrato", size=11, weight=700, fill=PURPLE,
            valign="top")
    s.arrow([(250, 262), (326, 272)], color=PURPLE, sw=1.4, dash="4 3")
    # endotelina
    s.box(640, 116, 200, 72, title="Endotelina", body="endotélio lesado →\nvasoconstrição potente", color=RED, size=11,
          key="endotelina")
    s.text(640, 228, "hemostasia em artérias até 5 mm", size=10, fill=MUTE)
    return s.svg()


# ---------------------------------------------------------------- remodelagem vascular
def remodelagem(hide=None):
    s = SVG(900, 300, hide)
    items = [("Normal", "", 40, 22, None, INK),
             ("Eutrófica\nconcêntrica", "↑ pressão (pequenas\nartérias e arteríolas)", 28, 30, "eut_conc", BLUE),
             ("Hipertrófica", "↑ pressão (grandes\nartérias): parede\nmais grossa e rígida", 40, 34, "hipert", RED),
             ("Eutrófica\nexcêntrica", "↑ fluxo (fístula AV,\nartéria radial)", 54, 22, "eut_exc", GREEN),
             ("Hipertrófica\nexcêntrica", "↑ pressão + ↑ fluxo\n(veia da fístula,\nponte de safena)", 54, 32, "hip_exc",
              PURPLE)]
    for i, (name, cause, rl, w, k, c) in enumerate(items):
        cx, cy = 90 + i * 180, 120
        s.circle(cx, cy, rl + w, fill="#f3c9cf" if k else "#f6d9dd", stroke=c, sw=2)
        s.circle(cx, cy, rl, fill=RED_L, stroke="#e3a6af", sw=1.2)
        s.label(cx, 228, name, key=k, size=12, weight=800, fill=c, anchor="middle", valign="top")
        s.text(cx, 266, cause, size=10, fill=MUTE, anchor="middle")
    s.text(450, 18, "Laplace: T = P × r · mais pressão → mais parede; mais fluxo (cisalhamento) → mais luz", size=11,
           fill=INK, anchor="middle", weight=600)
    return s.svg()


# ---------------------------------------------------------------- centro vasomotor
def centro_vasomotor(hide=None):
    s = SVG(900, 480, hide)
    # tronco encefálico estilizado
    s.path("M170,40 C150,120 150,220 170,300 L230,300 C250,220 250,120 230,40 Z", stroke="#c9b8a6", sw=2, fill="#f6efe7")
    s.text(200, 30, "tronco encefálico", size=10.5, fill=MUTE, anchor="middle")
    s.rect(160, 318, 80, 150, fill="#f6efe7", stroke="#c9b8a6", r=10, sw=2)
    s.text(200, 462, "medula", size=10, fill=MUTE, anchor="middle")
    # áreas (a via descendente vem antes, por baixo)
    s.path("M200,110 L200,470", stroke=RED, sw=3)
    s.ellipse(200, 110, 34, 18, fill=RED)
    s.ellipse(200, 170, 34, 16, fill=BLUE)
    s.ellipse(236, 220, 30, 16, fill=AMBER)
    s.ellipse(168, 244, 24, 14, fill=GREEN)
    s.label(40, 104, "área vasoconstritora\n(bulbo anterolateral\nsuperior) · tônus\n0,5–2 impulsos/s", key="vc", size=10.5,
            weight=700, fill=RED, valign="top")
    s.line(150, 110, 166, 110, stroke=RED, sw=1)
    s.label(40, 180, "área vasodilatadora\n(inibe a constritora)", key="vd", size=10.5, weight=700, fill=BLUE, valign="top")
    s.arrow([(222, 156), (222, 126)], color=BLUE, sw=2.2, dash="3 3")
    s.label(40, 214, "núcleo do trato\nsolitário (NTS)", key="nts", size=10.5, weight=700, fill=AMBER, valign="top")
    s.label(40, 262, "núcleo motor dorsal\ndo vago", key="vago", size=10.5, weight=700, fill=GREEN, valign="top")
    # aferências
    s.arrow([(560, 330), (420, 300), (266, 224)], color=AMBER, sw=2.2, curve=True)
    s.arrow([(560, 250), (420, 240), (268, 216)], color=AMBER, sw=2.2, curve=True)
    s.label(566, 316, "seio carotídeo → nervo de Hering\n→ glossofaríngeo (IX)", key="hering", size=11, weight=700,
            fill=AMBER, valign="top")
    s.label(566, 236, "arco aórtico → vago (X)", key="aortico", size=11, weight=700, fill=AMBER, valign="top")
    # eferências
    s.arrow([(240, 400), (560, 420)], color=RED, sw=2.6)
    s.text(566, 412, "simpático (NA, α1): arteríolas e veias contraem;\ncoração: FC e força ↑; adrenal", size=11,
           fill=RED, weight=600)
    s.arrow([(190, 250), (120, 330), (120, 400)], color=GREEN, sw=2.4, curve=True)
    s.text(40, 420, "vago (ACh):\nFC ↓", size=11, fill=GREEN, weight=700)
    # centros superiores
    s.rect(420, 40, 440, 84, fill=GREY_L, r=12)
    s.text(436, 64, "Centros superiores", size=12, weight=800)
    s.text(436, 84, "hipotálamo (posterolateral excita; anterior: vasodilatador\nmuscular), córtex motor, sistema límbico",
           size=10.5, fill=INK)
    s.arrow([(420, 90), (240, 104)], color=MUTE, sw=1.6, dash="4 4")
    return s.svg()


# ---------------------------------------------------------------- barorreflexo
def barorreceptor(hide=None):
    s = SVG(900, 380, hide)
    m = s.axes(70, 30, 360, 250, (0, 260), (0, 1.1), xticks=(0, 60, 100, 180, 260), yticks=(),
               xlabel="pressão arterial (mmHg)", ylabel="impulsos no nervo de Hering")
    f = lambda p: 0 if p < 55 else 1 / (1 + math.exp(-(p - 115) / 20)) * _step(55, 70, p)
    s.poly([m(p, f(p)) for p in range(0, 261, 2)], stroke=AMBER, sw=3.2)
    s.label(*m(8, 0.14), "0 a 50–60:\nsem disparo", key="limiar", size=10.5, weight=700, fill=MUTE)
    s.label(m(180, 0)[0], m(0, 1.06)[1], "máximo ≈ 180", key="max", size=10.5, weight=700, fill=AMBER, anchor="middle")
    s.circle(*m(100, f(100)), 6, fill=RED, stroke="#fff", sw=2)
    s.label(m(104, 0)[0], m(0, 0.28)[1], "maior ganho em ≈ 100\n(faixa normal)", key="ganho", size=10.5, weight=700,
            fill=RED, pill=PILL, pad=(3, 2))
    # alça do reflexo
    x0 = 470
    steps = [(RED, "↑ PA"), (AMBER, "estira seio carotídeo\ne arco aórtico"), (AMBER, "↑ disparo → NTS"),
             (BLUE, "inibe a área vasoconstritora\nexcita o vago"), (GREEN, "vasodilatação (arteríolas e veias)\n"
                                                                   "↓ FC e ↓ contratilidade"), (RED, "↓ PA de volta ao normal")]
    y = 30
    for i, (c, t) in enumerate(steps):
        h = 34 if "\n" not in t else 48
        s.rect(x0, y, 400, h, fill="#fff", stroke=c, r=10, sw=1.5)
        s.text(x0 + 200, y + h / 2, t, size=11, weight=700, fill=c, anchor="middle", valign="middle")
        if i < len(steps) - 1:
            s.arrow([(x0 + 200, y + h + 1), (x0 + 200, y + h + 13)], color=MUTE, sw=1.6)
        y += h + 14
    s.label(x0, 360, "Reajusta ao novo nível em 1 a 2 dias: controle rápido, não crônico.", key="reset", size=11,
            weight=700, fill=INK)
    return s.svg()


# ---------------------------------------------------------------- faixas de atuação dos mecanismos nervosos
def faixas(hide=None):
    s = SVG(860, 330, hide)
    m = s.axes(220, 40, 560, 220, (0, 200), (0, 4), xticks=(0, 20, 40, 60, 80, 100, 120, 160, 200), yticks=(),
               xlabel="pressão arterial média (mmHg)", grid=False)
    rows = [("Barorreceptores", 60, 180, 100, AMBER, AMBER_L, "baro", "60 a 180 (pico ≈ 100)"),
            ("Quimiorreceptores", 40, 80, 60, BLUE, BLUE_L, "quimio", "importantes abaixo de 80"),
            ("Resposta isquêmica\ndo SNC", 15, 60, 20, RED, RED_L, "isq", "abaixo de 60 · máximo 15 a 20")]
    for i, (name, a, b, peak, c, cl, k, txt) in enumerate(rows):
        y = 58 + i * 66
        s.text(210, y + 18, name, size=12, weight=700, anchor="end", valign="middle")
        s.rect(m(a, 0)[0], y, m(b, 0)[0] - m(a, 0)[0], 36, fill=cl, stroke=c, r=10, sw=1.4)
        s.circle(m(peak, 0)[0], y + 18, 7, fill=c, stroke="#fff", sw=2)
        s.label(m(b, 0)[0] + 10, y + 23, txt, key=k, size=10.5, weight=700, fill=c)
    s.text(220, 20, "Qual reflexo manda em cada faixa de pressão", size=13, weight=800)
    return s.svg()


# ---------------------------------------------------------------- receptores de baixa pressão
def baixa_pressao(hide=None):
    s = SVG(820, 320, hide)
    m = s.axes(90, 40, 300, 220, (0, 3), (0, 110), xticks=(), yticks=(0, 25, 50, 75, 100), ylabel="↑ PA (mmHg)")
    bars = [("todos\nintactos", 15, GREEN, "b15"), ("sem\nbarorreceptores", 40, AMBER, "b40"),
            ("sem baro e sem\nbaixa pressão", 100, RED, "b100")]
    for i, (n, v, c, k) in enumerate(bars):
        x = m(i + 0.2, 0)[0]
        w = m(0.6, 0)[0] - m(0, 0)[0]
        s.rect(x, m(0, v)[1], w, m(0, 0)[1] - m(0, v)[1], fill=c, r=6)
        s.label(x + w / 2, m(0, v)[1] - 8, f"+{v}", key=k, size=13, weight=800, fill=c, anchor="middle")
        s.text(x + w / 2, 280, n, size=10, fill=INK, anchor="middle", weight=600)
    s.text(90, 24, "Infusão rápida de 300 mℓ de sangue (cão)", size=12, weight=800)
    px = 430
    s.rect(px, 40, 380, 240, fill=BLUE_L, r=12)
    s.text(px + 16, 66, "Reflexo de volume (átrios estirados)", size=12, weight=800, fill=BLUE)
    s.label(px + 16, 80, "• ↓ simpático renal → dilata a aferente,\n  ↑ filtração, ↓ reabsorção\n• ↓ ADH (hipotálamo)\n"
            "• ↑ peptídeo natriurético atrial\n→ rim elimina o excesso de volume", key="volume", size=11, valign="top")
    s.text(px + 16, 200, "Reflexo de Bainbridge", size=12, weight=800, fill=RED)
    s.label(px + 16, 212, "átrio estirado → FC ↑ 40 a 60% (vago\naferente) + 15% por estirar o nó sinusal",
            key="bainbridge", size=11, valign="top")
    return s.svg()


FIGS = {"f_hiperemia": hiperemia, "f_autorregulacao": autorregulacao, "f_endotelio": endotelio,
        "f_remodelagem": remodelagem, "f_centro_vasomotor": centro_vasomotor, "f_barorreceptor": barorreceptor,
        "f_faixas": faixas, "f_baixa_pressao": baixa_pressao}

OCLUSOES = [
    ("f_hiperemia", "reativa", "O que acontece com o fluxo quando se libera uma artéria ocluída?", "<b>Hiperemia reativa</b>: fluxo ↑ 4 a 7×, que compensa o déficit de O₂."),
    ("f_hiperemia", "ativa", "O que acontece com o fluxo quando o metabolismo do tecido sobe?", "<b>Hiperemia ativa</b>: vasodilatadores locais ↑ o fluxo (músculo até 20×)."),
    ("f_autorregulacao", "faixa", "Faixa de autorregulação aguda e quanto o fluxo varia nela?", "<b>70 a 175 mmHg</b>; fluxo varia só <b>20 a 30%</b>."),
    ("f_autorregulacao", "agudo", "Quais as duas teorias da autorregulação aguda?", "<b>Metabólica</b> (excesso de O₂ lava vasodilatadores) e <b>miogênica</b> (estiramento → contração)."),
    ("f_autorregulacao", "longo", "Como fica o fluxo após semanas de pressão alterada?", "Quase normal entre <b>50 e 200 mmHg</b>, por mudança da vascularização."),
    ("f_endotelio", "enos", "Enzima que produz NO no endotélio?", "<b>eNOS</b> (óxido nítrico sintase endotelial), a partir de arginina e O₂."),
    ("f_endotelio", "gc", "Alvo do NO no músculo liso?", "<b>Guanilato ciclase solúvel</b> → GMPc → PKG → relaxamento."),
    ("f_endotelio", "pde5", "Enzima que degrada o GMPc e fármaco que a bloqueia?", "<b>PDE-5</b>; <b>sildenafila</b> (disfunção erétil)."),
    ("f_endotelio", "endotelina", "Vasoconstritor potente liberado pelo endotélio lesado?", "<b>Endotelina</b> (peptídeo de 27 aminoácidos)."),
    ("f_endotelio", "nitrato", "Como a nitroglicerina alivia a angina?", "Libera <b>NO</b>: vasodilatação sistêmica e coronariana."),
    ("f_remodelagem", "eut_conc", "Remodelagem de pequenas artérias à pressão alta?", "<b>Eutrófica concêntrica</b>: luz menor, parede mais grossa, mesma área de parede."),
    ("f_remodelagem", "hipert", "Remodelagem das grandes artérias à pressão alta?", "<b>Hipertrófica</b>: ↑ área da parede e rigidez."),
    ("f_remodelagem", "eut_exc", "Remodelagem da artéria radial numa fístula AV (↑ fluxo)?", "<b>Eutrófica excêntrica</b>: ↑ luz, parede quase igual."),
    ("f_centro_vasomotor", "vc", "Onde fica a área vasoconstritora e qual a frequência do tônus?", "<b>Bulbo anterolateral superior</b>; <b>0,5 a 2 impulsos/s</b>."),
    ("f_centro_vasomotor", "nts", "Área que recebe as aferências dos barorreceptores?", "<b>Núcleo do trato solitário</b> (área sensorial)."),
    ("f_centro_vasomotor", "hering", "Via dos barorreceptores carotídeos?", "Nervo de <b>Hering</b> → <b>glossofaríngeo (IX)</b> → NTS."),
    ("f_centro_vasomotor", "aortico", "Via dos barorreceptores aórticos?", "Nervo <b>vago (X)</b> → NTS."),
    ("f_barorreceptor", "limiar", "Abaixo de que pressão o seio carotídeo não dispara?", "<b>50 a 60 mmHg</b>."),
    ("f_barorreceptor", "max", "Em que pressão o disparo é máximo?", "≈ <b>180 mmHg</b>."),
    ("f_barorreceptor", "ganho", "Onde o barorreflexo tem maior ganho?", "Perto de <b>100 mmHg</b>, a faixa normal."),
    ("f_barorreceptor", "reset", "Por que os barorreceptores não controlam a PA a longo prazo?", "<b>Reajustam</b> ao novo nível em <b>1 a 2 dias</b>."),
    ("f_faixas", "quimio", "Abaixo de que PA os quimiorreceptores ficam importantes?", "<b>&lt; 80 mmHg</b>."),
    ("f_faixas", "isq", "Quando a resposta isquêmica do SNC atua?", "PA <b>&lt; 60 mmHg</b>; máxima em <b>15 a 20 mmHg</b> (último recurso)."),
    ("f_baixa_pressao", "b40", "Infusão de 300 mℓ sem barorreceptores arteriais: quanto sobe a PA?", "≈ <b>40 mmHg</b> (15 com tudo intacto; 100 sem os de baixa pressão)."),
    ("f_baixa_pressao", "bainbridge", "O que é o reflexo de Bainbridge?", "Átrio estirado → <b>FC ↑ 40 a 60%</b> (aferência vagal)."),
    ("f_baixa_pressao", "volume", "Efeitos do reflexo de volume (estiramento atrial)?", "↓ simpático renal, ↓ ADH, ↑ PNA → rim elimina volume."),
]

if __name__ == "__main__":
    print("ok", export("dia_f", FIGS, OCLUSOES))
