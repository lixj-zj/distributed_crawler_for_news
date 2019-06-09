# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from main_node.items import MainNodeItem

class MainSpider(scrapy.Spider):
    name = 'main'
    allowed_domains = ['main_node.io']
    start_urls = ['https://movie.douban.com/subject/1292052/']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        sel = Selector(response)
        item = MainNodeItem()
        item['name'] = sel.xpath('//*[@id="content"]/h1/span[1]/text()').extract()

        return item

        # pass
