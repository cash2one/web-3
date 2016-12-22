# -*- coding: utf-8 -*-
# @Date:   2016-12-21 17:31:48
# @Last Modified time: 2016-12-22 13:31:10
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from forms import LoginForm, EmailRegisterForm
from login.common.validate_code import send_email_code
from models import SimpleUser


class LoginView(View):

    def get(self, request, form_name):
        form = html = None
        if not form_name:
            form = LoginForm()
            html = "login/login.html"
        if form_name == "email_register":
            form = EmailRegisterForm()
            html = "login/email_register.html"
        return render(request, html, {'form': form})

    def post(self, request, **kwargs):
        form = html = None
        if request.path == '/login/':
            form = LoginForm(request.POST)
            html = "login/login.html"
        if request.path == '/login/email_register':
            form = EmailRegisterForm(request.POST)
            html = "login/email_register.html"
            if form.is_valid():
                u = SimpleUser(
                    email=form.cleaned_data['email'],
                    is_active=1,
                    pass_word=form.cleaned_data['pwd']
                )
                u.save()
        if request.path == '/login/phone_register':
            pass
        return render(request, html, {'form': form})


def get_email_code(request):
    email = request.GET.get('email')
    try:
        u = SimpleUser.objects.get(email=email)
        return HttpResponse("此邮箱已经被注册")
    except Exception, e:
        print(e)
        try:
            security_code = send_email_code(email)
            u = SimpleUser(email=email, security_code=security_code)
            u.save()
            return HttpResponse("验证码已发送，请在10分钟内完成注册")
        except Exception, e:
            print(e)
            return HttpResponse("邮箱地址不正确")
