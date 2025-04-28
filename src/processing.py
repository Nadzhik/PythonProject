def filter_by_state(data,state = 'EXECUTED'):
    filtered_data = []


    for item in data:
        if item.get('state') == state:
            filtered_data.append(item)

    return filtered_data




def sort_by_date(data, reverse=True):
    return sorted(data, key=lambda x: x['date'], reverse=reverse)