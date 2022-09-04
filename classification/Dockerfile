FROM python:3.10.6-slim

LABEL description="Classification service. Gets tweets and classifies as positive, negative or neutral."

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . . 

EXPOSE 3000

# CMD [ "uvicorn", "app:app", "--host=0.0.0.0", "--reload" ]