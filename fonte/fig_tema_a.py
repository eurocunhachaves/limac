"""Figuras esquemáticas do tema a (valores aproximados do Guyton, cap. 9)."""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "fig")
os.makedirs(FIG, exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9})
RED, BLUE, GREEN, GREY = "#9b1c2c", "#2a5ca8", "#2e7d32", "#777777"


def smooth(x, xp, fp):
    return np.interp(x, xp, fp)


def potencial_acao():
    t = np.linspace(-50, 400, 2000)
    xp = [-50, 0, 2, 8, 20, 40, 180, 230, 280, 300, 400]
    fp = [-85, -85, 20, 5, 2, 0, -8, -30, -80, -85, -85]
    v = smooth(t, xp, fp)
    fig, ax = plt.subplots(figsize=(6.2, 2.9), dpi=200)
    ax.plot(t, v, color=RED, lw=2)
    for x, y, lab in [(-5, -40, "0"), (12, 14, "1"), (110, 6, "2 (platô)"), (262, -45, "3"), (340, -78, "4")]:
        ax.annotate(lab, (x, y), fontsize=10, fontweight="bold")
    ax.text(398, 42, "Fase 0: entra Na⁺ (canais rápidos)\nFase 1: canais de Na⁺ fecham, sai K⁺ (transitório)\n"
            "Fase 2: entra Ca²⁺ (canais L) e ↓ saída de K⁺\nFase 3: canais de Ca²⁺ fecham, sai K⁺\n"
            "Fase 4: repouso ≈ −85 mV", fontsize=7.2, va="top", ha="right",
            bbox=dict(fc="white", ec=GREY, lw=0.5), transform=ax.transData)
    ax.axvspan(0, 270, ymin=0.02, ymax=0.06, color=GREY, alpha=0.5)
    ax.text(135, -104, "período refratário absoluto (≈ 0,25–0,30 s)", ha="center", fontsize=7)
    ax.set_xlim(-50, 400); ax.set_ylim(-110, 45)
    ax.set_xticks([0, 100, 200, 300]); ax.set_xticklabels(["0", "0,1", "0,2", "0,3"])
    ax.set_xlabel("tempo (s)"); ax.set_ylabel("mV")
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, "a_potencial_acao.png")); plt.close(fig)


def wiggers():
    t = np.linspace(0, 0.8, 1600)
    # tempos (s): sístole atrial 0-0.1; contração isovolumétrica 0.10-0.15; ejeção 0.15-0.40;
    # relaxamento isovolumétrico 0.40-0.47; enchimento 0.47-0.8
    ao = smooth(t, [0, .15, .25, .38, .40, .41, .8], [82, 80, 120, 105, 100, 103, 82])
    lv = smooth(t, [0, .05, .1, .15, .25, .38, .40, .47, .5, .8], [4, 6, 8, 80, 121, 104, 90, 5, 2, 4])
    la = smooth(t, [0, .05, .1, .13, .16, .2, .38, .47, .55, .8], [4, 8, 5, 7, 3, 4, 10, 6, 3, 4])
    vol = smooth(t, [0, .1, .15, .22, .40, .47, .58, .72, .8], [110, 120, 120, 80, 50, 50, 95, 105, 110])
    fig, axs = plt.subplots(3, 1, figsize=(6.4, 6.3), dpi=200, sharex=True,
                            gridspec_kw={"height_ratios": [3, 1.6, 1.1]})
    ax = axs[0]
    ax.plot(t, ao, color=RED, lw=1.8, label="aorta")
    ax.plot(t, lv, color=BLUE, lw=1.8, label="ventrículo esquerdo")
    ax.plot(t, la, color=GREEN, lw=1.8, label="átrio esquerdo")
    ax.annotate("incisura", (0.405, 101), (0.46, 118), fontsize=7, arrowprops=dict(arrowstyle="->", lw=0.6))
    for x, lab in [(0.03, "a"), (0.125, "c"), (0.36, "v")]:
        ax.text(x, 15, lab, color=GREEN, fontweight="bold")
    events = [(0.15, "abre\naórtica"), (0.40, "fecha\naórtica"), (0.10, "fecha\nmitral"), (0.47, "abre\nmitral")]
    for x, lab in events:
        for a in axs:
            a.axvline(x, color=GREY, lw=0.5, ls="--")
        ax.text(x + 0.004, 30 if "mitral" in lab else 45, lab.replace("\n", " "), rotation=90, ha="left", va="bottom", fontsize=6.3, color=GREY)
    ax.set_ylim(0, 150); ax.set_ylabel("pressão (mmHg)")
    ax.legend(loc="center right", fontsize=7, frameon=False)
    phases = [(0.0, .10, "sístole\natrial"), (.10, .15, "contr.\nisovol."), (.15, .40, "ejeção (rápida → lenta)"),
              (.40, .47, "relax.\nisovol."), (.47, .8, "enchimento rápido → diástase")]
    for a0, a1, lab in phases:
        ax.text((a0 + a1) / 2, 145, lab, ha="center", va="top", fontsize=6.3)
    axs[1].plot(t, vol, color="#6a1b9a", lw=1.8)
    axs[1].set_ylabel("volume VE (mℓ)"); axs[1].set_ylim(30, 135)
    axs[1].text(0.12, 123, "VDF ≈ 120", fontsize=7); axs[1].text(0.41, 38, "VSF ≈ 50", fontsize=7)
    ax3 = axs[2]
    ax3.set_ylim(-1, 1); ax3.set_yticks([])
    for x0, w, lab in [(0.10, 0.03, "B1"), (0.40, 0.025, "B2")]:
        tt = np.linspace(x0, x0 + w, 80)
        ax3.plot(tt, 0.8 * np.sin(2 * np.pi * 400 * tt) * np.hanning(80), color="k", lw=0.8)
        ax3.text(x0 + w / 2, -0.95, lab, ha="center", fontsize=8, fontweight="bold")
    tt = np.linspace(0.52, 0.55, 60)
    ax3.plot(tt, 0.3 * np.sin(2 * np.pi * 150 * tt) * np.hanning(60), color=GREY, lw=0.8)
    ax3.text(0.535, -0.95, "(B3)", ha="center", fontsize=7, color=GREY)
    tt = np.linspace(0.02, 0.05, 60)
    ax3.plot(tt, 0.25 * np.sin(2 * np.pi * 120 * tt) * np.hanning(60), color=GREY, lw=0.8)
    ax3.text(0.035, -0.95, "(B4)", ha="center", fontsize=7, color=GREY)
    ax3.set_ylabel("fono")
    ax3.set_xlabel("tempo (s) · ciclo de 0,8 s (FC ≈ 75 bpm)")
    for a in axs:
        a.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, "a_wiggers.png")); plt.close(fig)


def alca_pv():
    fig, ax = plt.subplots(figsize=(5.2, 3.8), dpi=200)
    v = np.linspace(40, 200, 200)
    ax.plot(v, 2 + 0.00000012 * (v - 20) ** 4, color=GREY, lw=1, ls="--")
    ax.text(185, 55, "curva de pressão\ndiastólica", fontsize=6.5, color=GREY, ha="right")
    # alça
    A, B, C, D = (50, 3), (120, 7), (120, 80), (50, 100)
    fill_v = np.linspace(50, 120, 50); fill_p = 3 + (fill_v - 50) ** 2 * 4 / 4900
    ej_v = np.linspace(120, 50, 50); ej_p = 80 + 42 * np.sin(np.pi * (120 - ej_v) / 70 * 0.85) - (120 - ej_v) * 0.05
    ej_p[-1] = 100
    xs = np.concatenate([fill_v, [120], ej_v, [50]]); ys = np.concatenate([fill_p, [80], ej_p, [3]])
    ax.fill(xs, ys, color="#f4c7cd")
    ax.plot(xs, ys, color=RED, lw=2)
    for (x, y), lab in zip([A, B, C, D], "ABCD"):
        ax.plot(x, y, "ko", ms=3); ax.text(x + 2, y + 3, lab, fontweight="bold")
    ax.text(85, -2, "I · enchimento", ha="center", fontsize=7.5, va="top")
    ax.text(123, 42, "II · contração\nisovolumétrica", fontsize=7.5)
    ax.text(85, 126, "III · ejeção", ha="center", fontsize=7.5)
    ax.text(47, 50, "IV · relaxamento\nisovolumétrico", fontsize=7.5, ha="right")
    ax.text(85, 55, "TE\n(trabalho\nsistólico)", ha="center", fontsize=8, color=RED)
    ax.annotate("", xy=(120, 145), xytext=(50, 145), arrowprops=dict(arrowstyle="<->", lw=0.7))
    ax.text(85, 149, "VS = VDF − VSF ≈ 70 mℓ", ha="center", fontsize=7)
    ax.set_xlim(0, 200); ax.set_ylim(-12, 165)
    ax.set_xlabel("volume do VE (mℓ)"); ax.set_ylabel("pressão do VE (mmHg)")
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, "a_alca_pv.png")); plt.close(fig)


if __name__ == "__main__":
    potencial_acao(); wiggers(); alca_pv()
    print("ok")
