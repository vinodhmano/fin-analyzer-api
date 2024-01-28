
from data.entity_data import EntityTransactions

GROCERIES = ['COSTCO']
GAS = ['GAS']
RESTAURANT = ['Paradise Biryani']
HOME_IMPROVEMENT = ['LOWES']

categories = {
    'GAS': ['GAS', 'SHELL'],
    'GROCERIES': ['COSTCO', 'CASH & CARRY', 'ALDI', 'SPROUTS', 'NAMASTE', 'TARGET', 'GLACIER'],
    'RESTAURANT': ['Paradise Biryani', 'MCDONALD', 'BAKERY', 'CAFE'],
    'HOME_IMPROVEMENT': ['LOWES', 'IKEA', 'SEARSPARTS', 'BOSH', 'DOLLAR'],
    'CLOTHING': ['MARSHALLS'],
    'INSURANCE': ['TRAVELERS', 'GEICO'],
    'TRAVELING': ['E-ZPass'],
    'UTILITIES': ['COX', 'NATURAL'],
    'CAR': ['SOAPY'],
    'ENTERTAINMENT': ['NETFLIX']
}


def get_category(description: str) -> str:
    for category, key_words in categories.items():
        for word in key_words:
            if word.lower() in description.lower():
                return category.lower()
    return 'misc'


def classify(entity_transactions: EntityTransactions) -> EntityTransactions:
    for transaction in entity_transactions.transactions:
        category = get_category(transaction.description)
        transaction.category = category
    return entity_transactions
