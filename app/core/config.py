"""
Configuration module for the Gym Chatbot API.
Handles environment variables and application settings.
"""

import os
from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # API Configuration
    app_name: str = "Gym Chatbot API"
    app_version: str = "1.0.0"
    debug: bool = False
    
    # Server Configuration
    host: str = "0.0.0.0"
    port: int = 8000
    
    # OpenRouter Configuration
    openrouter_api_key: Optional[str] = None
    openrouter_base_url: str = "https://openrouter.ai/api/v1"
    openrouter_model: str = "google/gemma-2-9b-it:free"
    
    # CORS Configuration
    cors_origins: list = ["*"]
    cors_allow_credentials: bool = True
    cors_allow_methods: list = ["*"]
    cors_allow_headers: list = ["*"]
    
    class Config:
        env_file = ".env"
        case_sensitive = False


# Create global settings instance
settings = Settings()

# System prompt for the gym assistant
SYSTEM_PROMPT = """You are a knowledgeable and supportive gym assistant. 
Help users with:
- Workout routines and exercise suggestions
- Form and technique advice
- Nutrition and diet guidance
- Fitness goal planning
- Motivation and encouragement
- Equipment usage

Be friendly, encouraging, and provide practical, safe advice. 
Always prioritize user safety and recommend consulting professionals for medical concerns."""
