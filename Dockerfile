# Модель: Метод золотого перерізу (5 семестр)
# Автор: Іщенко Дмитро, група АІ-232

FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
