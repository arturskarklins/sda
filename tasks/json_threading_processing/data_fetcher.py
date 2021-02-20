import csv
import threading
import requests
import time

start = time.time()


def store_json(theme, writer):
    print(f'Starting .. {theme}')
    response = requests.get(f'https://itunes.apple.com/search?term={theme}').json()

    for i in response.get('results'):
        try:
            writer.writerow([i["collectionId"], i.get("collectionName"), i.get('releaseDate')])
        except KeyError:
            pass

    print(f'Fetched .. {theme}')


threads = []
with open('results.txt', 'w') as file:
    csv_writer = csv.writer(file)
    for item in ['pokemon', 'terminator', 'cats', 'dogs', 'latvia', 'riga', 'nba', 'nhl']:
        thread = threading.Thread(target=store_json, args=(item, csv_writer))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

print(f'Process took {time.time() - start} sec(s)')
