# 💼 FastAPI Wallet Service

REST API для управления виртуальными кошельками с использованием FastAPI и PostgreSQL.

---

## 🚀 Возможности

- Создание кошелька при первом обращении
- Пополнение кошелька (**DEPOSIT**)
- Снятие средств (**WITHDRAW**) с проверкой баланса
- Получение текущего баланса кошелька

---

## 🛠 Технологии

- Python 3.11
- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL
- Docker и Docker Compose

---

## 📦 Установка и запуск

```bash
git clone https://github.com/AntonIlinskiy/project.git
cd project
docker-compose up --build

🔧 Примеры запросов
Получить баланс кошелька
bash
Копировать
GET /api/v1/wallets/{wallet_uuid}
Провести операцию с кошельком
http
Копировать
POST /api/v1/wallets/{wallet_uuid}/operation
Content-Type: application/json

{
  "operation_type": "DEPOSIT",
  "amount": 100.0
}
👤 Автор
AntonIlinskiy