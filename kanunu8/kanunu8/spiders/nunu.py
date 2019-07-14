# -*- coding: utf-8 -*-
import scrapy


class NunuSpider(scrapy.Spider):
    name = 'nunu'
    allowed_domains = ['kanunu8.io']
    start_urls = ['http://kanunu8.io/']

    def parse(self, response):
        pass
