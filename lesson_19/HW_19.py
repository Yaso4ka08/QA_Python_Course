import requests
import json

BASE_URL = "https://images-api.nasa.gov"

# Пошук зображень
search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",  # пошуковий запит
    "media_type": "image",  # тільки зображення
    "page_size": 20  # щоб було з чого вибрати
}
response = requests.get(url=search_url, params=search_params)

# Перевірка статус-коду
if response.status_code == 200:
    try:
        data = response.json()
        print('Отримано дані:', data)
        items = data["collection"]["items"]
        print(items)
        for i in items:
            nasa_id = i["data"][0]["nasa_id"]
            print(nasa_id)
            # Отримання файлів по nasa_id
            asset_url_template = f"{BASE_URL}/asset/{nasa_id}"
            print(asset_url_template)
            asset_url_response = requests.get(url=asset_url_template)
            try:
                asset_url_response_json = asset_url_response.json()
                asset_items = asset_url_response_json["collection"]["items"]
                # лише для перших елементів буду качати файли
                for index, i in enumerate(asset_items[:2]):
                    # знаходжу лінку за котрой качати
                    asset_image = i["href"]
                    img = requests.get(asset_image).content
                    # зберігаю файл разом із індексацією для файлів
                    with open(f"mars_photo{index + 1}.jpg", "wb") as f:
                        f.write(img)

            except json.JSONDecodeError as e:
                print('Помилка при серіалізації JSON:', e)
                print("Не має змоги скачати файл")

    except json.JSONDecodeError as e:
        print('Помилка при серіалізації JSON:', e)
else:
    print('Помилка. Статус-код:', response.status_code)





