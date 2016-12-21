# -*- coding: utf-8 -*-
# @Date:   2016-12-17 23:30:25
# @Last Modified time: 2016-12-17 23:30:50
import views
from django.conf.urls import url, include
urlpatterns = [
]

'''
from django.contrib.auth.decorators import login_required, permission_required
# 在url中使用登录验证、权限验证装饰器
urlpatterns += [
    url(r'^about/', login_required(TemplateView.as_view(template_name="secret.html"))),
    url(r'^vote/', permission_required('polls.can_vote')(VoteView.as_view())),
]
'''
