
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
http://localhost:8000/docs
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

To run this API locally, follow the instructions below.

### Prerequisites

- Python 3.8 or higher
- FastAPI
- Uvicorn (for running the server)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/project-name.git
    ```

2. Navigate to the project directory:
    ```bash
    cd project-name
    ```

3. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
    ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Server

1. Start the FastAPI server using Uvicorn:
    ```bash
    uvicorn api:app --reload
    ```

2. Open your browser and navigate to `http://localhost:8000/docs` to view the API documentation.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.
