"""
 !/usr/bin/env python3.6
 -*- coding: utf-8 -*-
 --------------------------------
 Description : 单例模式-requests请求
 --------------------------------
 @Time    : 2019/6/26 21:50
 @File    : new_requests.py
 @Software: PyCharm
 --------------------------------
 @Author  : lixj
 @contact : lixj_zj@163.com
"""

import requests
import logging
from main_node.com_config.user_agent import UserAgent

class NewRequests():

    def __init__(self):
        pass

    def get_html_from_url(self, url):
        req = requests.get(url, headers=UserAgent().get_headers(), timeout=10)
        try:
            if req.status_code == 200:
                req.encoding = req.apparent_encoding
                logging.info("requests url 请求完成！url:{}".format(url))
                return req.text
            else:
                logging.error("request url 请求状态异常！异常url：{}，异常链接状态：{}".format(url, req.status_code))
        except Exception as e:
            logging.error("request url 请求异常！异常信息:{}".format(str(e)))

