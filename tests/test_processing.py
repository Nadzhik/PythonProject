import pytest
from src.processing import sort_by_date, filter_by_state


@pytest.mark.parametrize("state, expected", [
    ("EXECUTED", 3),  # 3 элемента с state="EXECUTED"
    ("PENDING", 1),   # 1 элемент с state="PENDING"
    ("CANCELED", 0),  # 0 элементов с state="CANCELED"
])
def test_filter_by_state(sample_data, state, expected):
    result = filter_by_state(sample_data, state)
    assert len(result) == expected


def test_sort_descending(sample_transactions):
    """Сортировка по убыванию (reverse=True)"""
    result = sort_by_date(sample_transactions)
    # Ожидаемый порядок id: от самой новой даты к самой старой
    assert [t["id"] for t in result] == [2, 1, 4, 3]


def test_sort_ascending(sample_transactions):
    """Сортировка по возрастанию (reverse=False)"""
    result = sort_by_date(sample_transactions, reverse=False)
    # Ожидаемый порядок id: от самой старой даты к самой новой
    assert [t["id"] for t in result] == [3, 4, 1, 2]


# Тесты на пограничные случаи
def test_empty_list():
    """Пустой список на входе"""
    assert sort_by_date([]) == []


def test_single_element():
    """Список с одним элементом"""
    data = [{"date": "2023-01-01"}]
    assert sort_by_date(data) == data


def test_duplicate_dates():
    """Проверка стабильности сортировки"""
    data = [
        {"id": 1, "date": "2023-01-01"},
        {"id": 2, "date": "2023-01-01"},
        {"id": 3, "date": "2023-01-01"}
    ]
    result = sort_by_date(data)
    assert [item["id"] for item in result] == [1, 2, 3]


# Тесты на ошибки
def test_missing_date_field():
    """Отсутствует поле date"""
    with pytest.raises(KeyError):
        sort_by_date([{"id": 1}])


def test_invalid_date_comparison():
    """Некорректные даты (сортировка как строк)"""
    data = [
        {"id": 1, "date": "2023-02-30"},  # Несуществующая дата
        {"id": 2, "date": "2023-13-01"},  # Неправильный месяц
        {"id": 3, "date": "hello_world"}
    ]

    # Ожидаемый порядок при сортировке строк в обратном порядке (reverse=True)
    result = sort_by_date(data)
    assert [item["id"] for item in result] == [3, 2, 1]