# -*- coding: utf-8 -*-

import scrapy
from node_one.spiders.routing import Routing

class OneSpider(scrapy.Spider):
    name = 'one'
    allowed_domains = ['node_one.io']
    start_urls = [
                    'http://www.scio.gov.cn/xwbjs/zygy/33093/hd33096/Document/1656021/1656021.htm',
                    'http://www.scio.gov.cn/37234/Document/1656126/1656126.htm',
                    'http://www.scio.gov.cn/xwbjs/zygy/32310/hd32313/Document/1656303/1656303.htm'
                  ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        # yield 代替 return
        yield Routing().routing_method(response)
