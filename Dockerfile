FROM python:3.8-buster
ENV PYTHONUNBUFFERED 1

WORKDIR /code
COPY . /code/
COPY contrib/env-sample .env

RUN apt-get update && \
    apt-get install -y make && \
    rm -rf /var/lib/apt/lists/* && \
    pip install -U pip && \
    pip install -U pipenv && \
    pipenv install --system --dev

RUN python /code/manage.py migrate
