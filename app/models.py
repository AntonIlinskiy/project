from sqlalchemy import Column, String, Numeric
from app.database import Base


class Wallet(Base):
    __tablename__ = "wallets"

    uuid = Column(String, primary_key=True, index=True)
    balance = Column(Numeric(scale=2), default=0)

