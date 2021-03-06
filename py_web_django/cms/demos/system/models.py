# -*- coding: utf-8 -*-
# @Date:   2016-12-21 17:41:26
# @Last Modified time: 2017-03-02 22:30:04
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class SimpleUser(models.Model):
    # _database = "base"
    # # 使用多个数据库时指明用哪个
    # 自增长主键————id，默认自动生成
    id = models.AutoField(verbose_name="用户id", primary_key=True)
    phone = models.BigIntegerField(verbose_name="电话号码", blank=True, null=True)
    # 使用 EmailValidator 来验证输入合法性
    email = models.EmailField(verbose_name="邮箱", max_length=50)
    # CharField————必须设置max_length
    security_code = models.CharField(verbose_name='验证码', max_length=4)
    is_active = models.SmallIntegerField(verbose_name='是否通过验证', default=0)
    name = models.CharField(verbose_name="用户名", max_length=20)
    SEX_CHOICE = (
        (0, u'未知'),
        (1, u'男'),
        (2, u'女'),
    )
    sex = models.SmallIntegerField(
        verbose_name="性别", choices=SEX_CHOICE, default=0)
    pass_word = models.CharField(verbose_name="密码", max_length=100)
    create_at = models.DateTimeField("创建时间", auto_now_add=True)
    modify_at = models.DateTimeField("最后修改时间", auto_now=True)
    remarks = models.CharField(verbose_name="备注", max_length=50)
    role = models.ManyToManyField('Role', through='UserRole')
    current_role = models.IntegerField(default=-100)

    class Meta:
        verbose_name = "用户信息表"                         # 别名
        verbose_name_plural = "用户信息表"                  # 别名复数，默认'别名s'
        db_table = 'simple_user'                            # 自定义数据库表名————默认'库名_模块名'
        # 联合主键————不重复的字段组合————一维或多维元组
        unique_together = ('phone', 'email')
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
    user = models.ForeignKey('SimpleUser', verbose_name="用户ID外键")
    role = models.ForeignKey('Role', verbose_name="角色ID外键")
    create_id = models.IntegerField(verbose_name="创建人")
    create_name = models.CharField(verbose_name="创建人", max_length=50)
    create_at = models.DateTimeField("创建时间", auto_now_add=True)

    class Meta:
        db_table = "user_role"

# 关联表————可以分别建立多个关联
# 子表A————OneToOneField、ForeignKey、ManyToManyField字段所在的表
# 母表B————子表关联字段指向的表
# connectCol————OneToOneField、ForeignKey、ManyToManyField字段所在的列
# 过滤函数
# objects.get(...).field
# objects.filter(...)
# objects.filter(...).all()
# objects.filter(...).values()
# objects.filter(...).value_list()
"""
子查母————一对一（OneToOneField、ForeignKey）————A.objects.get(...).connectCol.B字段————B.objects.get/filter(A表名小写__A字段="***")
子查母————一对多（ManyToManyField）————A.objects.get(...).connectCol.all()/filter()————B.objects.filter(A表名小写__A字段="***")

母查子————一对一（OneToOneField）————B.objects.get(...).A表名小写.A字段————A.objects.get/filter(connectCol__B字段="***")
母查子————一对多（ForeignKey、ManyToManyField）————B.objects.get(...).A表名小写_set.all()/filter()————A.objects.filter(connectCol__B字段="***")————A.objects.filter(connectCol=B.objects.get(B字段="***")))

添加对象————a = A.objects.get(...);b = B.objects.get(...);a.connectCol.add(b)
删除对象————a = A.objects.get(...);b = B.objects.get(...);a.connectCol.remove(b) 或者 a.connectCol.filter(...).delete()
"""
# connectCol = OneToOneField("table"[, default=***[,
# to_field='field']])————一对一————用于某张表的补充（在子表中定义）
"""
to_field————默认关联母表的id，生成connectCol_id字段————如果指定关联其它列，母表须设置unique=True————唯一、非空，不能设默认值

CREATE TABLE `role` (
    ...
    UNIQUE KEY `menu_id` (`menu_id`),
    CONSTRAINT `role_menu_id_25fd2e17_fk_menu_id` FOREIGN KEY (`menu_id`) REFERENCES `menu` (`id`)
)
"""
# connectCol = models.ManyToManyField("table")————多对多————默认关联母表的id
"""
through————指定中间表对应的model
through_fields————明确指定（中间表中）哪些外键作为两表的关联字段————接收一个二元组，默认是table_id、self_id字段
related_name————定义抽象model (abstract models) 时，必须显式指定反向名称
db_table————指定生成的中间表表名————默认生成self_table表作为中间表

CREATE TABLE `role_menu` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `role_id` int(11) NOT NULL,
    `menu_id` int(11) NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `role_menu_role_id_c692b7c4_uniq` (`role_id`,`menu_id`),
    KEY `role_menu_menu_id_b54bc904_fk_menu_id` (`menu_id`),
    CONSTRAINT `role_menu_menu_id_b54bc904_fk_menu_id` FOREIGN KEY (`menu_id`) REFERENCES `menu` (`id`),
    CONSTRAINT `role_menu_role_id_8f901c2d_fk_role_id` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`)
)
self = models.ManyToManyField("self")————针对自身建立多对多关系
"""
# connectCol = models.ForeignKey(Menu)————一对多（外键）————默认生成connectCol_id字段
"""
to_field————默认关联母表的id，生成connectCol_id字段————如果指定关联其它列，母表须设置unique=True————唯一、非空，不能设默认值
db_constraint————默认为True，在数据库上建立外键约束
related_name————让关联的对象反查到源对象，设为 '+' 或者以'+' 结尾，不让Django 创建反向关联
null=True————允许NULL值，分配None来删除对应的关联性

CREATE TABLE `role` (
    ...
    `menu_id` int(11) NOT NULL,
    KEY `role_menu_id_25fd2e17_fk_menu_id` (`menu_id`),
    CONSTRAINT `role_menu_id_25fd2e17_fk_menu_id` FOREIGN KEY (`menu_id`) REFERENCES `menu` (`id`)
)
"""


class Role(models.Model):
    id = models.AutoField(verbose_name="角色ID", primary_key=True)
    role_name = models.CharField(verbose_name="角色名", max_length=50)
    role_code = models.IntegerField(verbose_name="角色码")
    create_id = models.IntegerField(verbose_name="创建人id")
    create_name = models.CharField(verbose_name="创建人", max_length=50)
    create_at = models.DateTimeField("创建时间", auto_now_add=True)
    menu = models.ManyToManyField('Menu', through="RoleMenu")

    class Meta:
        db_table = "role"


class RoleMenu(models.Model):
    id = models.AutoField(verbose_name="id", primary_key=True)
    role = models.ForeignKey("Role", verbose_name="角色ID外键")
    menu = models.ForeignKey("Menu", verbose_name="菜单ID外键")
    create_id = models.IntegerField(verbose_name="创建人id")
    create_name = models.CharField(verbose_name="创建人", max_length=50)
    create_at = models.DateTimeField("创建时间", auto_now_add=True)

    class Meta:
        db_table = "role_menu"


"""
insert into `menu`
(`menu_name`, `type`, `url_code`, `code`, `isvisible`, `parentid`, `menu_order`)
values
('personal space','0','/root','0','1','0','0'),
('系统管理','0','#','01','1','1','0');
"""


class Menu(models.Model):
    id = models.AutoField(verbose_name="菜单ID", primary_key=True)
    menu_name = models.CharField(verbose_name="名称", max_length=50, unique=True)
    TYPE_CHOICE = (
        (0, u'目录'),
        (1, u'菜单'),
        (2, u'功能'),
    )
    type = models.SmallIntegerField(
        verbose_name="菜单类型", choices=TYPE_CHOICE, db_index=0)
    url_code = models.CharField(verbose_name="请求路径", max_length=100)
    code = models.CharField(verbose_name="菜单编码",
                            max_length=10, help_text='0，目录；1，菜单；2，功能')
    isvisible = models.CharField(verbose_name="是否可见", max_length=2)
    parentid = models.CharField(verbose_name="父级菜单id", max_length=10)
    menu_order = models.CharField(verbose_name="菜单排序", max_length=10)

    # toDict————把QuerySet对象转化为字典对象（类似于django内置values()函数）
    def toDict(self):
        # python三元表达式
        self.parent_name = self.parent_name if hasattr(
            self, 'parent_name') else None
        self.parent_url_code = self.parent_url_code if hasattr(
            self, 'parent_url_code') else None
        # self.user_num = self.user_num if hasattr(self, 'user_num') else None
        return {
            'id': self.id,
            'menu_name': self.menu_name,
            'type': self.type,
            'url_code': self.url_code,
            'code': self.code,
            'isvisible': self.isvisible,
            'parentid': self.parentid,
            'menu_order': self.menu_order,
            # 动态生成的字段
            'parent_name': self.parent_name,
            'parent_url_code': self.parent_url_code,
            # 'user_num': self.user_num,
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
    # objects = models.Manager()  #
    # 管理器————django查询接口————默认为objects————可以在每个模型类中重命名

    class Meta:
        verbose_name = "下载信息表"
        verbose_name_plural = "下载信息表"
        db_table = 'download'
