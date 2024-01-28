import os
import re
from io import StringIO

from data.entity_data import EntityTransactions, EntityType, Transaction
from pdfminer.high_level import extract_text_to_fp

from parsers.card import Card
from parsers.helper import extract_from_pdf, get_payments_and_purchases


class BofACreditCard(Card):

    def __init__(self, card_name: str) -> None:
        super().__init__(card_name)

    def get_payments_and_credits(self, inputStr: str) -> str:
        payments = re.search('Purchases and Adjustments', inputStr)
        payments_and_credits = inputStr[:payments.start()]
        return payments_and_credits

    def get_purchases_and_adjustments(self, inputStr: str) -> str:
        payments = re.search('Purchases and Adjustments', inputStr)
        total = re.search(
            'TOTAL PURCHASES AND ADJUSTMENTS FOR THIS PERIOD', inputStr)
        purchases = inputStr[payments.end():total.start()]
        return purchases

    def get_transactions(self, inputStr: str) -> list[Transaction]:
        transactions_matches = re.finditer(
            r'\d{2}\/\d{4}\/\d{2}.+?\d{8}-?\d+\.\d{2}', inputStr)

        transactions = []

        for transaction_match in transactions_matches:
            transaction = transaction_match.group()
            if not 'PAYMENT - THANK YOU' in transaction:
                amount_match = re.search(
                    r'(?<=\d{8})-?\d+\.\d{2}', transaction).start()

                transaction_date = transaction[:5]
                desc = transaction[10:amount_match-8]
                amount = float(transaction[amount_match:])
                transactions.append(Transaction(
                    transaction_date, desc, amount, ""))

        return transactions

    def extract(self, pdf_name: str, card_name: str) -> EntityTransactions:
        extracted_output = extract_from_pdf(pdf_name=pdf_name)
        extracted_transactions = get_payments_and_purchases(
            extracted_output, "TransactionDate", "TOTAL INTEREST CHARGED")
        payments_and_credits = self.get_payments_and_credits(
            extracted_transactions)
        transactions = self.get_transactions(payments_and_credits)
        purchases = self.get_purchases_and_adjustments(extracted_transactions)
        transactions.extend(self.get_transactions(purchases))
        entity_transactions = EntityTransactions(
            card_name, EntityType.CARD, transactions)
        return entity_transactions
