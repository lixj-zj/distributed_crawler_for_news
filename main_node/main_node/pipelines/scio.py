"""
 !/usr/bin/env python3.6
 -*- coding: utf-8 -*-
 --------------------------------
 Description : scio 数据处理
 --------------------------------
 @Time    : 2019/6/22 15:41
 @File    : scio.py
 @Software: PyCharm
 --------------------------------
 @Author  : lixj
 @contact : lixj_zj@163.com
"""

import re
import logging


class ScioPipeline(object):
    def __init__(self):
        pass

    def process_item(self, item, spider):
        """
        scio 数据预处理
        :param item: parse()获取到的源数据
        :return: 数据清洗后的数据
        """
        result = dict()
        result['all_page_real_url'] = item['all_page_real_url']
        return result
