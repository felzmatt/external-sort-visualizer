FROM python:3.10 as build
WORKDIR /app
COPY requirements.txt .
RUN cd /app && pip install --no-cache -r requirements.txt