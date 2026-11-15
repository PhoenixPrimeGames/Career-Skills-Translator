
"""Automated boundary tests for user-provided career information."""

import pytest
from pydantic import ValidationError

from validation import CareerInput


VALID_INPUT = {
    "current_occupation": "Engineering Specialist",
    "experience_description": "Diagnose equipment issues and document solutions.",
    "target_career_field": "Software Development",
}

LIMITS = [
    ("current_occupation", 2, 100),
    ("experience_description", 20, 4000),
    ("target_career_field", 2, 100),
]


def test_valid_input_accepted():
    """A complete, valid career description should be accepted."""
    result = CareerInput.model_validate(VALID_INPUT)
    assert result.current_occupation == "Engineering Specialist"


def test_surrounding_whitespace_removed():
    """Leading and trailing whitespace should be removed."""
    payload = {
        key: f"  {value}  "
        for key, value in VALID_INPUT.items()
    }
    result = CareerInput.model_validate(payload)
    assert result.model_dump() == VALID_INPUT


@pytest.mark.parametrize("field,minimum,maximum", LIMITS)
def test_exact_minimum_allowed(field, minimum, maximum):
    """Each field must accept its exact minimum length."""
    payload = {**VALID_INPUT, field: "x" * minimum}
    result = CareerInput.model_validate(payload)
    assert len(getattr(result, field)) == minimum


@pytest.mark.parametrize("field,minimum,maximum", LIMITS)
def test_exact_maximum_allowed(field, minimum, maximum):
    """Each field must accept its exact maximum length."""
    payload = {**VALID_INPUT, field: "x" * maximum}
    result = CareerInput.model_validate(payload)
    assert len(getattr(result, field)) == maximum


@pytest.mark.parametrize("field,minimum,maximum", LIMITS)
def test_below_minimum_rejected(field, minimum, maximum):
    """Input shorter than the minimum must be rejected."""
    payload = {**VALID_INPUT, field: "x" * (minimum - 1)}
    with pytest.raises(ValidationError):
        CareerInput.model_validate(payload)


@pytest.mark.parametrize("field,minimum,maximum", LIMITS)
def test_above_maximum_rejected(field, minimum, maximum):
    """Input longer than the maximum must be rejected."""
    payload = {**VALID_INPUT, field: "x" * (maximum + 1)}
    with pytest.raises(ValidationError):
        CareerInput.model_validate(payload)


@pytest.mark.parametrize("field,minimum,maximum", LIMITS)
def test_blank_fields_rejected(field, minimum, maximum):
    """Whitespace-only values must not pass validation."""
    payload = {**VALID_INPUT, field: "   \t   "}
    with pytest.raises(ValidationError):
        CareerInput.model_validate(payload)


def test_extra_fields_rejected():
    """Unrecognized input fields must be rejected."""
    with pytest.raises(ValidationError):
        CareerInput.model_validate({
            **VALID_INPUT,
            "api_key": "not allowed",
        })


def test_trimming_does_not_bypass_minimum():
    """Whitespace around a too-short value must not make it valid."""
    payload = {
        **VALID_INPUT,
        "current_occupation": "  x  ",
    }
    with pytest.raises(ValidationError):
        CareerInput.model_validate(payload)
