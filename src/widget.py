from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_input: str) -> str:
    """Функция обработки информации как о картах, так и о счетах"""
    if " " not in user_input:
        return "Некорректный формат. Ожидается: 'Тип Номер'."
    last_space_index = user_input.rfind(" ")
    card_type = user_input[:last_space_index].strip()
    number = user_input[last_space_index + 1 :].strip()
    try:
        if card_type in ["Visa", "Visa Platinum", "Maestro", "MasterCard", "Visa Classic", "Visa Gold"]:
            masked_number = get_mask_card_number(number)
            return f"{card_type} {masked_number}"

        elif card_type == "Счет":
            masked_number = get_mask_account(number)
            return f"{card_type} {masked_number}"

        else:
            return "Неизвестный тип карты или счета."

    except ValueError as e:
        return str(e)


def get_date(date_str: str) -> str:
    """Функция возврата даты"""
    date_part = date_str.split("T")[0]
    year, month, day = date_part.split("-")
    formatted_date = f"{day}.{month}.{year}"

    return formatted_date
