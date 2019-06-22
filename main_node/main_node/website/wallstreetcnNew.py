# coding: utf-8 -*-
"""
 !/usr/bin/env python3.6
 -*- coding: utf-8 -*-
 --------------------------------
 Description : 华尔街见闻
 1. 分析接口待爬取链接及基本数据
 2. uri 去重
 3. 根据 uri 爬取详细信息数据
 4. 合并基本信息数据与详细信息数据
 5. 数据存入 mongodb
 --------------------------------
 @Time    : 2019/5/13 22:16
 @File    : wallstreetcn.py
 @Software: PyCharm
 --------------------------------
 @Author  : lixj
 @contact : lixj_zj@163.com
"""

import requests
import logging
import re
import json
from lxml import etree
from pymongo import MongoClient
# import comConfig.userAgent as ua
# import GZH
import logging
import requests
from main_node.com_config import user_agent as ua
import json



# logging.basicConfig函数对日志的输出格式及方式做相关配置
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


def requestUrl(url):
    """
    获取url的html内容
    :param url:
    :return:
    """
    re = requests.get(url, headers=ua.UserAgent().getRandomHeaders(), timeout=10)
    try:
        if re.status_code == 200:
            re.encoding = re.apparent_encoding
            logging.info("requests url 请求完成！url:{}".format(url))
            return re.text
        else:
            logging.error("request url 请求状态异常！异常url：{}，异常链接状态：{}".format(url, re.status_code))
    except Exception as e:
        logging.error("request url 请求异常！异常信息:{}".format(str(e)))


def getWallstreetData(url):
    """
    获取原数据
    :param url:
    :return:
    """
    html = requestUrl(url)
    dataInfoDict = str2dict(html)
    try:
        nextCursorStr = dataInfoDict.get('data').get('next_cursor')
        itemsList = dataInfoDict.get('data').get('items')
        logging.info("获取 wall street 源数据完成！url:{}".format(url))
        return nextCursorStr, itemsList
    except Exception as e:
        logging.error("wallstreet---获取数据异常！异常信息:", e)


def str2dict(str):
    """
    json格式的字符串转换成字典（json）
    :param str:
    :return:
    """
    return json.loads(str)


class mongoDB():
    """
    初始化并连接MongoDB
    """

    def __init__(self):
        self.mongodbLocalhost = "mongodb://192.168.131.24:27017"
        self.conn = MongoClient(self.mongodbLocalhost)
        self.db = self.conn.demo  # 连接数据库demo，没有自动创建
        self.demoJson = self.db.wallstreet  # 使用demo_json集合，没有自动创建


# dict中的数据入库
def data2oracle(dict):
    logging.info("wallstreet---开始操作mongodb！")
    try:
        # 1. 连接MongoDB
        demoJson = mongoDB().demoJson

        # 2. 插入数据
        demoJson.insert(dict)

        # 7. 插入json文件
        # with open(self.jsonPath, "r", encoding="utf-8") as f:
        #     jsonFile = json.load(f)
        #     demo_json.insert(jsonFile)
        logging.info("wallstreet---操作mongodb完成！")
    except:
        logging.error("wallstreet---操作mongodb数据库失败！")


def existUri(uriStr):
    global uriSet
    if uriStr not in uriSet:
        uriSet.add(uriStr)
        return False
    else:
        return True


def data2File(dataSet):
    # fileName = temp.txt
    pass


def routingMethod(basicInfoDict):
    """
    根据uri路由对应的方法
    :param basicInfoDict:
    :return:
    """
    # 拿到域名跳转指定的解析方法
    uri = basicInfoDict.get('resource').get('uri')

    # 分析 uri 是否是外部链接（微信文章），选择不同的正则匹配
    pattern = r'//(.*)/' if uri.find('?') == -1 else r'//(.*)/?'
    webSite = re.findall(pattern, uri[:uri.find('?')])[0]

    global routingDict
    if webSite in routingDict.keys():
        # globals()[func]() 以字典的方式访问局部（locals()[func]()）和全局变量
        detailInfoDict = globals()[routingDict.get(webSite)](uri)
        return detailInfoDict
    else:
        logging.info(">>>>>>>>>>>>>>wallstreet---uri {} 暂无解析方法".format(uri))


# 解析文章的详细信息，返回详细信息的字典
def getDetailInfoFromAwtmt(uri):
    logging.info("跳转至 awtmt 解析方法。uri:{}".format(uri))
    try:
        html = requestUrl(uri)
        struct = etree.HTML(html)
        abstract = struct.xpath('//*[@class="article-summary"]/text()')  # 摘要
        content = struct.xpath('//*[@class="article-text"]')  # 正文
        info = content[0].xpath('string(.)')  # xpath解析正文某个标签下的所有文字
        comment = struct.xpath('//*[@class="comment-total"]/text()')  # 评论条数
        detailInfoDict = {}
        detailInfoDict['abstract'] = abstract
        detailInfoDict['content'] = info
        detailInfoDict['comment'] = comment
        logging.info("get detail info from awtmt succeed!")
        return detailInfoDict
    except:
        logging.error("wallstreet---解析Awtmt错误！")


# 解析站内资讯
def getDetailInfoFromWallstreet(uri):
    logging.info("跳转至 Wall street 解析方法。uri:{}".format(uri))
    try:
        html = requestUrl(uri)
        struct = etree.HTML(html)
        abstract = struct.xpath('//*[@class="article-summary"]/text()')  # 摘要
        content = struct.xpath('//*[@class="rich-text"]')  # 正文
        info = content[0].xpath('string(.)')  # xpath解析正文某个标签下的所有文字
        # comment = struct.xpath('.//div[@class="comments"]/div[@class="container"]/div[@class="list"]/div[@class="header"]/div[@class="title"]/text()')  # 评论 ！从根目录找

        detailInfoDict = {}
        detailInfoDict['abstract'] = abstract
        detailInfoDict['content'] = info
        logging.info("get detail info from Wall street succeed!")
        return detailInfoDict
    except:
        logging.error("wallstreet---解析Wallstreet错误！")


def getDetailInfoFromApi(uri):
    """
    开两个线程
    :param uri:
    :return:
    """
    logging.info("跳转至 api Wall street 解析方法。uri:{}".format(uri))
    try:
        # 线程1
        # GZH.run(uri)  ！

        # 线程2
        html = requests.get(uri)
        struct = etree.HTML(str(html.text))
        title = struct.xpath('//*[@class="rich_media_title"]/text()')  # 标题
        originAll = struct.xpath('//*[@id="meta_content"]')  # 来源
        origin = originAll[0].xpath('string(.)')  # xpath解析来源某个标签下的所有文字
        content = struct.xpath('//*[@id="js_content"]')  # 正文
        info = content[0].xpath('string(.)')  # xpath解析正文某个标签下的所有文字

        partten = r"\d{4}-\d{1,2}-\d{1,2}"
        publishTime = re.search(partten, str(html.text))

        detailInfoDict = {}
        detailInfoDict['title'] = title[0].replace("\n", "").strip()
        detailInfoDict['origin'] = str(origin).replace(" ", "").replace("\n", " ").strip()
        detailInfoDict['publishTime'] = publishTime.group()  # 返回被 RE 匹配的字符串
        detailInfoDict['content'] = str(info).replace("\n", "").strip()

        logging.info("get detail info from api Wall street succeed!")
        return detailInfoDict
    except:
        logging.error("wallstreet---解析api错误！")


def run():
    # 记录全局缓存的uri，去重
    uriSet = set()

    # 记录跳转路由方法
    routingDict = {'awtmt.com/articles': 'getDetailInfoFromAwtmt',
                   'wallstreetcn.com/articles': 'getDetailInfoFromWallstreet',
                   'api.wallstreetcn.com/redirect': 'getDetailInfoFromApi'
                   }

    # 1.获取源数据
    LIMIT = 2  # 返回个数
    TARGET_URL = "https://api.wallstreetcn.com/apiv1/content/information-flow?limit=" + str(
        LIMIT) + "&cursor=&channel=kechuang&accept=article"
    nextCursorStr, limitItemsList = getWallstreetData(TARGET_URL)

    # 2.url去重
    for limitItem in limitItemsList:
        if existUri(limitItem['resource']['uri']):
            # limitItemsList删除重复的limitItem
            limitItemsList.remove(limitItem)

    # 3.分析；此时limitItemsList已经去重
    # 最终总的结果list
    resultList = []
    for basicInfoDict in limitItemsList:
        detailInfoDict = routingMethod(basicInfoDict)

        # 合并 detailInfoDict 与 basicInfoDict，在basicInfoDict上添加
        basicInfoDict.update(detailInfoDict)

        # 汇总所有limit个数的总数据
        resultList.append(basicInfoDict)

    # 已有的信息与详细信息合并后，数据入库
    data2oracle(resultList)

def test():
    print("wallstreet >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

if __name__ == '__main__':
    # run()
    test()