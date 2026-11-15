
"""Automated UI tests for the Streamlit career-input form."""

from pathlib import Path
from streamlit.testing.v1 import AppTest
from unittest.mock import Mock
import analysis
from app import format_analysis
from analysis import AnalysisUnavailableError
from schemas import AnalysisResult, SkillTranslation

APP_PATH = Path(__file__).resolve().parents[1] / "app.py"


def load_app() -> AppTest:
    """Start a simulated instance of the Streamlit application."""
    return AppTest.from_file(str(APP_PATH)).run()


def test_form_displays_required_fields():
    """The initial interface must display all required inputs."""
    app = load_app()

    assert not app.exception
    assert len(app.text_input) == 2
    assert len(app.text_area) == 1
    assert len(app.form_submit_button) == 1


def test_empty_form_displays_validation_errors():
    """An empty submission must produce three field errors."""
    app = load_app()

    app.form_submit_button[0].click().run()

    assert not app.exception
    assert len(app.error) == 3



def test_valid_form_displays_success(monkeypatch):
    """A valid submission displays mocked AI results."""
    monkeypatch.setenv("OPENAI_API_KEY", "fake-test-key")

    expected = AnalysisResult(
        status="completed",
        summary="Troubleshooting experience may transfer.",
        skills=[
            SkillTranslation(
                skill="Root-cause analysis",
                source_evidence="diagnose electrical equipment failures",
                target_application="Software defect investigation",
                explanation="Both involve investigating causes.",
                limitations="Does not establish programming proficiency.",
            )
        ],
    )

    fake_analysis = Mock(return_value=expected)
    monkeypatch.setattr(analysis, "analyze_career", fake_analysis)

    app = load_app()

    app.text_input[0].input("Engineering Technician")
    app.text_area[0].input(
        "I diagnose electrical equipment failures "
        "and document troubleshooting procedures."
    )
    app.text_input[1].input("Software Development")

    app.form_submit_button[0].click().run()

    assert not app.exception
    assert len(app.error) == 0
    assert len(app.success) == 1
    assert "Analysis completed" in app.success[0].value
    fake_analysis.assert_called_once()



def test_short_experience_displays_error():
    """A description below the minimum length must be rejected."""
    app = load_app()

    app.text_input[0].input("Technician")
    app.text_area[0].input("Short description")
    app.text_input[1].input("Software Development")

    app.form_submit_button[0].click().run()

    assert not app.exception
    assert len(app.success) == 0
    assert any(
        "at least 20 characters" in message.value
        for message in app.error
    )


def test_invalid_form_never_calls_ai(monkeypatch):
    """Invalid information must not trigger an API request."""
    monkeypatch.setenv("OPENAI_API_KEY", "fake-test-key")

    fake_analysis = Mock()
    monkeypatch.setattr(analysis, "analyze_career", fake_analysis)

    app = load_app()
    app.form_submit_button[0].click().run()

    assert not app.exception
    assert len(app.error) == 3
    fake_analysis.assert_not_called()


def test_insufficient_information_result(monkeypatch):
    """A valid empty-skill result should display useful feedback."""
    monkeypatch.setenv("OPENAI_API_KEY", "fake-test-key")

    fake_analysis = Mock(return_value=AnalysisResult(
        status="insufficient_information",
        summary="The description lacks sufficient supporting evidence.",
        skills=[],
    ))
    monkeypatch.setattr(analysis, "analyze_career", fake_analysis)

    app = load_app()
    app.text_input[0].input("Technician")
    app.text_area[0].input(
        "I perform general duties and help with daily operations."
    )
    app.text_input[1].input("Software Development")

    app.form_submit_button[0].click().run()

    assert not app.exception
    assert len(app.warning) == 1
    fake_analysis.assert_called_once()


def test_api_failure_displays_safe_message(monkeypatch):
    """An API failure must not expose internal provider details."""
    monkeypatch.setenv("OPENAI_API_KEY", "fake-test-key")

    fake_analysis = Mock(
        side_effect=AnalysisUnavailableError(
            "The AI service could not process the request."
        )
    )
    monkeypatch.setattr(analysis, "analyze_career", fake_analysis)

    app = load_app()
    app.text_input[0].input("Technician")
    app.text_area[0].input(
        "I diagnose equipment problems and document repairs."
    )
    app.text_input[1].input("Software Development")

    app.form_submit_button[0].click().run()

    assert not app.exception
    assert len(app.error) == 1
    assert "could not process" in app.error[0].value


def test_copyable_text_contains_all_schema_fields():
    """The export uses the central schema's field definitions."""
    result = AnalysisResult(
        status="completed",
        summary="Technical experience may transfer.",
        skills=[
            SkillTranslation(
                skill="Troubleshooting",
                source_evidence="diagnose equipment failures",
                target_application="Software debugging",
                explanation="Both involve finding causes.",
                limitations="Does not establish software experience.",
            )
        ],
    )

    output = format_analysis(result)

    for field in SkillTranslation.model_fields.values():
        assert field.title in output

    assert result.summary in output
    assert "does not verify professional qualifications" in output
