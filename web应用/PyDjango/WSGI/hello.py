# coding:utf-8

#(1)


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])  # (2)
    return '<h1>Hello, web!</h1>'  # (3)
    # return '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')  # 4

'''
(1)application()函数就是符合WSGI标准的一个HTTP处理函数，它接收两个参数：
environ：一个包含所有HTTP请求信息的dict对象；
start_response：一个发送HTTP响应的函数。


(2)start_response()发送了HTTP响应的Header。
【Header只能发送一次，也就是只能调用一次start_response()函数】
start_response()函数接收两个参数：
    一个是HTTP响应码；
    一个是一组list表示的HTTP Header。
每个Header用一个包含两个str的tuple表示。
通常情况下，都应该把Content-Type头发送给浏览器。其他很多常用的HTTP Header也应该发送。


(3)函数的返回值'<h1>Hello, web!</h1>'将作为HTTP响应的Body发送给浏览器。'


(4)Web应用可以稍微改造一下，从environ里读取PATH_INFO，这样可以显示更加动态的内容：
可以在地址栏输入用户名作为URL的一部分，将返回Hello, xxx!
'''