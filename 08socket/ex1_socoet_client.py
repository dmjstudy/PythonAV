#!/usr/bin/python3
# coding: utf-8 
"""
__title__ = ''
__author__ = ''dengminjie
__mtime__ = '18/06/06 0006'
# socket 客户端
"""
import socket


client = socket.socket()
client.connect(('localhost',6969))
while True:
    msg = input("请入服务器执行指令，end关闭服务器:").strip()
    client.send(msg.encode('utf-8'))
    data = client.recv(1024000)
    print("client接收到的数据:",data.decode('utf-8'))

client.close()
