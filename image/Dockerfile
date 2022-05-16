# syntax=docker/dockerfile:1
FROM python:3

WORKDIR /app

COPY ./src ./src

WORKDIR /app/src

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD [ "python", "main.py" ]
