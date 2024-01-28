from dataclasses import dataclass
from enum import Enum

from data.entity_data import Transaction


@dataclass
class Category(Enum):
    GROCERIES = 1
    GAS = 2
    RESTAURANT = 3
    HOME_IMPROVEMENT = 4
    RENT = 5
    UTILITIES = 6


@dataclass
class CategorizedTransactions:
    category_name: "Category"
    transactions: list[Transaction]
