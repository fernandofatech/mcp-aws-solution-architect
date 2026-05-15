"""Shared Pydantic models used across tools."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


WellArchitectedPillar = Literal[
    "operational_excellence",
    "security",
    "reliability",
    "performance_efficiency",
    "cost_optimization",
    "sustainability",
]


class ServiceSuggestion(BaseModel):
    """A single AWS service recommendation."""

    service: str = Field(..., description="AWS service name, e.g. 'Amazon DynamoDB'.")
    rationale: str = Field(..., description="Why this service fits the use case.")
    category: str = Field(..., description="Compute / Storage / Database / etc.")


class CostLineItem(BaseModel):
    """Input describing usage of one service for cost estimation."""

    service: str = Field(..., description="Service key, e.g. 'lambda', 'dynamodb', 's3'.")
    usage: dict[str, float] = Field(
        default_factory=dict,
        description="Service-specific usage knobs (e.g. requests, gb_storage, gb_seconds).",
    )


class CostEstimate(BaseModel):
    """Output of estimate_cost."""

    monthly_total_usd: float
    by_service: dict[str, float]
    notes: list[str]
    disclaimer: str = (
        "Approximate. Uses an embedded pricing table — verify against AWS Pricing Calculator "
        "before any commercial decision."
    )


class WellArchitectedFinding(BaseModel):
    """One finding on one pillar."""

    pillar: WellArchitectedPillar
    severity: Literal["info", "low", "medium", "high"]
    message: str
    recommendation: str


class WellArchitectedReview(BaseModel):
    """Output of review_well_architected."""

    summary: str
    findings: list[WellArchitectedFinding]
    score_by_pillar: dict[WellArchitectedPillar, int]


class ADRInput(BaseModel):
    """Input for generate_adr."""

    title: str
    context: str
    decision: str
    alternatives: list[str] = Field(default_factory=list)
    consequences: list[str] = Field(default_factory=list)
    status: Literal["proposed", "accepted", "deprecated", "superseded"] = "proposed"
