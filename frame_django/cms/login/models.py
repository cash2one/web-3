# -*- coding: utf-8 -*-
# @Date:   2016-12-21 17:41:26
# @Last Modified time: 2016-12-22 12:10:53
from __future__ import unicode_literals
from django.db import models


class SimpleUser(models.Model):
    phone = models.BigIntegerField(verbose_name="电话号码", unique=True)
    email = models.EmailField(verbose_name="邮箱", max_length=50, unique=True)
    security_code = models.CharField(verbose_name='验证码', max_length=4)
    is_active = models.SmallIntegerField(verbose_name='是否通过验证', default=0)
    name = models.CharField(verbose_name="用户名", max_length=20)
    role = models.CharField(verbose_name='角色', max_length=100, help_text="角色码")
    SEX_CHOICE = (
        (0, u'未知'),
        (1, u'男'),
        (2, u'女'),
    )
    sex = models.SmallIntegerField(verbose_name="性别", choices=SEX_CHOICE)
    pass_word = models.CharField(verbose_name="密码", max_length=100)
    create_at = models.DateTimeField("创建时间", auto_now_add=True)
    modify_at = models.DateTimeField("最后修改时间", auto_now=True)
    remarks = models.CharField(verbose_name="备注", max_length=50)

    class Meta:
        verbose_name = "用户信息表"
        verbose_name_plural = "用户信息表"
        db_table = 'simple_user'
        unique_together = ('phone', 'name')
        # default_permissions = ('add', 'change', 'delete')
        # permissions = ()
        ordering = ["-id"]
        # managed = True

    def __str__(self):
        return u'%s、%s' % (self.name, self.phone)
