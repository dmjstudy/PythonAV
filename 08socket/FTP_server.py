__author__ = "Alex Li"
import hashlib
import socket ,os,time
server = socket.socket()
server.bind(('0.0.0.0',9999) )
server.listen()
while True:
    conn, addr = server.accept()   #receive the conn and  address
    print("new conn:",addr)
    while True: # repeat receive the command
        print("等待新指令")
        data = conn.recv(1024)  #receive the package what has 1024 byte ,the type of data is "<class 'bytes'>"
        if not data:                    # if don't  receive the data then print  the remind info, at the same time break the circulate
            print("客户端已断开")
            break
        cmd,filename = data.decode().split() # each  receive the command and the file name
        print(filename)
        if os.path.isfile(filename):              # if  exist  the file ,then open the file with  the read and  binary  way
           f = open(filename,"rb")
           m = hashlib.md5()                # verify the file  with md5
           file_size = os.stat(filename).st_size  #os.stat('path/filename')  get the file or the directory of  the path
           conn.send( str(file_size).encode() ) #send file size to client
           conn.recv(1024)                             #wait for ack
           for line in f:                                  #read file the data ,add to the md5,and  send the data
              m.update(line)
              conn.send(line)
           print("file md5", m.hexdigest())  #print the md5 hex digest
           f.close()
           conn.send(m.hexdigest().encode()) #send md5 use binary  way
        print("send done")

server.close()
