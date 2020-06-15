import scrapy
import re

class EccoSpider(scrapy.Spider):
    name = "ecco2"
    
    # Gets all products from Acorelle
    start_urls = ["https://www.ecco-verde.co.uk/acorelle?page=1"]


    # 1st: gets max pages for all products and fetches all product urls
    def parse(self, response):

        # Identifies the number of product pages
        max_product_pages = response.xpath('//ul[@class="pagination"]//li//button/text()').getall()[-1]
        # returns "3" as expected

        # Fetches all overview pages
        all_product_pages = ["https://www.ecco-verde.co.uk/acorelle?page=" + str(page) for page in range(1, int(max_product_pages)+1)]
        yield from response.follow_all(all_product_pages, self.parse_prod)


    # 2nd: Gets the review URL for each product 
    def parse_prod(self, response): 

        # Gets the URL for each product
        product_urls = response.xpath('//a[@class="product__imagewrap"]/@href').extract() # eg: "/acorelle/organic-eau-de-parfum-lenvoutante"
        
        product_urls = ["https://www.ecco-verde.co.uk/reviews" + p + "?rating_page=1&lang=all" for p in product_urls]

        yield from response.follow_all(product_urls, self.parse_reviews)
    
    # 3rd: Checks review pagination    
    def parse_reviews(self, response):
        
        # Identifies the number of review pages
        try:
            max_review_pages = response.xpath('//ul[@class="pagination"]//li//button/text()').getall()[-1]

        # Not all products have more than 10 reviews and therefore don't need pagination
        except:
            max_review_pages = 1

        pre = response.xpath('//meta[@property="og:url"]/@content').get() #"https://www.ecco-verde.co.uk/reviews/acorelle/eau-fraiche-silky-rose"

        url_post_list = []
        
        for lang in ["de", "en", "fr", "es", "it"]:
            for num in range(1, int(max_review_pages)+1):
                url_post = pre + "?rating_page=" + str(num) + "&lang=" + lang
                url_post_list.append(url_post)
        
        # Returns all review URLs for each product
        yield{"all URLs": url_post_list}