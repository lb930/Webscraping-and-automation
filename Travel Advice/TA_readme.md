# Travel Advice Webscraping Project

This project scrapes the UK foreign travel advice website (https://www.gov.uk/foreign-travel-advice).

I started by scraping the URLs for each country and used those to scrape the summary website. I cleaned the data and exported it to a Word document, which displayed the data in the best way.

## Content

- **travel_advice_spider.py** uses Scrapy to fetch URLs for 264 countries and stores them in a country_links.json
- **country_detail_spider.py** uses the URLs from country_links.json to scrape the summary page for each country and stores the output in country_summary.json
- **Clean country_summary json file.ipynb** cleans country_summary.json and outputs the data in tabular format to Travel_advice2.docx
