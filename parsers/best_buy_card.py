import re
from io import StringIO

from data.entity_data import EntityTransactions, EntityType, Transaction
from parsers.card import Card
from parsers.helper import extract_from_pdf, get_payments_and_purchases


class BestBuyCard(Card):
    def __init__(self, card_name: str) -> None:
        super().__init__(card_name)

    def get_transactions(self, inputStr: str) -> list[Transaction]:
        transactions_matches = re.finditer(
            r"\d{2}/\d{2}.*?(?=\d{2}/\d{2})|\d{2}/\d{2}.*?FEES", inputStr)
        transactions = []

        for transaction_match in transactions_matches:
            transaction = transaction_match.group()
            if not 'AUTOPAY PAYMENT' in transaction:

                transaction_date = transaction[:5]
                # reference_number is required to cut the description from end of date to the start of reference number
                reference_number = re.search(
                    r"\d{6}\w{11}", transaction).start()
                desc = transaction[5:reference_number]

                # amount is in the format of $ 5.08
                # also it has negative sign at the end like $ 55.09-
                amount = re.search(
                    r'\$ \d+.\d{2}-?', transaction).group()
                if amount[-1] == '-':
                    amount = float(amount[2:-1])
                else:
                    amount = float(amount[2:])

                transactions.append(Transaction(
                    transaction_date, desc, amount, ""))

        return transactions

    def extract(self, pdf_name: str, card_name: str) -> EntityTransactions:
        extracted_text = extract_from_pdf(pdf_name)
        extracted_transactions = get_payments_and_purchases(
            extracted_text, "TRANSACTIONS", "FEES")
        transactions = self.get_transactions(extracted_transactions)
        entity_transactions = EntityTransactions(
            card_name, EntityType.CARD, transactions)
        return entity_transactions
