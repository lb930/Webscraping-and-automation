import scrapy
import re
import json

class EccoSpider(scrapy.Spider):
    
    name = "ecco4"

    def __init__(self, filename=None):
        
        # Opens the json file containing  all URLs and parses them into a list
        # Run with scrapy crawl myspider -a filename=ecco_all_urls.json -o ecco4_lang.json to read in file and export json
        if filename:
            with open('C:\\Users\\Luisa Bez\\Documents\\Python Scripts\\ecco_verde\\ecco_verde\\ecco2_lang.json') as json_file:
                data = json.load(json_file)

            start_urls = []
            self.start_urls = [item for i in data for item in i["all URLs"]]


    # Scrapes product, review title, review and rating
    def parse(self, response):
    
                  
        product_long = response.xpath('//h1[@class="review-detail-title"]/text()').getall()
        language = []
        for p in product_long:
            if "German" in p:
                language.append("de")
            elif "English" in p:
                language.append("en")
            elif "Spanish" in p:
                language.append("es")
            elif "Italian" in p:
                language.append("it")
            elif "French" in p:
                language.append("fr")
            else:
                language.append("invalid")
            
            
            product = re.sub(r"reviews written for Acorelle", "", p)
            product = re.sub(r"review written for Acorelle", "", product)
            product = re.sub(r"\d", "", product)
            product = product.strip()
            product = re.sub(r"^([\w]+)", "", product)
            product = product.strip()
        print(product)
        
        title = response.xpath('//div[@class="comment-box"]//h3/text()').getall()
        
        
        # The reviews contain empty values due to line breaks which have to be removed
        review = response.xpath('//p[@class="comment"]/text()').getall()
        try:
            review = [x for x in review if x != " "]
        except:
            review
        
        # Some reviews contain line breaks which are split into separate list items although they are part of the same review. The code below fixes that.
        parsedReviews = []

        for s in review:
            # Condition not
            if s.startswith("\r\n"):
                # if True concat 's' with the last String in the List
                parsedReviews[-1] += " " + s
            else:
                # Append 's' as a new String to the List
                parsedReviews.append(s)

        rating = response.xpath('//p//span[@class="visuallyhidden"]/text()').getall()
        
        # Extract the rating from the string which says "The rating is 5 out of 5 stars"
        rating_list = []
        for r in rating:
            rating_num = re.findall(("\d"), r)[0]
            rating_list.append(int(rating_num))
            
        yield{"Product": product, "Title": title, "Review": parsedReviews, "Rating": rating_list, "Language": language}