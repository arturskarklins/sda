import dataclasses
import random
import time
import typing


@dataclasses.dataclass
class CarRace:
    model: str = dataclasses.field(default='balloon')
    track: typing.ClassVar[int] = 50
    kms: typing.ClassVar[int] = 0

    def driving(self, number: int) -> int:
        if number % 2 == 0:
            self.kms += 5
        elif number % 3 == 0:
            self.kms += 3
        elif number % 5 == 0:
            self.kms += 1

        return self.kms

    def finnish(self) -> bool:
        return True if self.kms >= self.track else False


def random_int() -> int:
    return int(str(random.random()).split('.')[1])


participants = [
    CarRace('BMV'),
    CarRace('Audi'),
    CarRace('Volga'),
    CarRace('Mazda')
]

driver_won = False
while True:
    for participant in participants:
        participant.driving(random_int())

        if participant.finnish():
            print(f'*** Driver {participant.model} won the race! ***')
            driver_won = True
            break
    else:
        for participant in participants:
            print(f'{participant.model} => {participant.kms} km | ', end='')
        print()

    if driver_won:
        break
    time.sleep(1)
