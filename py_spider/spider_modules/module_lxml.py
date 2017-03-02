# -*- coding: utf-8 -*-
# @Date:   2016-07-12 13:06:09
# @Last Modified time: 2017-03-01 16:54:15
import lxml.html
import lxml.html.soupparser as soupparser
from lxml import etree
from demo_html import html
from module_urllib2 import DemoUrllib2


doc = lxml.html.fromstring(html.decode('utf-8'))  # HtmlElement
text_list = doc.xpath(
    u'//td[@style="padding‐bottom: 5px;" and @nowrap="" and not(@align="right")]/text()')
print text_list, type(text_list)
for i in text_list:
    print i.encode('utf-8'),


def ppk(num):
    # url = 'http://www.qiushibaike.com/hot/page/%s?s=4827870' % num
    url = 'http://www.qiushibaike.com/hot/page/%s' % num
    headers = {
        'Referer': 'http://www.qiushibaike.com/hot/page/3',
        'content-type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
    }
    d = DemoUrllib2(url, {'s': 4827870})
    r = d.send_get()
    content = etree.HTML(r.read())

    img = content.xpath('//img')
    for i in img:
        alls = i.attrib
        name = alls['alt']
        url = alls['src']
        urllib.urlretrieve(url, '%s.jpg' % name)


def main():
    for i in range(100):
        try:
            ppk(i)
        except:
            pass

if __name__ == '__main__':
    main()
