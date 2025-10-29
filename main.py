"""
Main entry point for the Gym Chatbot API.
This is the file you run to start the server.
"""

import uvicorn
from app.core.config import settings


def main():
    """Start the FastAPI server."""
    # Check for API key
    if not settings.openrouter_api_key:
        print("⚠️  Warning: OPENROUTER_API_KEY environment variable not set!")
        print("Set it with: export OPENROUTER_API_KEY='your-key'")
        print("Or create a .env file with: OPENROUTER_API_KEY=your-key")
    
    print(f"\n🏋️  Starting {settings.app_name} Server...")
    print(f"📝 API Documentation: http://localhost:{settings.port}/docs")
    print(f"🔄 Alternative docs: http://localhost:{settings.port}/redoc")
    print(f"🌐 Server running on: http://{settings.host}:{settings.port}\n")
    
    # Start the server
    uvicorn.run(
        "app.app:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug
    )


if __name__ == "__main__":
    main()