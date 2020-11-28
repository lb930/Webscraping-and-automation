import scrapy
import unidecode

class OzarkWikipedia(scrapy.Spider):
    name = 'wiki'
    start_urls = ['https://en.wikipedia.org/wiki/Ozark_(TV_series)#Episodes']

    def parse(self, response):
        wiki_dict = {}
        seasons = response.xpath('//span[@class="mw-headline"]/text()').getall()[7:11]
        season_tables = response.xpath('//tr').getall()
        for s in season_tables:
            title = response.xpath('//td[@class="summary"]/text()').getall()
            title = [unidecode.unidecode(t) for t in title]
            title = [t.replace('"', '') for t in title]
            director = response.xpath('//td[@style="text-align:center"]//text()').getall()
            overall_id = response.xpath('//th[@scope="row"][@id]/text()').getall()
            wiki_dict["overall_id"] = overall_id
            wiki_dict["title"] = title
            wiki_dict["director"] = director

        # Clean data to only return directors from Wikiedia table (xpath is identical between for several columns)
        directors = ['Jason Bateman', 'Daniel Sackheim', 'Andrew Bernstein', 'Ellen Kuras', 'Phil Abraham', 'Alik Sakharov', 'Ben Semanoff', 'Amanda Marsalis', 'Cherien Dabis', 'TBA']
        wiki_dict['director'] = [i for i in wiki_dict['director'] if i in directors][:-2] # excludes duplicate 'TBA' directors. Needs to be fixed for season 4
        print(wiki_dict)
        yield{'wikipedia': wiki_dict}

