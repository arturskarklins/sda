# import related base class and method decorators for abstract classes
# - ABC -> abstract base class, must be used as parent/inheritance for class which is expected to be abstract base class
# - abstractmethod -> decorator for methods, to declare method as abstract (requires implementation for child classes)
# abc module is dedicated for abstract class definitions and handling
from abc import ABC, abstractmethod


# out base class, which is set to be abstract, demonstrates Abstraction
class Profile(ABC):
    # sample of constructor, where we have 2 "public" attributes, one private with __ postfix, and rating as not
    # used, but having default value
    def __init__(self, name, age, telephone):
        self.name = name
        self.age = age
        self.rating = None
        self.telephone = telephone

    # method for Profile class and related objects, check attribute age and return content accordingly
    # remember, don t need to parse object attributes, we can access those via self reference
    def legal_content(self):
        if self.age > 18:
            print('allowed')
        else:
            print('blocked')

    # definition of abstract method with decorator, no content needed, use pass
    # abstract method in base class requires only definition, demonstrates Abstraction
    @abstractmethod
    def status(self):
        pass

    # setting property in Python style, using decorator, gives control of what we return
    # keep the name as attribute, excluding he private prefix __
    # following 3 properties/methods demonstrate Hermetization
    @property
    def telephone(self):
        return self.__telephone

    # setter function for property, user attribute name + . + setter
    # methods name must match the property defined above, so in this case telephone
    @telephone.setter
    def telephone(self, telephone):
        if len(str(telephone)) == 8:
            self.__telephone = telephone
        else:
            self.__telephone = None

    # deleter, same rules applied as for setter, just defines logic for delete action
    @telephone.deleter
    def telephone(self):
        self.__telephone = None


# child class User, inherits Profile class, demonstrates Inheritance
class User(Profile):
    def __init__(self, name, age, telephone, avatar):
        # super() function gives access to parent/base class, like in this case using it's own constructor,
        # plus handling some child class specific attributes
        super().__init__(name, age, telephone)
        self.avatar = avatar

    # mandatory method, defined by base class abstractmethod
    def status(self):
        print(f'{self.avatar} is basic user')


# child class Admin, inherits Profile class, demonstrates Inheritance
class Admin(Profile):
    def __init__(self, name, age, telephone, avatar):
        # super() function gives access to parent/base class, like in this case using it's own constructor,
        # plus handling some child class specific attributes
        super().__init__(name, age, telephone)
        self.avatar = avatar

    # mandatory method, defined by base class abstractmethod
    def status(self):
        print(f'{self.avatar} is admin user')


# child class Moderator, inherits Profile class, demonstrates Inheritance
class Moderator(Profile):
    def __init__(self, name, age, telephone, avatar):
        # super() function gives access to parent/base class, like in this case using it's own constructor,
        # plus handling some child class specific attributes
        super().__init__(name, age, telephone)
        self.avatar = avatar

    # mandatory method, defined by base class abstractmethod
    def status(self):
        print(f'{self.avatar} is moderator')


# generic function, printing profiles, their type, object id and content
# demonstrates Polymorphism
# something not in slides, function var(object) returns attributes of object in dict() format
def view(*profiles):
    for profile in profiles:
        print(type(profile), id(profile), vars(profile))
        profile.status()


# create different kind of Profile roles, User, Moderator, Admin
# important see that abstract base class Profile, can't be used, as it's abstraction of roles
bob = User('Bob', 34, 12345678, 'bob.jpg')
anna = Moderator('Anna', 18, 22334455, 'cars.jpg')
john = User('John', 45, 334455, 'cat.jpg')
tom = Admin('Tom', 34, 77889900, 'angry_cat.jpg')
george = Moderator('George', 34, 44556677, 'not_funny_cat.jpg')

# view our profiles with metadata
view(bob, anna, john, tom, george)
