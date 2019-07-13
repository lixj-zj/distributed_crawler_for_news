"""
 !/usr/bin/env python3.6
 -*- coding: utf-8 -*-
 --------------------------------
 Description : 
 --------------------------------
 @Time    : 2019/7/10 22:30
 @File    : wechat.py
 @Software: PyCharm
 --------------------------------
 @Author  : lixj
 @contact : lixj_zj@163.com
"""

class WechatPipeline(object):
    def __init__(self):
        pass

    def process_item(self, item, spider):
        """
        WeChat 数据预处理
        :param item: parse()获取到的源数据
        :return: 数据清洗后的数据
        """
        return item
