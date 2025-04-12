def mask_account_card(user_input):
    """Функция обработки информации как о картах, так и о счетах"""
    if ' ' not in user_input:
        return "Некорректный формат. Ожидается: 'Тип Номер'."


    last_space_index = user_input.rfind(' ')
    card_type = user_input[:last_space_index].strip()
    number = user_input[last_space_index + 1:].strip()


    if card_type in ["Visa", "Visa Platinum", "Maestro", "MasterCard", "Visa Classic", "Visa Gold"]:
        # Для карт маскируем все, кроме первых 4 и последних 4 цифр
        masked_number = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
        return f"{card_type} {masked_number}"

    elif card_type == "Счет":
        # Для счета маскируем все, кроме последних 4 цифр
        masked_number = f"**{number[-4:]}"
        return f"{card_type} {masked_number}"

    else:
        return "Неизвестный тип карты или счета."

