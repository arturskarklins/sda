import requests

response = requests.get('https://cat-fact.herokuapp.com/facts')

for fact in response.json():
    print(fact)
