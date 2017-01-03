# -*- coding: utf-8 -*-
# @Date:   2016-12-21 17:41:59
# @Last Modified time: 2016-12-21 17:48:32
#
"""
创建表单类————可便捷地创建表单、进行后台数据验证和html限定
pip install -U django
django1.10默认会在后台验证之前在前台进行必填字段验证，弹出悬浮提示标签
"""
from django import forms
# from django.utils import timezone
from models import SimpleUser
# security_code_delay = 3600


class LoginForm(forms.Form):
    email = forms.EmailField(
        # widget=forms.TextInput(
        #     # attrs=可以省略
        #     attrs={
        #         'class': 'form-control',
        #         'id': 'email',
        #         'placeholder': '请输入邮箱地址'
        #     }),
        # required=True,                   # 默认必填
        error_messages={                   # error_messages————自定义错误信息
            'required': '请填写邮箱地址',
            'invalid': '邮箱格式不正确'
        }
    )
    pwd = forms.CharField(
        min_length=6,
        max_length=12,
        widget=forms.PasswordInput(),      # 显示成密码输入框
        error_messages={
            'required': '请填写密码',
            'min_length': '密码不能小于6位',
            'max_length': '密码不能超过12位',
        }
    )


class EmailRegisterForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': '请填写邮箱地址',
            'invalid': '邮箱格式不正确'
        }
    )
    security_code = forms.CharField(
        error_messages={
            'required': '请填写验证码'
        }
    )
    pwd = forms.CharField(
        min_length=6,
        max_length=12,
        widget=forms.PasswordInput(),
        error_messages={
            'required': '请填写密码',
            'min_length': '密码不能小于6位',
            'max_length': '密码不能超过12位',
        }
    )
    pwd2 = forms.CharField(
        widget=forms.PasswordInput(),
        error_messages={
            'required': '请填写密码'
        }
    )

    def clean_email(self):
        # cleaned_data————在数据合法的情况下，包含干净的提交数据的字典
        # 可以在forms、views里调用
        cleaned_data = self.cleaned_data
        email = cleaned_data.get("email")
        try:
            u = SimpleUser.objects.get(email=email)
            if u.is_active != 0:
                raise forms.ValidationError("此邮箱已经被注册")
        except Exception, e:
            print(e)
        return email

    def clean_security_code(self):
        cleaned_data = self.cleaned_data
        email = cleaned_data.get("email")
        security_code = cleaned_data.get("security_code")
        try:
            u = SimpleUser.objects.get(email=email, is_active=0, security_code=security_code)
            # modify_at = u.modify_at
            # current = timezone.now()
        except Exception, e:
            print(e)
            raise forms.ValidationError("验证码不正确")
        return security_code

    def clean(self):
        cleaned_data = self.cleaned_data
        pwd = cleaned_data.get('pwd')
        pwd2 = cleaned_data.get('pwd2')
        if pwd != pwd2:
            raise forms.ValidationError('两次输入密码不匹配')
        return cleaned_data
