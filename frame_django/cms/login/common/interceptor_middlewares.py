# -*- coding: utf-8 -*-
# @Date:   2016-12-21 17:43:59
# @Last Modified time: 2016-12-27 09:19:10
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from security import check_pwd

white_ips = [
    '127.0.0.1',
]


class LoginMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.META.has_key('HTTP_X_FORWARDED_FOR'):
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']

        if request.path != '/login/' or ip not in white_ips:
            try:
                phone = request.session['phone']
                passwd = request.session['passwd']
                if not check_pwd(phone, passwd):
                    return HttpResponseRedirect('/login')
            except Exception, e:
                print(e)
                return HttpResponseRedirect('/login')
        return None


class MenuMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.META.has_key('HTTP_X_FORWARDED_FOR'):
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']

        if request.path != '/login/' or ip not in white_ips:
            try:
                phone = request.session['phone']
                passwd = request.session['passwd']
                if not check_pwd(phone, passwd):
                    return HttpResponseRedirect('/login')
            except Exception, e:
                print(e)
                return HttpResponseRedirect('/login')
        return None
