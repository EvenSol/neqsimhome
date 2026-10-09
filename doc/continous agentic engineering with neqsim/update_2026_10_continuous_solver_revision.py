#!/usr/bin/env python3
"""Apply the October 2026 Continuous Solver book revision.

The book was originally published as a self-contained Pandoc HTML file without
its manuscript source.  This script keeps the revision reviewable and
repeatable: every insertion has a stable anchor and the script refuses to
silently continue when the previous publication no longer matches.
"""

from pathlib import Path


HERE = Path(__file__).resolve().parent
BOOK = HERE / "Continuous_Agentic_Engineering_with_NeqSim.html"
REVISION_MARKER = "continuous-solver-revision-2026-10"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one anchor, found {count}")
    return text.replace(old, new, 1)


def main() -> None:
    text = BOOK.read_text(encoding="utf-8")
    if REVISION_MARKER in text:
        print("October 2026 revision is already applied")
        return

    text = replace_once(
        text,
        "NeqSim Project · First public edition · September 2026",
        "NeqSim Project · Public revision · October 2026",
        "edition line",
    )

    preface_anchor = (
        "tested improvements to NeqSim.</p>\n"
    )
    preface_addition = """tested improvements to NeqSim.</p>
<!-- continuous-solver-revision-2026-10 -->
<p><strong>October 2026 revision.</strong> The persistent-resume,
evidence-impact and reviewed Final Report capabilities described here are now
implemented on NeqSim's default branch. This revision adds the stop-today,
resume-tomorrow hand-off, the five-second status view, evidence-driven selective
reruns, the four-report contract and a multi-day acceptance walkthrough.</p>
"""
    text = replace_once(text, preface_anchor, preface_addition, "preface")

    task_anchor = (
        "result should become the accepted baseline.</p>\n"
        "<figure id=\"fig:living-plate\">"
    )
    task_addition = """result should become the accepted baseline.</p>
<blockquote>
<p><strong>The task folder, not the chat, is the source of truth.</strong>
Conversation context can help an agent work, but resuming the engineering task
must depend only on persisted goals, evidence hashes, cycle checkpoints,
results, decisions and reviewer records. The same contract applies to general
engineering tasks; the production-optimization case in this book is one public,
synthetic acceptance example rather than the product boundary.</p>
</blockquote>
<figure id="fig:living-plate">"""
    text = replace_once(text, task_anchor, task_addition, "durable task rule")

    chapter6_anchor = (
        "A pressure copied from the historian and then\n"
        "“predicted” from that same value is not validation.</p>\n"
        "<figure id=\"fig:monitor-plate\">"
    )
    chapter6_addition = """A pressure copied from the historian and then
“predicted” from that same value is not validation.</p>
<h2 data-number="6.1" id="evidence-change-impact-and-selective-reruns"><span class="header-section-number">6.1</span> Evidence change, impact and selective reruns</h2>
<p>A living task inventories configured technical evidence with task-relative
SHA-256 hashes. Added, modified and removed documents remain visible with their
before and after provenance. Start with the status view, then update only after
the impact is understood:</p>
<div class="sourceCode"><pre class="sourceCode bash"><code class="sourceCode bash">neqsim task-status &lt;task&gt;     # pending files, conclusions, stages and next action
neqsim task-update &lt;task&gt;     # record provenance and execute the impact plan</code></pre></div>
<p>Impact rules map an evidence family to affected calculation stages, KPIs and
conclusions. When every changed path is mapped, <code>task-update</code> reruns
those stages, their declared dependencies and the common KPI, goal, difference,
ledger and digest stages. Unaffected KPIs are retained with their source cycle.
The resulting Living Report records the change, provenance and rerun scope, and
the ordinary current-best Task Solver report is refreshed through its existing
canonical report settings.</p>
<p>The safety direction is conservative. An unmapped file causes a full planned
cycle. A degraded update, including one that does not recompute an affected KPI,
does not advance the accepted evidence inventory; the same change stays pending
for a safe retry. A newer unsupported evidence schema fails closed with an
upgrade message.</p>
<figure id="fig:monitor-plate">"""
    text = replace_once(text, chapter6_anchor, chapter6_addition, "evidence workflow")
    text = replace_once(
        text,
        '<h2 data-number="6.1" id="what-the-detector-computes"><span class="header-section-number">6.1</span>',
        '<h2 data-number="6.2" id="what-the-detector-computes"><span class="header-section-number">6.2</span>',
        "chapter 6.2 number",
    )
    text = replace_once(
        text,
        '<h2 data-number="6.2" id="score-the-backtest-against-a-decision"><span class="header-section-number">6.2</span>',
        '<h2 data-number="6.3" id="score-the-backtest-against-a-decision"><span class="header-section-number">6.3</span>',
        "chapter 6.3 number",
    )

    chapter7_anchor = "<p>The Standard first status"
    chapter7_addition = """<h2 data-number="7.1" id="stop-today-resume-tomorrow"><span class="header-section-number">7.1</span> Stop today, resume tomorrow</h2>
<p>Closing an editor, losing a process or moving to another supported machine
must not restart the investigation from memory. Copy or reopen the complete task
folder and begin with:</p>
<div class="sourceCode"><pre class="sourceCode bash"><code class="sourceCode bash">neqsim task-status &lt;task&gt;     # the five-second operational view
neqsim task-resume &lt;task&gt;     # continue the interrupted cycle or solve</code></pre></div>
<p><code>task-status</code> summarizes the goal, current conclusion, best
validated result, attempts and rejected hypotheses, blockers, evidence and
validation state, changes, last and next run, and the recommended next action.
It is reconstructed from the task folder and needs no prior conversation.</p>
<p>Resume reuses an incomplete cycle identifier and skips completed stages while
restoring their recorded outputs and side-effect metadata. If a cycle completed
just before the process stopped but its outer solve checkpoint did not, the solve
adopts that cycle rather than duplicating it. Versioned task state migrates the
earlier supported schema without dropping unknown fields, fails closed on a
newer incompatible schema, stores task-relative identity rather than checkout
paths and retains the writer provenance needed for an auditable machine hand-off.</p>
<p>The four report surfaces have deliberately different jobs:</p>
<table>
<thead><tr class="header"><th>Surface</th><th>Question answered</th><th>Contract</th></tr></thead>
<tbody>
<tr class="odd"><td><strong>Status</strong></td><td>What matters now?</td><td>Five-second operational view and next action from persisted state.</td></tr>
<tr class="even"><td><strong>Living Report</strong></td><td>How did the task get here?</td><td>Regenerated history of cycles, changes, decisions and audit links.</td></tr>
<tr class="odd"><td><strong>Current-best Task Solver report</strong></td><td>What is the best supported engineering answer?</td><td>The ordinary canonical Word/HTML report in <code>step3_report/</code>.</td></tr>
<tr class="even"><td><strong>Final Report</strong></td><td>What reviewed result was issued?</td><td>An immutable numbered revision generated through that same canonical pipeline.</td></tr>
</tbody>
</table>
<p>After a complete, non-degraded cycle has been reviewed and promoted and no
evidence change is pending, issue a delivery with
<code>neqsim task-report &lt;task&gt; --final --reviewer "A. Engineer"</code>.
The command writes <code>step3_report/final/FR-001/</code> (then FR-002 and so on)
without replacing the ordinary current-best report or the Living Report.</p>
<p>The Standard first status"""
    text = replace_once(text, chapter7_anchor, chapter7_addition, "resume and report contract")
    for old_number, new_number, ident in [
        ("7.1", "7.2", "schedule-monitoring"),
        ("7.2", "7.3", "triage-an-exception"),
        ("7.3", "7.4", "review-a-result"),
    ]:
        text = replace_once(
            text,
            f'<h2 data-number="{old_number}" id="{ident}"><span class="header-section-number">{old_number}</span>',
            f'<h2 data-number="{new_number}" id="{ident}"><span class="header-section-number">{new_number}</span>',
            f"chapter {new_number} number",
        )

    chapter9_anchor = (
        "incremental value remains a separate experiment.</p>\n"
        "<h1 data-number=\"10\""
    )
    chapter9_addition = '''incremental value remains a separate experiment.</p>
<h2 data-number="9.8" id="a-multi-day-final-report-handoff"><span class="header-section-number">9.8</span> A multi-day Final Report hand-off</h2>
<ol type="1">
<li><strong>Day 1 - solve and stop.</strong> Run <code>task-solve</code>. If a
later cycle is incomplete when work stops, leave the task folder intact; do not
summarize hidden chat state as the hand-off.</li>
<li><strong>Day 2 - inspect and resume.</strong> Reopen or copy the folder to
another supported machine. Run <code>task-status</code>, then
<code>task-resume</code>. Review the completed evidence and promote the validated
cycle.</li>
<li><strong>Day 3 - accept new evidence.</strong> Add a revised public datasheet
or other technical document. Status identifies its changed hash and affected
conclusions. <code>task-update</code> performs the mapped selective rerun and
retains unaffected KPIs with provenance. Review and promote the updated cycle.</li>
<li><strong>Generate Final Report.</strong> Run
<code>neqsim task-report &lt;task&gt; --final --reviewer NAME --note "Issued for delivery"</code>.
The ordinary current-best report remains in place, the Living Report retains the
three-day history, and <code>FR-001</code> becomes the standalone reviewed
delivery.</li>
</ol>
<p>The deterministic acceptance case exercises this sequence with general task
state and report machinery. The compressor study supplies public synthetic data;
it does not narrow the workflow to production optimization.</p>
<h1 data-number="10"''' 
    text = replace_once(text, chapter9_anchor, chapter9_addition, "multi-day acceptance")

    status_row = """<tr class="odd">
<td style="text-align: left;"><code>task-status</code></td>
<td style="text-align: left;">Inspect one or many living tasks</td>
<td style="text-align: left;">State, phase and next action.</td>
</tr>"""
    enhanced_rows = """<tr class="odd">
<td style="text-align: left;"><code>task-resume</code></td>
<td style="text-align: left;">Resume an interrupted cycle or solve from persisted state</td>
<td style="text-align: left;">Same cycle, restored checkpoints and next action.</td>
</tr>
<tr class="even">
<td style="text-align: left;"><code>task-update</code></td>
<td style="text-align: left;">Detect evidence changes, analyze impact and rerun safely</td>
<td style="text-align: left;">Hashes, provenance, affected conclusions and selective-rerun manifest.</td>
</tr>
<tr class="odd">
<td style="text-align: left;"><code>task-status</code></td>
<td style="text-align: left;">Read the five-second view for one or many living tasks</td>
<td style="text-align: left;">Conclusion, evidence, changes, blockers and next action.</td>
</tr>"""
    text = replace_once(text, status_row, enhanced_rows, "command map status")

    report_row = """<tr class="even">
<td style="text-align: left;"><code>task-report</code></td>
<td style="text-align: left;">Rebuild the living or formal report</td>
<td style="text-align: left;"><code>LIVING_REPORT.md</code> and optional
formal output.</td>
</tr>"""
    enhanced_report_rows = """<tr class="even">
<td style="text-align: left;"><code>task-report [--formal]</code></td>
<td style="text-align: left;">Rebuild the Living Report and optionally the ordinary current-best report</td>
<td style="text-align: left;"><code>LIVING_REPORT.md</code> and canonical Word/HTML outputs.</td>
</tr>
<tr class="odd">
<td style="text-align: left;"><code>task-report --final --reviewer NAME</code></td>
<td style="text-align: left;">Generate or reuse an immutable reviewed delivery revision</td>
<td style="text-align: left;"><code>final/FR-NNN/</code>, manifest and canonical Word/HTML outputs.</td>
</tr>"""
    text = replace_once(text, report_row, enhanced_report_rows, "command map report")

    terms_anchor = """<strong>Campaign.</strong> A recurring issue to PR software improvement
workflow with a persistent engineering goal.</p>"""
    terms_addition = """<strong>Campaign.</strong> A recurring issue to PR software improvement
workflow with a persistent engineering goal. <strong>Status.</strong> A compact
operational view reconstructed from task evidence. <strong>Living
Report.</strong> The regenerated history of changes, cycles and decisions.
<strong>Current-best Task Solver report.</strong> The ordinary canonical
engineering report representing the best supported answer.
<strong>Final Report.</strong> A named-reviewer, immutable delivery revision
generated from the canonical report pipeline after readiness checks.</p>"""
    text = replace_once(text, terms_anchor, terms_addition, "terms")

    repro_start = "<p>This book’s implementation descriptions were checked against the\n"
    repro_end = (
        "qualification or autonomous-agent performance benchmark is claimed.</p>"
    )
    start = text.find(repro_start)
    end = text.find(repro_end, start)
    if start < 0 or end < 0:
        raise RuntimeError("reproducibility record anchors not found")
    end += len(repro_end)
    repro = """<p>This book's implementation descriptions were rechecked on 9 October
2026 against NeqSim default-branch commit
<code>ffde2f43443ae65d57d02497e31fefb71b637555</code>, including
<code>docs/development/CONTINUOUS_TASK_SOLVING.md</code>, the continuous-task
CLI and state/evidence/final-report implementations, the public skill,
<code>AGENTS.md</code> and <code>ImprovementCycle.java</code>. The focused
Task Solver regression set completed 105 tests, including the deterministic
multi-day acceptance case that generates canonical Word and self-contained HTML
Final Report outputs. The figures remain original conceptual drawings. Chapter
9's NeqSim 3.20.0 capacity calculations and twelve-cycle synthetic replay retain
their saved runtime versions, source hash, inputs and outputs. They are distinct
from the schematic reference timeline and do not claim a live facility
connection, vendor-map qualification or autonomous-agent performance
benchmark.</p>"""
    text = text[:start] + repro + text[end:]

    text = text.replace("Source inspected September 2026.", "Source rechecked October 2026.")
    text = text.replace("Accessed September 2026.", "Accessed October 2026.")

    BOOK.write_text(text, encoding="utf-8")
    print(f"Updated {BOOK.name}")


if __name__ == "__main__":
    main()
