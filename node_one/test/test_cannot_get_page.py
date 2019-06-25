"""
 !/usr/bin/env python3.6
 -*- coding: utf-8 -*-
 --------------------------------
 Description : 
 --------------------------------
 @Time    : 2019/6/25 15:21
 @File    : test_cannot_get_page.py
 @Software: PyCharm
 --------------------------------
 @Author  : lixj
 @contact : lixj_zj@163.com
"""
import requests
url = 'http://www.scio.gov.cn/37234/Document/1656126/1656126.htm'
req = requests.get(url)
req.encoding=req.apparent_encoding
print(req.url)
print(req.content)
print(req.text)
