# Task

Create JSON fetching app, that fetches different themes (at least 5, pick yourself, anything) from `https://itunes.apple.com/search?term=` processes all fetched JSON files, extract `collectionId`, `collectionName` and `releaseDate`, store that to file as CSV, on your own disk. Data with those fields missing (as `None` should be avoided and skipped). File should have data of entries which have all 3 present.

Important! Test this application with using threads and multiprocess. Pick up one of the solution [None, threads, multiprocess] which gives result the fastest. Try to argument why.

# Result

File with content like:
```
1394174978,Fox Searchlight Pictures Director Spotlight Wes Anderson 4 Movies,2018-03-23T07:00:00Z
1446087382,All Dogs Go to Heaven Collection,1989-11-17T08:00:00Z
1185090812,"Dogs: The Untold Stories, Season 1",2017-01-01T08:00:00Z
1529181532,Cats and Dogs 3-Film Collection,2010-07-30T07:00:00Z
```

# Hints

- to fetch data install and import `requests` module, and use `response = requests.get(f'https://itunes.apple.com/search?term={theme}'.json()`) to fetch JSON file for specific theme.
- all data fetching (like theme) can be "wrapped" as thread or "multiprocess"
- while accessing None data in JSON, might want to think about using try/except

# Solution 

With threads provided as .py file attached. Not saying that it's the best way, just as sample, if you're having challenges.