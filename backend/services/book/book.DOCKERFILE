FROM python:3.9-slim

WORKDIR /backend/services/book

COPY requirements.txt .

RUN apt-get update \ 
    && pip install -r requirements.txt

COPY ./book.py .

CMD ["python", "./book.py"]