def filter_by_state(data,state = 'EXECUTED'):
    filtered_data = []


    for item in data:
        if item.get('state') == state:
            filtered_data.append(item)

    return filtered_data