# Base image
FROM python:3.13.2

# Встановлюємо робочу директорію всередині контейнера
WORKDIR /app

# Копіюємо файл залежностей першим (для кешування шарів)
COPY requirements.txt .

# Встановлюємо всі залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь проект в контейнер
COPY . .

# Запуск всіх тестів
CMD ["pytest", ".", "-v", "--tb=short"]
