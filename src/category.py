from src.utils import read_products


class Category:
    name: str
    description: str
    products: list
    total_number_of_categories = 0
    total_number_of_unique_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        self.total_number_of_categories = 1

        Category.total_number_of_unique_products = len(products)

    def add_products(self, product):
        self.__products.extend(product)

    @property
    def print_quantity_products(self):
        for product in self.__products:
            return f'{product.name}, {product.price} руб. Остаток: {product.quantity}'
