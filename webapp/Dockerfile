FROM python:3.9.0-slim-buster as builder

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY Pipfile* .

RUN apt-get update --no-install-recommends && \
  pip install --upgrade pip && \
  pip install pipenv && \
  pipenv install --system --ignore-pipfile

FROM builder as webapp

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
