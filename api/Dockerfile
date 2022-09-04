FROM python:3.10.6-slim

LABEL description="Firebase api gateway."

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . . 

EXPOSE 8000

# CMD [ "uvicorn", "app:app", "--host=0.0.0.0", "--reload" ]