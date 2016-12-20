# -*- coding: utf-8 -*-
# @Date:   2016-07-12 13:06:06
# @Last Modified time: 2016-10-11 15:27:08
#
# 为了给所有的Publisher建立一个列表页，我们将按照这样的方式来配置URLconf:
from django.conf.urls import patterns, url
from django.views.generic import PublisherDetailView, AcmeBookListView
from books.models import Publisher


urlpatterns = patterns[
    url(r'^publishers/$',
        # 如果仅仅修改类视图中少量简单的属性，可以直接传递新的属性到类本身调用 as_view 方法中
        PublisherDetailView.as_view(
            model=Publisher,
            template_name="publisher_list.html",
            context_object_name="book_list"
        )),
   url(r'^books/(w&#43;)/$',AcmeBookListView.as_view()),
]

