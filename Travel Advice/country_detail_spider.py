import json
import scrapy

with open("C:\\Users\\Luisa Bez\Documents\\Python Scripts\\Travel Advice\\aopa\\aopa\\country_links.json") as f:
    countries = json.load(f)

countries_list = countries[0]["Country"]

class CountrySummarySpider(scrapy.Spider):
    name = "country_summary"

    def start_requests(self):
        urls = ["https://www.gov.uk" +
                country_url for country_url in countries_list]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        yield{"Country": response.xpath('//h1[@class="gem-c-title__text "]/text()').get(),
              "Current at": response.xpath('//dd[@class="gem-c-metadata__definition"]/text()').get(),
              "Updated": response.xpath('//dd[@class="gem-c-metadata__definition"]/text()').getall()[1],
              "Latest update": response.xpath('//dd[@class="gem-c-metadata__definition"]//p/text()').get(),
              "Summary": response.xpath('//div[@class="gem-c-govspeak govuk-govspeak direction-ltr"]').getall()}
