# -*- coding: utf-8 -*-
# @Date:   2016-07-12 13:06:09
# @Last Modified time: 2017-02-26 17:25:13
import re
import json
from scrapy.selector import Selector

from scrapy.spiders import Spider
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.sgml import SgmlLinkExtractor as sle
from demo_scrapy.items import *
from demo_scrapy.misc.log import *


class JobSpider(CrawlSpider):
    name = "job"                                         # 项目启动名称（scrapy crawl job）
    allowed_domains = ["tencent.com"]                    # 搜索的域名范围
    start_urls = ["http://hr.tencent.com/position.php"]  # 起始url
    # 定义爬取URL的规则
    rules = [
        Rule(
            sle(allow=("/position.php\?&start=\d{,4}#a")), follow=True, callback='parse')
    ]

    def parse(self, response):
        """
        """
        items = []
        base_url = get_base_url(response)
        # print base_url
        sel = Selector(response)
        """
        实例化一个Selector对象，提取数据到Items里面
        Selector.xpath(xpath表达式)————返回该表达式所对应的所有节点的selector list列表
        Selector.css(CSS表达式)————————返回该表达式所对应的所有节点的selector list列表
        Selector.extract()—————————————序列化该节点为unicode字符串并返回list
        Selector.re(正则表达式)————————返回unicode字符串list列表
        """
        tr_even_list = sel.css('table.tablelist tr.even')
        tr_odd_list = sel.css('table.tablelist tr.odd')
        # print tr_even_list
        # print tr_odd_list
        tr_list = tr_even_list + tr_odd_list
        for site in tr_list:
            item = JobItem()
            item['name'] = site.css('.l.square a').xpath('text()').extract()
            relative_url = site.css('.l.square a').xpath('@href').extract()[0]
            item['detailLink'] = urljoin_rfc(base_url, relative_url)
            item['catalog'] = site.css('tr > td:nth-child(2)::text').extract()
            item['workLocation'] = site.css(
                'tr > td:nth-child(4)::text').extract()
            item['recruitNumber'] = site.css(
                'tr > td:nth-child(3)::text').extract()
            item['publishTime'] = site.css(
                'tr > td:nth-child(5)::text').extract()
            items.append(item)
            # print repr(item).decode("unicode-escape") + '\n'
        warn('process' + str(response))
        return items

    def _process_request(self, request):
        info('process' + str(request))
        return request
