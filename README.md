# tryps
https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}

@app.get("/ping")
def ping():
    return {"status": "ok"}
