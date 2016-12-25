# -*- coding: utf-8 -*-
# @Date:   2016-11-28 12:41:50
# @Last Modified time: 2016-12-25 17:35:47
from __future__ import unicode_literals
from django.db import models
# django中获取当前时间不要用datetime.today()，要用timezone.now()
from django.utils import timezone


class SimpleUser(models.Model):
    # _database = "base" # 使用多个数据库时指明用哪个
    # id = models.AutoField()
    name = models.CharField(verbose_name="用户名", max_length=20)
    sex = models.IntegerField(
        verbose_name="性别", default=0, help_text="1，男；2，女")
    passwd = models.CharField(verbose_name="密码", max_length=100)
    # 电话号码唯一————unique————非空、不能设默认值
    phone = models.BigIntegerField(verbose_name="电话号码", unique=True)
    # 使用 EmailValidator 来验证输入合法性
    email = models.EmailField(verbose_name="邮箱", max_length=50)
    create_at = models.DateTimeField("创建时间", auto_now_add=True)
    modify_at = models.DateTimeField("最后修改时间", auto_now=True)
    remarks = models.CharField(verbose_name="备注", max_length=50)

    class Meta:
        # 别名
        verbose_name = "用户信息表"
        # 别名复数，默认————'别名s'
        verbose_name_plural = "用户信息表"
        # 自定义数据库表名————默认————'库名_模块名'
        db_table = 'simple_user'
        # 联合主键————不重复的字段组合————可以是一维或多维
        unique_together = ('phone', 'name')
        # 减少默认权限
        # default_permissions = ('add', 'change', 'delete')
        # 添加额外权限————一维或多维元组
        # permissions = ()
        # 根据哪些字段排序，"-"表示倒序，"?"表示随机
        ordering = ["-id"]
        # 由manage.py命令管理生命周期，设为False，关联表也不接受管理
        # managed = True

    def __str__(self):
        # 将一个（或多个）对象以unicode的方式显示出来————旧版为__unicode__
        return u'%s -- %s' % (self.name, self.phone)


class UserLoginLog(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    last_login_at = models.DateTimeField("最后登录时间", default=timezone.now())
    last_logout_at = models.DateTimeField("最后退出时间", default=timezone.now())
    login_count = models.IntegerField()
    remarks = models.CharField(verbose_name="备注", max_length=50)

    class Meta:
        verbose_name = "用户登录信息表"
        verbose_name_plural = "用户登录信息表"
        db_table = 'user_login_log'

    def __str__(self):
        return u'%s:%s' % (self.name, self.id)


class DownLoad(models.Model):
    file_name = models.CharField(max_length=100)
    create_at = models.DateTimeField(default=timezone.now())
    create_name = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    # 管理器————django查询接口
    # Django 默认为每个模型类添加一个名为objects的管理器
    # 如果想将objects用于字段名称，或者想使用其它名称而不是objects访问管理器，你可以在每个模型类中重命名它们
    # objects = models.Manager()

    class Meta:
        verbose_name = "下载信息表"
        verbose_name_plural = "下载信息表"
        db_table = 'download'
