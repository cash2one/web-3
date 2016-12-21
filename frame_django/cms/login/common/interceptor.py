from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

white_ips = [
    '127.0.0.1',
]


class InterceptorMiddleware(MiddlewareMixin):
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
                return HttpResponseRedirect('/login')
