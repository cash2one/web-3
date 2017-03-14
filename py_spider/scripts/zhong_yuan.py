# -*- coding: utf-8 -*-
# @Date:   2017-03-14 17:38:55
# @Last Modified time: 2017-03-14 17:39:01
from __future__ import division
import logging

logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='error.log',
    filemode='a')

starturl = [
    "http://bj.centanet.com/xiezilou/chuzu/",
    "http://sh.centanet.com/xiezilou/chuzu/"
]


def process(p):
    if p.isDefaultLevel():
        xpath = p.HtmlSelector().xpath

        url_lists = xpath("//div[@class='page']/a/@href").textall()
        for url in url_lists:
            p.addurl(url, level="")

        url_details = xpath(
            "//dl[@class='detail fl']/dt[@class='fyahei']/h2/a/@href").textall()
        for url in url_details:
            p.addurl(url, level="xiangqingye")

    elif p.isLevel("xiangqingye"):
        xpath = p.HtmlSelector().xpath
        name = xpath("//div[@class='navcon']/i/text()").text().strip()
        price = xpath(
            "//div[@class='topbase_cont fr']/ul[1]/li[1]/span[@class='cRed f18 mr6']/b/text()").text().strip()
        area = xpath(
            "//div[@class='topbase_cont fr']/ul[1]/li[2]/span[@class='f000 txt_r']/text()").text().strip("平米 ")

        if p.getUrl().startswith("http://bj.centanet.com/"):
            city = "北京"
            floor = xpath(
                "//div[@class='topbase_cont fr']/ul[2]/li[3]/span[@class='f000 txt_r']/text()").text().strip()
            zx = xpath(
                "//div[@class='topbase_cont fr']/ul[2]/li[5]/span[@class='f000 txt_r']/text()").text().strip()
        else:
            city = "上海"
            floor = xpath(
                "//div[@class='topbase_cont fr']/ul[2]/li[2]/span[@class='f000 txt_r']/text()").text().strip()
            zx = xpath(
                "//div[@class='topbase_cont fr']/ul[2]/li[3]/span[@class='f000 txt_r']/text()").text().strip()

        keyid = p.getUrl().split("/")[-1].split(".")[0]
        if name and price and area and floor and zx:
            try:
                price_month = '%.2f' % (float(price) * float(area) * 30)
                p.put({
                    "keyid": keyid,
                    "price_month": price_month
                })
            except Exception, e:
                print e
                logging.error("price=%s, area=%s, %s" % (price, area, e))
            finally:
                p.put({
                    "keyid": keyid,
                    "city": city,
                    "name": name,
                    "price": price,
                    "area": area,
                    "floor": floor,
                    "zx": zx
                })
        else:
            print "field is not complete"
            logging.error("%s, %s, %s, %s, %s, %s" %
                          (p.getUrl(), name, price, area, floor, zx))
