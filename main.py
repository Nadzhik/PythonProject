from src import masks
from datetime import datetime
import os


if __name__ == "__main__":
    print(os.listdir())
    print(os.getcwd())
    put = os.path.join(os.getcwd(), "src/.py")
    with open(put, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)

    print(put)
    print(datetime.now())
    print(masks.get_mask_card_number("1234567891234567"))