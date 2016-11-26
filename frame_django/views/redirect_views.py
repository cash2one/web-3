# -*- coding: utf-8 -*-
# @Date:   2016-10-11 11:45:20
# @Last Modified time: 2016-10-11 11:52:56
from django.http import HttpResponseRedirect
from django.shortcuts import redirect


def test8(request):
    return HttpResponseRedirect('../../?message=error')
#
# HttpResponseRedirect(url_str)————重定向到url
#


def test9(request):
    return redirect(reverse('commons.views.invoice_return_index', args=[]))
#
# reverse(指定重定向的views处理函数,args是url匹配的值)
#

'''
其他的也可以直接在url中配置，但是不知道怎么传参数。

from django.views.generic.simple import redirect_to
在url中添加 (r'^one/$', redirect_to, {'url': '/another/'}),



我们甚至可以使用session的方法传值


request.session['error_message'] = 'test'
redirect('%s?error_message=test' % reverse('page_index'))

这些方式类似于location刷新，客户端重新指定url
'''
