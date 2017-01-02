# -*- coding: utf-8 -*-
# @Date:   2016-12-17 23:33:53
# @Last Modified time: 2017-01-02 22:01:58
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic import View

from base.common.send_email import return_a_code
from base.forms import MyForm, LoginForm
from base.models import EmailLogin


def test_form(request):
    if request.method == 'GET':
        #
        # 用未绑定的form类渲染模板，生成<label><input>标签
        fm = MyForm()
        if request.GET.get("second") == "second":
            #
            # form表单绑定接收的数据，进行数据验证，反馈错误提示信息
            fm_check = MyForm(request.GET)
            if fm_check.is_valid():
                return HttpResponse("ok")
            #
            # “提交的信息不符合要求”时被调用
            return render(request, "test/test_form.html", {'form': fm_check})
        #
        # “首次访问”时被调用
        return render(request, 'test/test_form.html', {'form': fm})


class LoginView(View):

    # method_decorator————传递 *args 和 **kwargs 给这个类上的装饰器
    # 如果方法不兼容参数集合，会抛出 TypeError 异常
    # @method_decorator(login_required)
    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super(LoginView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        fm = LoginForm()
        if request.GET.get("not_first") == "not_first":
            fm_check = LoginForm(request.GET)
            if fm_check.is_valid():
                # 查询一条要更新的数据
                u = EmailLogin.objects.get(
                    email=fm_check.cleaned_data['email'])
                # 赋值给要更新的字段
                u.is_active = 1
                # 保存
                u.save()
                return HttpResponse("ok")
            else:
                return render(request, "test/test_login.html", {'form': fm_check})
        return render(request, "test/test_login.html", {'form': fm})


def login_email_validate(request):
    email = request.GET.get("email")
    if email:
        try:
            EmailLogin.objects.get(email)
            return HttpResponse("此邮箱已经被注册")
        except Exception, e:
            print(e)
            code = return_a_code(email)
            u = EmailLogin(email=email, random=code, is_active=0)
            u.save()
            return HttpResponse("ok")
    return HttpResponse("邮箱必填")
