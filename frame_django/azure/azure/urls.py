# -*- coding: utf-8 -*-
# @Date:   2016-11-28 11:03:52
# @Last Modified time: 2016-12-20 18:30:33
#
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from login import urls as login_urls
#
# "r"————正则表达式字符串开头字母————匹配原始字符串，不需要处理"/"（转义符）
# 默认参数值是字符串————因为捕捉的url请求路径总是Unicode str
#
# 查找第一个匹配“请求路径字符”的URLpatterns
# 如果找到匹配，将调用相应的view函数，并把 HttpRequest 对象作为第一个参数
urlpatterns = [
    # django默认的后台管理
    # 默认会重定向多次，变成一个较长的地址
    url(r'^admin/', admin.site.urls),
    # url(r'^admin/', include(admin.site.urls)),
    #
    # RedirectView————url重定向
    # 此处为站点根目录重定向，由于有了拦截器重定向，可以不写
    # url(r'^$', RedirectView.as_view(url='/base/hello')),
    #
    # include————包含其它URLconf，此处r'^'不应有$
    url(r'^base/', include('base.urls')),
    url(r'^forward/', include('forward.urls')),
    url(r'^login/', include(login_urls)),
]

