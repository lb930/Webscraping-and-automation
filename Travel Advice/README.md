# Travel Advice Webscraping Project

This project scrapes the UK foreign travel advice website (https://www.gov.uk/foreign-travel-advice).

I started by scraping the URLs for each country and used those to scrape the summary website. This is all done with the 'follow_links.py' spider. I cleaned the data and exported it to a Word document, which displayed the data in the best way.

## Spiders

This project contains one spider:

    $ scrapy list
    country_follow

You can run it using the ```scrapy crawl``` command:

    $ scrapy crawl country_follow

## Storing the data

Use the following command to save the extracted data as json:

    $ scrapy crawl country_follow -o country_summary.json

## Extracted Data
The website uses new lines and a varying number of paragraphs and lists which is returned as raw data:

    {
        "Country": "\n    Afghanistan\n  ", 
        "Current at": "\n              30 May 2020\n\n          ", 
        "Updated": "\n              28 May 2020\n\n          ", 
        "Latest update": "Addition of information on Qatar Airways flights from Kabul on Saturday 30 May and 6, 13, 20 and 27 June 2020 ('Summary' and 'Return to the UK' pages)", 
        "Summary": ["<div class=\"gem-c-govspeak govuk-govspeak direction-ltr\" data-module=\"govspeak\">\n      \n<div class=\"call-to-action\">\n<p><strong>Coronavirus: stay up to date</strong></p>\n\n<ul>\n  <li>\n    <p>Find out how to <a href=\"/foreign-travel-advice/afghanistan/return-to-the-uk\">return to the UK from Afghanistan</a></p>\n  </li>\n  <li>\n]
    }

**Clean country_summary json file.ipynb** handles the cleaning of the data and outputs it to Travel_advice2.docx.
Find and replace <br> with ^l adds new lines.

![image](https://user-images.githubusercontent.com/59416844/83358499-e5c5e000-a36b-11ea-9d4f-53c5978cef2c.png)

