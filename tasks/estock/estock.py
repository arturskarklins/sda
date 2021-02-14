from abc import ABC, abstractmethod
import random
import pprint


# abstract Product class
class Product(ABC):
    def __init__(self, name: str, price: float):
        self.name = name  # this should be private, see all the properties below
        self.price = price
        self._id = self.__id()  # this uses class method to create value, and the method is private
        self.price_with_vat = self.vat_price()  # value calculated and set by class mathod

    # sets id using random module and concatenating it with the name
    def __id(self) -> str:
        return f'{str(random.random()).split(".")[1]}_({self.name})'

    # get s the price amount with VAT
    def vat_price(self):
        return f'{self.price * 1.21: .2f}'

    # name propery
    @property
    def name(self):
        return self.__name

    # name setter
    @name.setter
    def name(self, name):
        if len(name) > 2:
            self.__name = name
        else:
            print('Invalid name provided, placeholder will be used')
            self.__name = 'product'

    # name deleter (in this sample obsolete), but shows an option how this could be implemented
    @name.deleter
    def name(self):
        self.__name = None

    # abstract method -> required by child classes
    @abstractmethod
    def product_view(self):
        pass


class Game(Product):
    def __init__(self, name: str, price: float, genre: str):
        # reference to super/base class
        super().__init__(name, price)
        self.genre = genre

    # mandatory method as defined by base class
    def product_view(self):
        print(f"Game: {self.name} ({self.genre})")


class Console(Product):
    def __init__(self, name: str, price: float, brand: str):
        super().__init__(name, price)
        self.brand = brand

    # mandatory method as defined by base class
    def product_view(self):
        print(f"Console: {self.name} ({self.brand})")


class Merchandise(Product):
    def __init__(self, name: str, price: float, category: list):
        super().__init__(name, price)
        self.category = category

    # mandatory method as defined by base class
    def product_view(self):
        print(f"Merchandise: {self.name} ({self.category})")


# simulates the view, note uses imported pprint function for pretty print
def view(*products):
    for product in products:
        product.product_view()
        pprint.pprint(vars(product))
        print('*' * 80)


# just parse all created object directly to view() function, no need for intermediator variables, stack more if needed
view(
    Console('PS3', 200.00, 'Sony Play Station'),
    Console('XBOX360', 230.99, 'Microsoft XBOX'),
    Game('Final Fantasy X', 23.00, 'JRPG'),
    Game('Need For Speed Most Wanted', 34.99, 'Racing'),
    Merchandise('Marvel Avengers', 10.45, ['cup', 'dishes']),
    Merchandise('Silent Hill', 12.99, ['poster', 'decorations', 'design'])
)
