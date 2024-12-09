FROM python:3.12-alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY requirements.txt /tmp/requirements.txt

RUN apk update && \
    apk add postgresql-dev gcc python3-dev musl-dev

COPY /app /app

WORKDIR /app

RUN pip install --no-cache-dir -r /tmp/requirements.txt

RUN rm -rf /tmp

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]