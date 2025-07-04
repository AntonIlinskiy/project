from pydantic import BaseModel
from enum import Enum


class OperationType(str, Enum):
    deposit = "DEPOSIT"
    withdraw = "WITHDRAW"


class WalletOperation(BaseModel):
    operation_type: OperationType
    amount: float
