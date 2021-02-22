import dataclasses
import pickle


@dataclasses.dataclass
class Profiles:
    name: str
    age: int


profiles = [Profiles('bob', 45), Profiles('anna', 34)]

with open('data.pickle', 'wb') as f:
    pickle.dump(profiles, f)
