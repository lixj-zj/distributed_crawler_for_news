# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging
import pymongo


class SingleMongodbPipeline(object):
    """
    初始化并连接MongoDB
    """
    def __init__(self, mongo_uri, mongo_db, mongo_collection):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_collection = mongo_collection

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get("MONGODB_URI"),
            mongo_db=crawler.settings.get("MONGODB_DATABASE"),
            mongo_collection=crawler.settings.get("MONGODB_COLLECTION")
        )

    def open_spider(self, spider):
        logging.info("开启mongo client spider...")
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        logging.info("关闭mongo client spider...")
        self.client.close()

    def process_item(self, item, spider):
        logging.info(">>>>>>开始操作mongodb！")
        self.db[self.mongo_collection].insert_one(dict(item))
        return item  # return会在控制台显示输出入库的item数据，可以选择不写（此时显示None）
