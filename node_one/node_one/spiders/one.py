# -*- coding: utf-8 -*-

import scrapy
from scrapy_redis.spiders import RedisSpider
from node_one.spiders.routing import Routing


class OneSpider(RedisSpider):
    name = 'one'
    allowed_domains = ['node_one.io']
    # start_urls = [
    #                 'http://www.scio.gov.cn/37236/37377/Document/1650050/1650050.htm',
    #                 'http://www.scio.gov.cn/xwbjs/zygy/33093/hd33096/Document/1656021/1656021.htm',
    #                 'http://www.scio.gov.cn/37234/Document/1656126/1656126.htm',
    #                 'http://www.scio.gov.cn/xwbjs/zygy/32310/hd32313/Document/1656303/1656303.htm'
    #               ]

    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    # redis_key = 'main:start_urls'

    # def start_requests(self):
    #     return self.next_requests()

    def parse(self, response):
        # yield 代替 return
        yield Routing().routing_method(response)
