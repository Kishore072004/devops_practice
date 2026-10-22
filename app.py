from fastapi import FastAPI

app = FastAPI(title="DevOps Demo")


@app.get("/")
def home():
    return {"message": "Hello from my DevOps deployment!"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/add/{a}/{b}")
def add_numbers(a: int, b: int):
    return {"result": a + b}