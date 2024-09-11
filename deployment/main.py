from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel, Field
from models_functions import classification_model, sentiment_model, summary_model, label_model
app = FastAPI()


class classificationParam(BaseModel):
    chat:str
    classes:list[str]

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/classification")
def classification(classificationParam:classificationParam):
    _class = classification_model(classificationParam.chat, classificationParam.classes)
    return {'output': _class}

@app.post("/sentiment")
def sentiment(chat: str):
    result, degree = sentiment_model(chat)
    return {"result": result, "degree": degree}

@app.post("/summary")
def summary(chat):
    summary = summary_model(chat)
    return {"summary": summary}

@app.post("/label")
def label(chat):
    label = label_model(chat)
    return {"label": label}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)