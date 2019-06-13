# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from main_node.items import MainNodeItem
import random

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

        # 插入mongodb时避免 KeyError: 'xxx does not support field: _id'
        item['_id'] = str(random.randint(1, 1000000))
        item['title'] = sel.xpath('//*[@class="tc A_title"]/text()')[0].extract()
        sub_title_str = sel.xpath('//*[@class="tc A_t1 f12 pr"]/div[1]/text()')[0].extract()
        sub_title = sub_title_str.strip().replace(u'\u3000', u' ')
        result = sub_title.split("   ")
        item['sub_title_info'] = result[0]
        item['publish_time'] = result[1]
        item['resource'] = result[2].split("：")[1]
        item['content'] = sel.xpath('//*[@id="content"]')[0].xpath('string(.)').extract()
        item['author'] = sel.xpath('//*[@class="tr A_t1 f12"]/text()')[0].extract()

        # yield 代替 return
        yield item


