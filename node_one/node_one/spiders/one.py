# -*- coding: utf-8 -*-

import scrapy
from scrapy_redis.spiders import RedisSpider
from node_one.spiders.routing import Routing


class OneSpider(RedisSpider):
    name = 'one'
    # allowed_domains = ['node_one.io']



    def parse(self, response):
        # yield 代替 return
        yield Routing().routing_method(response)
