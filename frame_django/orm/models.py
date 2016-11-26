# -*- coding: utf-8 -*-
# @Date:   2016-10-10 15:22:13
# @Last Modified time: 2016-10-10 16:25:59
from __future__ import unicode_literals

from django.db import models


class Person(models.Model):
    # Django会自动适时将verbose_name首字母大写
    # ManyToManyField和ForeignKey字段，第一个参数必须是模块类。
    # 因此，必须显式使用verbose_name这个参数名称。
    name = models.CharField(max_length=30)
    # blank=True————字段允许为空
    # null=True————空值存储为NULL————需要手动更新数据库，把字段上的NOT NULL删除
    # ALTER TABLE tab_name ALTER COLUMN column_name DROP NOT NULL;
    # 数字型
    num1 = models.IntegerField(blank=True, null=True)
    num2 = models.DecimalField(blank=True, null=True)
    num3 = models.FloatField(blank=True, null=True)
    # 时间型
    time1 = TimeField(blank=True, null=True)
    time2 = DateTimeField(blank=True, null=True)
    time3 = DateField(blank=True, null=True)

    class Meta:
        '''内部类'''
        verbose_name = 'Pe'  # 别名
        verbose_name_plural = 'Pes'  # 别名复数，默认verbose_name+"s"
        abstract = True  # 抽象类————不会对应数据库表
        app_label = 'my_app'  # 当模型不在app包里时，指定模型类属于哪个app
        db_table = "person"  # 指定自定义数据库表名
        db_tablespace = 'abc'  # 指定数据表空间（如oracle）
        get_latest_by = time2  # 依据DateField或DateTimeField字段获取最新对象
        managed = True  # 根据模型类自动生成映射的数据库表
        ordering = ["-name", "?num1"]  # 根据哪些字段排序，"-"表示倒序，"?"表示随机
        # order_with_respect_to————多对多关系中，指向一个关联对象，得到get_XXX_order()和set_XXX_order()
        # permissions————添加权限
        # proxy————实现代理
        unique_together = (("name1", "name2"),)  # 通过两个字段保持唯一性

    def __unicode__(self):
        # 将一个（或多个）对象以unicode的方式显示出来（python3.*为__str__）
        return u'%s:%s'(self.name, self.age)

# SQL指定了独特的NULL————表示为未知的、非法的、或其它程序指定的含义。这意味着某个字符型字段的值不可能同时包含NULL和空字符串。

# 如果留空一个字符型字段，它会为此插入一个空字符串（而不是NULL）。
# 但是有例外：日期型、时间型和数字型字段不接受空字符串。
# 在这种情况下，NULL是唯一指定空值的方法。
