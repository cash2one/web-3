# -*- coding: utf-8 -*-
# @Date:   2016-07-12 13:06:06
# @Last Modified time: 2017-01-04 17:53:58
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
    url(r'^books/(w&#43;)/$', AcmeBookListView.as_view()),
]

from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView


'''
使用session的方法传值

request.session['error_message'] = 'test'
redirect('%s?error_message=test' % reverse('page_index'))

这些方式类似于location刷新，客户端重新指定url
'''


def month_archive(request, year='2006', month='03'):
    return 'success'


def login(request):
    if request.method == 'POST':
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            return HttpResponse("已登录")
        else:
            return HttpResponse("请允许浏览器都接受cookie")
    else:
        raise Http404('Only POSTs are allowed')
    request.session.set_test_cookie()
    return render_to_response('foo/login_form.html')

'''
外键是一对多的模型，如果需要通过OrderProduct查Order可以用select_related，sql使用join来实现的。

问题是需要通过Order查所有的OrderProduct，可以这么写
Order.objects.filter(pk=1).prefetch_related('OrderProduct_set')
prefetch_related的sql语句有2条，第二条会使用到where in，但是不是通过连接


用原生SQL
from django.db import connection
cursor=connection.cursor()
cursor.execute(sql)#这里的SQL就是标准SQL语句


posts_list = Blog.objects.raw('select a.*,b.blog_id,count(*) as count
from biziapp_blog as a left join biziapp_blogfavor as b on  a.id=b.blog_id
  left join biziapp_comment as c on a.id=c.blog_id group by c.blog_id order
 by a.date')
 rawqueryset中至少要有 select a.id（主键）
分页 paginator = Paginator(list(posts_list),8)
'''
