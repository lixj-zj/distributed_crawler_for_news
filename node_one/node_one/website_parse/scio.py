"""
 !/usr/bin/env python3.6
 -*- coding: utf-8 -*-
 --------------------------------
 Description :
 --------------------------------
 @Time    : 2019/6/23 11:50
 @File    : scio.py
 @Software: PyCharm
 --------------------------------
 @Author  : lixj
 @contact : lixj_zj@163.com
"""


from scrapy.selector import Selector
from node_one.items import ScioItem
import uuid
import logging


class Scio():
    def __init__(self):
        pass

    def scio_parse(self, response):
        """
        解析scio网站内容
        :param response: spider中parse解析函数入参
        :return: 提取数据后的item
        """
        sel = Selector(response)
        item = ScioItem()

        # TODO 随机数问题: random() -> uuid
        # 插入mongodb时避免 KeyError: 'xxx does not support field: _id'
        item['_id'] = str(uuid.uuid1())

        # real_url 经过跳转之后的url
        item['page_url'] = response.url
        item['title'] = sel.xpath('//*[@class="tc A_title"]/text()').extract()
        item['sub_title_str'] = sel.xpath('//*[@class="tc A_t1 f12 pr"]/div[1]/text()').extract()
        item['img'] = sel.xpath('//*[@id="content"]//img/@src').extract()
        item['video'] = sel.xpath('//*[@id="content"]//video/@src').extract()
        item['audio'] = sel.xpath('//*[@id="content"]//audio/@src').extract()
        item['content'] = sel.xpath('//*[@id="content"]').xpath('string(.)').extract()
        item['author'] = sel.xpath('//*[@class="tr A_t1 f12"]/text()').extract()

        logging.info(">>>> scio_parse result: {}".format(str(item)))
        return item
