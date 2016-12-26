# -*- coding: utf-8 -*-
# @Date:   2016-12-21 17:41:26
# @Last Modified time: 2016-12-22 12:10:53
from __future__ import unicode_literals
from django.db import models


class SimpleUser(models.Model):
    id = models.AutoField(verbose_name="用户id", primary_key=True)
    phone = models.BigIntegerField(verbose_name="电话号码", blank=True, null=True)
    email = models.EmailField(verbose_name="邮箱", max_length=50)
    security_code = models.CharField(verbose_name='验证码', max_length=4)
    is_active = models.SmallIntegerField(verbose_name='是否通过验证', default=0)
    name = models.CharField(verbose_name="用户名", max_length=20)
    SEX_CHOICE = (
        (0, u'未知'),
        (1, u'男'),
        (2, u'女'),
    )
    sex = models.SmallIntegerField(verbose_name="性别", choices=SEX_CHOICE, default=0)
    pass_word = models.CharField(verbose_name="密码", max_length=100)
    create_at = models.DateTimeField("创建时间", auto_now_add=True)
    modify_at = models.DateTimeField("最后修改时间", auto_now=True)
    remarks = models.CharField(verbose_name="备注", max_length=50)

    class Meta:
        verbose_name = "用户信息表"
        verbose_name_plural = "用户信息表"
        db_table = 'simple_user'
        unique_together = ('phone', 'email')
        ordering = ["-id"]

    def __str__(self):
        return u'%s、%s' % (self.name, self.phone)


class UserRole(models.Model):
    id = models.AutoField(verbose_name="id", primary_key=True)
    user_id = models.IntegerField(verbose_name="用户id")
    role_id = models.IntegerField(verbose_name="角色id")
    create_id = models.IntegerField(verbose_name="创建人")
    create_name = models.CharField(verbose_name="创建人")
    create_at = models.DateTimeField("创建时间", auto_now_add=True)


class Role(models.Model):
    id = models.AutoField(verbose_name="角色id", primary_key=True)
    role_name = models.CharField(verbose_name="角色名")
    role_code = models.CharField(verbose_name="角色码")
    create_id = models.IntegerField(verbose_name="创建人id")
    create_name = models.CharField(verbose_name="创建人")
    create_at = models.DateTimeField("创建时间", auto_now_add=True)


class RoleMenu(models.Model):
    id = models.AutoField(verbose_name="id", primary_key=True)
    role_id = models.CharField(verbose_name="角色id", primary_key=True)
    menu_id = models.CharField(verbose_name="菜单id", primary_key=True)
    create_id = models.CharField(verbose_name="创建人id")
    create_name = models.CharField(verbose_name="创建人")
    create_at = models.DateTimeField("创建时间", auto_now_add=True)


class Menu(models.Model):
    id = models.AutoField(verbose_name="菜单ID", primary_key=True)
    menu_name = models.CharField(verbose_name="名称")
    TYPE_CHOICE = (
        (0, u'目录'),
        (1, u'菜单'),
        (2, u'功能'),
    )
    type = models.CharField(verbose_name="菜单类型", choices=TYPE_CHOICE)
    url_code = models.CharField(verbose_name="请求路径")
    code = models.CharField(verbose_name="菜单编码")
    isvisible = models.CharField(verbose_name="是否可见")
    parentid = models.CharField(verbose_name="父级菜单id")
    menu_order = models.CharField(verbose_name="菜单排序")
