# coding:utf-8
# 飘逸的python -- 用urlparse从url中抽离出想要的信息
from urlparse import urlparse
# 1)urlunparse，url重构，丢弃url多余的部分
url = 'https://www.baidu.com/baidu?tn=monline_3_dg&ie=utf-8&wd=urlparse'
parsed = urlparse(url)
print parsed
print parsed.scheme
##
print parsed.hostname
print parsed.netloc
print parsed.hostname == parsed.netloc
##
print parsed.port
print parsed.path
print parsed.query
print parsed.fragment

# 2)urlsplit，urlsplit比urlparse的数组少了一项params
from urlparse import urlsplit
splited = urlsplit(url)
print splited

# 3)geturl，结果为原url
print parsed.geturl()
print splited.geturl()

# 4)urlunparse，url重构，丢弃url多余的部分
from urlparse import urlunparse
print urlunparse(parsed)
# print urlunparse(splited) # 报错

# 5)urljoin
from urlparse import urljoin
print urljoin(url, 'another.html')
print urljoin(url, '/another.html')
print urljoin(url, '.../another.html')