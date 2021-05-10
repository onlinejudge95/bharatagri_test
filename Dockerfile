FROM python:3.9.4-slim

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --requirement requirements.txt

COPY . .

CMD gunicorn --bind 0.0.0.0:8000 --workers 2 --worker-class eventlet "src.app:create_app()"
