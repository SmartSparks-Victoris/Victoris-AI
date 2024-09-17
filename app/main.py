import logging
from fastapi import FastAPI, Query, HTTPException, Request
import uvicorn
from pydantic import BaseModel, Field
from app.models_functions import classification_model, sentiment_model, summary_model, label_model
import re
app = FastAPI()

VERIFY_TOKEN = "your_unique_verify_token_123"
class classificationParam(BaseModel):
    chat:str
    classes:list[str]

logging.basicConfig(level=logging.INFO)

@app.get("/")
def read_root():
    response = {"message": "weebhook updated_3"}
    logging.info(f"Response: {response}")
    return response

@app.post("/webhook")
async def webhook(request: Request):
    headers = request.headers
    body = await request.json()
    logging.info(f"Headers: {headers}\n")
    logging.info(f"Body: {body}\n")
    return {"message": "post success"}

@app.get("/webhook")
def webhook(hub_mode: str = Query(None,alias="hub.mode"),
            hub_verify_token: str = Query(None,alias="hub.verify_token"),
            hub_challenge: str=Query(None, alias="hub.challenge")):
    
    if hub_verify_token == VERIFY_TOKEN and hub_mode == "subscribe":
        # return only digits from the challenge
        return int(re.search(r'\d+', hub_challenge).group())
    else:
        message = f"Invalid verify token: {hub_verify_token}, or hub_mode {hub_mode}"
        raise HTTPException(status_code=401, detail=message)
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