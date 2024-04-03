from src.product import Product
from abc import ABC, abstractmethod


class BaseCategory(ABC):
    @abstractmethod
    def __init__(self):
        pass


class Category(BaseCategory):
    name: str
    description: str
    products: list
    total_number_of_categories = 0
    total_number_of_unique_products = 0

    def __init__(self, name, description, products):
        super().__init__()
        self.name = name
        self.description = description
        self.__products = products

        Category.total_number_of_categories += 1
        Category.total_number_of_unique_products = len(products)

    def __len__(self):
        count = 0
        for i in self.__products:
            count += i.quantity
        return count

    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self)} шт.'

    def add_products(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
        raise ValueError('Добавляемое значение не является экземпляром класса Product или его наследником')

    @property
    def print_quantity_products(self):
        string_products = ""
        for product in self.__products:
            string_products += f'{str(product)}'
        return string_products


class Order(BaseCategory):
    def __init__(self, product, quantity):
        super().__init__()
        self.product = product
        self.quantity = quantity
        self.final_price = product._price * quantity

