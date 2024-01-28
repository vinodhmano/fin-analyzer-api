from data.entity_data import EntityTransactions


def aggregate(data: list[EntityTransactions]) -> dict:
    output_dict = {}
    for entity in data:
        for transaction in entity.transactions:
            key = transaction.category
            if output_dict.get(key) is None:
                output_dict[key] = 0
            output_dict[key] += float(transaction.amount)
    return output_dict


def combine_transactions(all_transactions: list[EntityTransactions]) -> dict:
    result = {}
    for card_transactions in all_transactions:
        for key, value in card_transactions.items():
            if result.get(key) is None:
                result[key] = []
            result[key].append(value)
    return result
