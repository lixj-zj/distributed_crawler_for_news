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

res = requests.get('http://www.scio.gov.cn/xwbjs/zygy/38848/38852/Document/1653987/1653987.htm')
res.encoding=res.apparent_encoding
struct = etree.HTML(res.text)
title = struct.xpath('//*[@class="tc A_title"]/text()')[0]

sub_title_str = struct.xpath('//*[@class="tc A_t1 f12 pr"]/div[1]/text()')[0]
sub_title = sub_title_str.strip().replace(u'\u3000', u' ')

result = sub_title.split("   ")
sub_title_info = result[0]
publish_time = result[1]
resource = result[2].split("：")[1]
content = struct.xpath('//*[@id="content"]')[0].xpath('string(.)').strip()
author = struct.xpath('//*[@class="tr A_t1 f12"]/text()')[0]

print()
