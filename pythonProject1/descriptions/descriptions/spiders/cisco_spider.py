import scrapy
from ..items import CiscoItem


class CiscoSpider(scrapy.Spider):
    name = 'cisco'
    start_urls = {
        'https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sip-Cv28sQw2'
    }

    def parse(self, response):
        items = CiscoItem()

        items['id'] = response.css("div.CVEList").css("div::text")[1].extract()
        items['pub'] = response.css("div#ud-published").css("div.divLabelContent::text").extract()
        items['BugId'] = response.css("div#ud-ddts").css("a::text").extract()
        items['Score'] = response.css("div.ud-CVSSScore").css("div.divLabelContent").css("a::text").extract()
        items['Summary'] = response.css("div#summaryfield").css("p::text").extract()
        yield items
