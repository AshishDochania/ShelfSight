from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import shelf_status, tasks

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(shelf_status.router)
app.include_router(tasks.router)

@app.get("/")
async def root():
    return {"message": "Welcome to ShelfSight AI API"}