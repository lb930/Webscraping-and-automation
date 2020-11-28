# Ozark Webscraping Project

This project scrapes IMDB, Wikipedia and Ozark Wikia to extract seasons, episodes, ratings, actors and their characters.

## Scripts

### Selenium

scrape_episodes_and_seasons.py stores data regarding episodes, seasons and ratings in a csv file.

### Spiders

This project contains two spiders:

    actors
    wiki
    
'actors' scrapes the actors for each Ozark episode from https://ozark-netflix.fandom.com/.
'wiki' scrapes episode IDs, episode titles and directors from Wikipedia.

You can run them using the ```scrapy crawl``` command:

    $ scrapy crawl actors

#### Storing the data

Use the following command to save the extracted data as json:

    $ scrapy crawl actors -o ozark_actors.json
