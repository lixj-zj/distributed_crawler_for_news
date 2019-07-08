# -*- coding: utf-8 -*-

import scrapy
from main_node.items import ScioItem
from scrapy_redis.spiders import RedisSpider
from main_node.spiders.routing import Routing
import re
import logging
from main_node.website_parse.scio import Scio

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
        resp_url = response.url
        logging.info("url:... {}".format(resp_url))

        # TODO 当直接传递response时，发现会在控台输出大量的http链接，并且重复循环输出，原因？

        next_url = self.get_scio_next_url(url=resp_url)

        with open("main_node/spiders/main_urls.txt", "r", encoding="utf-8") as f:
            main_urls = f.read()

        if next_url:
            yield scrapy.Request(url=next_url, callback=self.parse, dont_filter = True) # dont_filter = True 不过滤相同域名的网址

        if resp_url not in main_urls:
            with open("main_node/spiders/main_urls.txt", "a", encoding="utf-8") as f:
                f.write(resp_url)
                f.write("\n")
            yield Routing().routing_method(resp_url)


    def get_scio_next_url(self, url):
        max_page_num = Scio().max_num_of_pages(url)
        part = r'_(.*).htm'
        res = re.findall(part, url)
        next_url = ""
        base_url = url.split(".")[0]
        base_suffix = url.split(".")[1]
        if res:  # 含有_
            if int(res[0]) < max_page_num:
                logging.info("res[0] 的值 {}".format(res[0]))
                next_url = base_url + "_" + str(int(res[0]) + 1) + "." + base_suffix
        else:  # 不含有_  http://www.scio.gov.cn/34473/34474/index_1.htm
            next_url = base_url + "_1" + "." + base_suffix
        return next_url















