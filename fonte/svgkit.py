"""Kit de diagramas vetoriais (SVG) com identidade visual única para os resumões e os cartões do Anki.

Cada diagrama é uma função f(hide=None) -> SVG. Rótulos criados com label(..., key=...) viram uma
pílula laranja "?" quando key == hide (frente dos cartões de oclusão).
Texto aceita **negrito** e quebras de linha (\\n).
"""
import html
import json
import math
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
SVG_DIR = os.path.join(HERE, "svg")
os.makedirs(SVG_DIR, exist_ok=True)

# paleta (tons fortes para traço, claros para preenchimento)
INK, MUTE, LINE, BG = "#1f2328", "#6b7280", "#d7dbe0", "#ffffff"
RED, RED_L = "#b42336", "#fde8eb"
BLUE, BLUE_L = "#2458b3", "#e6eefb"
TEAL, TEAL_L = "#0f766e", "#e0f4f1"
AMBER, AMBER_L = "#c26a05", "#fff1dc"
PURPLE, PURPLE_L = "#6d3fc4", "#efe8fc"
GREEN, GREEN_L = "#23803d", "#e4f5e8"
GREY_L = "#f3f4f6"
OCC = "#e8590c"
FONT = "Inter, 'DejaVu Sans', sans-serif"

_md_b = re.compile(r"\*\*(.+?)\*\*")


def _tspans(s, bold_start=False):
    """Converte **negrito** em tspans; devolve (html, negrito_aberto_no_fim)."""
    parts = s.split("**")
    out, bold = [], bold_start
    for i, p in enumerate(parts):
        if i > 0:
            bold = not bold
        if p:
            out.append(f'<tspan font-weight="700">{html.escape(p)}</tspan>' if bold else html.escape(p))
    return "".join(out), bold


def text_width(s, size, weight=400):
    s = _md_b.sub(r"\1", s)
    k = 0.56 if weight < 600 else 0.6
    return max((len(line) for line in s.split("\n")), default=0) * size * k


class SVG:
    def __init__(self, w, h, hide=None):
        self.w, self.h, self.hide = w, h, hide
        self.els = []
        self.markers = set()

    # ------------------------------------------------------------ primitivas
    def add(self, s):
        self.els.append(s)

    def rect(self, x, y, w, h, fill=GREY_L, stroke="none", r=10, sw=1.2, shadow=False, dash=None, opacity=1):
        f = ' filter="url(#sh)"' if shadow else ""
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r}" fill="{fill}" '
                 f'stroke="{stroke}" stroke-width="{sw}" opacity="{opacity}"{d}{f}/>')

    def circle(self, cx, cy, r, fill=RED, stroke="none", sw=1.2, opacity=1):
        self.add(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{opacity}"/>')

    def ellipse(self, cx, cy, rx, ry, fill=GREY_L, stroke="none", sw=1.2, opacity=1):
        self.add(f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{opacity}"/>')

    def path(self, d, stroke=INK, sw=1.6, fill="none", dash=None, opacity=1, cap="round"):
        ds = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="{cap}" '
                 f'stroke-linejoin="round" opacity="{opacity}"{ds}/>')

    def line(self, x1, y1, x2, y2, stroke=INK, sw=1.4, dash=None, opacity=1):
        self.path(f"M{x1:.1f},{y1:.1f} L{x2:.1f},{y2:.1f}", stroke, sw, dash=dash, opacity=opacity)

    def poly(self, pts, stroke=INK, sw=2.2, fill="none", dash=None, opacity=1, smooth=False):
        if smooth and len(pts) > 2:
            d = _catmull(pts)
        else:
            d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
        self.path(d, stroke, sw, fill, dash, opacity)

    def arrow(self, pts, color=INK, sw=1.8, dash=None, both=False, curve=False, head=True):
        """Seta por uma lista de pontos; curve=True usa uma curva quadrática pelo ponto do meio."""
        mk = self._marker(color)
        if curve and len(pts) == 3:
            (x1, y1), (cx, cy), (x2, y2) = pts
            d = f"M{x1:.1f},{y1:.1f} Q{cx:.1f},{cy:.1f} {x2:.1f},{y2:.1f}"
        else:
            d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
        ds = f' stroke-dasharray="{dash}"' if dash else ""
        end = f' marker-end="url(#{mk})"' if head else ""
        start = f' marker-start="url(#{mk}s)"' if both else ""
        self.add(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" '
                 f'stroke-linejoin="round"{ds}{end}{start}/>')

    def _marker(self, color):
        self.markers.add(color)
        return "m" + color.strip("#")

    def text(self, x, y, s, size=12, weight=400, fill=INK, anchor="start", italic=False, lh=1.25, valign="baseline",
             rotate=0):
        lines = s.split("\n")
        if valign == "middle":
            y -= (len(lines) - 1) * size * lh / 2 - size * 0.35
        elif valign == "top":
            y += size * 0.9
        it = ' font-style="italic"' if italic else ""
        rot = f' transform="rotate({rotate} {x:.1f} {y:.1f})"' if rotate else ""
        spans, bold = [], False
        for i, l in enumerate(lines):
            inner, bold = _tspans(l, bold)
            spans.append(f'<tspan x="{x:.1f}" dy="{0 if i == 0 else size * lh:.1f}">{inner}</tspan>')
        spans = "".join(spans)
        self.add(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="{weight}" fill="{fill}" '
                 f'text-anchor="{anchor}"{it}{rot}>{spans}</text>')

    # ------------------------------------------------------------ rótulos com oclusão
    def label(self, x, y, s, key=None, size=12, weight=400, fill=INK, anchor="start", valign="baseline", pill=None,
              pad=(7, 4)):
        """Rótulo; pill=(fundo, borda) desenha uma etiqueta arredondada. Se key == hide vira '?'."""
        w = text_width(s, size, weight)
        n = s.count("\n") + 1
        h = size * 1.25 * n
        x0 = x - (w / 2 if anchor == "middle" else w if anchor == "end" else 0)
        if valign == "middle":
            y0 = y - h / 2
        elif valign == "top":
            y0 = y
        else:
            y0 = y - size * 0.95
        if key is not None and key == self.hide:
            pw, ph = max(w, 26) + 2 * pad[0], h + 2 * pad[1]
            cx = x0 + w / 2
            self.rect(cx - pw / 2, y0 - pad[1], pw, ph, fill=OCC, r=ph / 2 if n == 1 else 8)
            self.text(cx, y0 + h / 2, "?", size=size + 2, weight=800, fill="#fff", anchor="middle", valign="middle")
            return
        if pill:
            bg, bd = pill
            self.rect(x0 - pad[0], y0 - pad[1], w + 2 * pad[0], h + 2 * pad[1], fill=bg, stroke=bd, r=min(h / 2 + pad[1], 10))
        self.text(x, y, s, size, weight, fill, anchor, valign=valign)

    def box(self, x, y, w, h, title=None, body=None, color=BLUE, fill=None, key=None, size=12, align="middle",
            shadow=True, r=12):
        """Caixa de conceito: faixa colorida à esquerda, título em negrito e corpo."""
        self.rect(x, y, w, h, fill=fill or "#fff", stroke=color, r=r, sw=1.4, shadow=shadow)
        cx = x + w / 2 if align == "middle" else x + 12
        anchor = "middle" if align == "middle" else "start"
        parts = []
        if title:
            parts.append((title, size + 1, 700, color))
        if body:
            parts.append((body, size, 400, INK))
        total = sum(p[1] * 1.25 * (p[0].count("\n") + 1) for p in parts) + (4 if len(parts) == 2 else 0)
        yy = y + h / 2 - total / 2
        for s, sz, wt, col in parts:
            n = s.count("\n") + 1
            self.label(cx, yy, s, key=key if s is body or not body else None, size=sz, weight=wt, fill=col,
                       anchor=anchor, valign="top")
            yy += sz * 1.25 * n + 4

    # ------------------------------------------------------------ gráficos
    def axes(self, x, y, w, h, xr, yr, xticks=(), yticks=(), xlabel="", ylabel="", grid=True, tick_fmt=str):
        """Eixos cartesianos; devolve a função de mapeamento (dx, dy) -> (px, py)."""
        (x0, x1), (y0, y1) = xr, yr
        fx = lambda v: x + (v - x0) / (x1 - x0) * w
        fy = lambda v: y + h - (v - y0) / (y1 - y0) * h
        for t in yticks:
            if grid:
                self.line(x, fy(t), x + w, fy(t), stroke="#eceef1", sw=1)
            self.text(x - 7, fy(t), tick_fmt(t), size=10.5, fill=MUTE, anchor="end", valign="middle")
        for t in xticks:
            self.text(fx(t), y + h + 16, tick_fmt(t), size=10.5, fill=MUTE, anchor="middle")
        self.line(x, y + h, x + w, y + h, stroke="#9aa1ab", sw=1.3)
        self.line(x, y, x, y + h, stroke="#9aa1ab", sw=1.3)
        if xlabel:
            self.text(x + w / 2, y + h + 34, xlabel, size=11.5, fill=MUTE, anchor="middle")
        if ylabel:
            self.text(x - 42, y + h / 2, ylabel, size=11.5, fill=MUTE, anchor="middle", rotate=-90)
        return lambda dx, dy: (fx(dx), fy(dy))

    # ------------------------------------------------------------ saída
    def svg(self, width_attr=True):
        defs = ['<filter id="sh" x="-10%" y="-10%" width="130%" height="140%"><feDropShadow dx="0" dy="1.5" '
                'stdDeviation="2.2" flood-color="#1f2328" flood-opacity="0.13"/></filter>']
        for c in sorted(self.markers):
            i = "m" + c.strip("#")
            defs.append(f'<marker id="{i}" viewBox="0 0 10 10" refX="8.6" refY="5" markerWidth="7" markerHeight="7" '
                        f'orient="auto"><path d="M0,0.8 L9.5,5 L0,9.2 L2.6,5 z" fill="{c}"/></marker>')
            defs.append(f'<marker id="{i}s" viewBox="0 0 10 10" refX="1.4" refY="5" markerWidth="7" markerHeight="7" '
                        f'orient="auto"><path d="M10,0.8 L0.5,5 L10,9.2 L7.4,5 z" fill="{c}"/></marker>')
        wh = f' width="{self.w}" height="{self.h}"' if width_attr else ""
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}"{wh} '
                f'font-family="{FONT}"><defs>{"".join(defs)}</defs>{"".join(self.els)}</svg>')


def _catmull(pts, t=0.5):
    d = f"M{pts[0][0]:.1f},{pts[0][1]:.1f}"
    for i in range(len(pts) - 1):
        p0 = pts[i - 1] if i > 0 else pts[i]
        p1, p2 = pts[i], pts[i + 1]
        p3 = pts[i + 2] if i + 2 < len(pts) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) * t / 3, p1[1] + (p2[1] - p0[1]) * t / 3)
        c2 = (p2[0] - (p3[0] - p1[0]) * t / 3, p2[1] - (p3[1] - p1[1]) * t / 3)
        d += f" C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}"
    return d


def sample(fn, a, b, n=200):
    return [(a + (b - a) * i / (n - 1), fn(a + (b - a) * i / (n - 1))) for i in range(n)]


# ------------------------------------------------------------ exportação
def _font_css():
    import base64
    css = []
    for w in (400, 500, 600, 700, 800):
        for sub in ("latin", "latin-ext"):
            p = os.path.join(HERE, "web", "fonts", f"inter-{sub}-{w}-normal.woff2")
            b = base64.b64encode(open(p, "rb").read()).decode()
            css.append(f"@font-face{{font-family:Inter;font-weight:{w};src:url(data:font/woff2;base64,{b})}}")
    return "".join(css)


def export(module_name, figs, oclusoes, scale=2.4):
    """Grava svg/<nome>.svg e renderiza PNG (normal e cada oclusão) em fig/ para o Anki."""
    jobs = []
    for name, fn in figs.items():
        s = fn()
        open(os.path.join(SVG_DIR, name + ".svg"), "w").write(s)
        jobs.append({"svg": s, "png": os.path.join(HERE, "fig", name + ".png"), "scale": scale})
    for name, key, _, _ in oclusoes:
        jobs.append({"svg": figs[name](hide=key), "png": os.path.join(HERE, "fig", f"{name}__occ_{key}.png"), "scale": scale})
    jf = os.path.join(HERE, f".jobs_{module_name}.json")
    json.dump({"css": _font_css(), "jobs": jobs}, open(jf, "w"))
    subprocess.run(["node", os.path.join(HERE, "web", "render_svg.js"), jf], check=True)
    os.remove(jf)
    return len(jobs)
