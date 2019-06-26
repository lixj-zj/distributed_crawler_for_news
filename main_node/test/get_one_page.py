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
        html = get_html_from_url(first_page_url)
        struct = etree.HTML(html)
        navi_last_page = struct.xpath('//*[@id="naviLastPage"]/text()')
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
    req = requests.get(url, timeout=5)
    try:
        if req.status_code == 200:
            req.encoding = req.apparent_encoding
            logging.info("requests url 请求完成！url:{}".format(url))
            return req.text
        else:
            logging.error("request url 请求状态异常！异常url：{}，异常链接状态：{}".format(url, req.status_code))
    except Exception as e:
        logging.error("request url 请求异常！异常信息:{}".format(str(e)))


def get_all_news_urls(father_url, max_num):
    try:
        # 记录所有目标新闻页面的url
        all_page_result = set()
        for one_page_url in father_url[:max_num]:
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

def get_real_urls(url_list):
    real_url = []
    base_url = "http://www.scio.gov.cn/"
    for url in url_list:
        html = get_html_from_url(url)
        # 重定向地址匹配的re pattern
        pattern = r'window.location.replace\(\"../../../(.*)\"\);'
        match_location = re.findall(pattern, html)
        # 存在页面重定向的地址，则添加拼接后的新的地址，否则直接添加该地址
        if len(match_location) is not 0:
            real_url.append(base_url + match_location[0])
        else:
            real_url.append(url)
    return real_url

def run():
    first_page_url = "http://www.scio.gov.cn/37234/index.htm"
    max_page_num = max_num_of_pages(first_page_url)
    father_url = get_url_pages(first_page_url, max_page_num)
    all_page_result = get_all_news_urls(father_url, max_num=2)
    all_page_real_url = get_real_urls(all_page_result)
    return list(all_page_real_url)[:5]

if __name__ == '__main__':
    # run()

    start_urls = ['http://www.scio.gov.cn/37234/Document/1656378/1656378.htm',
                  'http://www.scio.gov.cn/37234/Document/1656147/1656147.htm',
                  'http://www.scio.gov.cn/37234/Document/1656881/1656881.htm',
                  'http://www.scio.gov.cn/37234/Document/1652787/1652787.htm',
                  'http://www.scio.gov.cn/37234/Document/1654528/1654528.htm']
    print(get_real_urls(start_urls))
