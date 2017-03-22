# -*- coding: utf-8 -*-
# @Date:   2016-12-20 16:35:58
# @Last Modified time: 2017-03-22 22:34:40
#
from __future__ import unicode_literals
# 继承django.contrib.auth.models.AbstractUser类来扩充User字段
from django.contrib.auth.models import AbstractUser
#
# django自带的用户登录信息模型————User
# 修改方式————继承、扩展、自定义（修改AUTH_USER_MODEL）
# 在创建任何迁移或者第一次运行 manage.py migrate 前设置它
from django.contrib.auth.models import User
#
# django自带的用户信息验证————authenticate(username=username,password=password)
from django.contrib.auth import authenticate, login

from django.db import models
# @python_2_unicode_compatible————django内置的一个装饰器
# 针对 __str__ 方法，兼容python2和python3的unicode语法
from django.utils.six import python_2_unicode_compatible
# 进行用户验证的python类的路径————调用django.contrib.auth.authenticate()会一一尝试
# 如果用户名和密码在多个后台中都是合法的，Django 将在第一个匹配成功后停止处理
from django.contrib.auth.backends import ModelBackend

from django.contrib.sessions.middleware import SessionMiddleware


# django自带的用户登录信息模型————AUTH_USER_MODEL = 'auth.User'
# 修改方式————继承、扩展、自定义
# 在创建任何迁移或者第一次运行 manage.py migrate 前设置它
# from django.contrib.auth.models import User
#
# 引用User模型————如果直接引用User（例如：通过一个外键引用它），代码将不能工作
# from django.contrib.auth import get_user_model
@python_2_unicode_compatible
class NewUser(AbstractUser):
    profile = models.CharField('profile', default='', max_length=256)

    def __str__(self):
        return self.username

'''
# 扩展自带User————存储新字段到已有的User里
class UserProfile(models.Model):
    # OneToOneField————关联到一个存储额外信息的Model
    user = models.OneToOneField(User)
    department = models.CharField(max_length=100)
'''

# 定义一个Article模型的管理器
# Manager.get_queryset()————得到相关的查询集


class ArticleManager(models.Manager):

    def query_by_column(self, column_id):
        query = self.get_queryset().filter(column_id=column_id)

    def query_by_user(self, user_id):
        user = NewUser.objects.get(id=user_id)
        article_list = user.article_set.all()
        return article_list

    def query_by_polls(self):
        query = self.get_queryset().order_by('poll_num')
        return query

    def query_by_time(self):
        query = self.get_queryset().order_by('-pub_date')
        return query

    def query_by_keyword(self, keyword):
        query = self.get_queryset().filter(title__contains=keyword)
        return query
