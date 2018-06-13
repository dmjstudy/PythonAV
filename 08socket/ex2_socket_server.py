#!/usr/bin/python3
# coding: utf-8 
"""
__title__ = ''
__author__ = ''dengminjie
__mtime__ = '18/06/06 0006'
# 服务器
"""
import socket
import os

server = socket.socket()
server.bind(('localhost',6969))
server.listen( )
print("等待指令")
conn, addr = server.accept( )  # 等电话打入
while True:
    print(conn,addr)
    print("指令来了")
    data = conn.recv(1024)
    if data.decode('utf-8') =='end':
        over_msg = "服务器已关闭"
        conn.send(over_msg.encode('utf-8'))
        server.close( )
        print("接收到关闭指令")
        break
    else:
        print("server_resv:",data.decode('utf-8'))
        cmd_res = os.popen(data.decode('utf-8')).read()
        res = str(len(cmd_res.encode()))
        if len(cmd_res) == 0:
            res = "error"
        conn.send(res.encode('utf-8'))
        # try:
        #     res = os.popen(data.decode('utf-8')).read()
        #     # print(res)
        #     if len(res) == 0:
        #         res = 'test'
        #
        # except Exception as e:
        #     res = str(e)
        # finally:
        #     conn.send(res.encode('utf-8'))



