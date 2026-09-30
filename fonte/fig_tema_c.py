"""Figuras esquemáticas do tema c (ECG normal; Guyton caps. 11 e 12), com versões de oclusão para o Anki."""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from fig_tema_a import BLUE, GREY, RED, lab, save

PINK_MIN, PINK_MAJ = "#f6c9cf", "#e99aa5"


def g(t, mu, sd, amp):
    return amp * np.exp(-0.5 * ((t - mu) / sd) ** 2)


def batimento(t, t0):
    """ECG sintético (mV) com P 0,10 s, PR 0,16 s, QRS 0,08 s, QT 0,35 s."""
    x = t - t0
    return (g(x, 0.145, 0.022, 0.18)                        # P (0,10–0,19)
            + g(x, 0.272, 0.006, -0.10)                     # Q
            + g(x, 0.295, 0.010, 1.20)                      # R
            + g(x, 0.318, 0.007, -0.30)                     # S
            + g(x, 0.50, 0.045, 0.30))                      # T (termina ≈ 0,61)


def papel(ax, x0, x1, y0, y1):
    for xv in np.arange(x0, x1 + 1e-9, 0.04):
        major = abs((xv - x0) / 0.2 - round((xv - x0) / 0.2)) < 1e-6
        ax.axvline(xv, color=PINK_MAJ if major else PINK_MIN, lw=0.8 if major else 0.35, zorder=0)
    for yv in np.arange(y0, y1 + 1e-9, 0.1):
        major = abs(yv / 0.5 - round(yv / 0.5)) < 1e-6
        ax.axhline(yv, color=PINK_MAJ if major else PINK_MIN, lw=0.8 if major else 0.35, zorder=0)
    ax.set_xlim(x0, x1); ax.set_ylim(y0, y1); ax.set_aspect(0.4)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)


def ecg_normal(hide=None):
    fig, ax = plt.subplots(figsize=(7.2, 3.4), dpi=200)
    papel(ax, 0, 1.6, -0.6, 1.6)
    t = np.linspace(0, 1.6, 3000)
    v = batimento(t, 0.0) + batimento(t, 0.83)
    ax.plot(t, v, color="#222", lw=1.3, zorder=3)
    # rótulos das ondas
    lab(ax, "P", hide, 0.135, 0.26, "P", fontweight="bold", color=RED, ha="center")
    lab(ax, "Q", hide, 0.262, -0.28, "Q", fontweight="bold", color=RED, ha="center")
    lab(ax, "R", hide, 0.295, 1.28, "R", fontweight="bold", color=RED, ha="center")
    lab(ax, "S", hide, 0.33, -0.45, "S", fontweight="bold", color=RED, ha="center")
    lab(ax, "T", hide, 0.50, 0.38, "T", fontweight="bold", color=RED, ha="center")

    def bracket(xa, xb, y, text, key, dy=0.07):
        ax.annotate("", (xa, y), (xb, y), arrowprops=dict(arrowstyle="<->", lw=0.8, color=BLUE))
        lab(ax, key, hide, (xa + xb) / 2, y + dy, text, ha="center", fontsize=7, color=BLUE,
            bbox=dict(fc="white", ec="none", pad=0.5))
    bracket(0.10, 0.26, -0.33, "PR ≈ 0,16 s", "PR", dy=-0.16)
    bracket(0.26, 0.61, 1.0, "QT ≈ 0,35 s", "QT")
    bracket(0.295, 1.125, 1.45, "RR ≈ 0,83 s → FC 72/min", "RR")
    bracket(0.26, 0.34, 0.62, "QRS", "QRS", dy=0.08)
    ax.plot([0.34, 0.43], [-0.05, -0.05], color="#2e7d32", lw=1.5, zorder=2)
    lab(ax, "ST", hide, 0.42, -0.2, "segmento ST", ha="center", fontsize=6.5, color="#2e7d32")
    # calibração
    ax.plot([1.42, 1.44, 1.44, 1.52, 1.52, 1.54], [0, 0, 1.0, 1.0, 0, 0], color="#222", lw=1.1)
    lab(ax, "cal", hide, 1.48, 1.08, "1 mV = 10 mm", ha="center", fontsize=6.5)
    fig.tight_layout()
    save(fig, "c_ecg_normal", hide)


def papel_zoom(hide=None):
    fig, ax = plt.subplots(figsize=(4.4, 3.0), dpi=200)
    papel(ax, 0, 0.4, 0, 1.0)
    ax.annotate("", (0.0, 1.05), (0.04, 1.05), arrowprops=dict(arrowstyle="<->", lw=0.8), annotation_clip=False)
    lab(ax, "peq_t", hide, 0.02, 1.1, "1 mm = 0,04 s", ha="center", fontsize=7)
    ax.annotate("", (0.2, 1.05), (0.4, 1.05), arrowprops=dict(arrowstyle="<->", lw=0.8), annotation_clip=False)
    lab(ax, "grd_t", hide, 0.3, 1.1, "5 mm = 0,20 s", ha="center", fontsize=7)
    ax.annotate("", (-0.012, 0.0), (-0.012, 0.1), arrowprops=dict(arrowstyle="<->", lw=0.8), annotation_clip=False)
    lab(ax, "peq_v", hide, -0.02, 0.05, "0,1 mV", ha="right", va="center", fontsize=7)
    ax.annotate("", (-0.012, 0.5), (-0.012, 1.0), arrowprops=dict(arrowstyle="<->", lw=0.8), annotation_clip=False)
    lab(ax, "grd_v", hide, -0.02, 0.75, "0,5 mV", ha="right", va="center", fontsize=7)
    lab(ax, "vel", hide, 0.2, -0.12, "velocidade padrão: 25 mm/s (25 mm = 1 s)", ha="center", fontsize=7)
    fig.subplots_adjust(left=0.2, right=0.97, top=0.85, bottom=0.12)
    save(fig, "c_papel", hide)


def hexaxial(hide=None):
    fig, ax = plt.subplots(figsize=(4.4, 4.4), dpi=200)
    ax.set_xlim(-1.45, 1.45); ax.set_ylim(-1.55, 1.45); ax.set_aspect("equal"); ax.axis("off")
    leads = [("I", 0, RED), ("II", 60, RED), ("III", 120, RED), ("aVR", -150, BLUE), ("aVL", -30, BLUE), ("aVF", 90, BLUE)]
    for name, ang, c in leads:
        a = np.deg2rad(ang)
        dx, dy = np.cos(a), -np.sin(a)  # 0° à esquerda do paciente (direita da figura), +90° para baixo
        ax.plot([-dx, dx], [-dy, dy], color=c, lw=1, alpha=0.35)
        ax.annotate("", (dx, dy), (0, 0), arrowprops=dict(arrowstyle="-|>", color=c, lw=1.6))
        lab(ax, "L_" + name, hide, 1.22 * dx, 1.22 * dy, name, ha="center", va="center", fontsize=10, fontweight="bold", color=c)
        sign = "+" if ang > 0 else ("−" if ang < 0 else "")
        lab(ax, "A_" + name, hide, 0.72 * dx + 0.12 * dy, 0.72 * dy - 0.12 * dx, f"{sign}{abs(ang)}°", ha="center",
            va="center", fontsize=7, color="#333")
    a = np.deg2rad(59)
    ax.annotate("", (0.9 * np.cos(a), -0.9 * np.sin(a)), (0, 0), arrowprops=dict(arrowstyle="-|>", color="#2e7d32", lw=2.4))
    lab(ax, "eixo", hide, -1.42, 1.25, "eixo QRS médio +59° (seta verde)\n(normal 20° a 100°, Guyton)", ha="left", fontsize=7, color="#2e7d32")
    ax.text(0, -1.45, "lado direito ←   → lado esquerdo do paciente", ha="center", fontsize=6.5, color=GREY)
    fig.tight_layout()
    save(fig, "c_hexaxial", hide)


def quadrantes(hide=None):
    fig, ax = plt.subplots(figsize=(4.6, 4.2), dpi=200)
    ax.set_xlim(-1.4, 1.4); ax.set_ylim(-1.4, 1.35); ax.set_aspect("equal"); ax.axis("off")
    ax.axhline(0, color="#333", lw=1); ax.axvline(0, color="#333", lw=1)
    ax.text(1.32, 0.05, "DI (0°)", fontsize=7, ha="right")
    ax.text(0.05, -1.35, "aVF (+90°)", fontsize=7)
    quads = [("q_norm", 0.65, -0.6, "#d8f0d8", "NORMAL\nDI + / aVF +\n(0° a +90°)"),
             ("q_esq", 0.65, 0.6, "#fff1c9", "DESVIO À ESQUERDA\nDI + / aVF −"),
             ("q_dir", -0.65, -0.6, "#dbe7fb", "DESVIO À DIREITA\nDI − / aVF +"),
             ("q_ext", -0.65, 0.6, "#f8d7da", "EXTREMO\nDI − / aVF −")]
    for k, x, y, c, text in quads:
        ax.add_patch(plt.Rectangle((x - 0.62, y - 0.55), 1.24, 1.1, fc=c, ec="none", zorder=0))
        lab(ax, k, hide, x, y, text, ha="center", va="center", fontsize=7.2, fontweight="bold")
    fig.tight_layout()
    save(fig, "c_quadrantes", hide)


def precordiais(hide=None):
    fig, ax = plt.subplots(figsize=(4.6, 4.2), dpi=200)
    ax.set_xlim(-6.5, 7.5); ax.set_ylim(-8.9, 1.2); ax.set_aspect("equal"); ax.axis("off")
    ax.add_patch(plt.Rectangle((-0.8, -5.2), 1.6, 6.0, fc="#efe6d8", ec="#b9a888"))
    for y in [0.3, -0.9, -2.1, -3.3, -4.5, -5.7]:
        for s in (-1, 1):
            xx = np.linspace(0.8, 5.6, 50) * s
            ax.plot(xx, y - 0.06 * (np.abs(xx) - 0.8) ** 1.6, color="#c8b9a0", lw=5, solid_capstyle="round")
    for x, name in [(2.9, "LHC"), (4.6, "LAA"), (6.1, "LAM")]:
        ax.plot([x, x], [0.8, -6.6], color=GREY, lw=0.6, ls=":")
        ax.text(x, 0.95, name, fontsize=6, ha="center", color=GREY)
    pts = [("V1", -1.1, -3.9, "4º EIC D, paraesternal"), ("V2", 1.1, -3.9, "4º EIC E, paraesternal"),
           ("V3", 2.0, -4.65, "entre V2 e V4"), ("V4", 2.9, -5.2, "5º EIC E, LHC"),
           ("V5", 4.6, -5.35, "LAA, nível de V4"), ("V6", 6.1, -5.5, "LAM, nível de V4")]
    for k, x, y, text in pts:
        ax.plot(x, y, "o", ms=11, color=RED, mec="white")
        ax.text(x, y, k[1], color="white", fontsize=6.5, ha="center", va="center", fontweight="bold")
    # legenda em linhas separadas para permitir ocultar cada uma
    for i, (k, _, _, t) in enumerate(pts):
        lab(ax, "P_" + k, hide, -6.0 if i < 3 else 1.0, -7.0 - (i % 3) * 0.6, f"{k}: {t}", fontsize=6.4)
    fig.tight_layout()
    save(fig, "c_precordiais", hide)


FIGS = {"c_ecg_normal": ecg_normal, "c_papel": papel_zoom, "c_hexaxial": hexaxial, "c_quadrantes": quadrantes,
        "c_precordiais": precordiais}

OCLUSOES = [
    ("c_ecg_normal", "P", "Qual onda e o que representa?", "Onda <b>P</b>: despolarização atrial."),
    ("c_ecg_normal", "Q", "Qual onda e o que representa?", "Onda <b>Q</b>: despolarização do septo da esquerda para a direita."),
    ("c_ecg_normal", "T", "Qual onda e o que representa?", "Onda <b>T</b>: repolarização ventricular."),
    ("c_ecg_normal", "PR", "Nome e valor normal deste intervalo?", "Intervalo <b>PR (PQ)</b> ≈ <b>0,16 s</b> (início da P ao início do QRS)."),
    ("c_ecg_normal", "QT", "Nome e valor normal deste intervalo?", "Intervalo <b>QT</b> ≈ <b>0,35 s</b> (contração ventricular)."),
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
    ("c_precordiais", "P_V1", "Onde fica V1?", "<b>4º EIC direito</b>, borda esternal."),
    ("c_precordiais", "P_V2", "Onde fica V2?", "<b>4º EIC esquerdo</b>, borda esternal."),
    ("c_precordiais", "P_V4", "Onde fica V4?", "<b>5º EIC esquerdo</b>, linha hemiclavicular."),
    ("c_precordiais", "P_V6", "Onde fica V6?", "<b>Linha axilar média</b>, no nível de V4."),
]

if __name__ == "__main__":
    for f in FIGS.values():
        f()
    for name, key, _, _ in OCLUSOES:
        FIGS[name](hide=key)
    print("ok", len(OCLUSOES))
