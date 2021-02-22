import dataclasses
import pickle


@dataclasses.dataclass
class Profiles:
    name: str
    age: int


with open('data.pickle', 'rb') as file:
    read_data = pickle.load(file)

    print(read_data)
