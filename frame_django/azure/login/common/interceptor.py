# -*- coding: utf-8 -*-
# @Date:   2016-12-08 17:01:10
# @Last Modified time: 2016-12-08 17:01:30
#
# 拦截器————重定向未登陆的用户访问
# 可以通过自定义中间件实现，也可以通过在给每个视图添加拦截装饰器实现
#
# 中间————服务器接收到Request----View处理----发送Response到客户端
#
# process_request(self, request)————接受request之后，确定所执行的view之前
# 返回None————继续处理这个request，执行后续的中间件，然后调用相应的view
# 返回HttpResponse对象————不再执行任何其它的中间件以及相应的view
#
# process_view(self, request, view_func, view_args, view_kwargs)————确定了所要执行的view之后，view真正执行之前
#
# process_response(self, request, response)————view执行之后————在整个流程中，每一个process_response都会执行到————必须返回 HttpResponse 对象
#
# process_exception(self, request, exception)————view抛出异常
import re
from django.http import HttpResponseRedirect
from security import check_pwd
try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - 1.9.x

# ip访问白名单
white_ips = [
    '127.0.0.1',
]


class InterceptorMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.META.has_key('HTTP_X_FORWARDED_FOR'):
            # 使用ngix等代理http时的用户ip
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        # 不对/login/test下的url进行拦截
        reg = re.compile("/login/test/")
        if re.match(reg, request.path) or request.path == '/login/test':
            return None
        else:
            if request.path != '/login/' or ip not in white_ips:
                try:
                    phone = request.session['phone']
                    passwd = request.session['passwd']
                    if not check_pwd(phone, passwd):
                        return HttpResponseRedirect('/login')
                except Exception, e:
                    return HttpResponseRedirect('/login')
