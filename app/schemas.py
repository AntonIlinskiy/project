from pydantic import BaseModel
from enum import Enum

class OperationType(str, Enum):
    deposit = "deposit"
    withdraw = "withdraw"

class WalletOperation(BaseModel):
    operation_type: OperationType
    amount: float
