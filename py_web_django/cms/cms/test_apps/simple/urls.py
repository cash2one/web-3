# -*- coding: utf-8 -*-
# @Date:   2017-01-02 21:55:03
# @Last Modified time: 2017-01-02 21:56:06
#
# 传递额外的参数到视图函数
# url(r'^foo/$', views.foobar_view, {'template_name': 'template1.html'}),
from django.conf.urls import url, include
from django.views.generic import RedirectView

import tests
from tests import hello

urlpatterns = [
    url(r'^test/', include([
        url(r'^$', hello),
        url(r'^old_home', tests.redirect_new),                               # 在views中重定向

        url(r'^new_home', tests.new_home, name='new'),                       # name用于重定向等
        url(r'^real_page', tests.real_page),

        url(r'^surface_page', RedirectView.as_view(url='/test/real_page')),  # RedirectView————url重定向
        url(r'^short', tests.short),
        url(r'^end', tests.end)
    ]))
]
