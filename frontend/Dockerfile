FROM python:3.10.6-slim

LABEL description="Frontend service for user sentiments system"

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . . 

EXPOSE 8501
