#!/usr/bin/python3
# coding: utf-8 
"""
__title__ = ''
__author__ = ''dengminjie
__mtime__ = '18/05/28 0028'
#  use  calc running time
"""

import time

def calc_time(func):
    start_time = time.time()
    func()
    stop_time = time.time()
    print("the func run time is %s"%(stop_time-start_time))

def timer(func):
    def calc_time(*args, **kwargs):
        start_time = time.time( )
        func(*args,**kwargs)
        stop_time = time.time( )
        print("the func run time is %s" % (stop_time - start_time))
    return  calc_time


if __name__ == '__main__':
    @timer # test_fun= timer(test_fun)
    def test_fun():
        time.sleep(3)
        print("dengminjie")

    @timer
    def test_fun1(age):
        time.sleep(3)
        print("dengminjie,%s"%age)

    # calc_time(test_fun)

    test_fun()
    test_fun1(28)