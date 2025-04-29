def filter_by_state(data: list[dict[str, str]], state: str = 'EXECUTED') -> list[dict[str, str]]:
    """Фильтрует список словарей по заданному состоянию."""
    filtered_data = []

    for item in data:
        if item.get('state') == state:
            filtered_data.append(item)

    return filtered_data


def sort_by_date(data: list[dict[str, str]], reverse: bool = True) -> list[dict[str, str]]:
    """Сортирует список словарей по дате."""
    return sorted(data, key=lambda x: x['date'], reverse=reverse)
