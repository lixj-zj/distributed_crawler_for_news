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
from main_node.items import ScioItem

import os
import logging
from lxml import etree
import time
import re
from main_node.spiders.new_requests import NewRequests as new_requests


class Scio():
    def __init__(self):
        pass

    # 获取总页数
    def max_num_of_pages(self, html):
        try:
            # TODO 优化获取html与struct的过程
            struct = etree.HTML(html)
            navi_last_page = struct.xpath('//*[@id="PagerOutline1_PageIndex"]/text()')
            r = re.search(r"共\d*页", navi_last_page[0])
            last_page = r.group()[1:-1]
            return last_page
        except Exception as e:
            logging.error("获取总页数错误！url：{}，错误信息：{}".format(html, e))

    def list_url_pages(self, first_page_url, max_page_num):
        # "http://www.scio.gov.cn/37234/index_3.htm"
        # 记录所有父页面的地址 index_2.htm
        try:
            father_url = []
            father_url.append(first_page_url)
            no_filename_url = first_page_url.rsplit("/", maxsplit=1)
            for page in range(1, int(max_page_num)):
                father_url.append(no_filename_url[0] + "/index_" + str(page) + ".htm")
            return father_url
        except Exception as e:
            logging.error("获取url列表页错误！错误信息：{}".format(e))

    def all_news_urls(self, page_url):
        """
        由父链接获取其主要部分的所有链接
        :param father_url: 父链接
        :param max_num:
        :return:
        """
        try:
            # 记录所有目标新闻页面的url
            all_page_result = set()
            # for one_page_url in father_url[:max_num]:
            html = new_requests().get_html_from_url(page_url)
            pre_url = page_url.rsplit("/", maxsplit=1)[0]
            struct = etree.HTML(html)
            # 查找指定标签下的所有的a标签的href属性
            page_contains_url = struct.xpath('//*[@id="PagerOutline1"]//a/@href')
            for url in page_contains_url:
                if "Document" in url:
                    all_page_result.add(pre_url + os.altsep + url)
            time.sleep(1)
            return list(all_page_result)

        except Exception as e:
            logging.error("获取目标新闻页面url错误！错误信息：{}".format(e))


    def real_urls(self, base_url, url_list):
        """
        获取网页真实链接
        :param base_url:
        :param url_list:
        :param max:
        :return:
        """
        # TODO 列表筛选值优化
        result = []
        for url in url_list:
            html = new_requests().get_html_from_url(url)
            # 重定向地址匹配的re pattern
            pattern = r'window.location.replace\(\"../../../(.*)\"\);'
            match_location = re.findall(pattern, html)
            # 存在页面重定向的地址，则添加拼接后的新的地址，否则直接添加该地址
            if len(match_location) is not 0:
                result.append(base_url + os.altsep + match_location[0])
            else:
                result.append(url)
        return result


    def scio_parse(self, url):
        """
        解析scio网站内容
        :param response: spider中parse解析函数入参
        :return: 提取数据后的item
        """
        base_url = 'www.scio.gov.cn'
        item = ScioItem()

        # html = new_requests().get_html_from_url(start_url)
        # max_pages_num = self.max_num_of_pages(html)
        # father_url = self.list_url_pages(url, 3)
        all_page_result = self.all_news_urls(url)
        result_urls = self.real_urls(base_url, all_page_result)

        item['all_real_urls'] = result_urls

        return item
