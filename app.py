
"""Streamlit interface for Career Skills Translator.

Milestone 3.4A: Collect and validate career information.
AI analysis will be connected in Milestone 3.4B.
"""

import streamlit as st
from pydantic import ValidationError

from validation import CareerInput


FIELD_LABELS = {
    "current_occupation": "Current occupation",
    "experience_description": "Responsibilities and experience",
    "target_career_field": "Target career field",
}


def validation_messages(error: ValidationError) -> list[str]:
    """Convert Pydantic validation errors into safe, readable messages."""
    messages = []

    for issue in error.errors(include_input=False):
        field = issue["loc"][0] if issue["loc"] else ""
        label = FIELD_LABELS.get(field, "Input")
        error_type = issue["type"]
        context = issue.get("ctx") or {}

        if error_type == "string_too_short":
            message = (
                f"{label} must contain at least "
                f"{context['min_length']} characters."
            )
        elif error_type == "string_too_long":
            message = (
                f"{label} must contain no more than "
                f"{context['max_length']} characters."
            )
        elif error_type == "missing":
            message = f"{label} is required."
        else:
            message = f"Please check {label.lower()}."

        messages.append(message)

    return messages


def main() -> None:
    """Build the career-input form and display validation feedback."""
    st.set_page_config(
        page_title="Career Skills Translator",
        page_icon="🧭",
        layout="centered",
    )

    st.title("Career Skills Translator")
    st.write(
        "Explore how your existing professional experience "
        "may apply to a different career field."
    )

    st.caption(
        "Do not include confidential employer information. "
        "When AI analysis is enabled, submitted descriptions "
        "will be sent to an external AI provider."
    )

    with st.form("career_form"):
        occupation = st.text_input(
            "Current occupation",
            placeholder="e.g., Engineering Specialist",
        )

        experience = st.text_area(
            "Responsibilities and experience",
            placeholder=(
                "Describe the work you perform, the problems "
                "you solve, and the responsibilities you hold."
            ),
            height=180,
        )

        target = st.text_input(
            "Target career field",
            placeholder="e.g., Software Development",
        )

        submitted = st.form_submit_button(
            "Validate information",
            type="primary",
        )

    if submitted:
        try:
            CareerInput(
                current_occupation=occupation,
                experience_description=experience,
                target_career_field=target,
            )
        except ValidationError as error:
            for message in validation_messages(error):
                st.error(message)
        else:
            st.success(
                "Your information is valid. "
                "AI analysis will be connected in the next milestone."
            )

    st.info(
        "Development version: This interface currently validates "
        "inputs only. No AI request is made."
    )


if __name__ == "__main__":
    main()
