"""
 !/usr/bin/env python3.6
 -*- coding: utf-8 -*-
 --------------------------------
 Description :
 --------------------------------
 @Time    : 2019/6/19 21:25
 @File    : data_pro_process.py
 @Software: PyCharm
 --------------------------------
 @Author  : lixj
 @contact : lixj_zj@163.com
"""
import re

url = "http://www.scio.gov.cn/37234/Document/1650333/1650333.htm"
# 分析 url 是否是外部链接（微信文章），选择不同的正则匹配
pattern = r'//(.*)/' if url.find('?') == -1 else r'//(.*)/?'
web_site = re.findall(pattern, url[:url.find('?')])[0]
print(web_site)


import uuid
print(str(uuid.uuid1()).__class__)
