# -*- coding: utf-8 -*-
# @Date:   2016-12-20 16:35:58
# @Last Modified time: 2016-12-20 16:39:14
#
from __future__ import unicode_literals
# 继承django.contrib.auth.models.AbstractUser类来扩充User字段
from django.contrib.auth.models import AbstractUser
from django.db import models
# @python_2_unicode_compatible————django内置的一个装饰器
# 针对 __str__ 方法，兼容python2和python3的unicode语法
from django.utils.six import python_2_unicode_compatible


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


# column————文章分类数据模型
# 文章和分类是多对一的关系
@python_2_unicode_compatible
class Column(models.Model):
    name = models.CharField('column_name', max_length=256)
    intro = models.TextField('introduction', default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'column'
        verbose_name_plural = 'column'
        ordering = ['name']


# article————文章数据模型
@python_2_unicode_compatible
class Article(models.Model):
    column = models.ForeignKey(Column, blank=True, null=True, verbose_name='belong to')
    title = models.CharField(max_length=256)
    # 文章和作者是多对一的关系
    author = models.ForeignKey('Author')
    # 文章和普通用户是多对多的关系(点赞，收藏)
    user = models.ManyToManyField('NewUser', blank=True)
    content = models.TextField('content')
    pub_date = models.DateTimeField(auto_now_add=True, editable=True)
    update_time = models.DateTimeField(auto_now=True, null=True)
    published = models.BooleanField('notDraft', default=True)
    poll_num = models.IntegerField(default=0)
    comment_num = models.IntegerField(default=0)
    keep_num = models.IntegerField(default=0)
    # 申明管理器
    objects = ArticleManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'article'


# comment————评论数据模型
@python_2_unicode_compatible
class Comment(models.Model):
    user = models.ForeignKey('NewUser', null=True)
    article = models.ForeignKey(Article, null=True)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, editable=True)
    poll_num = models.IntegerField(default=0)

    def __str__(self):
        return self.content


# author————作者数据模型
class Author(models.Model):
    name = models.CharField(max_length=256)
    profile = models.CharField('profile', default='',max_length=256)
    password = models.CharField('password', max_length=256)
    register_date = models.DateTimeField(auto_now_add=True, editable=True)

    def __str__(self):
        return self.name


# poll————增加点赞数据模型
class Poll(models.Model):
    user = models.ForeignKey('NewUser', null=True)
    article = models.ForeignKey(Article, null=True)
    comment = models.ForeignKey(Comment, null=True)


'''
同步数据模型到数据库
python manage.py makemigrations focus
python manage.py migrate
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
