# Ozark Webscraping Project

This project scrapes IMDB, Wikipedia and Ozark Wikia to extract seasons, episodes, ratings, actors and their characters.

## Spiders

This project contains one spider:

    $ scrapy list
    actors

You can run it using the ```scrapy crawl``` command:

    $ scrapy crawl actors

## Storing the data

Use the following command to save the extracted data as json:

    $ scrapy crawl actors -o ozark_actors.json
    
### Format

    [{"The Badger": {"Jason Bateman": "Martin Byrde", "Laura Linney": "Wendy Byrde", "Sofia Hublitz": "Charlotte Byrde", "Skylar Gaertner": "Jonah Byrde", "Julia Garner": "Ruth Langmore", "Jordana Spiro": "Rachel Garrison", "Jason Butler Harner": "Roy Petty", "Esai Morales": "Camino Del Rio", "Peter Mullan": "Jacob Snell", "Lisa Emery": "Darlene Snell", "Charlie Tahan": "Wyatt Langmore", "Janet McTeer": "Helen Pierce", "Tom Pelphrey": "Ben Davis", "Jessica Francis Dukes": "Maya Miller"}}]
