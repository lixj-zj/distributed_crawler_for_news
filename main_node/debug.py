"""
 !/usr/bin/env python3.6
 -*- coding: utf-8 -*-
 --------------------------------
 Description : 调试spider的debug文件，放在与scrapy.cfg同目录下！
 使用：修改name为对应的爬虫名，右键debug该文件，在断点处调试。
 --------------------------------
 @Time    : 2019/6/18 21:49
 @File    : debug.py
 @Software: PyCharm
 --------------------------------
 @Author  : lixj
 @contact : lixj_zj@163.com
"""

from scrapy import cmdline


name = 'main'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())
