"""
 !/usr/bin/env python3.6
 -*- coding: utf-8 -*-
 --------------------------------
 Description :
 --------------------------------
 @Time    : 2019/7/13 16:49
 @File    : test_main_page.py
 @Software: PyCharm
 --------------------------------
 @Author  : lixj
 @contact : lixj_zj@163.com
"""

import requests
from lxml import etree
from com_config.user_agent import UserAgent

# url = "https://www.kanunu8.com/"
# req=requests.get(url, headers=UserAgent().get_headers(), timeout=10)
# req.encoding=req.apparent_encoding
# with open("main_page.txt", "w", encoding="utf-8") as f:
#     f.write(req.text)

with open("main_page.txt", "r", encoding="utf-8") as f:
    html = f.read()
structure = etree.HTML(html)
all_url = structure.xpath("//a/@href")
print(all_url)
print(len(all_url))
