from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chatbot import Chatbot

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize chatbot with a domain (e.g., science)
chatbot = Chatbot(domain="science")


# Pydantic model for request body
class Question(BaseModel):
    question: str


@app.post("/api/ask")
async def ask_question(data: Question):
    question = data.question.strip()
    if not question:
        raise HTTPException(status_code=400, detail="No question provided")

    response = chatbot.get_response(question)
    return {"question": question, "response": response}


@app.get("/api/history")
async def get_history():
    return chatbot.get_history()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)