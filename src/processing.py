# tests/test_processing.py
import pytest
from processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_data():
    return [
        {"date": "2023-01-01", "state": "EXECUTED"},
        {"date": "2023-02-01", "state": "PENDING"},
        {"date": "2023-03-01", "state": "EXECUTED"},
    ]


def test_filter_by_state(sample_data):
    filtered = filter_by_state(sample_data, "EXECUTED")
    assert len(filtered) == 2
    assert all(item["state"] == "EXECUTED" for item in filtered)


def test_sort_by_date_asc(sample_data):
    sorted_data = sort_by_date(sample_data)
    assert sorted_data[0]["date"] == "2023-01-01"


def test_sort_by_date_desc(sample_data):
    sorted_data = sort_by_date(sample_data, reverse=True)
    assert sorted_data[0]["date"] == "2023-03-01"