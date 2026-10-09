#!/usr/bin/env python3
"""Regenerate the published PDF from the self-contained HTML edition."""

from pathlib import Path

from weasyprint import CSS, HTML


HERE = Path(__file__).resolve().parent
HTML_BOOK = HERE / "Continuous_Agentic_Engineering_with_NeqSim.html"
PDF_BOOK = HERE / "Continuous_Agentic_Engineering_with_NeqSim.pdf"

PRINT_CSS = r"""
@page {
  size: Letter;
  margin: 0.67in 0.64in 0.72in;
  @top-left {
    content: "CONTINUOUS AGENTIC ENGINEERING WITH NEQSIM";
    color: #526979;
    font: 6.5pt "DejaVu Sans", sans-serif;
    letter-spacing: 0.08em;
  }
  @top-right {
    content: "OCTOBER 2026 PUBLIC REVISION";
    color: #526979;
    font: 6.5pt "DejaVu Sans", sans-serif;
    letter-spacing: 0.06em;
  }
  @bottom-center {
    content: counter(page);
    color: #526979;
    font: 7pt "DejaVu Sans", sans-serif;
  }
}
@page :first {
  margin: 0;
  @top-left { content: none; }
  @top-right { content: none; }
  @bottom-center { content: none; }
}
html, body { font-size: 9.7pt !important; line-height: 1.48 !important; }
main { padding: 0 !important; }
.front-cover {
  box-sizing: border-box;
  width: 8.5in !important;
  height: 11in !important;
  margin: 0 !important;
  break-after: page !important;
  aspect-ratio: auto !important;
}
.front-cover h1 { font-size: 34pt !important; line-height: 0.99 !important; break-before: auto !important; }
.cover-series { font-size: 7.5pt !important; }
.cover-subtitle { font-size: 12pt !important; }
.cover-credit { font-size: 18pt !important; }
main > h1:first-of-type { font-size: 23pt !important; }
h1 { font-size: 19pt !important; line-height: 1.13 !important; break-before: page !important; }
h2 { font-size: 13.5pt !important; line-height: 1.2 !important; }
h3 { font-size: 11pt !important; }
p, li { orphans: 3; widows: 3; }
figure, pre, table, blockquote { break-inside: avoid; }
figure img { max-height: 7.45in; object-fit: contain; }
table { font-size: 7.8pt; }
pre { font-size: 7.5pt; }
blockquote {
  margin: 1.1em 0;
  padding: 0.55em 0.85em;
  border-left: 4px solid #39a9b8;
  background: #eef7f8;
}
"""


def main() -> None:
    HTML(filename=str(HTML_BOOK), base_url=str(HERE)).write_pdf(
        str(PDF_BOOK), stylesheets=[CSS(string=PRINT_CSS)]
    )
    print(f"Wrote {PDF_BOOK.name}")


if __name__ == "__main__":
    main()
