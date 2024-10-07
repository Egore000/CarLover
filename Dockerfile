FROM python:3.12

COPY requirements.txt /tmp/requirements.txt

COPY /app /app

WORKDIR /app

RUN pip install -r /tmp/requirements.txt