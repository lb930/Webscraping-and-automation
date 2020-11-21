# Ozark Webscraping Project

This project scrapes IMDB, Wikipedia and Ozark Wikia to extract seasons, episodes, ratings, actors and their characters.

## Scripts

### Selenium

scrape_episodes_and_seasons.py stores data regarding episodes, seasons and ratings in a csv file.

### Spiders

This project contains one spider:

    $ scrapy list
    actors

You can run it using the ```scrapy crawl``` command:

    $ scrapy crawl actors

#### Storing the data

Use the following command to save the extracted data as json:

    $ scrapy crawl actors -o ozark_actors.json
