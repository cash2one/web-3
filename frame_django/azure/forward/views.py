# -*- coding: utf-8 -*-
# @Date:   2016-12-17 23:33:53
# @Last Modified time: 2016-12-17 23:34:04
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic import View
from .forms import MyForm, LoginForm
from .models import UserLogin
from common.send_email import return_a_code


def form_test(request):
    if request.method == 'GET':
        #
        # 用未绑定的form类渲染模板，生成<label><input>标签
        fm = MyForm()
        if request.GET.get("second") == "second":
            #
            # form表单绑定接收的数据，进行数据验证，反馈错误提示信息
            fm_check = MyForm(request.GET)
            if fm_check.is_valid():
                # new_product = fm_check.save()
                # return HttpResponseRedirect(new_product.get_absolute_url())
                return render(request, "forward/form_with_style.html", {'form': fm})
            #
            # “提交的信息不符合要求”时被调用
            return render(request, "forward/form_test.html", {'form': fm_check})
        #
        # “首次访问”时被调用
        return render(request, 'forward/form_test.html', {'form': fm})
    else:
        #
        # form表单绑定接收的数据，进行数据验证，反馈错误提示信息
        fm_check = MyForm(request.POST)
        if fm_check.is_valid():
            return HttpResponse("ok")
        #
        # “提交的信息不符合要求”时被调用
        return render(request, "forward/form_with_style.html", {'form': fm_check})


class LoginView(View):
    # method_decorator————传递 *args 和 **kwargs 给这个类上的装饰器
    # 如果方法不接受兼容参数集合，它会抛出 TypeError 异常
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
                u = UserLogin.objects.get(email=fm_check.cleaned_data['email'])
                # 赋值给要更新的字段
                u.is_active = 1
                # 保存
                u.save()
                return HttpResponse("ok")
            else:
                return render(request, "forward/login.html", {'form': fm_check})
        return render(request, "forward/login.html", {'form': fm})


def login_email_validate(request):
    email = request.GET.get("email")
    if email:
        try:
            UserLogin.objects.get(email)
            return HttpResponse("此邮箱已经被注册")
        except Exception, e:
            code = return_a_code(email)
            u = UserLogin(email=email, random=code, is_active=0)
            u.save()
            return HttpResponse("ok")
    return HttpResponse("邮箱必填")
