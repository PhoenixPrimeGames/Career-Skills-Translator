
"""Automated UI tests for the Streamlit career-input form."""

from pathlib import Path

from streamlit.testing.v1 import AppTest


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


def test_valid_form_displays_success():
    """Valid input must pass validation without an AI request."""
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
    assert "information is valid" in app.success[0].value


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
