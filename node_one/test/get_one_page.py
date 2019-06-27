"""
 !/usr/bin/env python3.6
 -*- coding: utf-8 -*-
 --------------------------------
 Description :
 --------------------------------
 @Time    : 2019/6/17 13:43
 @File    : get_one_page.py
 @Software: PyCharm
 --------------------------------
 @Author  : lixj
 @contact : lixj_zj@163.com
"""

import requests
from lxml import etree
import re
import logging
import time


# 获取总页数
def max_num_of_pages(first_page_url):
    try:
        req = requests.get(first_page_url)
        req.encoding = req.apparent_encoding
        struct = etree.HTML(req.text)
        navi_last_page = struct.xpath('//*[@id="PagerOutline1_PageIndex"]/text()')
        r = re.search(r"共\d*页", navi_last_page[0])
        last_page = r.group()[1:-1]
        return last_page
    except Exception as e:
        logging.error("获取总页数错误！url：{}，错误信息：{}".format(first_page_url, str(e)))


def get_url_pages(first_page_url, max_page_num):
    # "http://www.scio.gov.cn/37234/index_3.htm"
    # 记录所有父页面的地址 index_2.htm
    try:
        father_url = []
        father_url.append(first_page_url)
        base_url = first_page_url.rsplit("/", maxsplit=1)
        for page in range(1, int(max_page_num)):
            father_url.append(base_url[0] + "/index_" + str(page) + ".htm")
        return father_url
    except Exception as e:
        logging.error("获取url列表页错误！错误信息：{}".format(str(e)))


def get_html_from_url(url):
    req = requests.get(url, timeout=10)
    try:
        if req.status_code == 200:
            req.encoding = req.apparent_encoding
            return req.text
        else:
            logging.error("request url 请求状态异常！异常url：{}，异常链接状态：{}".format(url, req.status_code))
    except Exception as e:
        logging.error("request url 请求异常！异常信息:{}".format(str(e)))


def get_all_news_urls(father_url):
    try:
        # 记录所有目标新闻页面的url
        all_page_result = set()
        for one_page_url in father_url[:2]:
            html = get_html_from_url(one_page_url)
            struct = etree.HTML(html)
            # 查找指定标签下的所有的a标签的href属性
            page_contains_url = struct.xpath('//*[@id="PagerOutline1"]//a/@href')
            for url in page_contains_url:
                if "Document" in url:
                    all_page_result.add(one_page_url.rsplit("/",maxsplit=1)[0] + "/" + url)
            logging.info("{}记录完成！".format(str(one_page_url)))
            time.sleep(3)
        return all_page_result
    except Exception as e:
        logging.error("获取目标新闻页面url错误！错误信息：{}".format(str(e)))

def run():
    first_page_url = "http://www.scio.gov.cn/37234/index.htm"
    max_page_num = max_num_of_pages(first_page_url)
    father_url = get_url_pages(first_page_url, max_page_num)
    all_page_result = get_all_news_urls(father_url)
    print(all_page_result[:5])
    return list(all_page_result[:5])

if __name__ == '__main__':
    run()
