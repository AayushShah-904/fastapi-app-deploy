from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"message": "This is home page"}

@app.get("/health")
def health():
    return {"status": "OK", "version": 1}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"greeting": f"Hello {name}"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
