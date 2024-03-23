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
        self.__products.extend(product)

    @property
    def print_quantity_products(self):
        string_products = ""
        for product in self.__products:
            # string_products += f'{product.name}, {product.price} руб. Остаток: {product.quantity}\n'
            string_products += f'{str(product)}'
        return string_products
