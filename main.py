import socket
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}

@app.get("/ping")
def ping():
    return {"status": "ok"}


@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
