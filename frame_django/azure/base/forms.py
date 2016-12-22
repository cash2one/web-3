# -*- coding: utf-8 -*-
# @Date:   2016-12-08 11:46:30
# @Last Modified time: 2016-12-08 11:47:05
#
# forms————可便捷地创建表单，进行后台验证和html限定
# 模型类的属性映射到数据库的字段
# 表单类的字段会映射到HTML的<input>表单的元素
from django import forms


# 创建表单类————进行后台数据验证
class UserForm(forms.Form):
    # widget=forms.TextInput————默认，对应<input type="text"/>
    # forms.Textarea...
    phone = forms.CharField(label="你的电话", max_length=11, required=True)
    passwd = forms.CharField(label="你的密码", required=True)
