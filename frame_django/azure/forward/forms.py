# -*- coding: utf-8 -*-
# @Date:   2016-12-17 23:16:13
# @Last Modified time: 2016-12-17 23:16:31
from django import forms


class MyForm(forms.Form):
    textInput = forms.CharField(label='字段1', max_length=100)
    textArea = forms.CharField(label='字段2', max_length=100, widget=forms.Textarea)


class LoginForm(forms.Form):
    email = forms.EmailField()
    random = forms.CharField(max_length=4, min_length=4)
