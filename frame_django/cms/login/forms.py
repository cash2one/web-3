# -*- coding: utf-8 -*-
# @Date:   2016-12-21 17:41:59
# @Last Modified time: 2016-12-21 17:48:32
from django import forms


class LoginForm(forms.Form):
    uname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'uname',
                'placeholder': '请输入用户名'
            }))
    pwd = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'pwd',
                'placeholder': '请输入密码'
            }))
