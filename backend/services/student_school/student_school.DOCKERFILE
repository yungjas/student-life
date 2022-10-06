FROM python:3.9-slim

WORKDIR /backend/services/student_school

COPY requirements.txt .

RUN apt-get update \ 
    && pip install -r requirements.txt

COPY . .

CMD ["python", "./student_school_api.py"]