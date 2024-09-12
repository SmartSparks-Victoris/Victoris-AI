
# Project Name

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
https://insthub-container-app.proudtree-0393b2da.germanywestcentral.azurecontainerapps.io/docs#/default/classification_classification_post
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

## Setup Instructions


## License

This project is licensed under the MIT License.
