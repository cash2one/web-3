# -*- coding: utf-8 -*-
# @Date:   2016-11-28 11:03:52
# @Last Modified time: 2016-12-20 18:30:33
#
"""
https://docs.djangoproject.com/en/1.10/topics/http/urls/
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from focus import urls as focus_urls
#
# "r"————正则表达式字符串的开头字母————匹配原始字符串，不需要处理"/"（转义符）
# 默认参数值是字符串————这是为了保持一致，因为捕捉的url请求路径总是字符串（Unicode str）
#
# 查找第一个匹配【请求路径字符】的URLpatterns
# 如果找到匹配，将调用相应的view函数，并把 HttpRequest 对象作为第一个参数
urlpatterns = [
    # django默认的后台管理————默认会重定向多次，变成一个较长的地址
    url(r'^admin/', admin.site.urls),
    #
    # RedirectView————url重定向
    # 此处为站点根目录重定向，由于有了拦截器重定向，可以不写
    # url(r'^$', RedirectView.as_view(url='/base/login')),
    #
    # 包含其它URLconf，此处r'^'不应有$
    url(r'^base/', include('base.urls')),
    url(r'^forward/', include('forward.urls')),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^focus/', include(focus_urls)),
]
#
#
#
import settings
from base import tests
from base.tests import hello
from django.views.generic import RedirectView
#
# 调试模式特例————DEBUG 为 True 时才有效
# 个人测试————isTest
isTest = False
if settings.DEBUG and isTest:
    urlpatterns += [
        # 根目录的URL————"^$"，代表一个空字符串
        url(r'^$', hello),
        # 在views中重定向
        url(r'^old_home', tests.redirect_new),
        # name用于重定向等
        url(r'^new_home', tests.new_home, name='new'),
        url(r'^real_page', tests.real_page),
        # 在url中重定向
        url(r'^surface_page', RedirectView.as_view(url='/real_page')),
        url(r'^short', tests.short),
        url(r'^end', tests.end)
    ]
# from django.conf.urls import patterns
# urlpatterns += patterns(***)————旧版本
