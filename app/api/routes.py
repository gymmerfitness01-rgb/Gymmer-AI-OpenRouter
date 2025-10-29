"""
API routes for the Gym Chatbot.
This module defines all the HTTP endpoints for the FastAPI application.
"""

from fastapi import APIRouter, HTTPException
from app.models.schemas import (
    ChatRequest, ChatResponse, HistoryResponse, 
    StatusResponse, SessionsResponse
)
from app.api.chat_service import chat_service

# Create router for API endpoints
router = APIRouter()


@router.get("/")
def read_root():
    """Root endpoint with API information."""
    return {
        "message": "Gym Chatbot API",
        "version": "1.0.0",
        "endpoints": {
            "POST /chat": "Send a message",
            "GET /history/{session_id}": "Get conversation history",
            "DELETE /history/{session_id}": "Clear conversation history",
            "GET /sessions": "List active sessions",
            "DELETE /sessions/{session_id}": "Delete a session"
        }
    }


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Send a message and get a response from the gym assistant."""
    try:
        response = await chat_service.process_message(
            request.session_id, 
            request.message
        )
        
        return ChatResponse(
            session_id=request.session_id,
            response=response
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/history/{session_id}", response_model=HistoryResponse)
async def get_history(session_id: str):
    """Get conversation history for a specific session."""
    history = chat_service.get_conversation_history(session_id)
    
    return HistoryResponse(
        session_id=session_id,
        history=history
    )


@router.delete("/history/{session_id}", response_model=StatusResponse)
async def clear_history(session_id: str):
    """Clear conversation history for a specific session."""
    success = chat_service.clear_session_history(session_id)
    
    if success:
        return StatusResponse(
            status="success",
            message=f"History cleared for session {session_id}"
        )
    else:
        return StatusResponse(
            status="info",
            message=f"No session found with ID {session_id}"
        )


@router.get("/sessions", response_model=SessionsResponse)
async def list_sessions():
    """List all active sessions."""
    sessions = chat_service.get_all_sessions()
    
    return SessionsResponse(
        total_sessions=len(sessions),
        session_ids=list(sessions.keys())
    )


@router.delete("/sessions/{session_id}", response_model=StatusResponse)
async def delete_session(session_id: str):
    """Delete a session completely."""
    success = chat_service.delete_session(session_id)
    
    if success:
        return StatusResponse(
            status="success",
            message=f"Session {session_id} deleted"
        )
    else:
        return StatusResponse(
            status="error",
            message=f"Session {session_id} not found"
        )
