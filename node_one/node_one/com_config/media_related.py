"""
 !/usr/bin/env python3.6
 -*- coding: utf-8 -*-
 --------------------------------
 Description : 多媒体文件相关公共类
 --------------------------------
 @Time    : 2019/6/17 19:50
 @File    : test_mutifile.py
 @Software: PyCharm
 --------------------------------
 @Author  : lixj
 @contact : lixj_zj@163.com
"""

from lxml import etree
import logging
import os
from urllib.parse import unquote

class MediaFile():
    def __init__(self):
        pass

    def contained_images(self, html, tag_type, tag_name):
        """
        查找页面指定标签下包含的image地址
        :param html: 页面的html
        :param tag_type: 标签类型
        :param tag_name: 标签名
        :return: 图片url地址
        """
        struct = etree.HTML(html)
        img_url_list = struct.xpath('//*[@' + tag_type + '=" ' + tag_name + ' "]//img/@src')
        return img_url_list


    def contained_videos(self, html, tag_type, tag_name):
        """
        查找页面指定标签下包含的video地址
        :param html: 页面的html
        :param tag_type: 标签类型
        :param tag_name: 标签名
        :return: video url地址
        """
        struct = etree.HTML(html)
        video_url_list = struct.xpath('//*[@' + tag_type + '=" ' + tag_name + ' "]//video/@src')
        return video_url_list


    def contained_audios(self, html, tag_type, tag_name):
        """
        查找页面指定标签下包含的audio地址
        :param html: 页面的html
        :param tag_type: 标签类型
        :param tag_name: 标签名
        :return: audio url地址
        """
        struct = etree.HTML(html)
        audio_url_list = struct.xpath('//*[@' + tag_type + '=" ' + tag_name + ' "]//audio/@src')
        return audio_url_list


    def get_image_urls(self, page_url, img_urls):
        """
        截取页面名称后的url地址，并与image列表中的每个地址拼接
        :param page_url: 页面地址
        :param img_urls: 图片列表
        :return: 完整的图片下载地址
        """
        try:
            download_urls = []
            if len(img_urls) is not 0:
                for one_img_url in img_urls:
                    download_urls.append(page_url.rsplit("/", maxsplit=1)[0] +
                                         os.altsep + unquote(one_img_url, "utf-8"))
            logging.info("page_url:{}, img_urls:{}".format(page_url, download_urls))
            return download_urls
        except Exception as e:
            logging.error("获取图片下载地址错误！错误信息：{}".format(str(e)))


    def get_video_urls(self, page_url, video_urls):
        """
        截取页面名称后的url地址，并与video列表中的每个地址拼接
        :param page_url: 页面地址
        :param video_urls: 视频列表
        :return: 完整的视频下载地址
        """
        try:
            download_urls = []
            if len(video_urls) is not 0:
                for one_video_url in video_urls:
                    download_urls.append(page_url.rsplit("/", maxsplit=1)[0] + os.altsep + one_video_url)
            logging.info("page_url:{}, video_urls:{}".format(page_url, download_urls))
            return download_urls
        except Exception as e:
            logging.error("获取视频下载地址错误！错误信息：{}".format(str(e)))


    def get_audio_urls(self, page_url, audio_urls):
        """
        截取页面名称后的url地址，并与audio列表中的每个地址拼接
        :param page_url: 页面地址
        :param video_urls: 音频列表
        :return: 完整的音频下载地址
        """
        try:
            download_urls = []
            if len(audio_urls) is not 0:
                for one_audio_url in audio_urls:
                    download_urls.append(page_url.rsplit("/", maxsplit=1)[0] + os.altsep + one_audio_url)
            logging.info("page_url:{}, audio_urls:{}".format(page_url, download_urls))
            return download_urls
        except Exception as e:
            logging.error("获取音频下载地址错误！错误信息：{}".format(str(e)))


    # TODO 下载多媒体文件暂缓，暂时用处不大

if __name__ == '__main__':
    pass
