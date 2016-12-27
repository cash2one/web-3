# -*- coding: utf-8 -*-
# @Date:   2016-12-21 17:31:48
# @Last Modified time: 2016-12-22 23:45:30
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render
from django.views.generic import FormView
from django.views.generic import ListView

from forms import LoginForm, EmailRegisterForm
from login.common.validate_code import send_email_code
from login.common.security import create_pwd
from models import SimpleUser


class LoginView(View):

    def get(self, request, form_name):
        form = html = None
        if not form_name:
            form = LoginForm()
            html = "login/email_login.html"
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
                u = SimpleUser.objects.filter(
                    email=form.cleaned_data['email'],
                    is_active=0
                ).update(
                    is_active=1,
                    pass_word=create_pwd(form.cleaned_data['pwd'])
                )
                return HttpResponseRedirect("/login")
        return render(request, html, {'form': form})


def get_email_code(request):
    email = request.GET.get('email')
    try:
        u = SimpleUser.objects.get(email=email)
        if u.is_active != 0:
            return HttpResponse("此邮箱已经被注册")
        security_code = send_email_code(email)
        u = SimpleUser.objects.filter(
            email=email
        ).update(
            security_code=security_code
        )
    except Exception, e:
        print(e)
        try:
            security_code = send_email_code(email)
            u = SimpleUser(
                email=email,
                security_code=security_code
            )
            u.save()
        except Exception, e:
            print(e)
            return HttpResponse("邮箱地址不正确")
    return HttpResponse("ok")


class MenuView(ListView):
    pass
