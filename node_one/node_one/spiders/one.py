# -*- coding: utf-8 -*-

import scrapy
from node_one.spiders.routing import Routing
import logging

class OneSpider(scrapy.Spider):
    name = 'one'
    allowed_domains = ['node_one.io']
    start_urls = ['http://www.scio.gov.cn/37234/Document/1650333/1650333.htm']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # yield 代替 return
        yield Routing().routing_method(response)
