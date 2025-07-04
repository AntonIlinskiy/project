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

API будет доступен по адресу:
http://localhost:8000/docs

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
🔧 Примеры запросов и тестирование API с curl
Для проверки работы API через командную строку удобно использовать curl.

Отправка операции на пополнение кошелька (DEPOSIT)
bash
Копировать
curl -X POST "http://localhost:8000/api/v1/wallets/{wallet_uuid}/operation" \
-H "Content-Type: application/json" \
-d '{"operation_type":"DEPOSIT", "amount":100}'
{wallet_uuid} — уникальный идентификатор вашего кошелька (например, test-wallet).

-X POST — метод HTTP-запроса.

-H "Content-Type: application/json" — заголовок, который сообщает, что тело запроса в формате JSON.

-d — данные JSON с операцией и суммой.

Пример с конкретным кошельком
bash
Копировать
curl -X POST "http://localhost:8000/api/v1/wallets/test-wallet/operation" \
-H "Content-Type: application/json" \
-d '{"operation_type":"DEPOSIT", "amount":100}'
Ожидаемый ответ
json
Копировать
{
  "uuid": "test-wallet",
  "balance": 100.0
}
Другие операции
Для снятия средств (WITHDRAW) просто замените "operation_type":

bash
Копировать
curl -X POST "http://localhost:8000/api/v1/wallets/test-wallet/operation" \
-H "Content-Type: application/json" \
-d '{"operation_type":"WITHDRAW", "amount":50}'
Получение текущего баланса кошелька
bash
Копировать
curl "http://localhost:8000/api/v1/wallets/test-wallet"
Ожидаемый ответ
json
Копировать
{
  "uuid": "test-wallet",
  "balance": 50.0
}
👤 Автор
AntonIlinskiy