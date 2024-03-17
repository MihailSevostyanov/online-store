class Category:
    name: str
    description: str
    products: str
    total_number_of_categories = 0
    total_number_of_unique_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        self.total_number_of_categories = 1

        Category.total_number_of_unique_products = len(products)
