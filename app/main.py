from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import WalletOperation

# Создаём таблицы (если не созданы)
models.Base.metadata.create_all(bind=engine)

# Инициализируем FastAPI
app = FastAPI()

# Настраиваем CORS (можно убрать, если не нужно)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Получение сессии БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Эндпоинт для операций с кошельком
@app.post("/api/v1/wallets/{wallet_uuid}/operation")
def operate_wallet(wallet_uuid: str, operation: WalletOperation, db: Session = Depends(get_db)):
    wallet = crud.apply_operation(db, wallet_uuid, operation)
    return wallet

# Эндпоинт для получения информации о кошельке
@app.get("/api/v1/wallets/{wallet_uuid}")
def get_wallet(wallet_uuid: str, db: Session = Depends(get_db)):
    wallet = crud.get_wallet(db, wallet_uuid)
    return wallet
