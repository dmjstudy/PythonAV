#!/usr/bin/python3
# coding: utf-8 
"""
__title__ = ''
__author__ = ''dengminjie
__mtime__ = '18/06/06 0006'
# 服务器
"""
import socket

server = socket.socket()
server.bind(('localhost',6969))
server.listen()

print("等电话")
conn,addr = server.accept()  #等电话打入
print(conn,addr)
print("电话来了")
data = conn.recv(1024)
print("server_resv:",data)

conn.send(data.upper())

server.close()


