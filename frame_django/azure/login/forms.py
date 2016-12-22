# -*- coding: utf-8 -*-
# @Date:   2016-12-20 17:41:53
# @Last Modified time: 2016-12-20 17:44:11
#
# forms————可便捷地创建表单，进行后台验证和html限定
# 模型类的属性映射到数据库的字段
# 表单类的字段会映射到HTML的<input>表单的元素
from django import forms


class UserForm(forms.Form):
    # widget=forms.TextInput————默认，对应<input type="text"/>
    # widget=forms.Textarea————对应<textarea></textarea>
    # required=True————默认
    phone = forms.CharField(label="你的电话", max_length=11, required=True)
    passwd = forms.CharField(label="你的密码", required=True)
