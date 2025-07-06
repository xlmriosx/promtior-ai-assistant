import os
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from app.models import ChatRequest, ChatResponse
from app.rag_chain import RAGChain
from app.utils import ensure_ollama_model
from langchain.schema.runnable import RunnableLambda
from langserve import add_routes
from pydantic import BaseModel, Field

load_dotenv()

model_name = os.getenv("MODEL_NAME", "llama3")
ensure_ollama_model(model_name)

app = FastAPI(
    title="Promtior RAG Chatbot",
    description="Chatbot que responde preguntas sobre Promtior usando RAG",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

rag_chain = RAGChain()

@app.get("/")
async def root():
    return {"message": "Promtior RAG Chatbot API", "status": "running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        result = rag_chain.query(request.message)
        return ChatResponse(
            response=result["response"],
            sources=result["sources"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ask")
async def ask_question(request: ChatRequest):
    try:
        result = rag_chain.query(request.message)
        return {
            "question": request.message,
            "answer": result["response"],
            "sources": result["sources"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class RAGInput(BaseModel):
    question: str = Field(..., description="La pregunta sobre Promtior")

def create_rag_runnable():
    def rag_function(input_data: dict) -> str:
        result = rag_chain.query(input_data["question"])
        return result["response"]
    
    return RunnableLambda(rag_function).with_types(
        input_type=RAGInput,
        output_type=str
    )

try:
    rag_runnable = create_rag_runnable()
    add_routes(
        app,
        rag_runnable,
        path="/langserve"
    )
    print("LangServe routes added successfully!")
except Exception as e:
    print(f"Warning: Could not add LangServe routes: {e}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)