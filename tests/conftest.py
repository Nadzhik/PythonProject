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
        {"id": 1, "date": "2023-01-15"},  # Самая ранняя дата
        {"id": 2, "date": "2023-03-01"},  # Самая поздняя дата
        {"id": 3, "date": "2022-12-31"},  # Самая старая дата
        {"id": 4, "date": "2023-01-01"},  # Средняя дата
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
def sample_data():
    return [
        {"id": 1, "date": "2023-01-01", "state": "EXECUTED"},
        {"id": 2, "date": "2023-03-01", "state": "EXECUTED"},
        {"id": 3, "date": "2022-12-31", "state": "PENDING"},
        {"id": 4, "date": "2023-02-01", "state": "EXECUTED"},
        {"id": 5, "date": "2023-04-01"}  # Элемент без поля 'state'
    ]