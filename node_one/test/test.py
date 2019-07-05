"""
 !/usr/bin/env python3.6
 -*- coding: utf-8 -*-
 --------------------------------
 Description :
 --------------------------------
 @Time    : 2019/6/11 22:36
 @File    : test.py
 @Software: PyCharm
 --------------------------------
 @Author  : lixj
 @contact : lixj_zj@163.com
"""

import requests
from lxml import etree
import re

from user_agent import UserAgent

# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Accept-Language': 'en',
# }

# url='http://www.scio.gov.cn/37236/37377/Document/1650050/1650050.htm'
# res = requests.get(url, headers=UserAgent().get_headers())
# res.encoding=res.apparent_encoding
# struct = etree.HTML(res.text)
# print(res.text)
#
# aa = struct.xpath('//*[@id="Affix1"]//a/@href')
# print(aa)


# title = struct.xpath('//*[@class="tc A_title"]/text()')[0]
#
# sub_title_str = struct.xpath('//*[@class="tc A_t1 f12 pr"]/div[1]/text()')[0]
# sub_title = sub_title_str.strip().replace(u'\u3000', u' ')
#
# result = sub_title.split("   ")
# sub_title_info = result[0]
# publish_time = result[1]
# resource = result[2].split("：")[1]
# content = struct.xpath('//*[@id="content"]')[0].xpath('string(.)').strip()
# author = struct.xpath('//*[@class="tr A_t1 f12"]/text()')[0]


page_contains_url = ['Document/1654022/1654022.htm']
for url in page_contains_url:
    if "Document" in url:
        all_page_result.add(url.rsplit("/", maxsplit=1)[0] + os.altsep + url)