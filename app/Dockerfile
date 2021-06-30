FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "app:flask_app", "--bind=0.0.0.0:5000", "--workers=1", "--log-level=debug", "--timeout=60"]
