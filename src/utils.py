import json

from config import file_path


def read_products():
    """
    Функция читает файл products.json
    :return:
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        file = f.read()
        products = json.loads(file)
    return products
