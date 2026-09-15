#!/usr/bin/env python3
"""Gera um PDF de livro a partir do markdown produzido pelo /digerir.

Uso:
    python3 build_pdf.py livro.md
    python3 build_pdf.py livro.md --title "GTD" --subtitle "66 fontes" --header "GTD"
    python3 build_pdf.py livro.md --cover-from-h1   # usa o primeiro # e ## como capa

Requer:  pip install weasyprint markdown
"""
import argparse
import pathlib
import re
import sys

try:
    import markdown
except ImportError:
    sys.exit("faltou a lib markdown: pip install markdown")


CSS = """
@page {
  size: 170mm 240mm;
  margin: 20mm 18mm 18mm 18mm;
  @top-center {
    content: string(bookheader);
    font-family: Georgia, serif; font-size: 7.5pt;
    letter-spacing: .12em; color: #9a9187;
  }
  @bottom-center {
    content: counter(page);
    font-family: Georgia, serif; font-size: 8.5pt; color: #9a9187;
  }
}
@page :first { @top-center { content: none; } @bottom-center { content: none; } }

html { string-set: bookheader "%%HEADER%%"; }

body {
  font-family: Georgia, "Times New Roman", serif;
  font-size: 10.2pt; line-height: 1.62;
  color: #23201d; hyphens: auto; text-align: justify;
}

h1, h2, h3, h4 {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  color: #1a1714; text-align: left; hyphens: none;
  page-break-after: avoid;
}
h1 {
  font-size: 19pt; line-height: 1.18; margin: 0 0 1.4em;
  page-break-before: always; padding-top: .2em;
  border-bottom: 2px solid #23201d; padding-bottom: .35em;
}
h2 { font-size: 13pt; margin: 2.2em 0 .7em; }
h3 { font-size: 11pt; margin: 1.7em 0 .5em; color: #4a433c; }
h4 { font-size: 10pt; margin: 1.3em 0 .4em; color: #6b6259; }

p { margin: 0 0 .85em; }
strong { color: #000; }

blockquote {
  margin: 1.1em 0; padding: .1em 0 .1em 1.1em;
  border-left: 2.5px solid #c9b8a0;
  color: #4a433c; font-style: italic;
  page-break-inside: avoid;
}
blockquote p { margin-bottom: .5em; }
blockquote p:last-child { margin-bottom: 0; }

ul, ol { margin: 0 0 .9em; padding-left: 1.3em; }
li { margin-bottom: .32em; }

table {
  width: 100%; border-collapse: collapse; margin: 1.2em 0;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 8.6pt; page-break-inside: avoid; text-align: left;
}
th {
  background: #efe9e0; border-bottom: 1.5px solid #b9ac99;
  padding: .45em .6em; font-weight: 600; hyphens: none;
}
td { border-bottom: .5px solid #ddd5c9; padding: .45em .6em; vertical-align: top; hyphens: none; }
tr:nth-child(even) td { background: #faf7f3; }

pre {
  background: #f6f2ec; border: .5px solid #e0d8cc; border-radius: 3px;
  padding: .7em .9em; margin: 1.1em 0;
  font-family: "DejaVu Sans Mono", "Courier New", monospace;
  font-size: 7.4pt; line-height: 1.35; white-space: pre;
  page-break-inside: avoid; text-align: left; hyphens: none;
  overflow-wrap: normal;
}
code {
  font-family: "DejaVu Sans Mono", "Courier New", monospace;
  font-size: 8.4pt; background: #f2ece4; padding: .08em .3em; border-radius: 2px;
}
pre code { background: none; padding: 0; font-size: inherit; }

hr { border: none; border-top: .5px solid #d8cfc2; margin: 2em 0; }

.cover { page-break-after: always; text-align: left; padding-top: 55mm; }
.cover h1 {
  font-size: 40pt; border: none; padding: 0; margin: 0 0 .35em;
  page-break-before: avoid; letter-spacing: -.02em;
}
.cover .sub {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 12pt; color: #6b6259; line-height: 1.45; font-style: normal;
}
.cover .rule { border-top: 2px solid #23201d; width: 60mm; margin: 1.6em 0; }

.front h1 { page-break-before: avoid; }
.pagebreak { page-break-after: always; }
"""


def main():
    ap = argparse.ArgumentParser(description="markdown do /digerir -> PDF de livro")
    ap.add_argument("source", help="arquivo .md")
    ap.add_argument("-o", "--out", help="PDF de saída (padrão: mesmo nome, .pdf)")
    ap.add_argument("--title", help="título da capa (padrão: primeiro # do arquivo)")
    ap.add_argument("--subtitle", help="subtítulo da capa (padrão: primeiro ## do arquivo)")
    ap.add_argument("--header", help="texto do cabeçalho das páginas (padrão: o título)")
    ap.add_argument("--body-starts-at", default=None,
                    help="string que marca o início do corpo, ex: '\\n# Parte I'. "
                         "Antes dela é front matter (sem quebra de página por capítulo)")
    ap.add_argument("--html-only", action="store_true", help="gera só o .html")
    args = ap.parse_args()

    src = pathlib.Path(args.source)
    raw = src.read_text(encoding="utf-8")

    # título e subtítulo: dos argumentos ou do topo do arquivo
    m_title = re.search(r"^#\s+(.+)$", raw, re.M)
    m_sub = re.search(r"^##\s+(.+)$", raw, re.M)
    title = args.title or (m_title.group(1).strip() if m_title else src.stem)
    subtitle = args.subtitle or (m_sub.group(1).strip() if m_sub else "")
    header = args.header or title

    # remove o título/subtítulo do corpo, já que viram capa
    body_raw = raw
    if m_title and not args.title:
        body_raw = body_raw.replace(m_title.group(0), "", 1)
    if m_sub and not args.subtitle:
        body_raw = body_raw.replace(m_sub.group(0), "", 1)
    body_raw = body_raw.lstrip("\n-\n ")

    # separa front matter do corpo, se pedido
    front_md, rest_md = "", body_raw
    if args.body_starts_at:
        marker = args.body_starts_at.replace("\\n", "\n")
        i = body_raw.find(marker)
        if i > 0:
            front_md, rest_md = body_raw[:i], body_raw[i:]

    # "---" seguido de "---" vira quebra de página explícita
    rest_md = re.sub(r"\n---\n+---\n", "\n\n<!--PAGEBREAK-->\n\n", rest_md)

    md = markdown.Markdown(extensions=["tables", "fenced_code", "attr_list", "sane_lists"])
    front_html = md.convert(front_md) if front_md else ""
    md.reset()
    body_html = md.convert(rest_md)
    body_html = body_html.replace("<p><!--PAGEBREAK--></p>", '<div class="pagebreak"></div>')

    def esc(s):
        return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    cover = f'<div class="cover"><h1>{esc(title)}</h1><div class="rule"></div>'
    if subtitle:
        cover += f'<div class="sub">{esc(subtitle)}</div>'
    cover += "</div>"

    html = (
        "<!doctype html><html><head><meta charset='utf-8'>"
        f"<title>{esc(title)}</title>"
        f"<style>{CSS.replace('%%HEADER%%', esc(header))}</style></head><body>"
        f"{cover}"
        + (f'<div class="front">{front_html}</div>' if front_html else "")
        + body_html
        + "</body></html>"
    )

    html_path = src.with_suffix(".html")
    html_path.write_text(html, encoding="utf-8")
    print("HTML:", html_path)
    if args.html_only:
        return

    try:
        from weasyprint import HTML
    except ImportError:
        sys.exit("faltou o weasyprint: pip install weasyprint  (o .html já foi gerado)")

    out = pathlib.Path(args.out) if args.out else src.with_suffix(".pdf")
    HTML(str(html_path)).write_pdf(str(out))
    print("PDF:", out)


if __name__ == "__main__":
    main()
