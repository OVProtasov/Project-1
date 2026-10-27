import requests


def main():
  print("=== Умный клиент FastAPI ===")

  # Запрашиваем ввод у пользователя одной строкой
  user_input = input(
      "Введите имя (для приветствия) или имя со знаком зодиака (например: Иван"
      " овен):\n> "
  ).strip()

  if not user_input:
    print("\n[Ошибка]: Вы ничего не ввели.")
    return

  # Разбиваем введенную строку на слова по пробелам
  words = user_input.split()

  try:
    if len(words) == 1:
      # Если одно слово — отправляем на /hello
      name = words[0]
      response = requests.post(
          "http://127.0.0.1:8000/hello", json={"name": name}
      )
    else:
      # Если два или больше слов — отправляем на /horoscope
      response = requests.post(
          "http://127.0.0.1:8000/horoscope", json={"text": user_input}
      )

    # Выводим результат ответа сервера
    print("\nОтвет сервера:", response.json())

  except requests.exceptions.ConnectionError:
    print(
        "\n[Ошибка]: Не удалось подключиться к серверу. Убедитесь, что Uvicorn"
        " запущен!"
    )


if __name__ == "__main__":
  main()