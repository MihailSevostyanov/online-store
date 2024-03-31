from abc import ABC, abstractmethod


class AbstractProduct(ABC):
    @abstractmethod
    def __init__(self):
        pass


class MixinLog:

    def __repr__(self):
        return (f"Создан объект {self.__class__.__name__}('{self.name}', '{self.description}', "
                f"'{self.price}', '{self.quantity}')")


class Product(AbstractProduct, MixinLog):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity, color):
        self.name = name
        self.description = description
        self._price = float(price)
        self.quantity = quantity
        self.color = color

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity}'

    def __add__(self, other):
        if type(self) == type(other):
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise ValueError("Нельзя складывать товары из разных категорий")

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


class Smartphone(Product, MixinLog):
    def __init__(self, name, description, price, quantity, color):
        super().__init__(name, description, price, quantity, color)
        self.productivity = productivity
        self.model = model
        self.memory = memory


class Grass(Product, MixinLog):
    def __init__(self, name, description, price, quantity, color):
        super().__init__(name, description, price, quantity, color)
        self.country = country
        self.germination_period = germination_period
