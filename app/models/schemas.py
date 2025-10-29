"""
Pydantic models for request and response schemas.
These define the structure of data sent to and received from the API.
"""

from pydantic import BaseModel
from typing import List, Dict


class ChatRequest(BaseModel):
    """Request model for chat messages."""
    session_id: str
    message: str


class ChatResponse(BaseModel):
    """Response model for chat messages."""
    session_id: str
    response: str


class HistoryResponse(BaseModel):
    """Response model for conversation history."""
    session_id: str
    history: List[Dict[str, str]]


class StatusResponse(BaseModel):
    """Response model for status messages."""
    status: str
    message: str


class SessionInfo(BaseModel):
    """Model for session information."""
    session_id: str
    message_count: int


class SessionsResponse(BaseModel):
    """Response model for listing sessions."""
    total_sessions: int
    session_ids: List[str]
