FROM python:3.10-slim

WORKDIR /EdgarsMicroCredito

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . .
