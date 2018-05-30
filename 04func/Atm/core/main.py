__author__ = "Alex Li"
import os
import sys
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )
from core import bak_atm

def login():
    print("Welcome to my atm")

user_data = {
    '_name':None,
    'is_authenticated':False,
    'accout_data':None
}

goods_all = [
    ['1','pen', '100', '10'],
    ['2','apple', '7000', '10'],
    ['3','iphone', '5000', '10'],
    ['4','mi2s', '500', '10'],
]

def goods_info():
    #货物与价格
    pass
def  goods_list():
    print("id--商品--单价--总数")
    for goods in goods_all:
        print(goods[0],goods[1],goods[2],goods[3])


def calc_money():
    #结账
    pass

def conn_bak():
    #连接,
    pass

def auth(func):
    def warpper(*args,**kwargs):
        # 认证
        _name = 'deng'
        _passwd = '1'
        name = input("请输入账号")
        passwd = input("请输入密码")
        if name==_name and passwd== _passwd:
            print("登录成功")
            func(*args,** kwargs)
        else:
            warpper(*args, **kwargs)
    return warpper

@auth
def main():
    deng_money = 10000;
    buy_sum = 0
    buy = 'y'
    while buy == 'y':
        goods_list()
        buy_id= int(input("请选择要买商品ID号"))
        buy_sum = buy_sum+int(goods_all[buy_id-1][2])
        print("已购买%s元商品"%buy_sum)
        while True:
            buy= input("是否继续买，买输入y，不买付款输入n.请输入：")
            if buy=='n':
                #结算
                print("所有商品共使用%s元"%buy_sum)
                bak_atm.view_account_info()
                print("欢迎下次再来")
                break
            elif buy == 'y':
                break
            else:
                pass

