# decorator as class
class TravelAdds:
    def __init__(self, func):
        self.func = func

    # add magic method __call__ to handle the decorator functionality
    def __call__(self, *args, **kwargs):
        print('London, Paris')
        self.func(*args, **kwargs)
        print('Ventspils, Liepāja')


@TravelAdds
def profile(name):
    print(f'{name} profile')


@TravelAdds
def stories(author, date):
    print(f'Stories by {author} on {date}')


profile('Bob')
stories('Anna', '2021-02-13')
