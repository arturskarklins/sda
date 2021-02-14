# The task - e-stock of "Best GameShop Ever"

Model very simple e-sock or product catalog for a game shop, having one abstract class Product and then 3 child classes (Games, Consoles, Merchandise) inheriting it. At the end printing the products.

# Solution

My solution is available is under file **estock.py**.

**Advice**, start with the very basic parts and the smallest pieces, leave out the parts for start which looks too complicate for you.

## Details

### Product class

* is abstract class, which can't be used directly, only subclasses, hint: `from abc import ABC, abstractmethod`


* attributes:
    * name: str, mandatory and private (hint: `self.__name`), Hermetization anyone?
    * price: float, mandatory
    * id: str, must be set by Product class private method, create attribute at protected (hint: one underscore prefix)
    * price_with_vat: must be set by Product method (can be public)

    
* methods:
  * method creating and returning unique id to `self.id` for example `def __id(self) -> str:` to create a unique id use random function, hint:
    ```
    import random
    
    random_number_as_string = str(random.random()).split('.')[1]
    ```
    refresh memory about `str()`, `split()` and indexes (this `random.random()` returns float)
    
  
  * method that returns value for `self.price_with_vat`, something like `def vat_price(self):`, use 21 as VAT, hint for calculation and keeping only 2 decimal numbers:
    ```
    return f'{self.price * 1.21: .2f}'
    ```
    `: .2f` is the little thingy that helps you format float number to have only 2 decimals
  

  * as `self.name` must be private and have some validation (for example add a rule, that name length must be at least 2 chars, else print some warning message and assign default as "product"), hint decorators `@property, @name.setter, @name.deleter`

    
  * and the last bit of methods, make `def product_view(self):` as abstract, hint `@abstractmethod, pass`
    
### Child classes

Merchandise, Game, Console (feel free to add more).

Child classes inherits `Product` as abstract base class, must have one mandatory method, which was set as abstractmethod in `Product` and each class has its own extra attribute:

* Game: `genre: str`
* Console `brand: str`
* Merchandise `category: list`

Hint for constructor: `super()`


### Viewing

For testing and viewing purpose you can use the same method as in course (remember Polymorphism?):

```
def view(*products):
    for product in products:
        product.product_view()
        pprint.pprint(vars(product))
        print('*' * 80)

```

Function `pprint.pprint(dict)` helps to print dictionary in pretty looking way, see sample output below, must be importer as `import pprint`. Don't spend much time on formatting though, the main idea is to practice OOP, classes and objects..

## Sample input

```
view(
    Console('PS3', 200.00, 'Sony Play Station'),
    Console('XBOX360', 230.99, 'Microsoft XBOX'),
    Game('Final Fantasy X', 23.00, 'JRPG'),
    Game('Need For Speed Most Wanted', 34.99, 'Racing'),
    Merchandise('Marvel Avengers', 10.45, ['cup', 'dishes']),
    Merchandise('Silent Hill', 12.99, ['poster', 'decorations', 'design'])
)
```

## Sample output

Using the same data as above, note: code uses pprint instead of print, but feel free to experiment on your own regarding the output formatting, that's not the main part in the task.
```
Console: PS3 (Sony Play Station)
{'_Product__name': 'PS3',
 '_id': '7458268105930618_(PS3)',
 'brand': 'Sony Play Station',
 'price': 200.0,
 'price_with_vat': ' 242.00'}
********************************************************************************
Console: XBOX360 (Microsoft XBOX)
{'_Product__name': 'XBOX360',
 '_id': '36399807589854316_(XBOX360)',
 'brand': 'Microsoft XBOX',
 'price': 230.99,
 'price_with_vat': ' 279.50'}
********************************************************************************
Game: Final Fantasy X (JRPG)
{'_Product__name': 'Final Fantasy X',
 '_id': '13680882801970085_(Final Fantasy X)',
 'genre': 'JRPG',
 'price': 23.0,
 'price_with_vat': ' 27.83'}
********************************************************************************
Game: Need For Speed Most Wanted (Racing)
{'_Product__name': 'Need For Speed Most Wanted',
 '_id': '8542064719923121_(Need For Speed Most Wanted)',
 'genre': 'Racing',
 'price': 34.99,
 'price_with_vat': ' 42.34'}
********************************************************************************
Merchandise: Marvel Avengers (['cup', 'dishes'])
{'_Product__name': 'Marvel Avengers',
 '_id': '9954744814397253_(Marvel Avengers)',
 'category': ['cup', 'dishes'],
 'price': 10.45,
 'price_with_vat': ' 12.64'}
********************************************************************************
Merchandise: Silent Hill (['poster', 'decorations', 'design'])
{'_Product__name': 'Silent Hill',
 '_id': '8822714744838074_(Silent Hill)',
 'category': ['poster', 'decorations', 'design'],
 'price': 12.99,
 'price_with_vat': ' 15.72'}
********************************************************************************
```