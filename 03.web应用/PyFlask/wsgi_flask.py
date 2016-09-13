# coding:utf-8
import sys

#Expand Python classes path with your app's path
sys.path.insert(0, "c:/Test_Web")

from test import app#test为flask运行入口文件

#Put logging code (and imports) here ...

#Initialize WSGI app object
application = app

'''
注意，application一定不能改成别的。因为mod_wsgi在解析这个文件时，只认application。
另外，同IIS不同的时，不需要给C:Test_Web文件夹加入NETWORK SERVICE用户的访问权限。
'''