import functools # for backwards compatibility in case multi-decorators fail to work


# decorator
def travel_adds(header, footer):
    def dec(func):  # decorator handles arguments, inner decorator function that accepts parsed function - func
        @functools.wraps(func)  # solves problems with older Python
        def wrapper(*args, **kwargs):  # *args and **kwargs used for functions that are decorated, if arguments used
            print(header)  # executes code before decorated function
            func(*args, **kwargs)  # call decorated function
            print(footer)  # executes code after decorated function

        return wrapper  # returns wrapper function
    return dec  # return decorator function


# decorator
def car_adds(header, footer):
    def dec(func):
        @functools.wraps(func)  # solves problems with older Python
        def wrapper(*args, **kwargs):
            print(header)
            func(*args, **kwargs)
            print(footer)

        return wrapper
    return dec


# decorated function with two decorators
@car_adds('Mazda', 'Audi')
@travel_adds('London, Paris', 'Ventspils, Liepāja')
def profile(name):
    print(f'Profile {name}')


@car_adds('Volvo', 'Opel')
@travel_adds('Oslo, Helsinki', 'Rēzekne, Daugavpils')
def stories(author, date):
    print(f'Friends stories by {author} on {date}')


profile('Bob')
stories('Anna', '2021-02-13')
