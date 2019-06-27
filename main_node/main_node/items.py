# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MainNodeItem(scrapy.Item):
    pass


class ScioItem(scrapy.Item):
    """
    解析scio的item
    """
    all_real_urls = scrapy.Field()




class WechatItem(scrapy.Item):
    """
    解析微信的item
    """
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

