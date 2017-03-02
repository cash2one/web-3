# coding:utf-8
# urllib2 默认会使用环境变量 http_proxy 来设置 HTTP Proxy。假如一个网站它会检测某一段时间某个IP
# 的访问次数，如果访问次数过多，它会禁止你的访问。所以你可以设置一些代理服务器来帮助你做工作，每隔一段时间换一个代理，网站君都不知道是谁在捣鬼了，这酸爽！
import urllib
import urllib2
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http": 'www.baidu.com'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
    # opener = urllib2.build_opener(proxy_handler,urllib2.HTTPHandler(debuglevel=1))
    # urllib2.HTTPHandler(debuglevel=1)打开 Debug Log ，这样收发包的内容就会在屏幕上打印出来，方便调试
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)


values = {}
values['username'] = "1016903103@qq.com"
values['password'] = "XXXX"
data = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login"
geturl = url + "?" + data
request = urllib2.Request(geturl)
# request.get_method = lambda: 'PUT' # or 'DELETE' # 使用 HTTP PUT 和 DELETE
# 捕获相应的异常
try:
    response = urllib2.urlopen(request)
    print response.read()
except urllib2.HTTPError, e:  # 子类
    print e.code
except urllib2.URLError, e:  # 父类，写在后
    # print e.code, e.reason
    # 加入 hasattr属性提前对属性进行判断
    if hasattr(e, 'code'):
    	print e.code
    if hasattr(e, 'reason'):
    	print e.reason
except Exception, e:
    print e
else:
    print 'OK'
