"""
 !/usr/bin/env python3.6
 -*- coding: utf-8 -*-
 --------------------------------
 Description : 
 --------------------------------
 @Time    : 2019/6/26 15:22
 @File    : test_all_url.py
 @Software: PyCharm
 --------------------------------
 @Author  : lixj
 @contact : lixj_zj@163.com
"""

import requests
from lxml import etree


headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
}

# url = "http://www.scio.gov.cn/index.htm"
# req = requests.get(url=url, headers=headers)
# req.encoding=req.apparent_encoding
# with open("test_all_url.txt", "w", encoding="utf-8") as f:
#     f.write(str(req.text))

# with open("test_all_url.txt", "r", encoding="utf-8") as f:
#     html = f.read()
# struct = etree.HTML(html)
# all_url = struct.xpath("//a/@href")
# result = []
# for url in set(all_url):
#     if "htm" in url:
#         result.append(url)
# print(result)
# print(len(result))


base = "http://www.scio.gov.cn/"
all_url_result = ['37234/Document/1654022/1654022.htm', 'video/34317/Document/1657265/1657265.htm', 'zfbps/32832/Document/1655934/1655934.htm', '37236/index.htm', '37259/Document/1657985/1657985.htm', 'video/34317/Document/1657554/1657554.htm', '33648/Document/1656290/1656290.htm', 'tt/Document/1657925/1657925.htm', 'qt/Document/331911/331911.htm', '32619/Document/1397925/1397925.htm', '37234/Document/1657697/1657697.htm', 'hzspsx/xwfw/Document/1364232/1364232.htm', '34473/34474/Document/1657805/1657805.htm', '32619/Document/1538506/1538506.htm', 'xwfbh/gssxwfbh/index.htm', 'qt/Document/331914/331914.htm', '33648/Document/1655260/1655260.htm', 'video/qwjd/34146/Document/1658000/1658000.htm', 'zfbps/32832/Document/1650847/1650847.htm', 'dfbd/dfbd/index.htm', 'video/34317/Document/1657870/1657870.htm', '32619/Document/1397905/1397905.htm', 'xwfbh/37429/Document/1643905/1643905.htm', '32619/Document/1398071/1398071.htm', '37232/Document/1654020/1654020.htm', '32344/Document/1656446/1656446.htm', 'video/index.htm', 'xwfbh/yg/index.htm', '34473/35351/index.htm', 'video/qwjd/34146/Document/1657595/1657595.htm', '37236/38180/Document/1638219/1638219.htm', '33648/Document/1656289/1656289.htm', 'video/34317/Document/1657086/1657086.htm', 'zfbps/32832/Document/1649841/1649841.htm', 'qt/Document/1630850/1630850.htm', '31773/35507/35514/35522/index.htm', '33648/index.htm', '32619/Document/1397907/1397907.htm', 'zfbps/32832/Document/1655898/1655898.htm', '32619/Document/1397917/1397917.htm', '32619/Document/1538502/1538502.htm', '31773/35507/35513/Document/1657504/1657504.htm', '37232/Document/1657234/1657234.htm', 'http://presscard.scio.gov.cn/index.html', '37231/37342/Document/1657927/1657927.htm', '32619/Document/1397911/1397911.htm', '37234/Document/1657953/1657953.htm', '34473/34474/Document/1657755/1657755.htm', 'zfbps/index.htm', 'xwfbh/gbwxwfbh/index.html', '32619/Document/1397903/1397903.htm', 'xwfbh/index.htm', 'xwfbh/xwbfbh/fbh/Document/1657890/1657890.htm', '32619/index.htm', '37259/Document/1657935/1657935.htm', '37232/Document/1657628/1657628.htm', 'xwfbh/gbwxwfbh/xwfbh/jyb/Document/1657929/1657929.htm', '32619/Document/1538505/1538505.htm', 'tt/index.htm', '37232/Document/1656109/1656109.htm', '37231/37342/Document/1657918/1657918.htm', '37231/index.htm', '31773/35507/35514/Document/1657970/1657970.htm', 'http://www.gov.cn/guoqing/index.htm', 'tt/Document/1657915/1657915.htm', '37231/37342/Document/1657920/1657920.htm', 'tt/Document/1657217/1657217.htm', '37259/Document/1657749/1657749.htm', '37234/Document/1657923/1657923.htm', 'index.htm', 'xwfbh/qyxwfbh/Document/1657733/1657733.htm', '32619/Document/1397920/1397920.htm', '31773/35507/35510/35524/index.htm', 'xwfbh/xwbfbh/index.htm', '31773/35507/35510/Document/1657955/1657955.htm', '37236/38180/Document/1638218/1638218.htm', '34473/34474/Document/1657589/1657589.htm', '34473/34474/Document/1657573/1657573.htm', 'xwbjs/index.htm', 'dfbd/dfbd/Document/1657039/1657039.htm', '32619/Document/1538509/1538509.htm', '31773/35507/35513/35521/index.htm', 'xwfbh/xwbfbh/fbh/Document/1657763/1657763.htm', '37234/Document/1657236/1657236.htm', '33648/Document/1655703/1655703.htm', '37259/Document/1657773/1657773.htm', '34473/34474/index.htm', 'dfbd/dfbd/Document/1657639/1657639.htm', '34473/35351/Document/1653456/1653456.htm', '32619/Document/1538504/1538504.htm', 'yswxp/index.html', 'xwfbh/qyxwfbh/index.htm', 'ztk/index.htm', 'xwfbh/xwbfbh/fbh/Document/1657772/1657772.htm', '37236/37377/Document/1638772/1638772.htm', '32344/index.htm', 'ztk/Document/1657477/1657477.htm', '32344/Document/1656659/1656659.htm', 'zfbps/32832/Document/1650692/1650692.htm', 'tt/Document/1657914/1657914.htm', 'ztk/Document/1657180/1657180.htm', 'tt/Document/1657913/1657913.htm', '33648/Document/1656291/1656291.htm', 'dfbd/dfbd/Document/1657734/1657734.htm', 'video/34317/index.htm', 'dfbd/dfbd/Document/1657048/1657048.htm', 'wzxx/index.htm', '32619/Document/1397922/1397922.htm', '37259/index.htm', 'ztk/dtzt/39912/40728/index.htm', '37232/index.htm', 'dfbd/dfbd/Document/1657397/1657397.htm', 'dfbd/dfbd/Document/1658013/1658013.htm', '37234/index.htm', '34473/35351/Document/1655257/1655257.htm', '33648/Document/1655705/1655705.htm', 'wzxx/ck/index.htm', '37236/1/Document/1637909/1637909.htm', 'video/qwjd/34146/Document/1657403/1657403.htm', '34473/34474/Document/1657156/1657156.htm', '32344/Document/1656625/1656625.htm', 'xwfbh/37380/index.htm', 'dfbd/dfbd/Document/1657644/1657644.htm', 'ztk/Document/1656666/1656666.htm', 'dfbd/dfbd/Document/1657389/1657389.htm', 'video/qwjd/34146/Document/1657185/1657185.htm', '32619/Document/1476968/1476968.htm', 'xwfbh/gssxwfbh/xwfbh/shan_xi/Document/1657968/1657968.htm']
full_url = []
for url in all_url_result:
    if "http" not in url:
        full_url.append(base + url)
print(full_url)
print(len(full_url))

