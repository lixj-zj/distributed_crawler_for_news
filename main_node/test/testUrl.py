"""
 !/usr/bin/env python3.6
 -*- coding: utf-8 -*-
 --------------------------------
 Description :
 --------------------------------
 @Time    : 2019/6/19 9:57
 @File    : testUrl.py
 @Software: PyCharm
 --------------------------------
 @Author  : lixj
 @contact : lixj_zj@163.com
"""


import requests
http_headers = { 'Accept': '*/*','Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}

start_urls = ['http://www.scio.gov.cn/37234/Document/1656378/1656378.htm',
              'http://www.scio.gov.cn/37234/Document/1656147/1656147.htm',
              'http://www.scio.gov.cn/37234/Document/1656881/1656881.htm',
              'http://www.scio.gov.cn/37234/Document/1652787/1652787.htm',
              'http://www.scio.gov.cn/37234/Document/1654528/1654528.htm']

# for url in start_urls:
#     resp = requests.get(url,headers = http_headers)
#     print(resp.url)
import re
# resp = requests.get("http://www.scio.gov.cn/37234/Document/1656881/1656881.htm")
# html = resp.text

html = """
window.onload=function()
{
    if("../../../37236/37385/Document/1656878/1656878.htm"=="Delete")
    {
        window.alert('');    
    }
    else
    {
        window.location.replace(afd"../../../37236/37385/Document/1656878/1656878.htm");
    }
}
"""
# r'../../../(.*.htm)'
par = r'window.location.replace\(\"../../../(.*)\"\);'
m = re.findall(par,html)
print(m)
print()

partten = r"window.location.replace(.*);"
partten1 = r'../../../(.*.htm)'
m1 = re.findall(partten,html)
print(m1[0])
m2 = re.findall(partten1,m1[0])
print(m2[0])
