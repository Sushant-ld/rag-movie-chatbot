from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from rag_pipeline import answer_question


# ==========================================
# Create FastAPI application
# ==========================================

app = FastAPI(
    title="Movie RAG Chatbot",
    description="RAG chatbot for Hollywood, Bollywood and Tollywood movies",
    version="1.0.0"
)


# ==========================================
# Enable CORS
# Allows frontend (port 5500)
# to communicate with backend (port 8000)
# ==========================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================================
# Request model
# ==========================================

class ChatRequest(BaseModel):
    question: str


# ==========================================
# Source model
# ==========================================

class MovieSource(BaseModel):
    title: str
    year: int
    industry: str
    language: str
    genre: str
    director: str
    distance: float


# ==========================================
# Response model
# ==========================================

class ChatResponse(BaseModel):
    question: str
    answer: str
    sources: list[MovieSource]


# ==========================================
# Root endpoint
# ==========================================

@app.get("/")
def root():

    return {
        "message": "Movie RAG Chatbot API is running"
    }


# ==========================================
# Chat endpoint
# ==========================================

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    # ------------------------------
    # Validate question
    # ------------------------------

    question = request.question.strip()

    if not question:

        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty"
        )

    # ------------------------------
    # Run RAG pipeline
    # ------------------------------

    try:

        result = answer_question(
            question
        )

    except Exception as error:

        print("RAG error:", error)

        raise HTTPException(
            status_code=500,
            detail="Unable to generate an answer right now"
        )

    # ------------------------------
    # Return response
    # ------------------------------

    return ChatResponse(
        question=question,
        answer=result["answer"],
        sources=result["sources"]
    )