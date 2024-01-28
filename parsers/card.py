from abc import ABC

from data.entity_data import EntityTransactions


class Card(ABC):
    card_name: str

    def __init__(self, card_name: str) -> None:
        self.card_name = card_name

    def get_transactions(self, inputStr: str) -> list[dict]:
        pass

    def extract(self, pdf_name: str, card_name: str) -> EntityTransactions:
        pass
