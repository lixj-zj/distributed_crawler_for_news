"""
 !/usr/bin/env python3.6
 -*- coding: utf-8 -*-
 --------------------------------
 Description : 路由类，跳转对应解析方法
 --------------------------------
 @Time    : 2019/6/22 18:59
 @File    : routing.py
 @Software: PyCharm
 --------------------------------
 @Author  : lixj
 @contact : lixj_zj@163.com
"""

import re
import logging
from main_node.website_parse.scio import Scio
from main_node.website_parse.wechat import Wechat


class Routing():
    def __init__(self):
        # 构造字符串映射到函数的字典，记录对应跳转路由的方法
        # 注意此中的value为函数名称，非字符串！
        self.routing_dict = \
            {
                # scio
                'www.scio.gov.cn': Scio().scio_parse,

                # 微信链接
                'mp.weixin.qq.com': Wechat().wechat_parse,

                # 华尔街见闻
                'awtmt.com': 'get_detail_info_from_awtmt',
                'wallstreetcn.com': 'get_detail_info_from_wallstreet',
                'api.wallstreetcn.com': 'get_detail_info_from_api'
            }

    def routing_method(self, url):
        """
        根据url路由对应的方法
        :param url: 解析的url
        :return: 对应解析函数函数返回的数据内容
        """
        try:
            logging.info("路由 routing_method url: {}".format(url))
            # 惰性匹配网址
            pattern = r'//(.*?)/'
            web_site = re.findall(pattern, url)[0]

            # TODO 正则匹配修改
            if web_site in self.routing_dict.keys():
                # 字符串映射到函数的字典。
                # 这种技术的主要优点是字符串不需要匹配函数的名称。
                detail_info = self.routing_dict[web_site](url)
                return detail_info
            else:
                # 不阻断后续url分析，记录无法解析的url
                logging.info("url: {} ，暂无解析方法！".format(url))
                # TODO 分离写文件。接口参数：文件路径、写入内容
                with open("../problems/url_problem.txt", "w+", encoding="utf-8") as f:
                    f.write(logging.info("url: {} ，暂无解析方法！".format(url)))
        except Exception as e:
            logging.error("routing_method 解析异常！异常信息：{}".format(str(e)))


if __name__ == '__main__':
    pass
