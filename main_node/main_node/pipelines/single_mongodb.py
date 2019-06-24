# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging
import pymongo
from pymongo import MongoClient
from scrapy.utils.project import get_project_settings


class SingleMongodbPipeline(object):
    """
    初始化并连接MongoDB
    """

    collcetion = 'scio'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        # settings = get_project_settings()
        # self.mongodb_localhost = settings.get("MONGODB_LOCALHOST")
        # self.mongodb_database = settings.get("MONGODB_DATABASE")
        # self.mongodb_collection = settings.get("MONGODB_COLLECTION")
        #
        # self.conn = MongoClient(self.mongodb_localhost)
        # self.db = self.conn.get_database(self.mongodb_database)  # 连接数据库demo，没有自动创建
        # self.collection = self.db.get_collection(self.mongodb_collection)  # 使用demo_json集合，没有自动创建

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get("MONGODB_URI"),
            mongo_db=crawler.settings.get("MONGODB_DATABASE")
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        logging.info(">>>>>>开始操作mongodb！")
        self.db[self.collcetion].insert_one(dict(item))
        return item  # ?

    # def data_storage(self, item):
    #     logging.info(">>>>>>开始操作mongodb！")
    #     logging.info("item is :--- {}".format(item))

    # try:
    #     # 1. 连接MongoDB
    #     # demo_json = self.demo_json
    #
    #     # 2. 插入数据
    #     self.demo_json.insert(item)
    #
    #     # 7. 插入json文件
    #     # with open(self.jsonPath, "r", encoding="utf-8") as f:
    #     #     jsonFile = json.load(f)
    #     #     demo_json.insert(jsonFile)
    #
    #     logging.info(">>>>操作mongodb完成！")
    # except Exception as e:
    #     logging.error(">>>>操作mongodb数据库失败！错误信息：", e)
