import re
from io import StringIO

from pdfminer.high_level import extract_text_to_fp


def extract_from_pdf(pdf_name: str) -> str:
    output = StringIO()
    with open(pdf_name, 'rb') as fin:
        extract_text_to_fp(fin, output)

    output_str = output.getvalue()
    output.close()
    return output_str


def get_payments_and_purchases(inputStr: str, starting_word: str, ending_word: str) -> str:
    match = re.search(starting_word, inputStr)
    start = match.start()

    match = re.search(ending_word, inputStr)
    end = match.end()

    payments_and_purchases = inputStr[start:end]
    return payments_and_purchases
