# -*- coding: utf-8 -*-
# @Date:   2016-07-12 13:06:06
# @Last Modified time: 2016-11-29 09:40:35
#
# 运行WSGI服务(编写一个server.py，负责启动WSGI服务器，加载application()函数)
#
from wsgiref.simple_server import make_server
from test_wsgi import application
#
# 创建一个服务器
# IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print "Serving HTTP on port 8000..."
#
# 开始监听HTTP请求
httpd.serve_forever()
#
# 启动成功后，打开浏览器，输入http://localhost:8000/
