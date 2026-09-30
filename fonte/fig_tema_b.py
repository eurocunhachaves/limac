"""Figuras esquemáticas do tema b (Guyton, cap. 10), com versões de oclusão para o Anki."""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch

from fig_tema_a import BLUE, FIG, GREEN, GREY, RED, lab, save

ORANGE = "#e8590c"


def sa_ciclo(t0, periodo, v_min=-60, limiar=-40):
    """Um ciclo do potencial nodal sinusal: do vale (v_min) em t0 até o vale seguinte em t0 + periodo."""
    r = periodo - 0.30
    return [t0, t0 + r, t0 + r + 0.08, t0 + r + 0.16, t0 + periodo], [v_min, limiar, 0, -10, v_min]


def potencial_sa(hide=None):
    fig, ax = plt.subplots(figsize=(6.4, 3.2), dpi=200)
    T = 0.8
    xs, ys = [], []
    for k in range(3):
        x, y = sa_ciclo(k * T, T)
        xs += x; ys += y
    ax.plot(xs, ys, color=RED, lw=2, label="nó sinusal")
    tv = np.array([2.45, 2.5, 2.502, 2.51, 2.53, 2.7, 2.75, 2.8, 2.85, 3.05])
    vv = np.array([-85, -85, 20, 5, 2, -5, -30, -80, -85, -85])
    ax.plot(tv, vv, color=GREEN, lw=1.6, label="músculo ventricular")
    ax.axhline(-40, color=GREY, lw=0.6, ls="--")
    lab(ax, "limiar", hide, 1.6, -37, "limiar ≈ −40 mV", fontsize=7, color=GREY)
    lab(ax, "repouso", hide, 0.02, -72, "repouso −55 a −60 mV\n(\"vaza\" Na⁺ e Ca²⁺)", fontsize=7)
    ax.annotate("", (0.35, -50), (0.15, -66), arrowprops=dict(arrowstyle="->", lw=0.6))
    lab(ax, "funny", hide, 0.95, -90, "despolarização diastólica lenta:\ncorrente funny (Na⁺)", fontsize=7)
    ax.annotate("", (1.2, -52), (1.2, -78), arrowprops=dict(arrowstyle="->", lw=0.6))
    lab(ax, "subida", hide, 0.2, 8, "subida lenta:\nCa²⁺ tipo L", fontsize=7)
    ax.annotate("", (0.47, -10), (0.36, 5), arrowprops=dict(arrowstyle="->", lw=0.6))
    lab(ax, "repol", hide, 0.72, 5, "repolarização:\nCa²⁺ fecha, sai K⁺", fontsize=7)
    ax.annotate("", (0.66, -30), (0.78, 3), arrowprops=dict(arrowstyle="->", lw=0.6))
    ax.set_ylim(-95, 30); ax.set_xlim(0, 3.1)
    ax.set_xlabel("tempo (s)"); ax.set_ylabel("mV")
    ax.legend(loc="lower center", fontsize=7, frameon=False, bbox_to_anchor=(0.55, 0.0))
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    save(fig, "b_potencial_sa", hide)


def conducao(hide=None):
    fig, ax = plt.subplots(figsize=(6.6, 3.9), dpi=200)
    ax.set_xlim(0, 10); ax.set_ylim(0, 6.3); ax.axis("off")
    nodes = [  # chave, x, y, nome, tempo
        ("sa", 1.0, 5.0, "Nó sinusal", "0"),
        ("av", 3.4, 5.0, "Nó AV", "0,03 s"),
        ("fp", 5.8, 5.0, "Feixe AV\npenetrante", "0,12 s"),
        ("ramos", 8.4, 5.0, "Ramos no\nsepto", "0,16 s"),
        ("purk", 8.4, 2.2, "Fim das fibras\nde Purkinje", "≈ 0,19 s"),
        ("epi", 4.6, 2.2, "Epicárdio\nventricular (último)", "≈ 0,22 s"),
    ]
    for k, x, y, name, t in nodes:
        ax.add_patch(FancyBboxPatch((x - 0.95, y - 0.45), 1.9, 0.9, boxstyle="round,pad=0.05",
                                    fc="#fff3d6", ec="#c9a227", lw=1))
        ax.text(x, y, name, ha="center", va="center", fontsize=7.4, fontweight="bold")
        lab(ax, "t_" + k, hide, x, y - 0.75, t, ha="center", va="center", fontsize=7.5, color=RED)
    arrows = [((1.95, 5.0), (2.45, 5.0), "vias internodais\n≈ 1 m/s", "v_intern", 2.2, 5.8),
              ((4.35, 5.0), (4.85, 5.0), "atraso nodal\n0,09 s", "d_av", 4.6, 5.8),
              ((6.75, 5.0), (7.45, 5.0), "+0,04 s", "d_fp", 7.1, 5.7),
              ((8.4, 4.55), (8.4, 2.65), "Purkinje\n1,5 a 4 m/s\n(+0,03 s)", "v_purk", 9.1, 3.6),
              ((7.45, 2.2), (5.55, 2.2), "músculo 0,3 a 0,5 m/s\nendo → epi +0,03 s", "v_musc", 6.5, 2.75)]
    for a, b, text, k, tx, ty in arrows:
        ax.annotate("", b, a, arrowprops=dict(arrowstyle="-|>", lw=1.2, color=GREY))
        lab(ax, k, hide, tx, ty, text, ha="center", va="center", fontsize=6.6, color="#333")
    lab(ax, "atraso_total", hide, 2.2, 0.8,
        "Atraso total até o ventrículo: 0,16 s (0,03 + 0,09 + 0,04)\nCausa: poucas junções comunicantes no nó AV",
        fontsize=7.2, ha="left", bbox=dict(fc="#fbeaec", ec=RED, lw=0.6))
    fig.tight_layout()
    save(fig, "b_conducao", hide)


def marcapassos(hide=None):
    fig, ax = plt.subplots(figsize=(5.4, 2.6), dpi=200)
    items = [("Nó sinusal", 70, 80, RED, "sa"), ("Nó AV", 40, 60, "#c9a227", "av"), ("Purkinje", 15, 40, BLUE, "pk")]
    for i, (name, lo, hi, c, k) in enumerate(items):
        ax.barh(i, hi - lo, left=lo, color=c, height=0.5)
        lab(ax, k, hide, hi + 2, i, f"{lo} a {hi} bpm", va="center", fontsize=8)
    ax.set_yticks(range(3)); ax.set_yticklabels([x[0] for x in items])
    ax.invert_yaxis(); ax.set_xlim(0, 100); ax.set_xlabel("frequência intrínseca (disparos/min)")
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_title("O mais rápido comanda e suprime os outros", fontsize=8, color=GREY)
    fig.tight_layout()
    save(fig, "b_marcapassos", hide)


def autonomo(hide=None):
    fig, ax = plt.subplots(figsize=(6.2, 2.9), dpi=200)
    for T, vmin, c, k, text, y in [(0.8, -60, RED, "norm", "normal", 12),
                                   (0.5, -58, ORANGE, "simp", "simpático: rampa mais íngreme", 22),
                                   (1.4, -72, BLUE, "vago", "vago (ACh): hiperpolariza (−65 a −75 mV)", -85)]:
        xs, ys = [], []
        t = 0
        while t < 2.8:
            x, yv = sa_ciclo(t, T, v_min=vmin)
            xs += x; ys += yv; t += T
        xs, ys = np.array(xs), np.array(ys)
        m = xs <= 2.8
        ax.plot(xs[m], ys[m], color=c, lw=1.6)
        lab(ax, k, hide, 0.02 if k != "vago" else 0.02, y, text, fontsize=7, color=c)
    ax.axhline(-40, color=GREY, lw=0.6, ls="--")
    ax.set_ylim(-92, 30); ax.set_xlim(0, 2.8)
    ax.set_xlabel("tempo (s)"); ax.set_ylabel("mV")
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    save(fig, "b_autonomo", hide)


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
    ("b_conducao", "d_av", "Quanto é o atraso dentro do nó AV?", "<b>0,09 s</b>."),
    ("b_conducao", "d_fp", "Atraso adicional no feixe AV penetrante?", "<b>0,04 s</b>."),
    ("b_conducao", "t_ramos", "Quando o impulso chega aos ramos no septo?", "≈ <b>0,16 s</b> (atraso total)."),
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
    for f in FIGS.values():
        f()
    for name, key, _, _ in OCLUSOES:
        FIGS[name](hide=key)
    print("ok", len(OCLUSOES))
