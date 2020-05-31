import scrapy

class TravelAdviceSpider(scrapy.Spider):
    name = "travel_advice"

    def start_requests(self):
        url = 'https://www.gov.uk/foreign-travel-advice/'
        yield scrapy.Request(url=url, callback=self.parse)

    # Fetches urls
    def parse(self, response):
        yield {'Country': response.xpath('//li//a[@class = "govuk-link countries-list__link"]/@href').extract()}
