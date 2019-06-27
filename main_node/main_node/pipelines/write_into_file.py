# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging
import os


class WriteIntoFilePipeline(object):
    """
    将数据写入文件
    """

    def __init__(self, file_path, file_name, file_suffix):
        self.file_path = file_path
        self.file_name = file_name
        self.file_suffix = file_suffix

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            file_path=crawler.settings.get("FILE_PATH"),
            file_name=crawler.settings.get("FILE_NAME"),
            file_suffix=crawler.settings.get("FILE_SUFFIX")
        )

    def process_item(self, item, spider):
        logging.info(">>>>>>开始操作写入下载链接文件！")
        logging.info("写入内容：{}".format(item))
        file_path = self.file_path + os.altsep + self.file_name + self.file_suffix

        # # 写入文件-去重
        # with open(file_path, "a+", encoding="utf-8") as f:
        #     for uri in item['all_real_urls']:
        #         f.write(uri if uri is item[-1] else uri + ",")
        #
        # return item  # return会在控制台显示输出入库的item数据，可以选择不写（此时显示None）
