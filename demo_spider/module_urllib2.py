# -*- coding: utf-8 -*-
# @Date:   2016-07-12 13:06:09
# @Last Modified time: 2017-03-01 16:52:26
#
import urllib
import urllib2


class DemoUrllib2(object):
    """docstring for DemoUrllib2"""

    def __init__(self, url, data, headers=None):
        if headers:
            self.headers = headers
        else:
            self.headers = {
                'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
                'Referer': url
            }
        self.url = url
        self.data = urllib.urlencode(data)  # 转化字典为username=***&...
        self.timeout = 10

    def send_post(self):
        '''
        发送POST请求
        '''
        request = urllib2.Request(
            self.url, data=self.data, headers=self.headers)
        response = urllib2.urlopen(request, timeout=self.timeout)
        # print response.headers.values()
        return response.read()

    def send_get(self):
        '''
        发送GET请求
        '''
        geturl = self.url + "?" + self.data
        request = urllib2.Request(geturl, headers=self.headers)
        response = urllib2.urlopen(request, timeout=self.timeout)
        # print response.headers.values()
        return response.read()


if __name__ == '__main__':
    url = "http://passport.csdn.net/account/login"
    # url = 'http://www.zhihu.com'
    data = {
        'username': "1016903103@qq.com",
        'password': "XXXX"
    }
    d = DemoUrllib2(url, data)
    d.send_get()
    # d.send_post()
