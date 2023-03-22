FROM python@sha256:0d753a7365274cef746b34dde9b4aaa27644f64e1567ed8f40ccd191ac4bd530

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python3.11", "app.py"]
