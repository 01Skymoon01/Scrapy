# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DescriptionsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    desc = scrapy.Field()
    id = scrapy.Field()
    pub = scrapy.Field()
    cvs3 = scrapy.Field()
    pass

class paloaltoneItem(scrapy.Item):
    id = scrapy.Field()
    desc = scrapy.Field()
    dd = scrapy.Field()
    cvs3 = scrapy.Field()
    solu = scrapy.Field()
    pass

class mozillaItem(scrapy.Item):
    id = scrapy.Field()
    desc = scrapy.Field()
    dd = scrapy.Field()
    cvs3 = scrapy.Field()
    fix = scrapy.Field()
    product = scrapy.Field()

    pass
class CiscoItem(scrapy.Item):
    # define the fields for your item here like:

    id = scrapy.Field()
    pub = scrapy.Field()
    BugId = scrapy.Field()
    Score = scrapy.Field()
    Summary = scrapy.Field()
    pass