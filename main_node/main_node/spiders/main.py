# -*- coding: utf-8 -*-

import scrapy
from main_node.items import ScioItem
from scrapy_redis.spiders import RedisSpider
from main_node.spiders.routing import Routing
import re
import logging

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


    def parse(self, response):
        logging.info("开始parse......")
        logging.info("url:... {}".format(response.url))

        # TODO 当直接传递response时，发现会在控台输出大量的http链接，并且重复循环输出，原因？

        url = response.url
        part = r'_(.*).htm'
        res = re.findall(part, url)
        next_url = ""
        if res:  # 含有_
            if int(res[0]) < 50:
                logging.info("res[0] 的值 {}".format(res[0]))
                next_url = "http://www.scio.gov.cn/34473/34474/index_" + str(int(res[0]) + 1) + ".htm"
        else:  # 不含有_  http://www.scio.gov.cn/34473/34474/index_2.htm
            next_url = "http://www.scio.gov.cn/34473/34474/index_1.htm"

        with open("main_node/spiders/main_urls.txt", "r", encoding="utf-8") as f:
            main_urls = f.read()

        if next_url:
            yield scrapy.Request(url=next_url, callback=self.parse, dont_filter = True) # dont_filter = True 不过滤相同域名的网址

        if response.url not in main_urls:
            with open("main_node/spiders/main_urls.txt", "a", encoding="utf-8") as f:
                f.write(response.url)
                f.write("\n")
            yield Routing().routing_method(response.url)


















