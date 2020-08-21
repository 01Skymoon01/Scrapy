import scrapy
from ..items import DescriptionsItem


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = {
        'https://exchange.xforce.ibmcloud.com/vulnerabilities/184190'
    }

    def parse(self, response):
        # title = response.css('title').extract()
        # yield {'titleText': title}

        items = DescriptionsItem()
        all_div_quotes = response.css("div.instantresults")

        for quotes in all_div_quotes:
            title = quotes.css(".description::text").extract()

            yield {
                'title': title
            }


