import scrapy
from ..items import paloaltoneItem

class CveSpider(scrapy.Spider):
    name = 'paloalto'
    start_urls = {
        'https://security.paloaltonetworks.com/CVE-2020-2033'
    }

    def parse(self, response):

            id = response.css("div.pad").css("a::text")[1].extract()
            desc = response.css("p::text")[0].extract()
            dd =  response.css("label::text")[1].extract()
            cvs3 = response.css("div.pad").css("a::text")[2].extract()
            solu = response.css("p::text")[6].extract()
            items = paloaltoneItem()

            items['id'] = id
            items['desc'] = desc
            items['dd'] = dd
            items['cvs3'] = cvs3
            items['solu'] = solu

            yield items


