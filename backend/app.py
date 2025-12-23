from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from backend.core.database import Base, engine
from backend.routes.quotation import router as quotation_router
import os

app = FastAPI(title="LMS Backend – NeonDB")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (frontend)
app.mount(
    "/static",
    StaticFiles(directory=os.path.join(BASE_DIR, "frontend")),
    name="static",
)

# Create tables
Base.metadata.create_all(bind=engine)

# APIs
app.include_router(quotation_router)

@app.get("/")
def root():
    return {"status": "Backend is running"}
