#!/usr/bin/python3 
#coding=utf-8 

from socket import * 
import sys 
import getpass

#创建网络连接
def main():
    if len(sys.argv) < 3:
        print("argv is error")
        return 
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    s = socket()
    try:
        s.connect((HOST,PORT))
    except Exception as e:
        print(e)
        return

    while True:
        print('''
            ===========Welcome==========
            -- 1.注册   2.登录    3.退出--
            ============================
            ''')
        
        try:
            cmd = int(input("输入选项>>"))
        except Exception as e:
            print("命令错误")
            continue 