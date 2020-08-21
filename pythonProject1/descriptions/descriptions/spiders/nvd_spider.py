import scrapy
from ..items import DescriptionsItem

class CveSpider(scrapy.Spider):
    name = 'cveFromNvd'
    start_urls = {
        'https://nvd.nist.gov/vuln/search/results?results_type=overview&form_type=Basic&search_type=all&startIndex=0'
    }

    def parse(self, response):

            id = response.css("#row").css("table")[0].css("tbody").css("th")[0].css("a::text").extract()
            desc = response.css("#row").css("table")[0].css("td")[0].css("p::text").extract()
            pub =  response.css("#row").css("table")[0].css("td")[0].css("span::text").extract()
            cvs3 = response.css("#row").css("table")[0].css("td")[1].css("span#Cvss3NAText::text")[1].extract()

            items = DescriptionsItem()

            items['id'] = id
            items['desc'] = desc
            items['pub'] = pub
            items['cvs3'] = cvs3

            yield items


import scrapy
from ..items import DescriptionsItem

class CveSpider(scrapy.Spider):
    name = 'cveFromNvd'
    start_urls = {
        'https://nvd.nist.gov/vuln/search/results?results_type=overview&form_type=Basic&search_type=all&startIndex=0'
    }

    def parse(self, response):

            id = response.css("#row").css("table")[0].css("tbody").css("th")[0].css("a::text").extract()
            desc = response.css("#row").css("table")[0].css("td")[0].css("p::text").extract()
            pub =  response.css("#row").css("table")[0].css("td")[0].css("span::text").extract()
            cvs3 = response.css("#row").css("table")[0].css("td")[1].css("span#Cvss3NAText::text")[1].extract()

            items = DescriptionsItem()

            items['id'] = id
            items['desc'] = desc
            items['pub'] = pub
            items['cvs3'] = cvs3

            yield items


import scrapy
from ..items import DescriptionsItem

class CveSpider(scrapy.Spider):
    name = 'cveFromNvd'
    start_urls = {
        'https://nvd.nist.gov/vuln/search/results?results_type=overview&form_type=Basic&search_type=all&startIndex=0'
    }

    def parse(self, response):

            id = response.css("#row").css("table")[0].css("tbody").css("th")[0].css("a::text").extract()
            desc = response.css("#row").css("table")[0].css("td")[0].css("p::text").extract()
            pub =  response.css("#row").css("table")[0].css("td")[0].css("span::text").extract()
            cvs3 = response.css("#row").css("table")[0].css("td")[1].css("span#Cvss3NAText::text")[1].extract()

            items = DescriptionsItem()

            items['id'] = id
            items['desc'] = desc
            items['pub'] = pub
            items['cvs3'] = cvs3

            yield items


import scrapy
from ..items import DescriptionsItem

class CveSpider(scrapy.Spider):
    name = 'cveFromNvd'
    start_urls = {
        'https://nvd.nist.gov/vuln/search/results?results_type=overview&form_type=Basic&search_type=all&startIndex=0'
    }

    def parse(self, response):

            id = response.css("#row").css("table")[0].css("tbody").css("th")[0].css("a::text").extract()
            desc = response.css("#row").css("table")[0].css("td")[0].css("p::text").extract()
            pub =  response.css("#row").css("table")[0].css("td")[0].css("span::text").extract()
            cvs3 = response.css("#row").css("table")[0].css("td")[1].css("span#Cvss3NAText::text")[1].extract()

            items = DescriptionsItem()

            items['id'] = id
            items['desc'] = desc
            items['pub'] = pub
            items['cvs3'] = cvs3

            yield items


