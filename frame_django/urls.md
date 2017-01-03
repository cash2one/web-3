####设置urls

def foobar_view(request, template_name):
    m_list = MyModel.objects.filter(is_new=True)
    return render_to_response(template_name, {'m_list': m_list})

伪造捕捉到的URLconf值
(r'^mydata/birthday/$', views.my_view, {'month': 'jan', 'day': '06'}),
/mydata/birthday/ ， 这个URL等价于 /mydata/jan/06/。


抽取出代码中共性的东西，共用一个视图函数
urlpatterns = patterns('',
    (r'^events/$', views.object_list, {'model': models.Event}),
    (r'^blog/entries/$', views.object_list, {'model': models.BlogEntry}),
)
# views.py
def object_list(request, model):
    obj_list = model.objects.all()
    #每个Python的类都有一个 __name__ 属性返回类名。
    template_name = 'mysite/%s_list.html' % model.__name__.lower()
    return render_to_response(template_name, {'object_list': obj_list})


硬编码的（额外字典的） id 将优先使用。就是说任何请求（比如， /mydata/2/ 或者 /mydata/432432/ ），不管URL里面能捕捉到什么样的值，都会把id作为3对待。
urlpatterns = patterns('',
    (r'^mydata/(?P<id>\d+)/$', views.my_view, {'id': 3}),
)

urlpatterns = patterns('',
    # ...
    ('^auth/user/add/$', views.user_add_stage),
    ('^([^/]+)/([^/]+)/add/$', views.add_stage),
    # ...
)
利用URLconf从顶向下的解析顺序这个特点，优先处理/auth/user/add/这个特殊情况。
然后处理在URLconf中的一系列URL。


在解析URLconf时，请求方法（例如， POST ， GET ， HEAD ）不会被考虑。换而言之，对于相同的URL的所有请求方法将被导向到相同的函数中。因此根据请求方法来处理分支是视图函数的责任。
#urls
urlpatterns = patterns('',
    # ...
    (r'^somepage/$', views.some_page),
    # ...
) 
#views
def some_page(request):
    if request.method == 'POST':
        do_something_for_post()
        return HttpResponseRedirect('/someurl/')
    elif request.method == 'GET':
        do_something_for_get()
        return render_to_response('page.html')
    else:
        raise Http404()
或者
#urls
urlpatterns = patterns('',
    # ...
    (r'^somepage/$', views.method_splitter, 
    {'GET': views.some_page_get, 'POST': views.some_page_post}),
    # ...
)
#views
def method_splitter(request, GET=None, POST=None):
    if request.method == 'GET'[ and GET is not None]:
        ...
        return GET(request)
    if request.method == 'POST'[ and POST is not None]:
        ...
        return POST(request)
    else:
        ...
        raise Http404
def some_page_get(request):
    assert request.method == 'GET'
    ...
def some_page_get(request):
    assert request.method == 'POST'
    ...

def method_splitter(request, *args, **kwargs):
    get_view = kwargs.pop('GET', None)
    post_view = kwargs.pop('POST', None)
    if request.method == 'GET' and get_view is not None:
        return get_view(request, *args, **kwargs)
    elif request.method == 'POST' and post_view is not None:
        return post_view(request, *args, **kwargs)
    raise Http404


def requires_login(view):
    def new_view(request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/accounts/login/')
        return view(request, *args, **kwargs)
    return new_view
urlpatterns = patterns('',
    (r'^view1/$', requires_login(my_view1)),
    (r'^view2/$', requires_login(my_view2)),
    (r'^view3/$', requires_login(my_view3)),
)
is_authenticated()，检查request.user是否是已经认证的，是的话，当前用户已经成功登陆站点否则就重定向/accounts/login/。
函数requires_login,传入一个视图函数view，然后返回一个新的视图函数new_view。这个新的视图函数new_view在函数requires_login内定义处理request.user.is_authenticated()这个验证，从而决定是否执行原来的view函数。
我们可以在URLconf中很容易的用requires_login来包装实现。


包含其他URLconf
URLconf都可以包含其他URLconf模块，从而让代码用在多个基于Django的站点上。
from django.conf.urls.defaults import *
urlpatterns = patterns('',
    (r'^weblog/', include('mysite.blog.urls'), {'blogid': 3}),
    (r'^photos/', include('mysite.photos.urls')),
    (r'^about/$', 'mysite.views.about'),
)
指向 include()的正则表达式不包含$（字符串结尾匹配符），但是包含了一个斜杆。每当Django遇到include()时，它将截断匹配的URL，并把剩余的字符串发往包含的URLconf作进一步处理。
额外的选项————{'blogid': 3}将总是被传递到被包含的URLconf————mysite.blog.urls中的每一行。