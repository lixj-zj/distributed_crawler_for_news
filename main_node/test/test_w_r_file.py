"""
 !/usr/bin/env python3.6
 -*- coding: utf-8 -*-
 --------------------------------
 Description : 
 --------------------------------
 @Time    : 2019/6/27 2:49
 @File    : test_w_r_file.py
 @Software: PyCharm
 --------------------------------
 @Author  : lixj
 @contact : lixj_zj@163.com
"""

with open("test_all_url.txt", "r", encoding="utf-8") as f:
    cont = f.read()
a = set(cont.split(","))
print(a)
# print(a.__contains__('www.scio.gov.cn/xwbjs/zygy/33093/hd33096/Document/1655360/1655360.htm'))
#
# item = ['1', '2', '3']
# with open("test_all_url.txt", "w", encoding="utf-8") as f:
#     for uri in item:
#         f.write(str(uri) if uri is item[-1] else str(uri) + ",")

