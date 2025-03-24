FROM python:3.10-slim

WORKDIR /EdgarsMicroCredito

COPY requirements.txt .
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    python3-dev \
    build-essential

RUN pip install -r requirements.txt



ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . .
