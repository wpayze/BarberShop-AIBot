from fastapi import FastAPI

app = FastAPI()


@app.get("/", tags=["health"])
def read_root():
    return {"message": "Hello, world!"}
