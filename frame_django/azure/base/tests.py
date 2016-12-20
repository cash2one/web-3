# -*- coding: utf-8 -*-
# @Date:   2016-11-28 12:41:50
# @Last Modified time: 2016-12-04 00:35:23
from django.test import TestCase

# Create your tests here.
#
# test_views
'''
每一个视图总是以一个django.http.HttpRequest实例————request，作为第一个参数。
这是一个触发这个视图、包含当前Web请求信息的对象。

每一个视图功能必须返回一个django.http.HttpResponse实例。
一旦做完，Django将完成剩余的转换Python的对象到一个合适的带有HTTP头和body的Web Response。
'''
from django.http import HttpResponse, HttpResponseRedirect
# redirect 类似HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import Template, Context
from django.template.loader import get_template
from django.core.urlresolvers import reverse


def hello(request):
    # HttpResponse，返回UnicodeStr
    return HttpResponse("<a href='/old_home'>hello django</a>")


def new_home(request):
    # 创建 Template 对象
    tem = Template(
        '<h1>My name is {{ name }},I\'m {{ age }} years old.<a href="/surface_page">more?</a></h1>')
    # Context————上下文对象————类字典对象
    c = Context({'name': 'Django', 'age': 10})
    # render————模板渲染
    # 从Context获取值来替换Template中变量，并执行所有的模板标签
    return HttpResponse(tem.render(c))


def redirect_new(request):
    # 重定向
    # return HttpResponseRedirect('/new_home')
    # reverse(viewname,args=[])
    # return HttpResponseRedirect(reverse('new'))
    return redirect(reverse('new'))


def real_page(request):
    # get_template————使用html模板————views里只认文件，不认路径
    tem = get_template('test/real.html')
    return HttpResponse(tem.render(Context({'name': 'Real'})))


# render_to_response('**.html'[,contextDict])————对get_template()的简单封装
def short(request):
    return render_to_response(
        'test/short.html',
        {"key": "中文"},  # 可选
        #
        # local()————返回一个包含当前作用域里面的所有变量和它们的值的字典
        # 可以替代contextDict以及其它局部变量
        # local()与context互斥
        # context_instance=RequestContext(request)————旧版本，支持{% csrf_token %}、{{STATIC_URL}}
        # context=RequestContext(request)————默认使用TEMPLATE_CONTEXT_PROCESSORS
        # 等价于
        # context_instance=RequestContext(request, processors=[***])
    )


# render不同于new_home()中的render
# render_to_response的一个崭新的快捷方式
# render能够自动将csrf_token添加至上下文中
from django.shortcuts import render


def end(request):
    return render(
        request,
        'test/end.html',
        # {} # 可选的字典参数
    )
