# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging
from pymongo import MongoClient

class SingleMongodbPipeline(object):
    """
    初始化并连接MongoDB
    """
    def __init__(self):
        self.mongodbLocalhost = "mongodb://192.168.131.24:27017"
        self.conn = MongoClient(self.mongodbLocalhost)
        self.db = self.conn.demo  # 连接数据库demo，没有自动创建
        self.demoJson = self.db.wallstreet  # 使用demo_json集合，没有自动创建


    def process_item(self, item, spider):
        logging.info("item>>>>>>>>>",item)

        logging.info("wallstreet---开始操作mongodb！")
        try:
            # 1. 连接MongoDB
            demoJson = SingleMongodbPipeline().demoJson

            # 2. 插入数据
            demoJson.insert(item)

            # 7. 插入json文件
            # with open(self.jsonPath, "r", encoding="utf-8") as f:
            #     jsonFile = json.load(f)
            #     demo_json.insert(jsonFile)
            logging.info("wallstreet---操作mongodb完成！")
        except:
            logging.error("wallstreet---操作mongodb数据库失败！")



