导入models类
###insert
- m = MODEL(name='ZDD', num1=26)
- m.save()————更新表，必须
- m.id————获取这条数据的id

---
- MODEL.objects.create(name='zd', num1=16)
- MODEL.save()

###select（可以连锁查询）
- 获取所有查询结果————QuerySet -> list比列出所有字段慢
    + select_all = MODEL.objects.all()————SELECT `*`
    + 列出所有字段遵循了Python的一个信条：明言胜于暗示
- 限制返回的数据（不支持负索引）
    + select_all_limit1 = MODEL.objects.all()[0]
    + select_all_offset1_limit2 = MODEL.objects.all()[1:3]
- 获取某列值
    + select_column = MODEL.name
- 数据过滤
    + select_all_where = MODEL.objects.filter(name='xx')
    + select_all_where_and = MODEL.objects.filter(name='xx', num1=xx)
    + select_all_where_like = MODEL.objects.filter(name_contains='xx')
    + select_all_where_like_'xxx%' = MODEL.objects.filter(name_contains)
    + select_all_where_lower_upper_like = MODEL.objects.filter(name_startwith='xx')
    + select_all_where_between = MODEL.objects.filter(range_time2(123456, 123666))
- 排序————默认根据classMeta的ordering排序
    + select_all_order_by = MODEL.objects.order_by('name', '-num1')
- 去重
    + select_all_distinct = MODEL.objects.distinct()
- 获取单个dict对象————多于一个或者没有，抛出异常：DoesNotExist
    + select_one = MODEL.objects.get(name='zd')
    + select_one_value = MODEL.objects.get(name='zd').num1
- 精确更新 -> int————受影响的记录条数
    + update_set_where = MODEL.objects.filter(name='zd').update(num1='100')

#####为了预防误删除掉某一个表内的所有数据，Django要求在删除表内所有数据时使用all()
delete_all = MODEL.objects.all().delete()
delete_one_line = MODEL.objects.get(name='zd').delete()

'''
在你视图的任何位置，临时插入一个 assert False 来触发出错页。
然后，你就可以看到局部变量和程序语句了。
Django 出错信息仅在 debug 模式下才会显现。
'''
