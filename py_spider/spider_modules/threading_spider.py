# -*- coding: utf-8 -*-
# @Date:   2017-03-02 13:33:36
# @Last Modified time: 2017-03-07 09:23:48
import urllib2
import time
import threading
from threading import Thread


class GetUrlThread(Thread):

    def __init__(self, url):
        self.url = url
        super(GetUrlThread, self).__init__()

    def run(self):
        """
        子线程全局变量————每个子线程各自独立
        """
        g = None
        if threading.currentThread().name == 'Thread-1':
            g = 10
            global g
        print threading.currentThread().name, g
        """
        通过实例来创建线程
        类变量是共享的
        实例变量是互不影响的
        """
        try:
            resp = urllib2.urlopen(self.url)
            print self.url, resp.getcode()
        except Exception as e:
            print self.url, e


def simple_spider(urls):
    """
    单线程爬虫
    url顺序的被请求
    除非cpu从一个url获得了回应，否则不会去请求下一个url
    """
    """
    g = 10
    global g
    主线程全局变量，所有子线程共享
    """
    for url in urls:
        try:
            resp = urllib2.urlopen(url)
            print url, resp.getcode()
        except Exception as e:
            print url, e


def threading_spider(urls):
    """
    多线程爬虫
    等待一个线程内的网络请求返回时，cpu可以切换到其他线程去进行网络请求
    """
    threads = []
    for url in urls:
        t = GetUrlThread(url)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


def get_responses(is_simple=True):
    urls = [
        'http://www.google.com',
        'http://www.amazon.com',
        'http://www.ebay.com',
        'http://www.alibaba.com',
        'http://www.reddit.com'
    ]
    start = time.time()
    simple_spider(urls) if is_simple else threading_spider(urls)
    end = time.time()
    print end - start

if __name__ == '__main__':
    # get_responses()
    # print("-" * 20)
    get_responses(is_simple=False)
