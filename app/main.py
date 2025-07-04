from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import engine
from app.deps import get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/api/v1/wallets/{wallet_uuid}/operation")
def operate_wallet(wallet_uuid: str, operation: schemas.WalletOperation, db: Session = Depends(get_db)):
    try:
        wallet = crud.apply_operation(db, wallet_uuid, operation)
        return {"uuid": wallet.uuid, "balance": float(wallet.balance)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/api/v1/wallets/{wallet_uuid}")
def get_balance(wallet_uuid: str, db: Session = Depends(get_db)):
    wallet = crud.get_wallet(db, wallet_uuid)
    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet not found")
    return {"uuid": wallet.uuid, "balance": float(wallet.balance)}


