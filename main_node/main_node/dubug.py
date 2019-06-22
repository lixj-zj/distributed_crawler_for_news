"""
 !/usr/bin/env python3.6
 -*- coding: utf-8 -*-
 --------------------------------
 Description :
 --------------------------------
 @Time    : 2019/6/18 21:49
 @File    : dubug.py
 @Software: PyCharm
 --------------------------------
 @Author  : lixj
 @contact : lixj_zj@163.com
"""

from scrapy import cmdline


cmd = 'scrapy crawl main'
cmdline.execute(cmd.split())
