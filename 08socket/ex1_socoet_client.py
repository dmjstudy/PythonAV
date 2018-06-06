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

client.send(b"hello world")
data = client.recv(1024)
print("client接收到的数据:",data)

client.close()
