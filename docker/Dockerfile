# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /
COPY ./requirements/base.txt .
RUN pip install -r base.txt
COPY . .

RUN chmod a+rwx ./scripts/local/start.sh