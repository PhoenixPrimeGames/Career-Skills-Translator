"""Unit tests for strict, extensible result schemas."""

import pytest
from pydantic import ValidationError

from schemas import AnalysisResult, SkillTranslation


VALID_SKILL = {
    "skill": "Root-cause analysis",
    "source_evidence": "diagnose electrical equipment failures",
    "target_application": "Investigating software defects",
    "explanation": "Both involve investigating causes.",
    "limitations": "Does not establish programming proficiency.",
}


def test_completed_analysis_accepts_supported_skill():
    result = AnalysisResult.model_validate({
        "status": "completed",
        "summary": "Some technical experience transfers.",
        "skills": [VALID_SKILL],
    })
    assert result.skills[0].skill == "Root-cause analysis"


def test_insufficient_information_accepts_empty_list():
    result = AnalysisResult(
        status="insufficient_information",
        summary="Insufficient details were provided.",
        skills=[],
    )
    assert result.skills == []


def test_missing_required_skill_field_rejected():
    incomplete_skill = {
        k: v for k, v in VALID_SKILL.items()
        if k != "limitations"
    }
    with pytest.raises(ValidationError):
        SkillTranslation.model_validate(incomplete_skill)


def test_extra_field_rejected():
    with pytest.raises(ValidationError):
        SkillTranslation.model_validate({
            **VALID_SKILL,
            "unapproved_field": "text",
        })


def test_whitespace_only_skill_field_rejected():
    with pytest.raises(ValidationError):
        SkillTranslation.model_validate({
            **VALID_SKILL,
            "explanation": "   ",
        })


@pytest.mark.parametrize("status,skills", [
    ("completed", []),
    ("insufficient_information", [VALID_SKILL]),
])
def test_status_list_mismatch_rejected(status, skills):
    with pytest.raises(ValidationError):
        AnalysisResult.model_validate({
            "status": status,
            "summary": "Summary",
            "skills": skills,
        })


def test_titles_available_for_future_renderer():
    assert (
        SkillTranslation.model_fields["source_evidence"].title
        == "Source Evidence"
    )
