# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from main_node.items import MainNodeItem
import random
from main_node.news import get_one_page
import logging

class MainSpider(scrapy.Spider):
    name = 'main'
    allowed_domains = ['main_node.io']
    start_urls = ['http://www.scio.gov.cn/37234/Document/1650333/1650333.htm']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        sel = Selector(response)
        item = MainNodeItem()

        # TODO 随机数问题
        # 插入mongodb时避免 KeyError: 'xxx does not support field: _id'
        item['_id'] = str(random.randint(1, 10000000))

        # TODO
        # item['page_url']  old_url 列表中爬取的url

        # real_url 经过跳转之后的url
        item['page_url'] = response.url
        item['title'] = sel.xpath('//*[@class="tc A_title"]/text()').extract()
        item['sub_title_str'] = sel.xpath('//*[@class="tc A_t1 f12 pr"]/div[1]/text()').extract()
        item['img'] = sel.xpath('//*[@id="content"]//img/@src').extract()
        item['video'] = sel.xpath('//*[@id="content"]//video/@src').extract()
        item['audio'] = sel.xpath('//*[@id="content"]//audio/@src').extract()
        item['content'] = sel.xpath('//*[@id="content"]').xpath('string(.)').extract()
        item['author'] = sel.xpath('//*[@class="tr A_t1 f12"]/text()').extract()

        # yield 代替 return
        yield item


