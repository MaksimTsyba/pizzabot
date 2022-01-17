FROM python:3.8.6-slim-buster

ENV APP_DIR = /app

WORKDIR $APP_DIR
COPY . .

#COPY bot ./bot
#COPY tests ./tests
#COPY requirements.txt .
#COPY pizzabot_docker ./pizzabot
RUN pip install -r requirements.txt