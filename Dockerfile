# Dockerfile à la racine pour le backend (quand Root Directory n'est pas configuré)
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

COPY portfolio_backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY portfolio_backend/ .

CMD python manage.py migrate && gunicorn portfolio_backend.wsgi:application --bind 0.0.0.0:${PORT:-8000}
