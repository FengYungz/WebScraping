from urllib import response
import scrap

class QuotesSpider(scrap.Spider):
    name='QuotesSpider'
    start_urls = ['http://localhost:3000/']

    def parse(self, response): 
        quote = response.xpath('*//div[@class="pega"]').get()
        print(quote)

