class Product:
    products = None
    name: str
    description: str
    price: float
    quantity: int

    # __products = []

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = float(price)
        self.quantity = quantity

    @classmethod
    def add_product(cls, product, products):
        new_product = cls(**product)

        for i in products:
            if i.name == new_product.name:
                i.quantity += new_product.quantity
                i._price = max(i._price, new_product._price)
                return i
        return new_product

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            if new_price >= self._price:
                self._price = new_price
                print('Цена обновлена')
            elif new_price < self._price and input("Вы хотите понизить цену? y/n") == 'y':
                self._price = new_price
                print("Цена понижена")
            else:
                print('Операция отменена')
        else:
            print("Введена некорректная цена")
