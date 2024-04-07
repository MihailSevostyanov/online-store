from src.product import Product, ZeroProductQuantity
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
        try:
            if isinstance(product, Product):
                self.__products.append(product)
                return self.__products
            raise ValueError('Добавляемое значение не является экземпляром класса Product или его наследником')
        except ValueError as e:
            print(e)
            return self.__products
        finally:
            print('Обработка добавления товара завершена')

    @property
    def print_quantity_products(self):
        string_products = ""
        for product in self.__products:
            string_products += f'{str(product)}'
        return string_products


    def average_price(self):
        try:
            average_price = round(sum([i._price for i in self.__products]) / len(self.__products), 2)
            return average_price
        except ZeroDivisionError:
            return 0



class Order(BaseCategory):
    def __init__(self, product, quantity):
        try:
            if quantity > 0:
                super().__init__()
                self.product = product
                self.quantity = quantity
                self.final_price = product._price * quantity
            else:
                raise ZeroProductQuantity
        except ZeroProductQuantity as e:
            print(e)
        else:
            print('Товар добавлен')
        finally:
            print('Обработка добавления товара завершена')
