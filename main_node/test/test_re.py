"""
 !/usr/bin/env python3.6
 -*- coding: utf-8 -*-
 --------------------------------
 Description : 
 --------------------------------
 @Time    : 2019/7/2 19:42
 @File    : test_re.py
 @Software: PyCharm
 --------------------------------
 @Author  : lixj
 @contact : lixj_zj@163.com
"""

import re

url = "http://www.scio.gov.cn/37234/index_32.htm"
part = r'_(.*).htm'
res = re.findall(part, url)
next_url = ""
if res:  # 含有_
    if int(res[0]) < 33:
        next_url = "http://www.scio.gov.cn/37234/index_" + str(int(res[0]) + 1) + ".htm"
    else:
        pass
else:  # 不含有_
    next_url = "http://www.scio.gov.cn/37234/index_1.htm"

if next_url:
    print("yes")
