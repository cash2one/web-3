# -*- coding: utf-8 -*-
# @Date:   2016-12-21 17:41:59
# @Last Modified time: 2016-12-21 17:48:32
from django import forms
# from django.utils import timezone
from models import SimpleUser
# security_code_delay = 3600


class LoginForm(forms.Form):
    phone = forms.CharField(
        widget=forms.TextInput({
                'class': 'form-control',
                'id': 'phone',
                'placeholder': '请输入手机号'
            }),
        error_messages={
            'required': '请填写手机号'
        }
    )
    pwd = forms.CharField(
        widget=forms.PasswordInput({
                'class': 'form-control',
                'id': 'pwd',
                'placeholder': '请输入6~12位密码'
            }),
        error_messages={
            'required': '请输入密码'
        }
    )
    from_id = forms.CharField(
        widget=forms.HiddenInput({
                'id': 'form_id',
                'value': 'login_form'
            })
    )


class PhoneRegisterForm(forms.Form):
    phone = forms.CharField(
        widget=forms.TextInput({
                'class': 'form-control',
                'id': 'phone',
                'placeholder': '请输入手机号'
            }),
        error_messages={
            'required': '请填写手机号'
        }
    )
    pwd = forms.CharField(
        widget=forms.PasswordInput({
                'class': 'form-control',
                'id': 'pwd',
                'placeholder': '请输入6~12位密码'
            }))

    def clean_phone(self):
        cleaned_data = self.cleaned_data
        phone = cleaned_data.get("phone")
        try:
            u = SimpleUser.objects.get(phone=phone)
            raise forms.ValidationError('手机号已存在')
        except Exception, e:
            print(e)
            return cleaned_data


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
        cleaned_data = self.cleaned_data
        email = cleaned_data.get("email")
        try:
            u = SimpleUser.objects.get(email=email).exclude(is_active=0)
            raise forms.ValidationError("此邮箱已经被注册")
        except Exception, e:
            print(e)
            return cleaned_data

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
        return cleaned_data

    def clean(self):
        cleaned_data = self.cleaned_data
        pwd = cleaned_data.get('pwd')
        pwd2 = cleaned_data.get('pwd2')
        if pwd != pwd2:
            raise forms.ValidationError('两次输入密码不匹配')
        return cleaned_data
