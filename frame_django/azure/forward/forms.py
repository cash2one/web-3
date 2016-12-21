# -*- coding: utf-8 -*-
# @Date:   2016-12-17 23:16:13
# @Last Modified time: 2016-12-17 23:16:31
from django import forms


class LoginForm(forms.Form):
    uid = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'uid',
                'placeholder': 'Username'
            }))
    pwd = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'pwd',
                'placeholder': 'Password'
            }))
