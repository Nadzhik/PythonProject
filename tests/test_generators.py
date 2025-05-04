import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_usd(sample_transactions):
    usd_transactions = list(filter_by_currency(sample_transactions, "USD"))
    assert len(usd_transactions) == 3
    for transaction in usd_transactions:
        assert transaction["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_rub(sample_transactions):
    rub_transactions = list(filter_by_currency(sample_transactions, "RUB"))
    assert len(rub_transactions) == 2


def test_filter_by_currency_empty():
    assert list(filter_by_currency([], "USD")) == []


def test_transaction_descriptions(sample_transactions):
    descriptions = list(transaction_descriptions(sample_transactions))
    expected = [t["description"] for t in sample_transactions]
    assert descriptions == expected


def test_transaction_descriptions_empty():
    assert list(transaction_descriptions([])) == []


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (1, 1, ["0000 0000 0000 0001"]),
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (9999999999999999, 9999999999999999, ["9999 9999 9999 9999"]),
        (10, 12, ["0000 0000 0000 0010", "0000 0000 0000 0011", "0000 0000 0000 0012"]),
    ],
)
def test_card_number_generator(start, end, expected):
    result = list(card_number_generator(start, end))
    assert result == expected


def test_card_number_generator_invalid_range():
    assert list(card_number_generator(5, 1)) == []
