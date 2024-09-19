FROM python:3.9-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt


RUN pip install --upgrade -r requirements.txt

# COPY ./embeddings_model /code/embeddings_model/

COPY ./app /code/app/

ENV PYTHONPATH=/code/app

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
