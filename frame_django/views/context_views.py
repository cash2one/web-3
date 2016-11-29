# -*- coding: utf-8 -*-
# @Date:   2016-10-10 15:49:21
# @Last Modified time: 2016-11-29 15:41:56

from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect


'''
from django.views.generic.simple import redirect_to
在url中添加 (r'^one/$', redirect_to, {'url': '/another/'}),



我们甚至可以使用session的方法传值


request.session['error_message'] = 'test'
redirect('%s?error_message=test' % reverse('page_index'))

这些方式类似于location刷新，客户端重新指定url
'''
