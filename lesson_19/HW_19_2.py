import requests
from requests.utils import quote

BASE_URL = "http://127.0.0.1:8080"

# Завантаження зображення

upload_url = f"{BASE_URL}/upload"
image_name = "mars_photo1.jpg"
encoded_image_name = quote(image_name)
post_response = requests.post(
    url=upload_url,
    files={"image": (f"{image_name}", open(f"{image_name}", "rb"), "image/jpeg")}
)
print(post_response.status_code)
print(post_response.json())

# Отримання URL завантаженого зображення

download_url = f"{BASE_URL}/image/{encoded_image_name}"
get_response = requests.get(url=download_url, headers={"Content-Type": "text"})
print(get_response)
print(get_response.json())

# Видалення зображення

delete_url = f"{BASE_URL}/delete/{encoded_image_name}"
delete_response = requests.delete(url=delete_url)
print(delete_response)
print(delete_response.json())