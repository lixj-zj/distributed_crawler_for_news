"""
 !/usr/bin/env python3.6
 -*- coding: utf-8 -*-
 --------------------------------
 Description :
 --------------------------------
 @Time    : 2019/6/23 11:18
 @File    : test_string_to_call_fun.py
 @Software: PyCharm
 --------------------------------
 @Author  : lixj
 @contact : lixj_zj@163.com
"""

def a():
    print("a")
    pass

def b():
    print("b")
    pass

dispatch = {'go': a, 'stop': b}  # Note lack of parens for funcs

dispatch['stop']()  # Note trailing parens to call function

