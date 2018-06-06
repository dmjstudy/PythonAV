#!/usr/bin/python3
# coding: utf-8 
"""
__title__ = ''
__author__ = ''dengminjie
__mtime__ = '18/06/04 0004'
# 
"""

import psutil

def cpu_info():
    cpu_logic=psutil.cpu_times()#使用cpu_times方法获取CPU完整信息,需要显示所有逻辑CPU信息,
    #指定方法变量percpu=True即可,如psutil.cpu_times(percpu=True)
    cpu_logic_user=cpu_logic.user    #获取单项数据信息,如用户user的CPU时间比
    cpu_logic_count=psutil.cpu_count()    #c,默认logical=True4
    cpu_physical_count =psutil.cpu_count(logical=False)

    print("用户user的CPU时间比%s"%cpu_logic_user)
    print("获取单项数据信息%s" % cpu_logic_count)
    print("获取CPU的物理个数%s" % cpu_physical_count)

cpu_info()