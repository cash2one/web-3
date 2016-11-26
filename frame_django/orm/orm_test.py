# -*- coding: utf-8 -*-
# @Date:   2016-10-11 13:31:06
# @Last Modified time: 2016-10-11 15:12:29
#
# 导入对应数据库的models类
from models import Person
# 可以连锁查询

# 创建对象并存储至数据库————insert
m = Person(name='ZDD', num1=26)
m.save()
Person.objects.create(name='zd', num1=16)
Person.save()  # 更新表

#
# 获取所有查询结果————QuerySet -> list
#
# SELECT `*`比列出所有字段慢
# 列出所有字段遵循了Python的一个信条：明言胜于暗示。
select_all = Person.objects.all()
# 限制返回的数据
# 不支持负索引
select_all_limit1 = Person.objects.all()[0]
select_all_offset1_limit2 = Person.objects.all()[1:3]

# 获取某列值
select_column = Person.name
# 数据过滤
select_all_where = Person.objects.filter(name='zd')
select_all_where_and = Person.objects.filter(name='zd', num1=16)
select_all_where_like = Person.objects.filter(name_contains='zd')
select_all_where_lower_upper_like = Person.objects.filter(name_icontains='zd')
select_all_order_by = Person.objects.order_by(
    'name', '-num1')  # 默认根据classMeta的ordering排序
select_all_distinct = Person.objects.distinct()  # 去重
select_all_where_between = Person.objects.filter(range_time2(123456, 123666))
#
# 获取单个对象 -> dict
#
# 多于一个或者没有，抛出异常：DoesNotExist
select_one = Person.objects.get(name='zd')
select_one_value = Person.objects.get(name='zd').num1

# 精确更新 -> int————受影响的记录条数
update_set_where = Person.objects.filter(name='zd').update(num1='100')

# 为了预防误删除掉某一个表内的所有数据，Django要求在删除表内所有数据时使用all()
delete_all = Person.objects.all().delete()
delete_one_line = Person.objects.get(name='zd').delete()

'''
在你视图的任何位置，临时插入一个 assert False 来触发出错页。
然后，你就可以看到局部变量和程序语句了。
Django 出错信息仅在 debug 模式下才会显现。
'''
