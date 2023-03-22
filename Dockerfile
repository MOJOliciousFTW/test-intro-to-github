FROM python:3.12.0a5-slim

WORKDIR /app

COPY . .

CMD ["python3.11", "app.py"]
