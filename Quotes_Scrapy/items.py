# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 需要保存名言和作者
    _id = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()

