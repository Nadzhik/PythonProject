import pytest
from src.masks import get_mask_card_number, get_mask_account


# Параметризованные тесты для get_mask_card_number
@pytest.mark.parametrize("card_number, expected", [
    ("1234567890123456", "1234 56** **** 3456"),
    ("0000000000000000", "0000 00** **** 0000"),
    ("9999999999999999", "9999 99** **** 9999"),
    ("1111222233334444", "1111 22** **** 4444"),
])
def test_get_mask_card_number_valid(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("invalid_card_number, error_msg", [
    ("1234567890", "Номер карты должен содержать числа."),
    ("12345678901234567890", "Номер карты должен содержать числа."),
    ("1234abcd56789012", "Номер карты должен содержать числа."),
    ("1234 5678 9012 3456", "Номер карты должен содержать числа."),
    ("1234-5678-9012-3456", "Номер карты должен содержать числа."),
    ("", "Номер карты должен содержать числа."),
    (" ", "Номер карты должен содержать числа."),
    (None, "Номер карты должен содержать числа."),
])
def test_get_mask_card_number_invalid(invalid_card_number, error_msg):
    with pytest.raises(ValueError, match=error_msg):
        get_mask_card_number(invalid_card_number)


# Параметризованные тесты для get_mask_account
@pytest.mark.parametrize("account_number, expected", [
    ("12345678", "**5678"),
    ("00000000", "**0000"),
    ("99999999", "**9999"),
    ("1234", "**1234"),
])
def test_get_mask_account_valid(account_number, expected):
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize("invalid_account_number, error_msg", [
    ("123", "Номер карты должен содержать числа."),
    ("", "Номер карты должен содержать числа."),
    ("12ab", "Номер карты должен содержать числа."),
    ("12-34", "Номер карты должен содержать числа."),
    ("12 34", "Номер карты должен содержать числа."),
    (" ", "Номер карты должен содержать числа."),
    (None, "Номер карты должен содержать числа."),
])
def test_get_mask_account_invalid(invalid_account_number, error_msg):
    with pytest.raises(ValueError, match=error_msg):
        get_mask_account(invalid_account_number)