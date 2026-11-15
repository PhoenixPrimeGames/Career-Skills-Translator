
"""Validate career information before sending it to the AI service."""

from pydantic import BaseModel, ConfigDict, Field


class CareerInput(BaseModel):
    """Three required user inputs, normalized and length-checked."""

    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    current_occupation: str = Field(
        min_length=2,
        max_length=100,
    )

    experience_description: str = Field(
        min_length=20,
        max_length=4000,
    )

    target_career_field: str = Field(
        min_length=2,
        max_length=100,
    )
