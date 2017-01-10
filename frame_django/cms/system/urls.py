# -*- coding: utf-8 -*-
# @Date:   2016-12-21 17:28:37
# @Last Modified time: 2017-01-03 16:37:52
from django.conf.urls import url, include
from system import views


urlpatterns = [
    # 声明共同的路径前缀，然后include
    # 不能直接把父级、子级写在一起
    # login必须有"/"
    url(r'^login/', include([
        # 使用命名组，传递关键字参数————忽略非命名组————(?P<name>pattern)
        # name————组的名字
        # pattern————匹配模式
        # 没有命名组，传递位置参数————(name)
        # 以上两种情况，Django同时会以关键字参数的方式传递一些额外参到视图函数
        url(r'^(?P<form_name>[a-z]+_[a-z]+|)$', views.LoginView.as_view(), name="login"),
        # 获取邮箱验证码
        url(r'^get_email_code$', views.get_email_code, name='get_email_code'),
    ])),
    url(r'^menu/', include([
        url(r'^$', views.MenuView.as_view(), name="menu"),
        url(r'^get_menu$', views.get_menu, name="get_menu"),
        url(r'^delete', views.delete_menu),
    ]))
]
