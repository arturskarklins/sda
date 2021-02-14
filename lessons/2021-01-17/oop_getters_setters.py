#
# NOTE: see first oop_extended.py for detailed comments, this one demonstrate just get, set function usage and how to
# use them as properties
#

class Profile:
    def __init__(self, name, age=21, telephone=''):
        self.name = name
        self.age = age
        self.rating = None
        self.__telephone = None
        self.set_telephone(telephone)

    def legal_content(self):
        if self.age > 18:
            print('allowed')
        else:
            print('blocked')

    def get_telephone(self):
        return f'This phone is {self.__telephone}'

    def set_telephone(self, telephone):
        if len(str(telephone)) == 8:
            self.__telephone = telephone
        else:
            self.__telephone = None

    telephone = property(get_telephone, set_telephone)


def view(*profiles):
    for profile in profiles:
        print(type(profile), vars(profile))


bob = Profile('Bob', 34, 12345678)
anna = Profile('Anna')

anna.telephone = 12345678
anna.set_telephone(12345678)
print(anna.telephone)

view(bob, anna)
