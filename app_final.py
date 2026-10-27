"""Итоговый вариант приложения для преподавателя и сверки."""

import os

from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel

# Словарь с предсказаниями для знаков зодиака
HOROSCOPES = {
    "овен": "завтра вас ожидает битва с кофемашиной — она снова победит",
    "телец": (
        "завтра вас ожидает находка: в холодильнике ждёт кусочек идеального"
        " сыра"
    ),
    "близнецы": (
        "завтра вас ожидает старт трёх дел — и мгновенное забывание о них"
    ),
    "рак": "завтра вас ожидает ответ на сообщение трёхлетней давности",
    "лев": (
        "завтра вас ожидает всеобщее внимание — даже за поеданием бутерброда"
    ),
    "дева": "завтра вас ожидает победа: порядок хотя бы в одном ящике",
    "весы": "завтра вас ожидает трудный выбор: чай или кофе",
    "скорпион": "завтра вас ожидает подвиг: удаление 37 непрочитанных писем",
    "стрелец": "завтра вас ожидает приключение — хотя бы в маршруте навигатора",
    "козерог": (
        "завтра вас ожидает уважение даже от кота — он не скинет вещи со стола"
    ),
    "водолей": "завтра вас ожидает гениальная идея: бутерброд наоборот",
    "рыбы": "завтра вас ожидает прилив вдохновения — хватит на один абзац",
}


class HoroscopeInput(BaseModel):
  text: str  # Ввод в формате: "Имя знак" (например: "Иван овен")

class UserInput(BaseModel):
  name: str

app = FastAPI(title="F : H")
load_dotenv('.env.example.env', override=True)


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

@app.post("/horoscope")
def get_horoscope(data: HoroscopeInput):
  # Разделяем введенную строку на имя и знак зодиака по первому пробелу
  parts = data.text.strip().split(maxsplit=1)

  if len(parts) < 2:
    return {
        "error": (
            "Пожалуйста, введите имя и знак зодиака через пробел (например:"
            " 'Иван овен')"
        )
    }

  name = parts[0]
  zodiac = parts[1].lower()

  # Ищем вариант предсказания, если знак не найден — выводим дефолтный
  variant = HOROSCOPES.get(
      zodiac, "завтра вас ожидает что-то загадочное и неизвестное"
  )

  return {"forecast": f"Привет, {name}, {variant}!"}