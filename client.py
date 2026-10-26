import requests

user_name = input("Введите ваше имя: ")

response = requests.post(
    "http://127.0.0.1:8000/hello", json={"name": user_name}
)

print("Ответ сервера:", response.json())