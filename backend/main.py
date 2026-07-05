from contextlib import asynccontextmanager
from llm.client import ask_llm
from fastapi import FastAPI
from routes.chat import router as chat_router
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Loading local LLM...")

    try:
        ask_llm("hello")
    except Exception as e:
        print(e)

    print("LLM ready.")

    yield

app = FastAPI(
    title="AgriSetu",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)