from sqlalchemy.orm import Session
from decimal import Decimal
from . import models, schemas
from .schemas import WalletOperation, OperationType
from fastapi import HTTPException

def get_wallet(db: Session, wallet_uuid: str):
    return db.query(models.Wallet).filter(models.Wallet.uuid == wallet_uuid).first()


def create_wallet(db: Session, wallet_uuid: str):
    wallet = models.Wallet(uuid=wallet_uuid, balance=Decimal("0.00"))
    db.add(wallet)
    db.commit()
    db.refresh(wallet)
    return wallet


from fastapi import HTTPException

def apply_operation(db: Session, wallet_uuid: str, op: WalletOperation):
    wallet = get_wallet(db, wallet_uuid)
    if not wallet:
        wallet = create_wallet(db, wallet_uuid)

    amount = Decimal(str(op.amount))

    if op.operation_type == OperationType.DEPOSIT:
        wallet.balance += amount
    elif op.operation_type == OperationType.WITHDRAW:
        if wallet.balance < amount:
            raise HTTPException(status_code=400, detail="Недостаточно средств")
        wallet.balance -= amount

    db.commit()
    db.refresh(wallet)
    return wallet
