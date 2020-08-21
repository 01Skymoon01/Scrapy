import scrapy
from ..items import DescriptionsItem

class CveSpider(scrapy.Spider):
    name = 'cve'
    start_urls = {
        'https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-1300'
    }

    def parse(self, response):

            div_table_cve = response.css("#GeneratedTable").css("table")[0]


            desc = div_table_cve.css("td")[3].re(r'<td colspan="2" class="note">\n\t\t\t<b>Note:</b> <a href="/data/refs/index.html">References</a>\s*(.*)')

            items = DescriptionsItem()

            items['desc'] = desc
            yield items


