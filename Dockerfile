FROM python:3.12.3-slim
LABEL authors="akapr"

WORKDIR /waiter_log_bot
COPY . .
RUN chmod 755 .
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

RUN pip install psycopg2-binary
RUN pip install --no-cache-dir -r requirements.txt


