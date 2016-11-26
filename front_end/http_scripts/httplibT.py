# coding:utf-8
# httplib是一个相对底层的http请求模块，其上有专门的包装模块，如urllib内建模块，goto等第三方模块，但是封装的越高就越不灵活，比如urllib模块里请求错误时就不会返回结果页的内容，只有头信息，对于某些需要检测错误请求返回值的场景就不适用，所以就得用这个模块了。
# 【httplib模块在Python3.0中已更名为http.client。当你的源代码转换时到3.0时，2to3脚本会自动修改import。】

# 一)
# 1)HTTPConnection类会创建一个https类型的请求实例，并返回一个HTTPConnection对象。
# HTTPConnection(host[, port[, strict[, timeout[, source_address]]]])
# host: 请求的服务器host，不能带http://开头
# strict: 是否严格检查请求的状态行，就是http1.0/1.1 协议版本的那一行，即请求的第一行，默认为False，为True时检查错误会抛异常。
# timeout: 单次请求的超时时间，没有时默认使用httplib模块内的全局的超时时间。

# 2)HTTPSConnection类，HttpConnection的子类，使用SSL与安全服务器通信。默认端口为443。会创建一个https类型的请求实例，并返回一个HTTPSConnection对象。
# HTTPSConnection(host[, port[, key_file[, cert_file[, strict[, timeout[, source_address]]]]]])
# key_file:一个包含PEM格式的私钥文件。
# cert_file:一个包含PEM格式的认证文件。

# 3)HTTPResponse(sock, debuglevel=0, strict=0)实例连接成功之后返回的类，不能由用户实例化。

# 4)HTTPMessage实例用于保存HTTP响应头。它使用mimetools.Message类实现，并提供了处理HTTP头的工具函数。它不能由用户直接实例化。

from httplib import HTTPConnection
conn1 = HTTPConnection('www.baidu.com:80')
conn2 = HTTPConnection('www.baidu.com', 80)
conn3 = HTTPConnection('www.baidu.com', 80, True, 10)
print conn1
print conn2
print conn3

from httplib import HTTPSConnection
conn4 = HTTPSConnection('accounts.google.com', 443)
print conn4

# 二)HTTPConnection对象方法
# 1)conn.request(method, url[, body[, headers]])：发送一个请求，无返回，相对于向服务器发送数据，但是没有最后回车。
#
request1 = conn1.request('GET', '/', '', {'user-agent': 'test'})
print request1

# 2)getresponse方法，获取一个http响应对象，相当于执行最后的2个回车。
response1 = conn1.getresponse()
print response1  # 返回HTTPResponse对象

# 3)close()方法，关闭到服务器的连接。
conn3.close()
print conn1

# 三)HTTPResponse对象方法
# read([amt])：获得http响应的内容部分，即网页源码。amt: 读取指定长度的字符，默认为空，即读取所有内容
# getheader(name[,default])：获得所有的响应头内容，是一个元组列表[(name,value),(name2,value2)]。
# getheaders()获得(header, value)元组的列表
# fileno()获得底层socket文件描述符
# msg，获得头内容
# version，获得头http版本
# status获得返回状态码
# reason获得返回说明

body1 = response1.read()
# print body1
header1 = response1.getheaders()
print header1
# fileno1 = response1.fileno()
# print fileno1
msg1 = response1.msg
print msg1
version1 = response1.version
print version1
status1 = response1.status
print status1
reason1 = response1.reason
print reason1
