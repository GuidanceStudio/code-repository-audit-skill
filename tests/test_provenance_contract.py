"""Contract tests for the M27 provenance and M29 pipeline/phrasing rules."""

from __future__ import annotations

from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
SKILL = REPO / "tech-audit"
PHRASING = SKILL / "templates" / "finding-phrasing.md"
ROUTER = SKILL / "SKILL.md"
FULL = SKILL / "cuts" / "full.md"


def _section(text: str, heading: str) -> str:
    """Return the body of a markdown section up to the next same-level heading."""
    start = text.index(heading)
    level = heading.split(" ")[0] + " "
    end = text.find("\n" + level, start + len(heading))
    return text[start:end] if end != -1 else text[start:]


def test_phrasing_gates_hedge_words_to_needs_verification() -> None:
    text = PHRASING.read_text()
    line = next(
        (ln for ln in text.splitlines() if '"probably"' in ln),
        "",
    )
    assert line, "hedge-word calibration missing"
    for word in ('"likely"', '"may"', '"seems"'):
        assert word in line
    assert "needs-verification" in line
    assert "observed fact" in line


def test_phrasing_requires_origin_not_symptom_locations() -> None:
    fmt = _section(PHRASING.read_text(), "## Finding format")
    assert "originate" in fmt
    assert "symptom" in fmt


def test_pipeline_caps_unread_yellow_findings() -> None:
    pipeline = _section(ROUTER.read_text(), "## Findings pipeline")
    assert "🟡" in pipeline
    assert "grep" in pipeline.lower()
    assert "needs-verification" in pipeline


def test_pipeline_filters_every_dimension_through_debt_register() -> None:
    """M29: the debt filter is a pipeline rule for EVERY dimension, not a D01 quirk."""
    pipeline = _section(ROUTER.read_text(), "## Findings pipeline")
    line = next(
        (ln for ln in pipeline.splitlines() if ".tech-audit/debt.tsv" in ln),
        "",
    )
    assert line, "pipeline debt-rule line missing"
    assert "every dimension" in line.lower()
    assert "once per run" in line
    # D01 stays the contract's single source — the rule references, never restates.
    assert "D01-code-essentiality.md" in line
    assert "suppress" in line
    assert "promote" in line


def test_severity_confidence_axes_carry_a_rationale() -> None:
    """M29: the independent-axes policy states WHY, generically."""
    sec = _section(PHRASING.read_text(), "## Severity vs confidence")
    assert "triage can usually verify" in sec
    assert "discount" in sec.lower()


def test_fanout_specifies_agent_brief_and_single_dispatch() -> None:
    fanout = _section(FULL.read_text(), "## Execution: fan-out")
    assert "single response" in fanout
    assert "languages/" in fanout
    assert "TSV schema" in fanout
    assert "inventory" in fanout
    assert "modify nothing" in fanout
