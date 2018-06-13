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
    data_len=client.recv(1024)
    print(data_len)
    recv_len =0
    while recv_len < int(data_len):
        data = client.recv(1024)
        recv_len = recv_len +len(data.encode('utf-8'))
        print(recv_len)
        recv_data = recv_data +data

    print("client接收到的数据:",recv_data.decode('utf-8'))
    print("收到数据长度",data_len)
    print("收到数据实践长度",recv_len)

client.close()
