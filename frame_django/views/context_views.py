# -*- coding: utf-8 -*-
# @Date:   2016-10-10 15:49:21
# @Last Modified time: 2016-10-11 11:31:33

from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render


def test3(request):
    # 创建 Template 对象
    tem = Template('My name is {{ name }}.')
    # 创建上下文对象
    c = Context({'name': 'Adrian', 'age': 10})
    # 返回响应对象
    return tem.render(c)
#
# render
# Context————类字典对象
# 模板渲染就是通过从Context获取值来替换模板中变量并执行所有的模板标签
#


def test4(request):
    tem = get_template('test.html')
    return tem.render(Context({'name': 'Adrian'}))
#
# 使用html模板
# get_template
#
