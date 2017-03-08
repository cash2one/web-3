# -*- coding: utf-8 -*-
# @Date:   2017-03-07 22:31:22
# @Last Modified time: 2017-03-07 22:31:34
# from django.test import TestCase
"""
重定向
"""
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


def page1(request):
    return HttpResponseRedirect('/test/page2')


def page2(request):
    return HttpResponseRedirect(reverse('page3', args=[]))


def page3(request):
    return redirect(reverse('page4'))


def page4(request):
    return redirect('/test/page5')


def real_page(request):
    return HttpResponse("real_page")
