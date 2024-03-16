class Category():
    name = str
    description = str
    goods = str
    total_number_of_categories = int
    total_number_of_unique_products = int

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.goods = goods


class Product():
    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
