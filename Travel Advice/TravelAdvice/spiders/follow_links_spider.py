import scrapy

class CountryFollowSpider(scrapy.Spider):
    name = "country_follow"

    start_urls = ["https://www.gov.uk/foreign-travel-advice/"]

    def parse(self, response):
        country_links = response.xpath('//li//a[@class = "govuk-link countries-list__link"]/@href')
        yield from response.follow_all(country_links, self.parse_country)

    def parse_country(self, response):
        yield{"Country": response.xpath('//h1[@class="gem-c-title__text "]/text()').get(),
              "Current at": response.xpath('//dd[@class="gem-c-metadata__definition"]/text()').get(),
              "Updated": response.xpath('//dd[@class="gem-c-metadata__definition"]/text()').getall()[1],
              "Latest update": response.xpath('//dd[@class="gem-c-metadata__definition"]//p/text()').get(),
              "Summary": response.xpath('//div[@class="gem-c-govspeak govuk-govspeak direction-ltr"]').getall()}