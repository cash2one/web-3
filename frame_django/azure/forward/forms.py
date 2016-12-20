# -*- coding: utf-8 -*-
# @Date:   2016-12-17 23:16:13
# @Last Modified time: 2016-12-17 23:16:31
from django import forms
from .models import UserLogin


class MyForm(forms.Form):
    textInput = forms.CharField(label='字段1', max_length=10)
    textArea = forms.CharField(label='字段2', max_length=30, widget=forms.Textarea)


# error_messages————自定义错误信息
# pip install -U django
# django1.10默认提示为在输入框下方弹出悬浮提示框
# django1.9以下默认在输入框下方生成提示列表
class LoginForm(forms.Form):
    email = forms.EmailField(
        # widget=forms.TextInput(
        #     {'class': 'form-control'}
        # ),
        error_messages={
            'required': '邮箱必填',
            'invalid': 'Email地址无效'
        }
    )
    random = forms.CharField(
        max_length=4,
        min_length=4,
        # 显示成密码样式
        widget=forms.PasswordInput(),
        error_messages={
            'required': '请填写验证码',
            'max_length': '字符长度为4',
            'min_length': '字符长度为4'
        }
    )

    # 验证用户输入的验证码的合法性
    # 校验函数————以clean_开头，并以字段名称结束
    # Django的form系统自动寻找合法的校验函数
    def clean_random(self):
        # cleaned_data————在数据合法的情况下，它包含干净的提交数据的字典
        email = self.cleaned_data['email']
        code = self.cleaned_data['random']
        try:
            u = UserLogin.objects.get(email=email)
            random = u.random
        except Exception, e:
            raise forms.ValidationError('邮箱地址不存在')
        else:
            if random != code:
                raise forms.ValidationError('验证码不正确')