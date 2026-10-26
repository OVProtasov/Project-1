"""Итоговый вариант приложения для преподавателя и сверки."""

import os

from fastapi import FastAPI
from dotenv import load_dotenv


app = FastAPI(title="F : H")
load_dotenv('settings.env', override=True)


@app.get("/")
def root():
    return {"message": "Сервис работает"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/hello")
def hello(name: str = "студент"):
    return {"message": f"Привет, {name}!"}

@app.get("/info")
def info():
    app_name = os.getenv("APP_NAME", "N/A")
    app_author = os.getenv("APP_AUTHOR", "N/A")

    return {
        "app_name": app_name,
        "author": app_author,
    }
