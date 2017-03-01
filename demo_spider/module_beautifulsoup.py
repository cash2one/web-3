# -*- coding: utf-8 -*-
# @Date:   2017-02-27 17:41:35
# @Last Modified time: 2017-02-27 17:49:59
#
# pip install beautifulsoup
# 处理不规范的html的能力比lxml.etree强
from BeautifulSoup import BeautifulSoup
from demo_html import html


soup = BeautifulSoup(html)
