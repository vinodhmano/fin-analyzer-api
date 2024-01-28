import glob
import os
import re
import sys
from pathlib import Path

from aggregators.aggregator import aggregate, combine_transactions
from classifiers.category_classifier import classify
from displays.plotter import plot_charts
from parsers.best_buy_card import BestBuyCard
from parsers.bofa_credit_card import BofACreditCard

FOLDER = r'C:\Users\vinod\OneDrive\Documents\US\Finances\2022\Apr'


def run() -> None:
    if not os.path.exists(FOLDER):
        print(f'FOLDER {FOLDER} not found')
        sys.exit(1)

    compiled_transactions = {}
    all_transactions = []

    _files = Path(FOLDER)
    files  = list(_files.rglob('*.pdf'))

    for file in files:
        if "CashRewardsCard" in file.name:
            cash_rewards_card = BofACreditCard("Cash Rewards")
            transactions = cash_rewards_card.extract(
                file.as_posix(), 'Cash Rewards Card')
            classified_transactions = classify(transactions)
            all_transactions.append(classified_transactions)

        if "TravelRewardsCard" in file.name:
            travel_rewards_card = BofACreditCard("Travel Rewards")
            transactions = travel_rewards_card.extract(
                file.as_posix(), 'Travel Rewards Card')
            classified_transactions = classify(transactions)
            all_transactions.append(classified_transactions)

        if "BestBuy" in file.name:
            bb_card = BestBuyCard("Best Buy Card")
            transactions = bb_card.extract(file.as_posix(), 'Best Buy Card')
            classified_transactions = classify(transactions)
            all_transactions.append(classified_transactions)

    print(all_transactions)

    # compiled_transactions = combine_transactions(all_transactions)
    aggregated_transactions = aggregate(all_transactions)
    plot_charts(aggregated_transactions)


if __name__ == '__main__':
    run()
