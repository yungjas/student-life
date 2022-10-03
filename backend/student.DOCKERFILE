FROM python:3.9-slim

WORKDIR /backend

COPY requirements.txt .

RUN apt-get update \ 
    && pip install -r requirements.txt

COPY ./student.py .

CMD ["python", "./student.py"]