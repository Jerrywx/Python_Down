# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Spider1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass

    name =  scrapy.Field()
    school = scrapy.Field()
    imgUrl = scrapy.Field()

