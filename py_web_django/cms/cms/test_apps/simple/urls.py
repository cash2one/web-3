# -*- coding: utf-8 -*-
# @Date:   2017-01-02 21:55:03
# @Last Modified time: 2017-01-02 21:56:06
#
# 传递额外的参数到视图函数
# url(r'^foo/$', views.foobar_view, {'template_name': 'template1.html'}),
from django.conf.urls import url, include
from django.views.generic import RedirectView

from demo_response import _str, _template, _get_template, _render_to_response, _render
from demo_redirect import page1, page2, page3, page4

urlpatterns = [
    url(r'^test/', include([
        url(r'^_str', _str),
        url(r'^_template', _template),
        url(r'^_get_template', _get_template),
        url(r'^_render_to_response', _render_to_response),
        url(r'^_render', _render),

        url(r'^page1', page1),                                     # 在views中重定向
        url(r'^page2', page2),
        url(r'^page3', page3, name='page3'),
        url(r'^page4', page4, name='page4'),                       # name用于重定向等

        # url(r'^surface_page', RedirectView.as_view(url='/test/real_page')),  # RedirectView————url重定向
        # url(r'^short', tests.short),
    ]))
]
