"""Shared data models for Career Skills Translator's AI results."""

from __future__ import annotations

from typing import Literal

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator,
    model_validator,
)


class SkillTranslation(BaseModel):
    """One transferable competency supported by the user's experience."""

    model_config = ConfigDict(extra="forbid")

    skill: str = Field(title="Transferable Skill")
    source_evidence: str = Field(title="Source Evidence")
    target_application: str = Field(title="Target Application")
    explanation: str = Field(title="Explanation")
    limitations: str = Field(title="Limitations")

    @field_validator("*")
    @classmethod
    def require_nonblank_text(cls, value: str) -> str:
        """Reject empty or whitespace-only skill descriptions."""
        if not value.strip():
            raise ValueError("Skill fields cannot be blank")
        return value


class AnalysisResult(BaseModel):
    """A completed analysis or a result with insufficient evidence."""

    model_config = ConfigDict(extra="forbid")

    status: Literal["completed", "insufficient_information"]
    summary: str
    skills: list[SkillTranslation]

    @field_validator("summary")
    @classmethod
    def require_summary(cls, value: str) -> str:
        """Every analysis must explain its outcome."""
        if not value.strip():
            raise ValueError("Summary cannot be blank")
        return value

    @model_validator(mode="after")
    def check_status_consistency(self) -> AnalysisResult:
        """Ensure the status agrees with the number of reported skills."""
        if self.status == "completed" and not self.skills:
            raise ValueError(
                "Completed analyses require at least one skill"
            )

        if self.status == "insufficient_information" and self.skills:
            raise ValueError(
                "Insufficient-information analyses cannot contain skills"
            )

        return self
