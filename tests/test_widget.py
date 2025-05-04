import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("Visa 1234567890123456", "Visa 1234 56** **** 3456"),
        ("Счет 12345678", "Счет **5678"),
        ("Unknown 12345678", "Неизвестный тип карты или счета."),
        ("InvalidFormat", "Некорректный формат. Ожидается: 'Тип Номер'."),
    ],
)
def test_mask_account_card(input_str: str, expected: str) -> None:
    assert mask_account_card(input_str) == expected


def test_get_date_valid() -> None:
    assert get_date("2023-12-31T12:34:56") == "31.12.2023"


def test_get_date_invalid_format() -> None:
    with pytest.raises(ValueError):
        get_date("2023/12/31")  # Неверный формат
