import scrapy
from ..items import mozillaItem

class CveSpider(scrapy.Spider):
    name = 'mozilla'
    start_urls = {
        'https://www.mozilla.org/en-US/security/advisories/mfsa2020-22/'
    }

    def parse(self, response):

            id = response.css("section.cve").css("h4").css("a::text").extract()
            desc = response.css("section.cve").css("p::text").extract()
            dd = response.css("dd::text")[0].extract()
            cvs3 = response.css("dd").css("span::text").extract()
            fix = response.css("dd").css("ul").css("li::text").extract()
            product = response.css("dd::text")[1].extract()
            items = mozillaItem()

            items['id'] = id
            items['desc'] = desc
            items['dd'] = dd
            items['cvs3'] = cvs3
            items['fix'] = fix
            items['product'] = product

            yield items
