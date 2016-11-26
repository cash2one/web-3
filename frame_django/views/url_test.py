# -*- coding: utf-8 -*-
# @Date:   2016-10-11 16:00:54
# @Last Modified time: 2016-10-12 11:55:53
'''
松耦合原则————一个重要的保证互换性的软件开发方法。
决定URL返回哪个视图函数和实现这个视图函数是在两个不同的地方。
这使得开发人员可以修改一块而不会影响另一块。
'''

from django.conf.urls import url
from django.conf.urls import patterns  # 旧版需要
from django.contrib import admin
from mysite import views
from mysite.views import ***
#
# 请求路径字符的捕获值 -> Unicode str
# "r"————正则表达式字符串的开头字母————匹配原始字符串，不需要处理里面的"/"（转义字符）
# 根目录的URL模式————"^$"，代表一个空字符串
#
# Django在URLconf中的所有URL模式中，查找第一个匹配【请求路径字符】的URLpatterns。
# 如果找到匹配，将调用相应的view函数，并把 HttpRequest 对象作为第一个参数。
urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
# 使用多个视图前缀
urlpatterns += patterns(
    url(r'^$', ***)
    url(r'test1', view.***)
    url(r'test', 'mysite.views.***')  # 注意引号
)

# 调试模式中的特例————DEBUG为 True 时才有效
if settings.DEBUG:
    urlpatterns += patterns(
        (
            # 使用命名组，传递关键字参数
            # 命名组和非命名组不能同时存在于同一个URLconf中
            # 如果有任何命名的组，Django会忽略非命名组而直接使用命名组
            # 否则，Django会把所有非命名组以位置参数的形式传递
            # 在以上的两种情况，Django同时会以关键字参数的方式传递一些额外参数
            #
            # 默认参数值是字符串，不是整数。
            # 这是为了保持一致，因为捕捉的值总是字符串。
            r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/$',
            views.month_archive
        ),  # 注意逗号
        # 传递额外的参数到视图函数
        (r'^foo/$', views.foobar_view, {'template_name': 'template1.html'}),
    )
