# -*- coding: utf-8 -*-
import scrapy
from main_node.spiders.routing import Routing


class MainSpider(scrapy.Spider):
    name = 'main'

    # 减慢爬取速度 为1s
    download_delay = 1

    allowed_domains = ['main_node.io']
    start_urls = [
                    'http://www.scio.gov.cn/37234/Document/1650333/1650333.htm',
                    'http://www.scio.gov.cn/dfbd/dfbd/Document/1657048/1657048.htm',
                    'http://www.scio.gov.cn/33648/Document/1651254/1651254.htm'
                  ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # yield 代替 return
        yield Routing().routing_method(response)
