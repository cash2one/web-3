# -*- coding: utf-8 -*-
# @Date:   2017-02-24 21:22:44
# @Last Modified time: 2017-03-01 15:30:36
import re
import urllib


def getHtml(url):
    """
    传递一个网址，把整个页面下载下来
    """
    page = urllib.urlopen(url)
    html = page.read()
    return html


def getImg(html):
    """
    获取的整个页面中筛选需要的图片连接
    """
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)           # 生成一个匹配对象
    img_list = re.findall(imgre, html)
    # print imglist
    for i, imgurl in enumerate(img_list):
        """
        遍历获取的图片连接，重命名，保存
        """
        try:
            x = urllib.urlretrieve(imgurl, 'images/%s.jpg' % i)
        except Exception as e:
            print imgurl


html = getHtml("http://tieba.baidu.com/p/2460150866")
getImg(html)
