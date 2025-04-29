import pytest


@pytest.fixture
def sample_card_numbers() -> list[str]:
    return [
        "1234567890123456",  # Валидный номер карты
        "1234567890",  # Неверная длина
        "abcd567890123456",  # Буквы в номере
    ]


@pytest.fixture
def sample_account_numbers() -> list[str]:
    return [
        "12345678",  # Валидный номер счета
        "123",  # Слишком короткий
        "abcd5678",  # Буквы в номере
    ]


@pytest.fixture
def sample_account_card_inputs() -> list[tuple]:
    return [
        ("Visa 1234567890123456", "Visa 1234 56** **** 3456"),
        ("Счет 12345678", "Счет **5678"),
        ("Unknown 12345678", "Неизвестный тип карты или счета."),
        ("InvalidFormat", "Некорректный формат. Ожидается: 'Тип Номер'."),
    ]


@pytest.fixture
def sample_data() -> list[dict[str, str]]:
    return [
        {"id": "1", "state": "EXECUTED", "date": "2023-01-15"},
        {"id": "2", "state": "EXECUTED", "date": "2023-03-01"},
        {"id": "3", "state": "PENDING", "date": "2022-12-31"},
        {"id": "4", "state": "EXECUTED", "date": "2023-01-01"},
    ]


@pytest.fixture
def sample_transactions() -> list[dict[str, str]]:
    return [
        {"id": "1", "date": "2023-01-15"},
        {"id": "2", "date": "2023-03-01"},
        {"id": "3", "date": "2022-12-31"},
        {"id": "4", "date": "2023-01-01"},
    ]
