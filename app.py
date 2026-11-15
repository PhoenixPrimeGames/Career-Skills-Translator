
"""Streamlit interface for Career Skills Translator.

Collects career information, requests AI analysis, and presents results.
"""

import os

import streamlit as st
from openai import OpenAI
from pydantic import ValidationError

from analysis import (
    API_TIMEOUT_SECONDS,
    AnalysisUnavailableError,
    EvidenceValidationError,
    analyze_career,
)
from schemas import AnalysisResult, SkillTranslation
from validation import CareerInput


FIELD_LABELS = {
    "current_occupation": "Current occupation",
    "experience_description": "Responsibilities and experience",
    "target_career_field": "Target career field",
}


def validation_messages(error: ValidationError) -> list[str]:
    """Convert Pydantic errors into safe, readable messages."""
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


def get_api_key() -> str:
    """Retrieve credentials without exposing them in the interface."""
    key = os.getenv("OPENAI_API_KEY", "").strip()

    if key:
        return key

    try:
        return str(st.secrets.get("OPENAI_API_KEY", "")).strip()
    except (FileNotFoundError, KeyError):
        return ""


def format_analysis(result: AnalysisResult) -> str:
    """Produce a complete plain-text analysis for copying."""
    lines = [
        "Career Skills Translator - Analysis Results",
        "",
        f"Status: {result.status.replace('_', ' ').title()}",
        f"Summary: {result.summary}",
    ]

    for index, skill in enumerate(result.skills, start=1):
        lines.extend(["", f"Skill {index}"])

        # Discover fields dynamically from the central schema.
        for name, field in SkillTranslation.model_fields.items():
            label = field.title or name.replace("_", " ").title()
            lines.append(f"{label}: {getattr(skill, name)}")

    lines.extend([
        "",
        "AI-generated interpretation of self-reported experience.",
        "This analysis does not verify professional qualifications.",
    ])

    return "\n".join(lines)


def render_analysis(result: AnalysisResult) -> None:
    """Present validated results using schema-defined field labels."""
    st.subheader("Career Analysis Results")

    if result.status == "insufficient_information":
        st.warning(
            "Insufficient information to identify supported skills."
        )
    else:
        st.success(
            f"Analysis completed. "
            f"{len(result.skills)} transferable skill(s) identified."
        )

    st.write(result.summary)

    for index, skill in enumerate(result.skills, start=1):
        with st.container(border=True):
            st.markdown(f"### Skill {index}")

            # New ordinary text fields appear automatically.
            for name, field in SkillTranslation.model_fields.items():
                label = field.title or name.replace("_", " ").title()

                st.markdown(f"**{label}**")
                st.write(getattr(skill, name))

    st.subheader("Copy Complete Analysis")
    st.code(
        format_analysis(result),
        language=None,
        wrap_lines=True,
    )

    st.caption(
        "These findings are AI-generated interpretations of "
        "self-reported experience. They do not establish "
        "professional qualifications or technical proficiency."
    )


def main() -> None:
    """Build the form, validate input, and execute AI analysis."""
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
        "Do not submit confidential employer information. "
        "Your description will be sent to an external AI provider "
        "when you request an analysis."
    )

    with st.form("career_form"):
        occupation = st.text_input(
            "Current occupation",
            placeholder="e.g., Engineering Specialist",
        )

        experience = st.text_area(
            "Responsibilities and experience",
            placeholder=(
                "Describe your responsibilities, experience, "
                "and the problems you solve."
            ),
            height=180,
        )

        target = st.text_input(
            "Target career field",
            placeholder="e.g., Software Development",
        )

        submitted = st.form_submit_button(
            "Analyze transferable skills",
            type="primary",
        )

    if submitted:
        try:
            career_input = CareerInput(
                current_occupation=occupation,
                experience_description=experience,
                target_career_field=target,
            )
        except ValidationError as error:
            for message in validation_messages(error):
                st.error(message)
        else:
            api_key = get_api_key()

            if not api_key:
                st.error(
                    "The AI service is not configured. "
                    "Contact the application administrator."
                )
            else:
                with st.spinner("Analyzing transferable skills..."):
                    try:
                        client = OpenAI(
                            api_key=api_key,
                            max_retries=0,
                            timeout=API_TIMEOUT_SECONDS,
                        )

                        result = analyze_career(
                            career_input,
                            client=client,
                        )

                    except (
                        AnalysisUnavailableError,
                        EvidenceValidationError,
                    ) as error:
                        st.error(str(error))

                    except Exception:
                        # Never expose raw exceptions or credentials.
                        st.error(
                            "An unexpected application error occurred. "
                            "Please try again later."
                        )

                    else:
                        render_analysis(result)


if __name__ == "__main__":
    main()
