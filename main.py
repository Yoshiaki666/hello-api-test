from fastapi import FastAPI

app = FastAPI()

@app.get("/process")
def process(text: str):
    return {"result": text.upper()}
