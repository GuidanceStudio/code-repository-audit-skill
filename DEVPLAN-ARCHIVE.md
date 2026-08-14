# Devplan Archive

Closed milestones, compressed to one line each. The sha is the pointer to the
full detail (Why/Approach/Tasks/Deviations) — it already lives in the commit
that shipped the milestone; `git show <sha>` recovers it. Where a milestone's
content shipped inside a commit whose message covers something else (e.g. M17-19
inside `a4f9b21`, nominally a repo-rename commit; M20/M22-26 inside `252c512`,
labelled "v0.4 token essentiality pass"), the sha points to that shipping
commit, not to the later devplan-only commit that only ticked the checkboxes.
Shas were re-derived from the current `git log` on 2026-08-14 (this repo's
history was flagged as force-rewritten today; re-checked against `origin/main`
before this file was committed — no divergence found at write time). M1-M9
are not archived: their headings carry no done marker (only a "Status: DONE"
line in the body), so they don't meet the archiving gate. Ordered by milestone
number (M20/M27-29 ship later, on 2026-07-03, than the M22-26 block they sit
between chronologically).

## Section context kept out of the compression

The archiving pass removed the section headers whose milestones all closed. Two
paragraphs under them were not milestone detail but the decisions the sections
were built on, so they are kept here verbatim rather than compressed away.

**v0.3 — Generic packaging + UX/UI depth.** Two arcs from the 2026-06-10
discussion. *Packaging:* the skill was nested under `claude/code-audit/` and
worded for Claude; research confirmed `SKILL.md` is a cross-assistant standard
(agentskills.io — Claude Code, Codex CLI, opencode all read the same folder
verbatim), so flattening + de-Claudizing makes one payload installable
everywhere, with a root installer that targets each assistant. *Content:* the
framework had no dedicated UX or UI dimension (D12 is admin-surface source only
and defers rendered review to the `ui-review` skill); a UX level and a UI level
were added, each source-level by default with an advanced rendered pass
(Playwright, delegated to `ui-review`).

**User decisions (2026-06-10):** installer = **broad** (native `SKILL.md` for
Claude + Codex + opencode, TOML for Gemini, generated `AGENTS.md` for the
Cursor/Windsurf/Copilot/Aider/Continue tier, plus a manual-copy path); UX/UI =
**hybrid** (base source-level always; advanced fires Playwright via
`ui-review`). Order followed: M10 → M11 → M12 (packaging first, so content
lands on the flat generic layout) → M13 → M14.

## Milestones

M10 | Flatten the layout | 2026-06-10 | ddbb263
M11 | De-Claudize the content | 2026-06-10 | 56799e1
M12 | Root multi-assistant installer | 2026-06-10 | 947217c
M13 | D15 — UX & interaction design | 2026-06-10 | 8c19722
M14 | D16 — UI & design-system craft | 2026-06-10 | b39d0d3
M15 | Add the Ponytail essentiality ladder to D1 | 2026-06-19 | 0f79a91
M16 | Lock the integration contract with content tests | 2026-06-19 | df28608
M17 | Comment essentiality — flag dead-weight comments in D01 | 2026-06-20 | a4f9b21
M18 | `ponytail:` recognition — audit-aware intentional shortcuts | 2026-06-20 | a4f9b21
M19 | Debt tracking cross-reference — `.code-audit/debt.tsv` in the audit loop | 2026-06-20 | a4f9b21
M20 | Unify severity scale across tech-audit and uxui-audit — adopt 0–4 everywhere | 2026-06-20 | 252c512
M21 | Align audit directories — `.code-audit/` vs `.tech-audit/` | 2026-07-03 | 87e6a8e
M22 | Compress finding-phrasing.md — tone vignettes, severity-vs-confidence, Bad→Good table | 2026-06-20 | 252c512
M23 | Compress SKILL.md — Topics column, meta-commentary, stack detection, pipeline | 2026-06-20 | 252c512
M24 | Compress D01 — shell code blocks, redundant commentary | 2026-06-20 | 252c512
M25 | Deduplicate cuts + operations — remove dimension-treatment restatements | 2026-06-20 | 252c512
M26 | Trim READMEs | 2026-06-20 | 252c512
M27 | Finding provenance — hedge-word gate, origin-not-symptom locations, fan-out briefs | 2026-07-03 | ac4381f
M28 | Commit the uxui-audit decoupling — standalone payload | 2026-07-03 | 6206613
M29 | Close the coherence gaps — debt readers, forge-flow-shaped stubs, confidence policy note | 2026-07-03 | 0813f32
M30 | Remove narrative comments from tests | 2026-08-14 | e11a671
