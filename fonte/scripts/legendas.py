"""Extrai as legendas completas das figuras usadas no material e grava
fonte/figuras/legendas.json (usado pelos README dos temas).

A legenda de uma figura é a sequência de trechos de texto em corpo pequeno que
começa em "Figura N.N" e segue até o texto voltar ao corpo normal. Os sobrescritos
(1ª, 2ª, 6ª ed.) ficam em corpo ainda menor e são mantidos no lugar, o que evita
cortar a legenda no meio, como acontecia ao pegar só o primeiro bloco de texto.

uso: python3 fonte/scripts/legendas.py
"""
import json
import re
from pathlib import Path

import pymupdf as fitz

FONTE = Path(__file__).resolve().parents[1]
# livro: pasta das figuras, PDF, páginas onde procurar, corpo do texto corrido (pt)
LIVROS = {
    "p": ("porto", "/mnt/project-files/Semiologia Médica.pdf", range(500, 700), 7.2),
    "g": ("guyton", "/mnt/project-files/Tratado de Fisiologia Médica.pdf", range(340, 920), 14.5),
}
SOBRESCRITO = {"a": "ª", "o": "º"}
ROTULO = re.compile(r"^\s*Figura\s*\d+\.\d+")


def linhas(pagina):
    """Linhas da página na ordem de leitura; cada uma é a lista de seus trechos (span)."""
    for b in pagina.get_text("dict")["blocks"]:
        for linha in b.get("lines", []):
            if linha["spans"]:
                yield linha["spans"]


def texto_linha(spans, tam):
    partes = []
    for x in spans:
        t = x["text"]
        if x["size"] < tam * 0.75:  # sobrescrito: 1ª bulha, 6ª ed.
            t = SOBRESCRITO.get(t.strip(), t.strip())
        partes.append(t)
    return "".join(partes).replace("\xa0", " ")


def junta(partes):
    texto = ""
    for p in partes:
        p = p.strip()
        if not texto:
            texto = p
        elif texto.endswith(("-", "\xad")):  # hífen no fim da linha: emenda sem espaço
            texto += p
        else:
            texto += " " + p
    texto = re.sub(r"\s+", " ", texto.replace("\xad", "-")).strip()
    return re.sub(r"(\d) ([ªº])", r"\1\2", texto)


def legenda(doc, paginas, corpo, cap, num):
    rotulo = re.compile(rf"^\s*Figura\s*{cap}\.{num}(?!\d)")
    for i in paginas:
        ls = list(linhas(doc[i]))
        for j, sp in enumerate(ls):
            s = sp[0]
            # o rótulo da legenda está em corpo menor que o texto corrido
            if not rotulo.match(s["text"].replace("\xa0", " ")) or s["size"] > corpo - 1:
                continue
            tam, partes, parou = s["size"], [], False
            for k, l in enumerate(ls[j:]):
                principal = max(l, key=lambda x: len(x["text"]))
                if k and (ROTULO.match(texto_linha(l, tam)) or principal["size"] > tam + 0.4):
                    parou = True
                    break
                partes.append(texto_linha(l, tam))
            if not parou and i + 1 < doc.page_count:
                # a legenda continua no alto da página seguinte
                for l in sorted(linhas(doc[i + 1]), key=lambda l: l[0]["bbox"][1]):
                    principal = max(l, key=lambda x: len(x["text"]))
                    if abs(principal["size"] - tam) > 0.4 or ROTULO.match(texto_linha(l, tam)):
                        break
                    partes.append(texto_linha(l, tam))
            return junta(partes)
    return None


def main():
    saida = {}
    for pref, (pasta, pdf, paginas, corpo) in LIVROS.items():
        doc = fitz.open(pdf)
        for f in sorted((FONTE / "figuras" / pasta).glob("*.png")):
            k = f.stem
            m = re.match(rf"{pref}(\d+)_(\d+)", k)
            cap, num = m.group(1), int(m.group(2))
            leg = legenda(doc, paginas, corpo, cap, num)
            if not leg:
                print("sem legenda:", k)
                continue
            saida[k] = leg
    destino = FONTE / "figuras" / "legendas.json"
    destino.write_text(json.dumps(saida, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{len(saida)} legendas em {destino}")


if __name__ == "__main__":
    main()
