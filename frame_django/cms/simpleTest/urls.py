# -*- coding: utf-8 -*-
# @Date:   2017-01-02 21:55:03
# @Last Modified time: 2017-01-02 21:56:06
#
# 传递额外的参数到视图函数
# url(r'^foo/$', views.foobar_view, {'template_name': 'template1.html'}),
from django.conf.urls import url, include
from azure import settings
from base import tests
from base.tests import hello
from django.views.generic import RedirectView
import views

# 邮箱验证码登录测试
urlpatterns = [
    # test必须有/
    url(r'^test/', include([
        url(r'^test_form', views.test_form),
        url(r'^test_login', views.LoginView.as_view()),
        url(r'^getcode', views.login_email_validate)
    ]))
]
#######################################
# 调试模式特例————DEBUG为True时才有效
# 个人测试————isTest为True时才有效
#######################################
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
