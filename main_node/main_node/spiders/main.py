# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from main_node.items import MainNodeItem


class MainSpider(scrapy.Spider):
    name = 'main'
    allowed_domains = ['main_node.io']
    start_urls = ['http://www.scio.gov.cn/xwbjs/zygy/38848/38852/Document/1653987/1653987.htm']

    def pre_process(self):
        # http://www.scio.gov.cn/37234/index.htm
        pass

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        sel = Selector(response)
        item = MainNodeItem()
        item['title'] = sel.xpath('//*[@class="tc A_title"]/text()').extract()
        item['time'] = sel.xpath('//*[@class="tc A_t1 f12 pr"]/div[1]/text()').extract()
        item['title'] = sel.xpath('//*[@class="tc A_title"]/text()').extract()
        item['source_name'] = sel.xpath('//*[@class="tc A_title"]/text()').extract()
        item['content'] = sel.xpath('//*[@class="tc A_title"]/text()').extract()
        item['editor'] = sel.xpath('//*[@class="tc A_title"]/text()').extract()
        return item


