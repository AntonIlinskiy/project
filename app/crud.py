from decimal import Decimal
from sqlalchemy.orm import Session
from app.models import Wallet
from app.schemas import WalletOperation, OperationType

def get_wallet(db: Session, wallet_uuid: str):
    wallet = db.query(Wallet).filter(Wallet.uuid == wallet_uuid).first()
    if not wallet:
        wallet = Wallet(uuid=wallet_uuid, balance=Decimal("0"))
        db.add(wallet)
        db.commit()
        db.refresh(wallet)
    return wallet

def apply_operation(db: Session, wallet_uuid: str, op: WalletOperation):
    wallet = get_wallet(db, wallet_uuid)

    amount = Decimal(str(op.amount))

    if op.operation_type == OperationType.deposit:
        wallet.balance += amount
    elif op.operation_type == OperationType.withdraw:
        if wallet.balance < amount:
            raise ValueError("Недостаточно средств")
        wallet.balance -= amount

    db.commit()
    db.refresh(wallet)
    return wallet
