import unidecode
import scrapy
import re

class ActorsSpider(scrapy.Spider):

    name = 'actors'
    start_urls = ['https://ozark-netflix.fandom.com/wiki/Category:Episodes']

    def parse(self, response):
        episode_urls = response.xpath('//a[contains(@class, "category-page__member-link") and not (contains(@title, "Season"))]/@href')
        yield from response.follow_all(episode_urls, self.parse_episode)

    def parse_episode(self, response):
        episode_title = response.xpath('//h1[@id="firstHeading"]/text()').get()
        episode_title = unidecode.unidecode(episode_title)
        
        # Only download list items from cast table. This includes html tags
        if episode_title != 'Sugarwood' and episode_title != 'BFF': # Sugarwood and BFF have a different structure
            chars_and_actors2 = response.xpath('//div[@class="mw-parser-output"]//ul').getall()[1]
        elif episode_title == 'Sugarwood':
            chars_and_actors2 = response.xpath('//div[@class="mw-parser-output"]//ul').getall()[3]
        elif episode_title == 'BFF':
            chars_and_actors2 = response.xpath('//div[@class="mw-parser-output"]//ul').getall()[0]
        
        # Remove html tags
        chars_and_actors2_regex = ["".join(x) for x in re.findall('href="/wiki/(.*?)"|title="(.*?)"|<li>(.*?)<a|Harner</a>(.*?)</li>|</a>(.*?)<small>', chars_and_actors2)]
        
        # Remove empty strings
        chars_and_actors2_clean = list(filter(None, chars_and_actors2_regex))
        
        # Remove duplicate items and creates [actor, character] list
        even_cleaner = []
        for i in chars_and_actors2_clean:
            i = i.replace('_', ' ').replace(' as ', '').replace('</a>', '').replace('<a href=\"/wiki/Roy Petty\" title=\"Roy Petty\">', '').rstrip()
            if i not in even_cleaner:
                even_cleaner.append(i)
        
        # Bring actor-character relationship into dictionary format
        zipped = list(zip(even_cleaner[0::2], even_cleaner[1::2]))
        actor_char = dict(zipped)
        
        yield{episode_title: actor_char}