import pytest


@pytest.fixture
def sample_data():
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01'},
        {'id': 2, 'state': 'CANCELED', 'date': '2023-01-02'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2023-01-03'},
        {'id': 4, 'state': 'EXECUTED', 'date': '2023-01-01'},
    ]

@pytest.fixture
def card_numbers():
    return [
        "1234567812345678",
        "123456781234567",
        "abcd1234efgh5678",
        "12345678123456789",
        "",
    ]

@pytest.fixture
def account_numbers():
    return [
        "1234567890123456",
        "1234",
        "",
        "abcd1234efgh"
    ]
