FROM python:3.10.6-slim

LABEL description="Scrapes tweets and stores them into firebase realtime database."

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . . 

