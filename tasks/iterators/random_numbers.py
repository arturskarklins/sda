import random


class RandomNumber:
    def __init__(self, number=1):
        self.number = number
        self.iterations = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations == self.number:
            raise StopIteration
        self.iterations += 1

        return str(random.random()).split('.')[1]


def sum_number(n: int) -> int:
    result = 0
    while n > 0:
        reminder = n % 10
        result += reminder
        n = n // 10
    return result


for rand_number in RandomNumber(5):
    print(f'Number\'s {rand_number} sum is {sum_number(int(rand_number))}')
