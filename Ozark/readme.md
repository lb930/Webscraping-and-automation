# Ozark Webscraping Project

This project scrapes IMDB, Wikipedia and Ozark Wikia to extract seasons, episodes, ratings, actors and their characters.

## Scripts

### Selenium

scrape_episodes_and_seasons.py stores data regarding episodes, seasons and ratings in a csv file. This was created for practice, but it is less efficient than scrapy.

### Spiders

This project contains three spiders:

    actors
    wiki
    imdb
    
'actors' scrapes the actors for each Ozark episode from https://ozark-netflix.fandom.com/.
'wiki' scrapes episode IDs, episode titles and directors from Wikipedia.
'imdb' scrapes episode titles, release dates and IMDB ratings from [IMDB API](https://imdb-api.com/title/tt5071412).

You can run them using the ```scrapy crawl``` command:

    $ scrapy crawl actors

#### Storing the data

Use the following command to save the extracted data as json:

    $ scrapy crawl actors -o ozark_actors.json
