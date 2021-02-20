# functions: sunny, foggy, rain
def sunny():
    return 'sunny'


def foggy():
    return 'foggy'


def rain():
    return 'rain'


# check if the module is executed as script
if __name__ == '__main__':
    print('Logging: this module is executed as script, run all functions')

    print(sunny())
    print(foggy())
    print(rain())

else:
    print(f'Logging: this module ({__name__}) has been imported')
