# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MainNodeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # _id：插入mongodb时避免 KeyError: 'xxx does not support field: _id'
    _id = scrapy.Field()

    title = scrapy.Field()
    sub_title_info = scrapy.Field()
    publish_time = scrapy.Field()
    resource = scrapy.Field()
    content = scrapy.Field()
    author = scrapy.Field()
