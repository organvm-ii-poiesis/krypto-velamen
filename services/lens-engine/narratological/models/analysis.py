"""Pydantic models for script/narrative analysis."""

from __future__ import annotations
from enum import Enum
from typing import Any, List, Optional, Dict
from pydantic import BaseModel, Field

class BeatFunction(str, Enum):
    SETUP = "SETUP"
    INCITE = "INCITE"
    COMPLICATE = "COMPLICATE"
    ESCALATE = "ESCALATE"
    REVEAL = "REVEAL"
    CRISIS = "CRISIS"
    CLIMAX = "CLIMAX"
    RESOLVE = "RESOLVE"
    TRANSITION = "TRANSITION"
    BREATHE = "BREATHE"
    PLANT = "PLANT"
    PAYOFF = "PAYOFF"
    MIRROR = "MIRROR"
    SUBPLOT = "SUBPLOT"
    CODA = "CODA"

class ArcClassification(str, Enum):
    POSITIVE = "positive"
    NEGATIVE = "negative"
    FLAT = "flat"
    CORRUPTED = "corrupted"
    REDEEMED = "redeemed"

class ConnectorType(str, Enum):
    BUT = "BUT"
    THEREFORE = "THEREFORE"
    AND_THEN = "AND THEN"
    MEANWHILE = "MEANWHILE"

class Character(BaseModel):
    name: str
    role: str
    description: str = ""
    first_appearance: Optional[int] = None
    want: Optional[str] = None
    need: Optional[str] = None
    lie: Optional[str] = None
    truth: Optional[str] = None
    arc_classification: Optional[ArcClassification] = None
    arc_summary: Optional[str] = None
    relationships: Dict[str, str] = Field(default_factory=dict)

class Scene(BaseModel):
    number: int
    slug: str = ""
    summary: str = ""
    function: Optional[BeatFunction] = None
    secondary_function: Optional[BeatFunction] = None
    characters_present: List[str] = Field(default_factory=list)
    connector_to_next: Optional[ConnectorType] = None
    tension_level: Optional[int] = None
    notes: Optional[str] = None
    role_observations: Dict[str, str] = Field(default_factory=dict)

class Act(BaseModel):
    number: int
    name: Optional[str] = None
    start_scene: int
    end_scene: int
    summary: str = ""
    inciting_incident: Optional[int] = None
    midpoint: Optional[int] = None
    crisis: Optional[int] = None
    climax: Optional[int] = None

class Script(BaseModel):
    title: str
    draft: Optional[str] = None
    format: str = "Feature"
    page_count: Optional[int] = None
    scene_count: Optional[int] = None
    primary_genre: Optional[str] = None
    tone: Optional[str] = None
    logline: Optional[str] = None
    scenes: List[Scene] = Field(default_factory=list)
    characters: List[Character] = Field(default_factory=list)
    acts: List[Act] = Field(default_factory=list)
