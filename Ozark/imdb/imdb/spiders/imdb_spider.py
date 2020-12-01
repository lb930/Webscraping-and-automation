import scrapy

class Imdb(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://imdb-api.com/episodes/tt5071412/1', 'https://imdb-api.com/episodes/tt5071412/2', 'https://imdb-api.com/episodes/tt5071412/3']

    def parse(self, response):
        title = response.xpath('//span[@class="text-large1"]/text()').getall()
        release_date = response.xpath('//span[@class="text-lightf"]/text()').getall()[::2]
        synopsis = response.xpath('//span[@class="text-lightf"]/text()').getall()[1::2]
        rating = response.xpath('//td[@class="text-center"]//text()').getall()[1::2]
        
        yield{'title': title,
              'release_date': release_date,
              'synopsis': synopsis,
              'rating': rating}
