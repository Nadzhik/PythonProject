def filter_by_state(data: list[dict[str, str]], state: str = 'EXECUTED') -> list[dict[str, str]]:
    """Функция возвращающая словари, у которых ключ state соответствует указанному значению"""
    filtered_data = []

    for item in data:
        if item.get('state') == state:
            filtered_data.append(item)

    return filtered_data


def sort_by_date(data: list[dict[str, str]], reverse: bool = True) -> list[dict[str, str]]:
    """Функция возвращающая список, отсортированный по дате"""
    return sorted(data, key=lambda x: x['date'], reverse=reverse)