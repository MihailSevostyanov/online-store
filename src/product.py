from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def new_product(cls, product, products):
        pass


class PrintMixin:

    def __init__(self, *args):
        print(repr(self))

    def __repr__(self):
        object_attributes = ''
        for k, v in self.__dict__.items():
            object_attributes += f'{k}: {v},'
        return f"создан объект со свойствами {object_attributes})"


class Product(BaseProduct, PrintMixin):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity, color):
        super().__init__()
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
    def new_product(cls, product, products):
        new_product = cls(**product)
        try:
            if new_product.quantity > 0:
                for i in products:
                    if i.name == new_product.name:
                        i.quantity += new_product.quantity
                        i._price = max(i._price, new_product._price)
                        return i
                return new_product
            raise ZeroProductQuantity()
        except ZeroProductQuantity as e:
            print(e)
        else:
            print('Товар добавлен')
        finally:
            print('Обработка добавления товара завершена')

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


class Smartphone(Product, PrintMixin):
    def __init__(self, name, description, price, quantity, color):
        super().__init__(name, description, price, quantity, color)
        self.productivity = productivity
        self.model = model
        self.memory = memory


class Grass(Product, PrintMixin):
    def __init__(self, name, description, price, quantity, color):
        super().__init__(name, description, price, quantity, color)
        self.country = country
        self.germination_period = germination_period


class ZeroProductQuantity(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else print
        'Количество товара не может быть менее 1'

    def __str__(self):
        return self.message
