import pytest

@pytest.fixture
def sample_card_numbers():
    return [
        "1234567890123456",  # Валидный номер карты
        "1234567890",       # Неверная длина
        "abcd567890123456",  # Буквы в номере
    ]

@pytest.fixture
def sample_account_numbers():
    return [
        "12345678",  # Валидный номер счета
        "123",       # Слишком короткий
        "abcd5678",  # Буквы в номере
    ]

@pytest.fixture
def sample_transactions():
    return [
        {"date": "2023-01-01", "state": "EXECUTED"},
        {"date": "2023-02-01", "state": "PENDING"},
        {"date": "2023-03-01", "state": "EXECUTED"},
        {"date": "2022-12-31", "state": "CANCELED"},
    ]

@pytest.fixture
def sample_account_card_inputs():
    return [
        ("Visa 1234567890123456", "Visa 1234 56** **** 3456"),
        ("Счет 12345678", "Счет **5678"),
        ("Unknown 12345678", "Неизвестный тип карты или счета."),
        ("InvalidFormat", "Некорректный формат. Ожидается: 'Тип Номер'."),
    ]

@pytest.fixture
def sample_dates():
    return [
        ("2023-12-31T12:34:56", "31.12.2023"),
        ("2023-01-01T00:00:00", "01.01.2023"),
    ]