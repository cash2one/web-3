# -*- coding: utf-8 -*-
# @Date:   2016-10-10 14:36:54
# @Last Modified time: 2016-10-10 14:49:09
import re
#
# 设置根URLconf
#
ROOT_URLCONF = 'djj_test.urls'
#
# 不需要在每个URL后添加斜杠
#
APPEND_SLASH = False
#
# 是否自动添加www
#
PREPEND_WWW = False
#
# 设置哪些域名可以访问
#
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
#
# 不允许访问的客户端————反爬虫
#
DISALLOWED_USER_AGENTS = [
    re.compile(r'^NaverBot.*'),
    re.compile(r'^EmailSiphon.*'),
    re.compile(r'^SiteSucker.*'),
    re.compile(r'^sohu-search')
]
ABSOLUTE_URL_OVERRIDES = {}
ALLOWED_INCLUDE_ROOTS = []
#
# 404异常不报错的url
#
IGNORABLE_404_URLS = [
    re.compile(r'^/apple-touch-icon.*\.png$'),
    re.compile(r'^/favicon.ico$'),
    re.compile(r'^/robots.txt$'),
    re.compile(r'^/phpmyadmin/'),
    re.compile(r'\.(cgi|php|pl)$'),
]
