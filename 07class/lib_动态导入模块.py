#!/usr/bin/python3
# coding: utf-8 
"""
__title__ = ''
__author__ = ''dengminjie
__mtime__ = '18/06/06 0006'
# 
"""
#方式1
# lib = __import__('lib.aa')
# lib.aa
# print(lib.aa)

#官方推荐
import importlib
aa = importlib.import_module('lib.aa')
print(aa.C().name)
