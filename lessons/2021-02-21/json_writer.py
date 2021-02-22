import json

profiles = [{
        'bob': {
            'name': 'Bob',
            'age': 45,
            'rank': 3.4,
            'is_liked': True,
            'payed': None
        },
    },
    {
        'anna': {
            'name': 'Anna',
            'age': 23,
            'rank': 4.5,
            'is_liked': True,
            'payed': {
                'ads': None
            }
        }
    }
]


with open('profiles.json', 'w') as file:
    json.dump(profiles, file, indent=2)
