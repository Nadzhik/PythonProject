import pytest
from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number_valid():
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"


def test_get_mask_card_number_invalid_length():
    with pytest.raises(ValueError, match="Номер карты должен содержать числа."):
        get_mask_card_number("1234567890")  # Неверная длина


def test_get_mask_card_number_not_digits():
    with pytest.raises(ValueError, match="Номер карты должен содержать числа."):
        get_mask_card_number("1234abcd56789012")  # Буквы в номере


def test_get_mask_account_valid():
    assert get_mask_account("12345678") == "**5678"


def test_get_mask_account_too_short():
    with pytest.raises(ValueError, match="Номер карты должен содержать числа."):
        get_mask_account("123")  # Слишком короткий