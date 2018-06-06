#!/usr/bin/python3
# coding: utf-8 
"""
__title__ = ''
__author__ = ''dengminjie
__mtime__ = '18/06/06 0006'
# 
"""
import json
import os
name = input("请输入姓名:").strip()
filename = name +'.json'

try:
    with open(filename) as fr_obj:
        file_info = json.load(fr_obj)
        print("欢迎回来",file_info)
except FileNotFoundError:
    username = name
    with open(filename,"w") as f_obj:
        json.dump(name, f_obj)
        print("将保存用户名")

