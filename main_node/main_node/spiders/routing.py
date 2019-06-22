"""
 !/usr/bin/env python3.6
 -*- coding: utf-8 -*-
 --------------------------------
 Description : 路由类，跳转对应解析方法
 --------------------------------
 @Time    : 2019/6/22 18:59
 @File    : routing.py
 @Software: PyCharm
 --------------------------------
 @Author  : lixj
 @contact : lixj_zj@163.com
"""

from scrapy.selector import Selector
from main_node.items import MainNodeItem
import random
import uuid
import re
import logging


class Routing():
    def __init__(self):
        # 记录跳转路由方法
        self.routing_dict = \
            {
                # scio
                'www.scio.gov.cn/37234/Document/1650333': 'scio_parse',

                # 华尔街见闻
                'awtmt.com/articles': 'getDetailInfoFromAwtmt',
                'wallstreetcn.com/articles': 'getDetailInfoFromWallstreet',
                'api.wallstreetcn.com/redirect': 'getDetailInfoFromApi'
            }

    def routing_method(self, response):
        """
        根据url路由对应的方法
        :param url: 解析的url
        :return: 对应解析函数函数返回的数据内容
        """
        try:
            url = response.url
            logging.info("路由 routing_method url: {}".format(url))
            # 分析 url 是否是外部链接（微信文章），选择不同的正则匹配
            pattern = r'//(.*)/' if url.find('?') == -1 else r'//(.*)/?'
            web_site = re.findall(pattern, url[:url.find('?')])[0]

            # TODO 正则匹配修改
            if web_site in self.routing_dict.keys():
                # globals()[func]() 以字典的方式访问局部（locals()[func]()）和全局变量
                # detail_info = locals()[self.routing_dict.get(web_site)](response)
                detail_info = self.scio_parse(response)
                logging.info("detail_info :{}".format(detail_info))
                return detail_info
            else:
                # 不阻断后续url分析，记录无法解析的url
                logging.info("url: {} ，暂无解析方法！".format(url))
                # TODO 分离写文件。接口参数：文件路径、写入内容
                with open("../problems/url_problem.txt","w+",encoding="utf-8") as f:
                    f.write(logging.info("url: {} ，暂无解析方法！".format(url)))
        except Exception as e:
            logging.error("routing_method 解析异常！异常信息：{}".format(str(e)))


    def scio_parse(self, response):
        sel = Selector(response)
        item = MainNodeItem()

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

        logging.info("scio_parse result: {}".format(str(item)))
        return item


if __name__ == '__main__':
    pass