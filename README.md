# 🏋️ Gym Chatbot API

A FastAPI-based gym assistant chatbot with conversation memory, built with Python and powered by OpenRouter's AI models.

## ✨ Features

- **Conversational AI**: Chat with an intelligent gym assistant
- **Session Memory**: Maintains conversation history per session
- **RESTful API**: Clean, well-documented API endpoints
- **CORS Support**: Ready for frontend integration
- **Modular Architecture**: Well-organized, maintainable code structure
- **Environment Configuration**: Easy configuration management

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- UV package manager (recommended) or pip
- OpenRouter API key

### Installation

1. **Clone or download this project**
   ```bash
   cd gymapp
   ```

2. **Install dependencies using UV (recommended)**
   ```bash
   uv sync
   ```

   Or using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   # Copy the example environment file
   cp env.example .env
   
   # Edit .env and add your OpenRouter API key
   OPENROUTER_API_KEY=your_actual_api_key_here
   ```

4. **Run the application**
   ```bash
   # Using UV
   uv run python main.py
   
   # Or using Python directly
   python main.py
   ```

5. **Access the API**
   - API Documentation: http://localhost:8000/docs
   - Alternative docs: http://localhost:8000/redoc
   - API Base URL: http://localhost:8000

## 📁 Project Structure

```
gymapp/
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── app.py          # FastAPI application setup
│   │   ├── routes.py       # API endpoints
│   │   └── chat_service.py # Chat logic and OpenAI integration
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py       # Configuration and settings
│   ├── models/
│   │   ├── __init__.py
│   │   └── schemas.py      # Pydantic models
│   └── __init__.py
├── main.py                 # Application entry point
├── pyproject.toml         # Project dependencies and metadata
├── env.example            # Environment variables template
└── README.md              # This file
```

## 🔧 Configuration

The application can be configured through environment variables or by modifying `app/core/config.py`:

| Variable | Default | Description |
|----------|---------|-------------|
| `OPENROUTER_API_KEY` | Required | Your OpenRouter API key |
| `DEBUG` | `false` | Enable debug mode |
| `HOST` | `0.0.0.0` | Server host |
| `PORT` | `8000` | Server port |
| `OPENROUTER_MODEL` | `meta-llama/llama-3.1-8b-instruct:free` | AI model to use |

### 🤖 Available Free Models

If you encounter issues with the default model, try these alternatives:

- `meta-llama/llama-3.1-8b-instruct:free` (default)
- `microsoft/phi-3-mini-128k-instruct:free`
- `google/gemma-2-9b-it:free`
- `mistralai/mistral-7b-instruct:free`

## 📚 API Endpoints

### Chat
- **POST** `/chat` - Send a message to the gym assistant
- **GET** `/history/{session_id}` - Get conversation history
- **DELETE** `/history/{session_id}` - Clear conversation history

### Sessions
- **GET** `/sessions` - List all active sessions
- **DELETE** `/sessions/{session_id}` - Delete a session

### General
- **GET** `/` - API information and available endpoints

## 💡 Usage Examples

### Send a Chat Message
```bash
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "user123",
    "message": "I want to start working out. What should I do?"
  }'
```

### Get Conversation History
```bash
curl "http://localhost:8000/history/user123"
```

### List All Sessions
```bash
curl "http://localhost:8000/sessions"
```

## 🛠️ Development

### Running in Development Mode
```bash
# Enable debug mode
export DEBUG=true
uv run python main.py
```

### Code Structure Explanation

1. **`main.py`**: Entry point that starts the server
2. **`app/api/app.py`**: Creates and configures the FastAPI application
3. **`app/api/routes.py`**: Defines all HTTP endpoints
4. **`app/api/chat_service.py`**: Handles chat logic and AI integration
5. **`app/models/schemas.py`**: Pydantic models for request/response validation
6. **`app/core/config.py`**: Configuration management

### Key Concepts for Beginners

- **FastAPI**: A modern Python web framework for building APIs
- **Pydantic**: Data validation using Python type annotations
- **LangChain**: Framework for working with language models
- **Session Management**: Keeping track of user conversations
- **CORS**: Cross-Origin Resource Sharing for web security

## 🔒 Security Notes

- The API key is loaded from environment variables for security
- CORS is configured to allow frontend integration
- Session data is stored in memory (use Redis/Database for production)

## 🔧 Troubleshooting

### Common Issues

**1. Model Not Found Error (404)**
```
Error code: 404 - No endpoints found matching your data policy
```
**Solution:** Some free models may have data policy restrictions. Try switching to a different model:
```bash
# In your .env file, change the model:
OPENROUTER_MODEL=microsoft/phi-3-mini-128k-instruct:free
```

**2. API Key Not Set**
```
Warning: OPENROUTER_API_KEY environment variable not set!
```
**Solution:** Make sure you've created a `.env` file with your API key:
```bash
# Copy the example file
cp env.example .env
# Edit .env and add your API key
OPENROUTER_API_KEY=your_actual_api_key_here
```

**3. Import Errors**
If you get import errors, make sure all dependencies are installed:
```bash
uv sync
# or
pip install -r requirements.txt
```

## 🚀 Production Deployment

For production deployment, consider:

1. **Database Storage**: Replace in-memory session storage with Redis or a database
2. **Environment Variables**: Use proper secret management
3. **HTTPS**: Enable SSL/TLS encryption
4. **Rate Limiting**: Implement API rate limiting
5. **Monitoring**: Add logging and monitoring
6. **Docker**: Containerize the application

## 📖 Learning Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)
- [LangChain Documentation](https://python.langchain.com/)
- [OpenRouter API Documentation](https://openrouter.ai/docs)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.
