# -*- coding: utf-8 -*-
# @Date:   2017-01-02 21:55:03
# @Last Modified time: 2017-01-02 21:56:06
#
# 传递额外的参数到视图函数
# url(r'^foo/$', views.foobar_view, {'template_name': 'template1.html'}),
from django.conf.urls import url, include
from django.views.generic import RedirectView

import demo_redirect
from demo_redirect import page1, page2, page3, page4
from demo_response import _str, template_str, template_file, render_html

urlpatterns = [
    url(r'^test/', include([
        url(r'^_str', _str),
        url(r'^template_str', template_str),
        url(r'^template_file', template_file),
        url(r'^render_html', render_html),

        url(r'^page1', page1),                                   # 在views中重定向
        url(r'^page2', page2),
        url(r'^page3', page3, name='page3'),
        url(r'^page4', page4, name='page4'),                     # 使用name重定向

        url(r'^page5', RedirectView.as_view(url='/test/page')),  # RedirectView————url重定向

        url(r'^page', demo_redirect.real_page),
    ]))
]
