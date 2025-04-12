def get_mask_card_number(user_card_number: str) -> str:
    """Функция принимает на вход номер карты в виде числа и возвращает маску номера"""
    if not user_card_number.isdigit():
        raise ValueError("Номер карты должен содержать числа.")
    masked_number = f"{user_card_number[:4]} {user_card_number[4:6]}** **** {user_card_number[12:]}"

    return masked_number


def get_mask_account(check_number: str) -> str:
    """Функция принимает на вход номер счета в виде числа и возвращает маску номера"""
    if not check_number.isdigit():
        raise ValueError("Номер карты должен содержать числа.")
    masked_check = f"**{check_number[-4:]}"

    return masked_check
