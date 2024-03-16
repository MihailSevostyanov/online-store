class Category:
    name: str
    description: str
    goods: str
    total_number_of_categories = 0
    total_number_of_unique_products = 0

    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.product = product
        self.total_number_of_categories = 1

        Category.total_number_of_unique_products += 1


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = float(price)
        self.quantity = quantity

