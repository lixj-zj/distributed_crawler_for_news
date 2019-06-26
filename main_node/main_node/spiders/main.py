# -*- coding: utf-8 -*-
import scrapy
from main_node.spiders.routing import Routing


class MainSpider(scrapy.Spider):
    name = 'main'

    allowed_domains = ['main_node.io']
    start_urls = [
                    'http://www.scio.gov.cn/37234/index.htm',
                    # 'http://www.scio.gov.cn/37236/index.htm',
                    # 'http://www.scio.gov.cn/tt/xjp/index.htm',
                    # 'http://www.scio.gov.cn/34473/34474/index.htm'
                  ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        # yield 代替 return
        yield Routing().routing_method(response)
