# October 2026 public revision

This revision was made after NeqSim's persistent resume/status, evidence-impact
and Final Report capability groups were merged to the default branch and their
focused regression set passed on commit
`ffde2f43443ae65d57d02497e31fefb71b637555`.

It adds or strengthens:

- the task folder, rather than chat history, as the durable source of truth;
- the stop-today/resume-tomorrow and cross-machine hand-off;
- the five-second Status view;
- document/evidence hashes, impact analysis, conservative selective reruns and
  updated current-best reporting;
- the distinction among Status, Living Report, ordinary current-best Task
  Solver report and immutable reviewed Final Report;
- a general multi-day acceptance walkthrough ending in Generate Final Report;
- current CLI commands, command-map entries and exact reproducibility evidence.

## Rebuild

The checked-in publication did not include its original manuscript. The
self-contained HTML is therefore the publication source. The companion update
script records every October insertion against stable anchors and refuses to
silently apply to a different prior edition.

```bash
python update_2026_10_continuous_solver_revision.py
python -m pip install weasyprint
python build_publication.py
```

Validate the generated PDF with `pdfinfo`, text extraction and rendered-page
inspection before publishing. Validate all non-fragment links in the HTML and
confirm that the relative PDF download link resolves beside the HTML file.

## Validation for this revision

- Current NeqSim `master`: 105 focused Task Solver tests passed, including the
  multi-day canonical Word/HTML Final Report acceptance case.
- Revision and build scripts: Python byte-compilation passed.
- HTML: parsed successfully; all 152 internal fragment links resolve; the
  relative PDF download resolves beside the HTML.
- External links: 22 unique targets checked. Public sites returned HTTP 200;
  GitHub file targets affected by transient web 503 responses were separately
  verified against the current NeqSim checkout or through the GitHub API.
- PDF: 61 Letter pages, text extraction confirmed every new workflow section,
  and rendered-page review covered the full contact sheet plus the cover,
  evidence, resume/report, multi-day, command-reference and final pages.
