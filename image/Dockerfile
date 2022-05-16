# syntax=docker/dockerfile:1
FROM dart:2.17

WORKDIR /app

COPY ./src ./src

WORKDIR /app/src

RUN dart pub get
RUN dart compile exe bin/main.dart -o /app/exec

EXPOSE 80

CMD [ "/app/exec" ]
