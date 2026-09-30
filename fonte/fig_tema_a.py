"""Figuras esquemáticas do tema a (valores aproximados do Guyton, cap. 9), com versões de oclusão para o Anki.

Cada rótulo desenhado com lab(...) tem uma chave. figura(hide=chave) desenha a mesma figura com esse rótulo
coberto por uma caixa "?" (frente do cartão de oclusão). OCLUSOES lista os cartões gerados.
"""
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


def lab(ax, key, hide, x, y, text, **kw):
    """Rótulo ocultável: quando key == hide, vira uma caixa '?' destacada."""
    if key == hide:
        kw = {k: v for k, v in kw.items() if k not in ("color", "bbox", "fontweight")}
        ax.text(x, y, "  ?  ", color="white", fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.35", fc="#e8590c", ec="#e8590c"), **kw)
    else:
        ax.text(x, y, text, **kw)


def save(fig, name, hide):
    suffix = f"__occ_{hide}" if hide else ""
    fig.savefig(os.path.join(FIG, f"{name}{suffix}.png"))
    plt.close(fig)


def potencial_acao(hide=None):
    t = np.linspace(-50, 400, 2000)
    v = np.interp(t, [-50, 0, 2, 8, 20, 40, 180, 230, 280, 300, 400],
                  [-85, -85, 20, 5, 2, 0, -8, -30, -80, -85, -85])
    fig, ax = plt.subplots(figsize=(6.2, 3.0), dpi=200)
    ax.plot(t, v, color=RED, lw=2)
    lab(ax, "f0", hide, 8, -45, "0 · entra Na⁺", fontsize=8, fontweight="bold")
    lab(ax, "f1", hide, 14, 22, "1 · sai K⁺ (Na⁺ fecha)", fontsize=8, fontweight="bold")
    lab(ax, "f2", hide, 75, 8, "2 · platô: entra Ca²⁺ (tipo L), ↓ saída de K⁺", fontsize=8, fontweight="bold")
    lab(ax, "f3", hide, 262, -40, "3 · sai K⁺", fontsize=8, fontweight="bold")
    lab(ax, "f4", hide, 310, -78, "4 · repouso −85 mV", fontsize=8, fontweight="bold")
    ax.axvspan(0, 270, ymin=0.02, ymax=0.06, color=GREY, alpha=0.5)
    lab(ax, "pra", hide, 135, -104, "período refratário absoluto (0,25–0,30 s)", ha="center", fontsize=7)
    ax.set_xlim(-50, 420); ax.set_ylim(-110, 40)
    ax.set_xticks([0, 100, 200, 300]); ax.set_xticklabels(["0", "0,1", "0,2", "0,3"])
    ax.set_xlabel("tempo (s)"); ax.set_ylabel("mV")
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    save(fig, "a_potencial_acao", hide)


def wiggers(hide=None):
    t = np.linspace(0, 0.8, 1600)
    ao = np.interp(t, [0, .15, .25, .38, .40, .41, .8], [82, 80, 120, 105, 100, 103, 82])
    lv = np.interp(t, [0, .05, .1, .15, .25, .38, .40, .47, .5, .8], [4, 6, 8, 80, 121, 104, 90, 5, 2, 4])
    la = np.interp(t, [0, .05, .1, .13, .16, .2, .38, .47, .55, .8], [4, 8, 5, 7, 3, 4, 10, 6, 3, 4])
    vol = np.interp(t, [0, .1, .15, .22, .40, .47, .58, .72, .8], [110, 120, 120, 80, 50, 50, 95, 105, 110])
    fig, axs = plt.subplots(3, 1, figsize=(6.4, 6.3), dpi=200, sharex=True,
                            gridspec_kw={"height_ratios": [3, 1.6, 1.1]})
    ax = axs[0]
    ax.plot(t, ao, color=RED, lw=1.8, label="aorta")
    ax.plot(t, lv, color=BLUE, lw=1.8, label="ventrículo esquerdo")
    ax.plot(t, la, color=GREEN, lw=1.8, label="átrio esquerdo")
    ax.annotate("", (0.405, 101), (0.46, 116), arrowprops=dict(arrowstyle="->", lw=0.6))
    lab(ax, "incisura", hide, 0.46, 117, "incisura", fontsize=7)
    for x, k in [(0.03, "a"), (0.125, "c"), (0.36, "v")]:
        lab(ax, "onda_" + k, hide, x, 15, k, color=GREEN, fontweight="bold")
    events = [(0.15, "abre aórtica", 45, "abre_ao"), (0.40, "fecha aórtica", 45, "fecha_ao"),
              (0.10, "fecha mitral", 30, "fecha_mi"), (0.47, "abre mitral", 30, "abre_mi")]
    for x, text, y, k in events:
        for a in axs:
            a.axvline(x, color=GREY, lw=0.5, ls="--")
        lab(ax, k, hide, x + 0.004, y, text, rotation=90, ha="left", va="bottom", fontsize=6.3, color=GREY)
    ax.set_ylim(0, 150); ax.set_ylabel("pressão (mmHg)")
    ax.legend(loc="center right", fontsize=7, frameon=False)
    phases = [(0.0, .10, "sístole\natrial", "ph_sa"), (.10, .15, "contr.\nisovol.", "ph_ci"),
              (.15, .40, "ejeção (rápida → lenta)", "ph_ej"), (.40, .47, "relax.\nisovol.", "ph_ri"),
              (.47, .8, "enchimento rápido → diástase", "ph_en")]
    for a0, a1, text, k in phases:
        lab(ax, k, hide, (a0 + a1) / 2, 145, text, ha="center", va="top", fontsize=6.3)
    axs[1].plot(t, vol, color="#6a1b9a", lw=1.8)
    axs[1].set_ylabel("volume VE (mℓ)"); axs[1].set_ylim(30, 135)
    lab(axs[1], "vdf", hide, 0.12, 123, "VDF ≈ 120", fontsize=7)
    lab(axs[1], "vsf", hide, 0.41, 38, "VSF ≈ 50", fontsize=7)
    ax3 = axs[2]
    ax3.set_ylim(-1, 1); ax3.set_yticks([])
    for x0, w, k in [(0.10, 0.03, "B1"), (0.40, 0.025, "B2")]:
        tt = np.linspace(x0, x0 + w, 80)
        ax3.plot(tt, 0.8 * np.sin(2 * np.pi * 400 * tt) * np.hanning(80), color="k", lw=0.8)
        lab(ax3, k, hide, x0 + w / 2, -0.95, k, ha="center", fontsize=8, fontweight="bold")
    for x0, k in [(0.52, "B3"), (0.02, "B4")]:
        tt = np.linspace(x0, x0 + 0.03, 60)
        ax3.plot(tt, 0.3 * np.sin(2 * np.pi * 140 * tt) * np.hanning(60), color=GREY, lw=0.8)
        lab(ax3, k, hide, x0 + 0.015, -0.95, f"({k})", ha="center", fontsize=7, color=GREY)
    ax3.set_ylabel("fono")
    ax3.set_xlabel("tempo (s) · ciclo de 0,8 s (FC ≈ 75 bpm)")
    for a in axs:
        a.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    save(fig, "a_wiggers", hide)


def alca_pv(hide=None):
    fig, ax = plt.subplots(figsize=(5.2, 3.8), dpi=200)
    v = np.linspace(40, 200, 200)
    ax.plot(v, 2 + 0.00000012 * (v - 20) ** 4, color=GREY, lw=1, ls="--")
    ax.text(185, 55, "curva de pressão\ndiastólica", fontsize=6.5, color=GREY, ha="right")
    fill_v = np.linspace(50, 120, 50); fill_p = 3 + (fill_v - 50) ** 2 * 4 / 4900
    ej_v = np.linspace(120, 50, 50); ej_p = 80 + 42 * np.sin(np.pi * (120 - ej_v) / 70 * 0.85) - (120 - ej_v) * 0.05
    ej_p[-1] = 100
    xs = np.concatenate([fill_v, [120], ej_v, [50]]); ys = np.concatenate([fill_p, [80], ej_p, [3]])
    ax.fill(xs, ys, color="#f4c7cd")
    ax.plot(xs, ys, color=RED, lw=2)
    for (x, y), p in zip([(50, 3), (120, 7), (120, 80), (50, 100)], "ABCD"):
        ax.plot(x, y, "ko", ms=3); ax.text(x + 2, y + 3, p, fontweight="bold")
    lab(ax, "I", hide, 85, -2, "I · enchimento", ha="center", fontsize=7.5, va="top")
    lab(ax, "II", hide, 123, 42, "II · contração\nisovolumétrica", fontsize=7.5)
    lab(ax, "III", hide, 85, 126, "III · ejeção", ha="center", fontsize=7.5)
    lab(ax, "IV", hide, 47, 50, "IV · relaxamento\nisovolumétrico", fontsize=7.5, ha="right")
    lab(ax, "TE", hide, 85, 55, "TE\n(trabalho\nsistólico)", ha="center", fontsize=8, color=RED)
    ax.annotate("", xy=(120, 145), xytext=(50, 145), arrowprops=dict(arrowstyle="<->", lw=0.7))
    lab(ax, "VS", hide, 85, 149, "VS = VDF − VSF ≈ 70 mℓ", ha="center", fontsize=7)
    ax.set_xlim(0, 200); ax.set_ylim(-12, 165)
    ax.set_xlabel("volume do VE (mℓ)"); ax.set_ylabel("pressão do VE (mmHg)")
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    save(fig, "a_alca_pv", hide)


def focos(hide=None):
    """Focos clássicos de ausculta (Porto): esquema do tórax anterior."""
    fig, ax = plt.subplots(figsize=(4.4, 4.2), dpi=200)
    ax.set_xlim(-6.5, 6.5); ax.set_ylim(-7.6, 1.2); ax.set_aspect("equal"); ax.axis("off")
    ax.add_patch(plt.Rectangle((-0.8, -5.2), 1.6, 6.0, fc="#efe6d8", ec="#b9a888"))
    for i, y in enumerate([0.3, -0.9, -2.1, -3.3, -4.5, -5.7]):
        for s in (-1, 1):
            xx = np.linspace(0.8, 5.2, 50) * s
            ax.plot(xx, y - 0.06 * (np.abs(xx) - 0.8) ** 1.6, color="#c8b9a0", lw=5, solid_capstyle="round")
        ax.text(5.5, y - 0.4, f"{i + 1}ª", fontsize=6, color=GREY) if i < 6 else None
    for x, y in [(-3.1, -2.6), (3.1, -2.6)]:
        pass
    ax.plot([2.9, 2.9], [0.8, -6.3], color=GREY, lw=0.6, ls=":")
    ax.text(2.9, 0.95, "linha hemiclavicular E", fontsize=6, ha="center", color=GREY)
    ax.add_patch(plt.Polygon([(-0.5, -5.2), (0.5, -5.2), (0, -6.0)], fc="#efe6d8", ec="#b9a888"))
    pts = [("ao", -1.1, -1.5, "Aórtico\n2º EIC D, justaesternal", "right"),
           ("pu", 1.1, -1.5, "Pulmonar\n2º EIC E, junto ao esterno", "left"),
           ("ac", 1.1, -2.9, "Aórtico acessório\n3º-4º EIC E, paraesternal", "left"),
           ("tr", 0.3, -5.45, "Tricúspide\nbase do apêndice xifoide, à E", "left"),
           ("mi", 2.9, -5.1, "Mitral\n5º EIC E, LHC (ictus)", "left")]
    for k, x, y, text, ha in pts:
        ax.plot(x, y, "o", ms=9, color=RED, mec="white")
        dx, dy = (-0.35 if ha == "right" else 0.35), 0.3
        if k == "mi":
            dx, dy = -0.2, -1.0
        elif k == "tr":
            dx, dy = -1.2, -1.2
        lab(ax, k, hide, x + dx, y + dy, text, ha=ha, va="center", fontsize=6.8)
    fig.tight_layout()
    save(fig, "a_focos", hide)


FIGS = {"a_potencial_acao": potencial_acao, "a_wiggers": wiggers, "a_alca_pv": alca_pv, "a_focos": focos}

# (figura, chave oculta, pergunta, resposta)
OCLUSOES = [
    ("a_potencial_acao", "f0", "Fase 0 do potencial ventricular: qual íon?", "Entrada de <b>Na⁺</b> (canais rápidos)."),
    ("a_potencial_acao", "f1", "Fase 1: o que acontece?", "Canais de Na⁺ fecham; <b>sai K⁺</b> (transitório)."),
    ("a_potencial_acao", "f2", "Fase 2: por que existe o platô?", "<b>Entra Ca²⁺</b> pelos canais tipo L e <b>cai a saída de K⁺</b>."),
    ("a_potencial_acao", "f3", "Fase 3: o que repolariza a fibra?", "Canais de Ca²⁺ fecham e <b>sai K⁺</b>."),
    ("a_potencial_acao", "pra", "O que representa essa faixa e quanto dura?", "<b>Período refratário absoluto</b> do ventrículo: 0,25 a 0,30 s."),
    ("a_wiggers", "ph_ci", "Nome da fase?", "<b>Contração isovolumétrica</b> (todas as valvas fechadas)."),
    ("a_wiggers", "ph_ri", "Nome da fase?", "<b>Relaxamento isovolumétrico</b>."),
    ("a_wiggers", "abre_ao", "Qual evento valvar?", "<b>Abertura da valva aórtica</b> (PVE supera ≈ 80 mmHg)."),
    ("a_wiggers", "fecha_mi", "Qual evento valvar?", "<b>Fechamento da mitral</b> (início da sístole, B1)."),
    ("a_wiggers", "abre_mi", "Qual evento valvar?", "<b>Abertura da mitral</b> (fim do relaxamento isovolumétrico)."),
    ("a_wiggers", "incisura", "Nome desse entalhe na curva aórtica?", "<b>Incisura</b>: refluxo breve e fechamento da valva aórtica."),
    ("a_wiggers", "onda_a", "Qual onda de pressão atrial e sua causa?", "Onda <b>a</b>: contração atrial."),
    ("a_wiggers", "onda_c", "Qual onda de pressão atrial e sua causa?", "Onda <b>c</b>: abaulamento das valvas AV no início da sístole."),
    ("a_wiggers", "onda_v", "Qual onda de pressão atrial e sua causa?", "Onda <b>v</b>: enchimento atrial com as AV fechadas."),
    ("a_wiggers", "B4", "Qual bulha ocorre aqui?", "<b>B4</b>: contração atrial contra ventrículo rígido."),
    ("a_wiggers", "B3", "Qual bulha ocorre aqui?", "<b>B3</b>: enchimento rápido; normal em jovens, IC em idosos."),
    ("a_alca_pv", "II", "Qual fase da alça (B → C)?", "<b>Contração isovolumétrica</b>."),
    ("a_alca_pv", "IV", "Qual fase da alça (D → A)?", "<b>Relaxamento isovolumétrico</b>."),
    ("a_alca_pv", "TE", "O que representa a área da alça?", "<b>Trabalho sistólico externo</b>."),
    ("a_alca_pv", "VS", "Qual grandeza é a largura da alça?", "<b>Volume sistólico</b> = VDF − VSF ≈ 70 mℓ."),
    ("a_focos", "ao", "Qual foco de ausculta?", "<b>Aórtico</b>: 2º EIC direito, justaesternal."),
    ("a_focos", "pu", "Qual foco de ausculta?", "<b>Pulmonar</b>: 2º EIC esquerdo, junto ao esterno."),
    ("a_focos", "ac", "Qual foco de ausculta?", "<b>Aórtico acessório</b>: 3º-4º EIC esquerdo, junto ao esterno."),
    ("a_focos", "tr", "Qual foco de ausculta?", "<b>Tricúspide</b>: base do apêndice xifoide, ligeiramente à esquerda."),
    ("a_focos", "mi", "Qual foco de ausculta?", "<b>Mitral</b>: 5º EIC esquerdo na linha hemiclavicular (ictus cordis)."),
]

if __name__ == "__main__":
    for f in FIGS.values():
        f()
    for name, key, _, _ in OCLUSOES:
        FIGS[name](hide=key)
    print("ok", len(OCLUSOES))
