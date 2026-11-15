
"""Run one controlled, live career-analysis request.

Uses fictional experience and reads the API key privately.
This script is not an automated unit test.
"""

from getpass import getpass

from openai import OpenAI

from analysis import (
    API_TIMEOUT_SECONDS,
    AnalysisUnavailableError,
    EvidenceValidationError,
    analyze_career,
)
from validation import CareerInput


def main() -> None:
    """Submit one fictional career profile and display its analysis."""

    career_input = CareerInput(
        current_occupation="Engineering Technician",
        experience_description=(
            "I diagnose electrical equipment failures, "
            "document troubleshooting procedures, "
            "analyze recurring system problems, and "
            "coordinate repairs with other technicians."
        ),
        target_career_field="Software Development",
    )

    # Read the credential without displaying or storing it in a file.
    api_key = getpass("Enter your OpenAI API key (hidden): ").strip()

    if not api_key:
        print("No API key entered. No request was made.")
        return

    # Disable SDK retries to limit unexpected additional requests.
    client = OpenAI(
        api_key=api_key,
        max_retries=0,
        timeout=API_TIMEOUT_SECONDS,
    )

    print("Submitting one fictional career analysis...")

    try:
        result = analyze_career(
            career_input,
            client=client,
        )

    except (AnalysisUnavailableError, EvidenceValidationError) as error:
        # Application error messages are sanitized and contain no API key.
        print(f"Analysis unsuccessful: {error}")
        return

    except Exception as error:
        # Avoid exposing raw provider errors or request information.
        print(f"Unexpected error category: {type(error).__name__}")
        return

    print("\nAnalysis completed successfully.")
    print(result.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
