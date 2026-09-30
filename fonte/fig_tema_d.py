"""Figuras esquemáticas do tema d (biofísica da circulação; Guyton caps. 14 e 15), com versões de oclusão para o Anki."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, FancyBboxPatch, Rectangle

from fig_tema_a import BLUE, GREEN, GREY, RED, lab, save

ORANGE = "#e8590c"


def pressoes(hide=None):
    """Pressão média (e pulsátil) ao longo das circulações sistêmica e pulmonar."""
    fig, ax = plt.subplots(figsize=(7.4, 3.4), dpi=200)
    segs = ["Aorta", "Grandes\nartérias", "Pequenas\nartérias", "Arteríolas", "Capilares", "Vênulas", "Veias",
            "Veias\ncavas", "|", "Artéria\npulmonar", "Capilar\npulm.", "Veias\npulm."]
    x = np.arange(len(segs))
    media = [100, 97, 90, 60, 17, 12, 8, 0, None, 16, 7, 4]
    sis, dia = [120, 120, 110, 70], [80, 78, 75, 50]
    for i in range(4):
        ax.fill_between([i - 0.4, i + 0.4], dia[i], sis[i], color=RED, alpha=0.15, lw=0)
    ax.fill_between([8.6, 9.4], 8, 25, color=BLUE, alpha=0.15, lw=0)
    ax.plot(x[:8], media[:8], "-o", color=RED, lw=2, ms=4)
    ax.plot(x[9:], media[9:], "-o", color=BLUE, lw=2, ms=4)
    ax.axvline(8, color=GREY, lw=0.6, ls=":")
    lab(ax, "aorta", hide, 0.05, 124, "120/80\nmédia 100", fontsize=7, ha="center", color=RED)
    lab(ax, "arteriola", hide, 3.35, 70, "maior queda:\narteríolas", fontsize=7, ha="left", color=RED)
    lab(ax, "capilar", hide, 4.2, 30, "35 → 10\n(média 17)", fontsize=7, ha="left")
    lab(ax, "ad", hide, 6.9, 10, "átrio D ≈ 0", fontsize=7, ha="center")
    lab(ax, "ap", hide, 9, 30, "25/8\nmédia 16", fontsize=7, ha="center", color=BLUE)
    lab(ax, "cp", hide, 10, 12, "≈ 7", fontsize=7, ha="center", color=BLUE)
    ax.text(3.5, -30, "SISTÊMICA", ha="center", fontsize=7.5, color=RED, fontweight="bold")
    ax.text(10, -30, "PULMONAR", ha="center", fontsize=7.5, color=BLUE, fontweight="bold")
    ax.set_xticks([i for i in x if segs[i] != "|"])
    ax.set_xticklabels([s for s in segs if s != "|"], fontsize=6.3)
    ax.set_ylim(-5, 140); ax.set_ylabel("pressão (mmHg)")
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    save(fig, "d_pressoes", hide)


def poiseuille(hide=None):
    fig, ax = plt.subplots(figsize=(6.6, 3.3), dpi=200)
    ax.set_xlim(0, 10); ax.set_ylim(0, 6.2); ax.axis("off")
    for (r, f, y, k) in [(1, 1, 5.2, "f1"), (2, 16, 3.9, "f2"), (4, 256, 2.2, "f4")]:
        h = 0.14 * r
        ax.add_patch(Rectangle((1.2, y - h), 5.2, 2 * h, fc="#f6c9cf", ec=RED, lw=1))
        ax.text(0.9, y, f"r = {r}", ha="right", va="center", fontsize=8)
        ax.annotate("", (7.2, y), (6.5, y), arrowprops=dict(arrowstyle="-|>", color=RED, lw=0.6 + r * 0.6))
        lab(ax, k, hide, 7.4, y, f"{f} mℓ/min", va="center", fontsize=8.5, fontweight="bold")
    ax.text(3.8, 6.0, "mesma ΔP = 100 mmHg", ha="center", fontsize=7.5, color=GREY)
    lab(ax, "lei", hide, 0.3, 0.55, "Lei de Poiseuille:  F = π·ΔP·r⁴ / (8·η·ℓ)", fontsize=9,
        bbox=dict(fc="#fbeaec", ec=RED, lw=0.6))
    lab(ax, "ohm", hide, 6.2, 0.55, "Lei de Ohm:  F = ΔP / R", fontsize=9, bbox=dict(fc="#e8f0fb", ec=BLUE, lw=0.6))
    fig.tight_layout()
    save(fig, "d_poiseuille", hide)


def fluxo(hide=None):
    fig, axs = plt.subplots(1, 2, figsize=(6.6, 2.6), dpi=200)
    ax = axs[0]
    ax.set_xlim(0, 6); ax.set_ylim(-1.3, 1.5); ax.axis("off")
    ax.plot([0, 6], [1, 1], color="#444", lw=2); ax.plot([0, 6], [-1, -1], color="#444", lw=2)
    for yy in np.linspace(-0.85, 0.85, 9):
        L = 3.2 * (1 - yy ** 2) + 0.2
        ax.annotate("", (1 + L, yy), (1, yy), arrowprops=dict(arrowstyle="-|>", color=RED, lw=0.8))
    lab(ax, "laminar", hide, 3, 1.2, "LAMINAR: perfil parabólico", ha="center", fontsize=7.5, fontweight="bold")
    lab(ax, "centro", hide, 3, -1.25, "centro rápido, parede ≈ 0", ha="center", fontsize=7, color=GREY)
    ax = axs[1]
    ax.set_xlim(0, 6); ax.set_ylim(-1.3, 1.5); ax.axis("off")
    ax.plot([0, 2], [1, 1], color="#444", lw=2); ax.plot([0, 2], [-1, -1], color="#444", lw=2)
    ax.plot([2, 2.6, 6], [1, 0.45, 0.45 + 0], color="#444", lw=2); ax.plot([2, 2.6, 6], [-1, -0.45, -0.45], color="#444", lw=2)
    rng = np.random.default_rng(3)
    for k in range(7):
        cx, cy = 3.0 + rng.random() * 2.6, rng.uniform(-0.3, 0.3)
        th = np.linspace(0, 2 * np.pi * 1.2, 60)
        rr = np.linspace(0.02, 0.18, 60)
        ax.plot(cx + rr * np.cos(th), cy + rr * np.sin(th), color=BLUE, lw=0.8)
    lab(ax, "turb", hide, 3, 1.2, "TURBULENTO: redemoinhos", ha="center", fontsize=7.5, fontweight="bold")
    lab(ax, "re", hide, 3, -1.25, "Re > 2.000 → turbulência", ha="center", fontsize=7, color=GREY)
    fig.tight_layout()
    save(fig, "d_fluxo", hide)


def complacencia(hide=None):
    fig, ax = plt.subplots(figsize=(5.8, 3.3), dpi=200)
    v = np.linspace(400, 900, 50)
    ax.plot(v, (v - 400) / 3, color=RED, lw=2.2)
    vv = np.linspace(1500, 3500, 50)
    ax.plot(vv, np.clip((vv - 1800) / 170, 0, None), color=BLUE, lw=2.2)
    ax.plot(700, 100, "o", color=RED); ax.plot(2500, 4.1, "o", color=BLUE)
    lab(ax, "art", hide, 760, 110, "arterial: 700 mℓ → 100 mmHg\n(400 mℓ → 0)", fontsize=7, color=RED)
    lab(ax, "ven", hide, 1900, 26, "venoso: 2.000–3.500 mℓ\ncentenas de mℓ mudam só 3–5 mmHg", fontsize=7, color=BLUE)
    lab(ax, "x24", hide, 1400, 62, "complacência venosa ≈ 24× a arterial\n(8× mais distensível × 3× o volume)", fontsize=7.2,
        bbox=dict(fc="#f3f3f3", ec=GREY, lw=0.5))
    ax.set_xlabel("volume (mℓ)"); ax.set_ylabel("pressão (mmHg)")
    ax.set_xlim(0, 3600); ax.set_ylim(0, 150)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    save(fig, "d_complacencia", hide)


def pulso(hide=None):
    fig, ax = plt.subplots(figsize=(6.4, 3.1), dpi=200)
    t = np.linspace(0, 1.6, 1600)

    def onda(tt):
        x = tt % 0.8
        up = 80 + 40 * np.sin(np.clip(x / 0.3, 0, 1) * np.pi / 2) ** 1.5
        dec = 80 + 32 * (np.exp(-(x - 0.33) / 0.25) - np.exp(-0.47 / 0.25) * (x - 0.33) / 0.47)
        y = np.where(x < 0.3, up, np.where(x < 0.33, 120 - (x - 0.3) / 0.03 * 12, dec))
        y = np.where((x > 0.33) & (x < 0.36), y + 3 * np.sin((x - 0.33) / 0.03 * np.pi), y)
        return y
    y = onda(t)
    ax.plot(t, y, color=RED, lw=2)
    ax.axhline(120, color=GREY, lw=0.5, ls="--"); ax.axhline(80, color=GREY, lw=0.5, ls="--")
    ax.axhline(96, color=GREEN, lw=1, ls="-.")
    lab(ax, "ps", hide, 1.62, 120, "sistólica 120", va="center", fontsize=7.5)
    lab(ax, "pd", hide, 1.62, 80, "diastólica 80", va="center", fontsize=7.5)
    lab(ax, "pam", hide, 1.62, 96, "PAM ≈ 96\n(60% PD + 40% PS)", va="center", fontsize=7, color=GREEN)
    ax.annotate("", (0.72, 120), (0.72, 80), arrowprops=dict(arrowstyle="<->", lw=0.8))
    lab(ax, "pp", hide, 0.74, 106, "pressão de\npulso = 40", fontsize=7, va="center")
    ax.annotate("", (0.34, 110), (0.5, 122), arrowprops=dict(arrowstyle="->", lw=0.6))
    lab(ax, "incisura", hide, 0.47, 124, "incisura (fecha a valva aórtica)", fontsize=7)
    ax.set_xlim(0, 1.6); ax.set_ylim(70, 132)
    ax.set_xlabel("tempo (s)"); ax.set_ylabel("mmHg")
    ax.spines[["top", "right"]].set_visible(False)
    fig.subplots_adjust(right=0.74, bottom=0.16, left=0.1)
    save(fig, "d_pulso", hide)


def korotkoff(hide=None):
    fig, ax = plt.subplots(figsize=(6.4, 3.2), dpi=200)
    t = np.linspace(0, 8, 4000)
    x = t % 0.8
    art = 80 + 40 * np.sin(np.pi * np.clip(x / 0.5, 0, 1)) ** 2
    cuff = 145 - 9 * t
    ax.plot(t, art, color=RED, lw=1.4)
    ax.plot(t, cuff, color="#333", lw=1.4)
    ax.fill_between(t, cuff, art, where=art > cuff, color=RED, alpha=0.25)
    ax.axvline((145 - 120) / 9, color=GREY, ls=":", lw=0.8); ax.axvline((145 - 80) / 9, color=GREY, ls=":", lw=0.8)
    lab(ax, "sis", hide, (145 - 120) / 9 + 0.05, 135, "1º som\n= sistólica", fontsize=7)
    lab(ax, "dia", hide, (145 - 80) / 9 + 0.05, 128, "abafa/some\n= diastólica", fontsize=7)
    lab(ax, "cuff", hide, 0.1, 150, "pressão do manguito", fontsize=7)
    lab(ax, "origem", hide, 3.2, 62, "sons de Korotkoff: jato turbulento pela artéria\nparcialmente ocluída", fontsize=7,
        bbox=dict(fc="#fbeaec", ec=RED, lw=0.5))
    ax.set_ylim(55, 160); ax.set_xlim(0, 8)
    ax.set_xlabel("tempo (s)"); ax.set_ylabel("mmHg")
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    save(fig, "d_korotkoff", hide)


def gravidade(hide=None):
    fig, ax = plt.subplots(figsize=(4.4, 4.6), dpi=200)
    ax.set_xlim(0, 10); ax.set_ylim(-0.5, 10.5); ax.axis("off")
    # silhueta simplificada
    ax.add_patch(Ellipse((3, 9.5), 1.1, 1.3, fc="#f3dccf", ec="#b98d7a"))
    ax.add_patch(FancyBboxPatch((2.2, 4.8), 1.6, 3.9, boxstyle="round,pad=0.1", fc="#f3dccf", ec="#b98d7a"))
    for dx in (-0.4, 0.4):
        ax.add_patch(Rectangle((3 + dx - 0.3, 0.2), 0.6, 4.6, fc="#f3dccf", ec="#b98d7a"))
    ax.add_patch(Rectangle((3.8, 5.6), 0.45, 2.9, fc="#f3dccf", ec="#b98d7a", angle=0))
    ax.plot([3, 3, 2.8, 2.8], [9.2, 5.0, 4.8, 0.4], color=BLUE, lw=2)
    ax.add_patch(Ellipse((3.2, 7.3), 0.6, 0.7, fc=RED, ec="none"))
    items = [("seio", 9.7, "seio sagital −10 mmHg"), ("pescoco", 8.6, "veias do pescoço 0 (colapsadas)"),
             ("ad", 7.3, "átrio direito 0"), ("mao", 5.6, "veias da mão +35"),
             ("pe", 0.4, "pés +90 (parado)\n< +20 caminhando")]
    for k, y, text in items:
        ax.plot([3.5, 5.2], [y, y], color=GREY, lw=0.5)
        lab(ax, k, hide, 5.3, y, text, va="center", fontsize=7.3)
    ax.text(5.3, 3.0, "+1 mmHg a cada 13,6 mm\nabaixo do coração", fontsize=6.6, color=GREY)
    fig.tight_layout()
    save(fig, "d_gravidade", hide)


FIGS = {"d_pressoes": pressoes, "d_poiseuille": poiseuille, "d_fluxo": fluxo, "d_complacencia": complacencia,
        "d_pulso": pulso, "d_korotkoff": korotkoff, "d_gravidade": gravidade}

OCLUSOES = [
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
    for f in FIGS.values():
        f()
    for name, key, _, _ in OCLUSOES:
        FIGS[name](hide=key)
    print("ok", len(OCLUSOES))
