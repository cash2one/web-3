# -*- coding: utf-8 -*-
# @Date:   2016-07-12 13:06:06
# @Last Modified time: 2016-10-12 14:41:55
#
# 运行WSGI服务(编写一个server.py，负责启动WSGI服务器，加载application()函数)

# 从wsgiref模块导入:
from wsgiref.simple_server import make_server

# 导入自己编写的application函数:
from test_wsgi import application

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print "Serving HTTP on port 8000..."
# 开始监听HTTP请求:
httpd.serve_forever()

# 启动成功后，打开浏览器，输入http://localhost:8000/，就可以看到结果了
