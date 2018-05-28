#!/usr/bin/python3
# coding: utf-8 
"""
__title__ = ''
__author__ = ''dengminjie
__mtime__ = '18/05/28 0028'
# 测试一下高级装饰器的写法
"""
username, password = 'deng','1'

def auth(func):
    def wrapper(*args,**kwargs):
        UserName = input("please input UserName:").strip()
        PassWord = input("please input PassWord:").strip()
        if UserName ==username and PassWord== password:
            print("\033[32;1m登录成功\033[0m")
            func(*args,**kwargs)
        else:
            exit("登录失败")
    return wrapper



def index():
    print("this is index")

@auth
def home():
    print("this is home")

@auth
def bbs():
    print("this is bbs")

index()
home()
bbs()
