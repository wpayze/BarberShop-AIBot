from fastapi import FastAPI
from app.routers.auth_router import router as auth_router

app = FastAPI()

@app.get("/", tags=["health"])
def read_root():
    return {"message": "Hello, world!"}

app.include_router(auth_router)
