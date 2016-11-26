# -*- coding: utf-8 -*-
# @Date:   2016-10-11 11:27:57
# @Last Modified time: 2016-10-11 11:28:48
from django.http import HttpResponse
'''
每一个视图总是以一个 django.http.HttpRequest 的实例对象————通常叫做request，作为第一个参数。
这是一个触发这个视图、包含当前Web请求信息的对象。

每一个视图功能必须返回一个HttpResponse实例。
一旦做完，Django将完成剩余的转换Python的对象到一个合适的带有HTTP头和body的Web Response。
'''


def test1(request):
    return HttpResponse("test")
#
# HttpResponse -> 返回UnicodeStr————django默认
#


def test2(request):
    return {
        'app': 'My app',
        'user': request.user,
        'ip_address': request.META['REMOTE_ADDR']
    }
#
# context处理器
# 接收一个 HttpRequest对象，返回一个字典
#
