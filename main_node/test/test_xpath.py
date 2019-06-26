"""
 !/usr/bin/env python3.6
 -*- coding: utf-8 -*-
 --------------------------------
 Description : 
 --------------------------------
 @Time    : 2019/6/27 0:15
 @File    : test_xpath.py
 @Software: PyCharm
 --------------------------------
 @Author  : lixj
 @contact : lixj_zj@163.com
"""
import requests
from user_agent import UserAgent
url = "http://www.scio.gov.cn/37234/index.htm"
req = requests.get(url=url, headers=UserAgent().get_headers())
req.encoding = req.apparent_encoding
print(req.text)

import re
from lxml import etree
struct = etree.HTML(req.text)
navi_last_page = struct.xpath('//*[@id="PagerOutline1_PageIndex"]/text()')
r = re.search(r"共\d*页", navi_last_page[0])
last_page = r.group()[1:-1]
print(last_page)