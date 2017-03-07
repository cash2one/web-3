# -*- coding: utf-8 -*-
# @Date:   2016-12-22 21:14:08
# @Last Modified time: 2017-03-07 14:06:22
#
"""
"r"————正则表达式字符串开头字母————匹配原始字符串，不处理"/"转义符
默认参数值是字符串————因为捕捉的url请求路径总是Unicode str

查找第一个匹配“请求路径字符”的URLpatterns
如果找到匹配，将调用相应的view函数，并把 HttpRequest 对象作为第一个参数
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from cms.test_apps.system import urls as system_urls
from cms import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),                       # django默认的后台管理（会重定向多次，变成一个长地址）
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(url='/system/login')),  # 重定向（如果有了拦截器重定向，可以不写）站点根目录URL（"^$"，代表一个空字符串）
]

"""
DEBUG == True————调试模式
isTest == True————个人测试
"""
isTest = True
if settings.DEBUG and isTest:
    """
    include————包含其它URLconf，此处r'^'不应有$
    """
    urlpatterns += [
        url(r'^', include('cms.test_apps.simple.urls'))
    ]
else:
    urlpatterns += [
        url(r'^system/', include(system_urls))
    ]
