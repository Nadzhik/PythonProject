# Виджет банковских операций клиента


## Описание

 Это виджет, который показывает несколько последних успешных банковских операций клиента.


## Установка

Убедитесь, что установлен Python 3.6 или выше. Установите зависимости:

```bash
pip install -r requirements.txt
```

## Использование

Импортируйте функции:

```python
from your_module import filter_by_state, sort_by_date, get_mask_card_number , get_mask_account, 
```

### Функции

- **filter_by_state(data, state='EXECUTED')**: Фильтрует транзакции по состоянию.
  
- **sort_by_date(data, reverse=True)**: Сортирует транзакции по дате.
- 
- **get_mask_account(check_number)**: Маскирует номер счета.
- 
- **get_mask_card_number(user_card_number)**: Маскирует номер карты.


### Примеры

#### Фильтрация и сортировка транзакций

```python
data = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01'},
    {'id': 2, 'state': 'CANCELED', 'date': '2023-01-02'},
]

executed = filter_by_state(data)
sorted_data = sort_by_date(data)
```

#### Маскирование номера карты

```python
card_number = "1234567812345678"
masked_card = get_mask_card_number(card_number)
print(masked_card)  # Ожидаемый вывод: "1234 56** **** 5678"
```

#### Маскирование номера счета

```python
account_number = "1234567890123456"
masked_account = get_mask_account(account_number)
print(masked_account)  # Ожидаемый вывод: "**3456"
```

## Лицензия

MIT License.