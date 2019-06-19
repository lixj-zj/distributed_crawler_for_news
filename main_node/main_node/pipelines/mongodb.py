# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging
from pymongo import MongoClient
import os
from urllib.parse import unquote
import re


class SingleMongodbPipeline(object):
    """
    初始化并连接MongoDB
    """

    def __init__(self):
        self.mongodb_localhost = "mongodb://192.168.131.24:27017"
        self.conn = MongoClient(self.mongodb_localhost)
        self.db = self.conn.demo  # 连接数据库demo，没有自动创建
        self.demo_json = self.db.scio  # 使用demo_json集合，没有自动创建

    def pro_process(self, item):
        """
        预处理
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

        result['img'] = self.get_image_urls(item['real_url'], item['img'])
        result['video'] = self.get_image_urls(item['real_url'], item['video'])
        result['audio'] = self.get_image_urls(item['real_url'], item['audio'])

        author_pattern = r'责任编辑：(.*)'
        result['author'] = re.findall(author_pattern, item['author'][0])

        # TODO 待优化点
        result['content'] = item['content'][0].strip().replace(u'\u3000', u' ').replace("\n","").replace("\r","")

        return result


    def process_item(self, item, spider):
        result = self.pro_process(item)
        print("process>>>>>>>>>>>>>>>>>>>>>")
        print(result)

        self.data_to_mongodb(result)


    def data_to_mongodb(self, item):
        logging.info("scio---开始操作mongodb！")
        try:
            # 1. 连接MongoDB
            # demo_json = self.demo_json

            # 2. 插入数据
            self.demo_json.insert(item)

            # 7. 插入json文件
            # with open(self.jsonPath, "r", encoding="utf-8") as f:
            #     jsonFile = json.load(f)
            #     demo_json.insert(jsonFile)

            logging.info("scio---操作mongodb完成！")
        except Exception as e:
            logging.error("scio---操作mongodb数据库失败！错误信息：", e)





    def get_image_urls(self, page_url, img_urls):
        try:
            download_urls = []
            if len(img_urls) is not 0:
                for one_img_url in img_urls:
                    download_urls.append(page_url.rsplit("/", maxsplit=1)[0] +
                                         os.altsep + unquote(one_img_url, "utf-8"))
            return download_urls
        except Exception as e:
            logging.error("获取图片下载地址错误！错误信息：{}".format(str(e)))

    def get_video_urls(self, page_url, video_urls):
        try:
            download_urls = []
            if len(video_urls) is not 0:
                for one_video_url in video_urls:
                    download_urls.append(page_url.rsplit("/", maxsplit=1)[0] + os.altsep + one_video_url)
            return download_urls
        except Exception as e:
            logging.error("获取视频下载地址错误！错误信息：{}".format(str(e)))

    def get_audio_urls(self, page_url, audio_urls):
        try:
            download_urls = []
            if len(audio_urls) is not 0:
                for one_audio_url in audio_urls:
                    download_urls.append(page_url.rsplit("/", maxsplit=1)[0] + os.altsep + one_audio_url)
            return download_urls
        except Exception as e:
            logging.error("获取音频下载地址错误！错误信息：{}".format(str(e)))
