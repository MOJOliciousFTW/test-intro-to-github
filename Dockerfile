FROM python:3.11

WORKDIR /app

COPY . .

CMD ["python3.11", "app.py"]
