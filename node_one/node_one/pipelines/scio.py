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

from node_one.com_config.media_related import MediaFile
from node_one.pipelines.single_mongodb import SingleMongodbPipeline
import re
import logging


class ScioPipeline(object):
    def __init__(self):
        pass

    def pro_process(self, item):
        """
        scio 数据预处理
        :param item: parse()获取到的源数据
        :return: 数据清洗后的数据
        """
        result = dict()
        result['_id'] = item['_id']
        result['page_url'] = item['page_url']
        result['title'] = item['title'][0]

        sub_title = item['sub_title_str'][0].strip().replace(u'\u3000', u' ')
        split_res = sub_title.split("   ")
        result['sub_title_info'] = split_res[0]
        result['publish_time'] = split_res[1]
        result['resource'] = split_res[2].split("：")[1]

        logging.info("page_url:{}, img_urls:{}".format(item['page_url'], item['img']))

        result['img'] = MediaFile().get_image_urls(item['page_url'], item['img'])
        result['video'] = MediaFile().get_image_urls(item['page_url'], item['video'])
        result['audio'] = MediaFile().get_image_urls(item['page_url'], item['audio'])

        author_pattern = r'责任编辑：(.*)'
        result['author'] = re.findall(author_pattern, item['author'][0])

        # TODO 待优化点
        result['content'] = item['content'][0].strip().replace(u'\u3000', u' ').replace("\n", "").replace("\r", "")

        return result


    def process_item(self, item, spider):
        result = self.pro_process(item)
        SingleMongodbPipeline().process_item(result, spider)
