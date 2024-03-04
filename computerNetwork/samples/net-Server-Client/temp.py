#coding:utf-8
from socket import *

# 创建socket，绑定到端口，开始监听
tcpSerPort = 8899
tcpSerSock = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
tcpSerSock.bind(('', tcpSerPort))
tcpSerSock.listen(5)

# root dir
root = 'D:\\webProjects\\net-Server-Client\\proxyFile\\'
# 开始从客户端接收请求
print('Ready to serve...')
tcpCliSock, addr = tcpSerSock.accept()
print('Received a connection from: ', addr)
message = tcpCliSock.recv(4096).decode()

# 从请求中解析出filename
print(message)
filename = message.split()[1]# .partition("//")[2].replace('/', '_')
print(filename)