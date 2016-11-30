# -*- coding: utf-8 -*-
# @Date:   2016-10-11 11:31:13
# @Last Modified time: 2016-11-29 18:44:29
from django.template.loader import get_template
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

# #
# # context处理器
# # 接收一个 HttpRequest对象，返回一个字典
# return {
#     'app': 'My app',
#     'user': request.user,
#     'ip_address': request.META['REMOTE_ADDR']
# }


def custom_pros(request):  # context处理器
    return {'age': 22, 'user': request.user}


def test5(request):
    tem = loader.get_template('template1.html')
    c = RequestContext(
        request,
        {'message': 'I am view 1.'},
        processors=[custom_proc]
    )
    return tem.render(c)


'''
我们甚至可以使用session的方法传值


request.session['error_message'] = 'test'
redirect('%s?error_message=test' % reverse('page_index'))

这些方式类似于location刷新，客户端重新指定url
'''


# print timezone.localtime(timezone)


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