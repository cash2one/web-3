# -*- coding: utf-8 -*-
# @Date:   2017-03-07 22:20:40
# @Last Modified time: 2017-03-07 22:21:17
"""
每一个视图总是以一个django.http.HttpRequest实例（触发当前视图、包含Web请求信息）作为第一个参数
每一个视图功能必须返回一个django.http.HttpResponse实例
一旦做完，Django将完成剩余的转换Python的对象到一个合适的带有HTTP头和body的Web Response
"""
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.template import Template, Context
from django.template.loader import get_template


def _str(request):
    """
    HttpResponse
    返回UnicodeStr
    """
    return HttpResponse("<h3><a href='/test/_temple'>django _str</a></h3>")


def _template(request):
    """
    Template 对象
    Context  上下文对象（类字典）
    render() 模板渲染（用Context值替换模板标签中的变量）
    """
    tem = Template("<h3><a href='/test/ha'>{{ name }} _template</a></h3>")
    c = Context({'name': 'Django'})
    return HttpResponse(tem.render(c))


def _get_template(request):
    """
    get_template()
    使用html模板
    """
    tem = get_template('get_template.html')
    return HttpResponse(tem.render(Context({'name': 'get_template'})))


def _render_to_response(request):
    """
    render_to_response('**.html'[, context])
    对get_template()的简单封装
    """
    return render_to_response(
        'render_to_response.html',
        {"name": "render_to_response"},
        # processors=[***],
        #
        # local()————返回一个包含当前作用域里面的所有变量和它们的值的字典————与context互斥————可替代contextDict及其它局部变量
        #
        # context_instance=RequestContext(request)————旧版本，支持{% csrf_token %}、{{STATIC_URL}}
        # context=RequestContext(request[,
        # processors=[***]])————默认使用TEMPLATE_CONTEXT_PROCESSORS
    )


def _render(request):
    """
    render('**.html'[,contextDict])
    render_to_response的短函数，默认携带csrf_token
    """
    return render(
        request,
        'render.html',
    )
