from dataclasses import dataclass
from datetime import date, datetime
from enum import Enum


@dataclass
class EntityType(Enum):
    CARD = 1
    CHECKING = 2
    SAVINGS = 3


@dataclass
class Transaction:
    transaction_date: str
    description: str
    amount: float
    category: str


@dataclass
class EntityTransactions:
    name: str
    type: "EntityType"
    transactions: list[Transaction]
