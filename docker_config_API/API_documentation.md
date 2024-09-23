
# InstaHub AI API Documentation

## Overview

This project provides a REST API for classification, sentiment analysis, and summarization of text. The API is built using **FastAPI** and serves as a backend for processing different types of text data, offering multiple endpoints for various functionalities.

## Features

- **Classification**: Classifies text based on user-defined classes.
- **Sentiment Analysis**: Analyzes the sentiment of the provided text.
- **Summarization**: Provides a summary of the input text.
- **Labeling**: Labels a given text based on specific criteria.

## API Documentation

The API is documented using Swagger, and you can access the interactive API documentation by visiting:

```
https://insthub-container-app.proudtree-0393b2da.germanywestcentral.azurecontainerapps.io/docs
```

This documentation provides details on all available endpoints and their request/response formats.

## Endpoints

Here’s a brief overview of the key endpoints:

- **Root (`/`)**
  - **GET**: A simple endpoint for root access.
  
- **Classification (`/classification`)**
  - **POST**: Accepts text input and a list of classes, then returns the classification result.
  
- **Sentiment Analysis (`/sentiment`)**
  - **POST**: Accepts a piece of text and returns its sentiment (positive, negative, or neutral).
  
- **Summarization (`/summary`)**
  - **POST**: Accepts a piece of text and returns a concise summary.
  
- **Labeling (`/label`)**
  - **POST**: Accepts a piece of text and applies labels based on predefined criteria.
### `GET /webhook`

- **Description**: Verifies WhatsApp messages to ensure they are sent by the WhatsApp server and not another source.
- **Request Parameters**:
  - **`hub.mode`** (query parameter, required): The mode of the webhook.
  - **`hub.verify_token`** (query parameter, required): The verification token to validate the request.
  - **`hub.challenge`** (query parameter, required): The challenge token sent by the WhatsApp server.
- **Response**:
  - **200 OK**: Returns the `hub.challenge` token if verification is successful.
  - **401 Unauthorized**: If verification fails.

### `POST /webhook`

- **Description**: Receives WhatsApp messages and forwards them to the .NET server.
- **Request Body**:
  - **`object`** (string, required): The type of object (e.g., "whatsapp_business_account").
  - **`entry`** (array, required): An array of entry objects containing the message data.
- **Response**:
  - **200 OK**: Acknowledges receipt of the message.

### `POST /send-data`

- **Description**: Stores the data of the chat history in the vector database.
- **Request Body**:
  - **`id`** (int, required): The unique identifier for the chat data.
  - **`data`** (string, required): The summary of the chat to be stored.
- **Response**:
  - **200 OK**: Acknowledges successful storage of the data.

### `GET /similarity`

- **Description**: Performs a semantic search based on the provided question.
- **Request Parameters**:
  - **`question`** (query parameter, required): The question to be encoded and searched.
- **Response**:
  - **200 OK**: Returns the top 5 results with their IDs and scores.

## Request and Response Examples

### Classification
**Request**:
```json
{
  "chat": "The product is great!",
  "classes": ["positive", "negative", "neutral"]
}
```

**Response**:
```json
{
  "classification": "positive"
}
```

### Sentiment Analysis
**Request**:
```json
{
  "chat": "I am very happy with the service!"
}
```

**Response**:
```json
{
  "sentiment": "positive"
}
```

### Summarization
**Request**:
```json
{
  "chat": "This is a long piece of text that needs to be summarized into something more concise."
}
```

**Response**:
```json
{
  "summary": "This is a long piece of text summarized."
}
```

### Labeling
**Request**:
```json
{
  "chat": "This is a long piece of text that needs to be summarized into something more concise."
}
```

**Response**:
```json
{
  "label": "Request for text summarization. \n"
}
```

### webhook GET
**Request**:
```json
{
  "hub.mode": "subscribe",
  "hub.verify_token":"your_unique_verify_token_123",
  "hub.challenge": 12453
}
```
**Response**:
```json
{
  12453
}
```
### send-data POST
**Request**:
```json
{
    "id": 12345,
    "data": "This is a summary of the chat."
}
```
**Response**:
HTTP/1.1 200 OK

### Similarity GET
**Request**:
```json
{
    "question": "What is the capital of France?"
}
```
**Response**:
```json
[
    {
        "id": "1",
        "score": 0.95
    },
    {
        "id": "2",
        "score": 0.90
    },
    {
        "id": "3",
        "score": 0.85
    },
    {
        "id": "4",
        "score": 0.80
    },
    {
        "id": "5",
        "score": 0.75
    }
]
```

