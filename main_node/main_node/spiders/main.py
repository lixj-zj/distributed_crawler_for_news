# -*- coding: utf-8 -*-

from scrapy_redis.spiders import RedisSpider
from main_node.spiders.routing import Routing


class MainSpider(RedisSpider):
    name = 'main'

    allowed_domains = ['main_node.io']
    # start_urls = [
    #                 'http://www.scio.gov.cn/37234/index.htm',
    #                 # 'http://www.scio.gov.cn/37236/index.htm',
    #                 # 'http://www.scio.gov.cn/tt/xjp/index.htm',
    #                 # 'http://www.scio.gov.cn/34473/34474/index.htm'
    #               ]
    redis_key = 'main:start_urls'

    # def start_requests(self):
    #     yield Routing().routing_method(self.start_urls)
        # for url in self.start_urls:
        #     yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        # TODO 当直接传递response时，发现会在控台输出大量的http链接，并且重复循环输出，原因？
        yield Routing().routing_method(response.url)
