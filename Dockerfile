FROM python:3.13-slim-buster
WORKDIR /app
COPY . /app

RUN apt update -y && apt install awscli -y
CMD ["pyhton3",application.py]