import pytest

from src.processing import filter_by_state, sort_by_date


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


# Тесты
@pytest.mark.parametrize(
    "state, expected",
    [
        ("EXECUTED", 3),
        ("PENDING", 1),
        ("CANCELED", 0),
    ],
)
def test_filter_by_state(sample_data: list[dict[str, str]], state: str, expected: int) -> None:
    result = filter_by_state(sample_data, state)
    assert len(result) == expected


def test_sort_descending(sample_transactions: list[dict[str, str]]) -> None:
    result = sort_by_date(sample_transactions)
    assert [t["id"] for t in result] == ["2", "1", "4", "3"]


def test_sort_ascending(sample_transactions: list[dict[str, str]]) -> None:
    result = sort_by_date(sample_transactions, reverse=False)
    assert [t["id"] for t in result] == ["3", "4", "1", "2"]


def test_duplicate_dates() -> None:
    data: list[dict[str, str]] = [
        {"id": "1", "date": "2023-01-01"},
        {"id": "2", "date": "2023-01-01"},
        {"id": "3", "date": "2023-01-01"},
    ]
    result = sort_by_date(data)
    assert [item["id"] for item in result] == ["1", "2", "3"]


def test_missing_date_field() -> None:
    with pytest.raises(KeyError):
        sort_by_date([{"id": "1"}])  # Все значения как строки


def test_invalid_date_comparison() -> None:
    data: list[dict[str, str]] = [
        {"id": "1", "date": "2023-02-30"},
        {"id": "2", "date": "2023-13-01"},
        {"id": "3", "date": "invalid_date"},
    ]
    result = sort_by_date(data)
    assert [item["id"] for item in result] == ["3", "2", "1"]
