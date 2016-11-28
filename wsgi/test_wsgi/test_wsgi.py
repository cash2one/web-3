# -*- coding: utf-8 -*-
# @Date:   2016-07-12 13:06:06
# @Last Modified time: 2016-11-28 18:59:02
#
# 测试uwsgi————通过uwsgi运行该文件
# uwsgi --http :8001 --wsgi-file test.py
# 通过浏览器访问localhost


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])  # (2)
    return '<h1>Hello, web!</h1>'  # (3)
    # return ['<html><body>Hello world!</body></html>']
    # return [b"Hello World"]
    # return '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')  # 4


'''
application()函数就是符合WSGI标准的一个HTTP处理函数，它接收两个参数：
environ：一个包含所有HTTP请求信息的dict对象；
start_response：一个发送HTTP响应的函数，加上application函数返回值作为Body。


(2)start_response()发送了HTTP响应的Header————只能发送一次，也就是只能调用一次start_response()函数
start_response()函数接收两个参数：
    一个是HTTP响应码；
    一个是一组list表示的HTTP Header。
每个Header用一个包含两个str的tuple表示。
通常情况下，都应该把Content-Type头发送给浏览器。其他很多常用的HTTP Header也应该发送。


(3)函数的返回值'<h1>Hello, web!</h1>'将作为HTTP响应的Body发送给浏览器。'


(4)Web应用可以稍微改造一下，从environ里读取PATH_INFO，这样可以显示更加动态的内容：
可以在地址栏输入用户名作为URL的一部分，将返回Hello, xxx!
'''

# 无论多么复杂的Web应用程序，入口都是一个WSGI处理函数。

# 有了WSGI，我们关心的就是如何从environ这个dict对象拿到HTTP请求信息，然后构造HTML，通过start_response()发送Header，最后返回Body。

# 整个application()函数本身没有涉及到任何解析HTTP的部分，也就是说，底层代码不需要我们自己编写，我们只负责在更高层次上考虑如何响应请求就可以了。

# application()函数如果我们自己调用，两个参数environ和startt_response我们没法提供，返回的str也没法发给浏览器。所以application()函数必须由WSGI服务器来调用。有很多符合WSGI规范的服务器，我们可以挑选一个来用。

# Python内置了一个WSGI服务器，这个模块叫wsgiref，它是用纯Python编写的WSGI服务器的参考实现。所谓“参考实现”是指该实现完全符合WSGI标准，但是不考虑任何运行效率，仅供开发和测试使用。
