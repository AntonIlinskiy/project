#!/bin/bash
set -e

echo "⌛ Ждём, пока БД станет доступной..."
while ! nc -z db 5432; do
  sleep 1
done

echo "✅ БД доступна. Применяем миграции..."
alembic upgrade head

echo "🚀 Запускаем сервер..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
