# -*- coding: utf-8 -*-
# @Date:   2017-01-02 20:06:42
# @Last Modified time: 2017-01-10 14:57:09

from django.test import TestCase

# Create your tests here.
"""
每一个视图总是以一个django.http.HttpRequest实例————request，作为第一个参数。
这是一个触发这个视图、包含当前Web请求信息的对象。

每一个视图功能必须返回一个django.http.HttpResponse实例。
一旦做完，Django将完成剩余的转换Python的对象到一个合适的带有HTTP头和body的Web Response。
"""
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import Template, Context
from django.template.loader import get_template
from django.core.urlresolvers import reverse


def hello(request):
    # HttpResponse，返回UnicodeStr
    return HttpResponse("<a href='/test/old_home'>hello django</a>")


def new_home(request):
    # 创建 Template 对象
    tem = Template('<h1><a href="/test/surface_page">{{ name }}?</a></h1>')
    # Context————上下文对象————类字典对象
    c = Context({'name': 'Django'})
    # render————模板渲染————用Context值替换模板标签中的变量
    return HttpResponse(tem.render(c))


def redirect_new(request):
    """
    重定向
    return HttpResponseRedirect('/new_home')
    return HttpResponseRedirect(reverse(viewname, args=[]))
    """
    return redirect(reverse('new'))


def real_page(request):
    # get_template————使用html模板
    tem = get_template('real.html')
    return HttpResponse(tem.render(Context({'name': 'Real'})))


# render_to_response('**.html'[,contextDict])————对get_template()的简单封装
def short(request):
    return render_to_response(
        'short.html',
        {"key": "中文"},
        # processors=[***],
        #
        # local()————返回一个包含当前作用域里面的所有变量和它们的值的字典————与context互斥————可替代contextDict及其它局部变量
        #
        # context_instance=RequestContext(request)————旧版本，支持{% csrf_token %}、{{STATIC_URL}}
        # context=RequestContext(request[,
        # processors=[***]])————默认使用TEMPLATE_CONTEXT_PROCESSORS
    )


from django.shortcuts import render


# render('**.html'[,contextDict])————render_to_response的短函数————默认携带csrf_token
def end(request):
    return render(
        request,
        'end.html',
    )
