#!/usr/bin/python3
# coding: utf-8 
"""
__title__ = ''
__author__ = ''dengminjie
__mtime__ = '18/06/06 0006'
# 
"""
import json

numbers = [2, 3, 5, 7, 11,13]

filename = 'number.json'
# with open(filename,'w') as f_obj:
#     json.dump(numbers, f_obj)

with open(filename) as fr_obj:
    numbers_config = json.load(fr_obj)

print(numbers)