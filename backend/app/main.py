from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.thoughts import router as thoughts_router
from app.db.session import engine
from app.models.thought import SQLModel

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        SQLModel.metadata.create_all(engine)
        yield
    finally:
        pass

# Create FastAPI app instance
app = FastAPI(
    title="chainofthought api",
    description="API for managing versioned chains of thoughts",
    version="0.1.0",
    lifespan=lifespan,
)

# Include routers
app.include_router(thoughts_router)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["GET, POST"],
    allow_headers=[],
)