# coding:utf-8
import urllib
import urllib2
import cookielib

filename = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)

userName = raw_input('userName:')
password = raw_input('password:')

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
    'userName': userName,
    'password': password
})

loginUrl = 'http://yun.baidu.com/?ref=PPZQ'

result = opener.open(loginUrl, postdata)
cookie.save(ignore_discard=True, ignore_expires=True)
# 访问另一网址
gradeUrl = 'http://yun.baidu.com/#from=share_yun_logo'
result = opener.open(gradeUrl)
print result.read()
