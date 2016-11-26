# -*- coding: utf-8 -*-
# @Date:   2016-10-11 11:31:13
# @Last Modified time: 2016-10-11 11:43:18
from django.template.loader import get_template
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext


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
#
# 当你渲染模板时，要用 RequestContext 替代 Context
#
# 每个试图中只需把custom_proc传递给RequestContext的参数processors就行了
#


def test6(request):
    return render_to_response(
        'template2.html',
        {'message': 'I am the second view.'},
        context_instance=RequestContext(request, processors=[custom_proc])
    )
#
# render_to_response————对get_template()的简单封装
# render_to_response('.../.../**.html'[,dict_obj])
# render_to_response('.../.../**.html',contextDict)
# 可以用local()替代contextDict以及其它局部变量，返回一个包含当前作用域里面的所有变量和它们的值的字典
#
# Django提供对全局 context 处理器的支持
# settings的TEMPLATE_CONTEXT_PROCESSORS指定了哪些context processors总是默认被使用
#

from django.conf import global_settings
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + \
    ("myapp.processor.foos",)  # 或者配置settings.py的TEMPLATE_CONTEXT_PROCESSORS


def test7(request):
    return render_to_response('xxx.html', {'age': 33}, context_instance=RequestContext(request))
