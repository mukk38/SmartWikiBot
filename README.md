# Wikipedia-Powered Q&A Chatbot with FastAPI

A chatbot that answers questions in a specific domain (e.g., science, history) using Hugging Face's NLP models and Wikipedia API. Supports terminal and web interfaces.

## Features
- Advanced NLP with `deepset/roberta-base-squad2`
- Dynamic context from Wikipedia API
- Domain-specific responses
- Terminal and web interfaces
- Chat history support
- FastAPI-powered API with OpenAPI docs

## Installation (Windows)
1. **Backend**:
   ```bash
   cd backend
   python -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```
2. **Frontend**:
   ```bash
    cd frontend
    python -m http.server 8001
   Open http://localhost:8001.
    ```
   
3. **Terminal**:
    ```bash
   .\venv\Scripts\activate
    python terminal_bot.py
    ```
   
## API Docs
- OpenAPI documentation: http://localhost:8000/docs

## License
MIT