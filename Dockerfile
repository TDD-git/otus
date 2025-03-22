# 1. Собрать образ: docker build -t my-fastapi-app .
# 2. Запустить контейнер: docker run -d -p 8000:8000 --name my-fastapi-container my-fastapi-app:1.0
# 3. Приложение будет доступно http://localhost:8000


FROM python:3.13-slim

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python", "./main.py" ]