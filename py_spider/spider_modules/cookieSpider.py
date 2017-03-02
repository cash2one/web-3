# -*- coding: utf-8 -*-
# @Date:   2016-07-12 13:06:09
# @Last Modified time: 2017-02-22 15:32:29
#
# cookielib模块的主要作用是提供可存储cookie的对象，以便于与urllib2模块配合使用来访问Internet资源。该模块主要的对象有CookieJar、FileCookieJar、MozillaCookieJar、LWPCookieJar。
# cookie模块很有用，有些网站必须登录了以后才能访问url，这时候就必须cookielib出马了。
import urllib2
import cookielib
'''
# 声明一个CookieJar对象实例来保存cookie。CookieJar类的对象用来捕获cookie并在后续连接请求时重新发送，比如可以实现模拟登录功能。
cookie = cookielib.CookieJar()
'''
# FileCookieJar对象（MozillaCookieJar是其子类），将cookie保存到文件中
filename = 'cookie.txt'  # 设置cookie的保存文件（同目录下）
cookie = cookielib.MozillaCookieJar(filename)


# 利用urllib2的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
# 通过handler来构建opener
opener = urllib2.build_opener(handler)
response = opener.open('http://www.baidu.com')  # 此处等同于urllib.urlopen方法
'''
for item in cookie:
	print 'Name = ' + item.name
	print 'Value = ' + item.value
'''

cookie.save(ignore_discard=True, ignore_expires=True)
# ignore_discard的意思是即使cookies将被丢弃也将它保存下来，
# ignore_expires的意思是覆盖写入


# 从文件中读取cookie内容到变量
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
request = urllib2.Request('http://www.baidu.com')
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

'''
不install_opener，直接用opener的open函数来访问url
'''
response = opener.open(request)
'''
response也可以这样：
urllib2.install_opener(opener)
response = urllib2.urlopen(request).read()
'''
print response.read()
