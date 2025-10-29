"""
Chat service module for handling conversation logic.
This module manages session memory and OpenAI API interactions.
"""

from typing import Dict, List
from openai import OpenAI
from app.core.config import settings, SYSTEM_PROMPT


class SimpleMemory:
    """Simple in-memory conversation storage."""
    
    def __init__(self):
        """Initialize empty conversation history."""
        self.messages: List[Dict[str, str]] = []
    
    def add_message(self, role: str, content: str):
        """Add a message to the conversation history."""
        self.messages.append({"role": role, "content": content})
    
    def get_messages(self) -> List[Dict[str, str]]:
        """Get all messages in the conversation."""
        return self.messages.copy()
    
    def clear(self):
        """Clear all messages from the conversation."""
        self.messages.clear()
    
    def get_message_count(self) -> int:
        """Get the number of messages in the conversation."""
        return len(self.messages)


class ChatService:
    """Service class for handling chat operations."""
    
    def __init__(self):
        """Initialize the chat service with OpenAI client and session storage."""
        self.sessions: Dict[str, SimpleMemory] = {}
        self.client = OpenAI(
            base_url=settings.openrouter_base_url,
            api_key=settings.openrouter_api_key,
        )
    
    def get_or_create_session(self, session_id: str) -> SimpleMemory:
        """Get existing session or create a new one."""
        if session_id not in self.sessions:
            self.sessions[session_id] = SimpleMemory()
        return self.sessions[session_id]
    
    async def process_message(self, session_id: str, message: str) -> str:
        """Process a user message and return AI response."""
        # Get or create session
        memory = self.get_or_create_session(session_id)
        
        # Get conversation history
        history_messages = memory.get_messages()
        
        # Build message list for API
        api_messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        
        # Add conversation history
        api_messages.extend(history_messages)
        
        # Add current user message
        api_messages.append({"role": "user", "content": message})
        
        # Get response from API
        completion = self.client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "https://gym-chatbot.app",
                "X-Title": "Gym Assistant Chatbot",
            },
            model=settings.openrouter_model,
            messages=api_messages
        )
        
        response = completion.choices[0].message.content
        
        # Save to memory
        memory.add_message("user", message)
        memory.add_message("assistant", response)
        
        return response
    
    def get_conversation_history(self, session_id: str) -> List[Dict[str, str]]:
        """Get formatted conversation history for a session."""
        if session_id not in self.sessions:
            return []
        
        memory = self.sessions[session_id]
        return memory.get_messages()
    
    def clear_session_history(self, session_id: str) -> bool:
        """Clear conversation history for a session."""
        if session_id in self.sessions:
            self.sessions[session_id].clear()
            return True
        return False
    
    def delete_session(self, session_id: str) -> bool:
        """Delete a session completely."""
        if session_id in self.sessions:
            del self.sessions[session_id]
            return True
        return False
    
    def get_all_sessions(self) -> Dict[str, int]:
        """Get all active sessions with their message counts."""
        session_info = {}
        for session_id, memory in self.sessions.items():
            session_info[session_id] = memory.get_message_count()
        return session_info


# Global chat service instance
chat_service = ChatService()
