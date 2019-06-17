"""
 !/usr/bin/env python3.6
 -*- coding: utf-8 -*-
 --------------------------------
 Description :
 --------------------------------
 @Time    : 2019/6/17 19:50
 @File    : test_mutifile.py
 @Software: PyCharm
 --------------------------------
 @Author  : lixj
 @contact : lixj_zj@163.com
"""
import requests
from lxml import etree
import re
import time
import logging
import os


# 判断是否含有多媒体文件
def contained_images(html):
    struct = etree.HTML(html)
    img_url_list = struct.xpath('//*[@id="content"]//img/@src')
    return img_url_list

def contained_videos(html):
    struct = etree.HTML(html)
    video_url_list = struct.xpath('//*[@id="content"]//video/@src')
    return len(video_url_list) is not 0

def contained_audios(html):
    struct = etree.HTML(html)
    audio_url_list = struct.xpath('//*[@id="content"]//audio/@src')
    return len(audio_url_list) is not 0

def get_image_urls(page_url, img_urls):
    try:
        download_urls = []
        if len(img_urls) is not 0:
            for one_img_url in img_urls:
                download_urls.append(page_url.rsplit("/", maxsplit=1)[0] + os.altsep + one_img_url)
        return download_urls
    except Exception as e:
        logging.error("获取图片下载地址错误！错误信息：{}".format(str(e)))

def get_video_urls(page_url, video_urls):
    try:
        download_urls = []
        if len(video_urls) is not 0:
            for one_video_url in video_urls:
                download_urls.append(page_url.rsplit("/", maxsplit=1)[0] + os.altsep + one_video_url)
        return download_urls
    except Exception as e:
        logging.error("获取视频下载地址错误！错误信息：{}".format(str(e)))

def get_audio_urls(page_url, audio_urls):
    try:
        download_urls = []
        if len(audio_urls) is not 0:
            for one_audio_url in audio_urls:
                download_urls.append(page_url.rsplit("/", maxsplit=1)[0] + os.altsep + one_audio_url)
        return download_urls
    except Exception as e:
        logging.error("获取音频下载地址错误！错误信息：{}".format(str(e)))




if __name__ == '__main__':
    page_url = "http://www.scio.gov.cn/xwbjs/zygy/32310/hd32313/Document/1651786/1651786.htm"
    req = requests.get(page_url)
    req.encoding=req.apparent_encoding
    html = str(req.text)

    print(get_image_urls(page_url, contained_images(html)))
