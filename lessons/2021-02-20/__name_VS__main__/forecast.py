import sys
import weather


def main():
    print(f'Today is {weather.foggy()} and {weather.rain()}')


if __name__ == '__main__':
    main()
else:
    print('Error: this module can be executed only as script / stand-alone component')
    sys.exit(1)
