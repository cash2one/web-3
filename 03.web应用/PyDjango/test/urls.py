# coding:utf-8
# 为了给所有的Publisher建立一个列表页，我们将按照这样的方式来配置URLconf:
from django.conf.urls import patterns, url
from django.views.generic import PublisherDetailView, AcmeBookListView
from books.models import Publisher
urlpatterns = patterns('',
                       url(r'^publishers/$',
                           PublisherDetailView.as_view(model=Publisher,
                                                       template_name="publisher_list.html",
                                                       context_object_name="book_list"
                                                       )),
                       url(r'^books/(w&#43;)/$',
                           AcmeBookListView.as_view()),
                       )
# 把URL指向 as_view 这个类方法来替代类本身，这是类视图的入口点
# 如果你仅仅修改类视图中少量简单的属性，你可以直接传递新的属性 到类本身调用 as_view 方法中
# 通用视图将所有相关Model的查询到的对象放到object_list变量中，这虽然能正常工作，但是对模板设计者不友好。我们应该使用context_object_name来指定上下文(context)变量。

'''
<ul>
{% for publisher in object_list %} 
	<li>{{ publisher.name }}</li>
{% endfor %}
</ul>
'''
