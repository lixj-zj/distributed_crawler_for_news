# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MainNodeItem(scrapy.Item):
    # _id：插入mongodb时避免 KeyError: 'xxx does not support field: _id'
    _id = scrapy.Field()

    page_url = scrapy.Field()
    sub_title_str = scrapy.Field()
    title = scrapy.Field()
    img = scrapy.Field()
    video = scrapy.Field()
    audio = scrapy.Field()
    content = scrapy.Field()
    author = scrapy.Field()
