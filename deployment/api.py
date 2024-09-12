from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from .models_functions import classification_model, sentiment_model, summary_model, label_model

app = FastAPI()

# Pydantic model for classification request
class ClassificationRequest(BaseModel):
    chat: str
    classes: list[str]

# Pydantic model for general chat requests (used for sentiment, summary, and label models)
class ChatRequest(BaseModel):
    chat: str

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Classification endpoint
@app.post("/classification")
def classification(request: ClassificationRequest):
    _class = classification_model(request.chat, request.classes)
    return {'output': _class}

# Sentiment analysis endpoint
@app.post("/sentiment")
def sentiment(request: ChatRequest):
    result, degree = sentiment_model(request.chat)
    return {"result": result, "degree": degree}

# Summary generation endpoint
@app.post("/summary")
def summary(request: ChatRequest):
    summary = summary_model(request.chat)
    return {"summary": summary}

# Label generation endpoint
@app.post("/label")
def label(request: ChatRequest):
    label = label_model(request.chat)
    return {"label": label}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
