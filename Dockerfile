FROM python:3.10-slim

WORKDIR /SIMPLE_ETL

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .