import logging
from fastapi import FastAPI, Query, HTTPException, Request
import uvicorn
from pydantic import BaseModel
from models_functions import *
import httpx
app = FastAPI()
VERIFY_TOKEN = "your_unique_verify_token_123"
logging.basicConfig(level=logging.INFO)
class classificationParam(BaseModel):
    chat:str
    classes:list[str]

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/webhook")
def webhook(hub_mode: str = Query(None,alias="hub.mode"),
            hub_verify_token: str = Query(None,alias="hub.verify_token"),
            hub_challenge: str=Query(None, alias="hub.challenge")):
    
    if hub_verify_token == VERIFY_TOKEN and hub_mode == "subscribe":
        # return only digits from the challenge
        digits = "".join([d for d in hub_challenge if d.isdigit()])
        return int(digits)
    else:
        message = f"Invalid verify token: {hub_verify_token}, or hub_mode {hub_mode}"
        raise HTTPException(status_code=401, detail=message)
    
@app.post("/webhook")
async def webhook(request: Request):
    headers = request.headers
    body = await request.json()
    
    # froward the body to  .Net servver
    url = "https://instahub20240922062720.azurewebsites.net/api/Ticket/receive-whatsapp-messages"
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=body)

    # log the response
    logging.info(f"Headers: {headers}\n\n")
    logging.info(f"Body: {body}\n")
    logging.info(f"Forwarded Response: {response.status_code} - {response.text}\n")

    return {"message": "post success"}

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

@app.post("/send-data")
def store_data(id:int, data:str):
    get_data(id, data)

@app.get("/similarity")
def similarity(question):
    similarity = query(question=question)
    return similarity

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
