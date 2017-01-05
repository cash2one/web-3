# -*- coding: utf-8 -*-
# @Date:   2016-12-21 17:41:26
# @Last Modified time: 2016-12-22 12:10:53
from __future__ import unicode_literals
from django.db import models

# unique————唯一、非空，不能设默认值
from django.utils import timezone


class SimpleUser(models.Model):
    # _database = "base"                                                            # 使用多个数据库时指明用哪个
    id = models.AutoField(verbose_name="用户id", primary_key=True)                  # 自增长主键————id，默认自动生成
    phone = models.BigIntegerField(verbose_name="电话号码", blank=True, null=True)
    email = models.EmailField(verbose_name="邮箱", max_length=50)                   # 使用 EmailValidator 来验证输入合法性
    security_code = models.CharField(verbose_name='验证码', max_length=4)           # CharField————必须设置max_length
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
        verbose_name = "用户信息表"                        # 别名
        verbose_name_plural = "用户信息表"                 # 别名复数，默认'别名s'
        db_table = 'simple_user'                           # 自定义数据库表名————默认'库名_模块名'
        unique_together = ('phone', 'email')               # 联合主键————不重复的字段组合————一维或多维元组
        # ordering = ["-id"]                                # 缺省排序字段，"-"表示倒序，"?"表示随机
        # managed = True                                    # 由manage.py命令管理生命周期，设为False，关联表也不接受管理
        # default_permissions = ('add', 'change', 'delete') # 减少默认权限
        # permissions = ()                                  # 添加额外权限————一维或多维元组

    # 将一个（或多个）对象以unicode的方式显示出来
    # 旧版为__unicode__
    def __str__(self):
        return u'%s、%s' % (self.name, self.phone)


class UserRole(models.Model):
    id = models.AutoField(verbose_name="id", primary_key=True)
    user_id = models.IntegerField(verbose_name="用户id")
    role_id = models.IntegerField(verbose_name="角色id")
    create_id = models.IntegerField(verbose_name="创建人")
    create_name = models.CharField(verbose_name="创建人", max_length=50)
    create_at = models.DateTimeField("创建时间", auto_now_add=True)

    class Meta:
        db_table = "user_role"


class Role(models.Model):
    id = models.AutoField(verbose_name="角色id", primary_key=True)
    role_name = models.CharField(verbose_name="角色名", max_length=50)
    role_code = models.IntegerField(verbose_name="角色码")
    create_id = models.IntegerField(verbose_name="创建人id")
    create_name = models.CharField(verbose_name="创建人", max_length=50)
    create_at = models.DateTimeField("创建时间", auto_now_add=True)
    # menu = models.ForeignKey(Menu, related_name='menu_role')              # 一对多（外键）
    # menu = models.ManyToManyField(Menu)                                   # 多对多

    class Meta:
        db_table = "role"


class RoleMenu(models.Model):
    id = models.AutoField(verbose_name="id", primary_key=True)
    role_id = models.IntegerField(verbose_name="角色id")
    menu_id = models.IntegerField(verbose_name="菜单id")
    create_id = models.IntegerField(verbose_name="创建人id")
    create_name = models.CharField(verbose_name="创建人", max_length=50)
    create_at = models.DateTimeField("创建时间", auto_now_add=True)

    class Meta:
        db_table = "role_menu"


class Menu(models.Model):
    id = models.AutoField(verbose_name="菜单ID", primary_key=True)
    menu_name = models.CharField(verbose_name="名称", max_length=50)
    TYPE_CHOICE = (
        (0, u'目录'),
        (1, u'菜单'),
        (2, u'功能'),
    )
    type = models.SmallIntegerField(verbose_name="菜单类型", choices=TYPE_CHOICE, db_index=0)
    url_code = models.CharField(verbose_name="请求路径", max_length=100)
    code = models.CharField(verbose_name="菜单编码", max_length=10, help_text='0，目录；1，菜单；2，功能')
    isvisible = models.CharField(verbose_name="是否可见", max_length=2)
    parentid = models.CharField(verbose_name="父级菜单id", max_length=10)
    menu_order = models.CharField(verbose_name="菜单排序", max_length=10)

    def toDict(self):
        return {
            'id': self.id,
            'menu_name': self.menu_name,
            'type': self.type,
            'url_code': self.url_code,
            'code': self.code,
            'isvisible': self.isvisible,
            'parentid': self.parentid,
            'menu_order': self.menu_order,
        }

    class Meta:
        db_table = "menu"


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
    # objects = models.Manager()  # 管理器————django查询接口————默认为objects————可以在每个模型类中重命名

    class Meta:
        verbose_name = "下载信息表"
        verbose_name_plural = "下载信息表"
        db_table = 'download'
