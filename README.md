# 💼 Wallet API — FastAPI + PostgreSQL + Docker + Alembic

REST API для операций с кошельками: пополнение, снятие, проверка баланса.

## 🚀 Запуск проекта

1. Убедитесь, что установлен Docker и Docker Compose

2. Распакуйте архив и перейдите в папку проекта

```bash
unzip wallet_app.zip
cd wallet_app
```

3. Запустите проект:

```bash
docker-compose up --build
```

4. Откройте документацию:

```
http://localhost:8000/docs
```

## 🧪 Запуск тестов

```bash
docker-compose exec web pytest
```

## 📦 Стек

- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Docker Compose
