import json

with open('profiles.json') as file:
    json_content = json.load(file)

    for person in json_content:
        print(person)
