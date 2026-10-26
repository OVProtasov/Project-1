"""Итоговый вариант приложения для преподавателя и сверки."""

import os

from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel

class UserInput(BaseModel):
  name: str

app = FastAPI(title="F : H")
load_dotenv('.env', override=True)


@app.get("/")
def root():
    return {"message": "Сервис работает"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/version")
def hi(vr: str = os.getenv("APP_VERSION", "N/A")):
    return {"version": vr}

@app.get("/info")
def info():
    app_name = os.getenv("APP_NAME", "N/A")
    app_author = os.getenv("APP_AUTHOR", "N/A")

    return {
        "app_name": app_name,
        "author": app_author,
    }

@app.post("/hello")
def hello(data: UserInput):
  return {"message": f"Привет, {data.name}!"}
