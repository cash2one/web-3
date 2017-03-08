# -*- coding: utf-8 -*-
# @Date:   2017-03-07 22:20:40
# @Last Modified time: 2017-03-07 22:21:17
"""
每一个视图总是接收一个django.http.HttpRequest实例（触发当前视图、包含Web请求信息）作为第一个参数
每一个视图必须返回一个django.http.HttpResponse实例，转换Python对象到一个合适的带有HTTP头和body的Web Response
"""
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.template import Template, Context
from django.template.loader import get_template


def _str(request):
    """
    class HttpResponse()
    返回UnicodeStr
    __init__(self, content='', *args, **kwargs)
    """
    return HttpResponse("<h3><a href='/test/template_str'>template_str</a></h3>")


def template_str(request):
    """
    class Template()
    __init__(self, template_string, origin=None, name=None, engine=None)
    Context  上下文对象（类字典）
    render() 模板渲染（用Context值替换模板标签中的变量）
    """
    tem = Template("<h3><a href='/test/template_file'>{{ name }} template_file</a></h3>")
    c = Context({'name': 'Django'})
    return HttpResponse(tem.render(c))


def template_file(request):
    """
    django.template.loader.get_template(template_name, using=None)
    Raises TemplateDoesNotExist if no such template exists.
    """
    tem = get_template('template_file.html')
    return HttpResponse(tem.render(Context({'name': 'template_file'})))


def render_html(request):
    """
    django.shortcuts.render_to_response(template_name, context=None, content_type=None, status=None, using=None)
    django.shortcuts.render(request, template_name, context=None, content_type=None, status=None, using=None)，默认携带csrf_token
    Returns a HttpResponse whose content is filled with the result of calling
    都是
    django.template.loader.render_to_string(template_name, context=None, request=None, using=None) with the passed arguments.
    """
    return render_to_response(
        'render_html.html',
        {"name": "render_html"},
        # processors=[***],
        #
        # local()————返回一个包含当前作用域里面的所有变量和它们的值的字典————与context互斥————可替代contextDict及其它局部变量
        #
        # context_instance=RequestContext(request)————旧版本，支持{% csrf_token %}、{{STATIC_URL}}
        # context=RequestContext(request[,
        # processors=[***]])————默认使用TEMPLATE_CONTEXT_PROCESSORS
    )
