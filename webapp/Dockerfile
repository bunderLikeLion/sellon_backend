FROM python:3.9.0-slim-buster as builder

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update --no-install-recommends && \
  pip install --upgrade pip && \
  pip install pipenv

FROM builder as package

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY ./Pipfile* ./

RUN pipenv requirements > requirements.txt
RUN pip install -r requirements.txt
# RUN pipenv install --system --ignore-pipfile

FROM package as webapp

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY . .

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
