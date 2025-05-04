def filter_by_currency(transactions, currency):
    """Генератор, фильтрующий транзакции по заданной валюте."""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions):
    """Генератор, возвращающий описание каждой транзакции."""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start, end):
    """Генератор номеров карт в заданном диапазоне."""
    for number in range(start, end + 1):
        card_str = f"{number:016d}"
        formatted_number = " ".join([card_str[i : i + 4] for i in range(0, 16, 4)])
        yield formatted_number
