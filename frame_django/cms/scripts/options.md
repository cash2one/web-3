导入models类

###QuerySet
- lazy evaluation（惰性评估）————用的时候才真正的去数据库查
- 查看queryset执行的 SQL
    + str(QuerySet.query)
    + QuerySet.query.__str__()

###insert
- 方法1
    + m = MODEL(field="***",...)
    + m.save()————更新表，必须
    + m.id————获取这条数据的id
- 方法2
    + MODEL.objects.create(field='***', ...)
    + MODEL.save()

###精确更新 -> int————受影响的记录条数
update_set_where ———— MODEL.objects.filter(field='zd').update(num1='100')

###select（可以连锁查询）
- 获取所有查询结果————QuerySet
    + select_all ———— MODEL.objects.all()
- 限制返回的数据（不支持负索引）
    + select_all_limit1 ———— MODEL.objects.all()[1]
    + select_all_limit3_offset1 ———— MODEL.objects.all()[1:3]
- 获取某列值
    + select_column ———— MODEL.field
- 排序————默认根据classMeta的ordering排序
    + select_all_order_by ———— MODEL.objects.order_by('field', '-num1')
- 获取单个dict对象————多于一个或者没有，抛出异常：DoesNotExist
    + select_one ———— MODEL.objects.get(field='zd')
    + select_one_value ———— MODEL.objects.get(field='zd').num1

select *比列出所有字段慢，列出所有字段遵循了Python的一个信条：明言胜于暗示
#####查询函数
|  查询函数  | 含义 |                              示例                             |
|------------|------|---------------------------------------------------------------|
| filter()   | =    | select__where[_and]————MODEL.objects.filter(field='***', ...) |
| exclude()  | !=   |                                                               |
| distinct() | 去重 | select__distinct————MODEL.objects.distinct()                  |

#####查询参数
|    查询参数   |            含义            |                      示例                      |
|---------------|----------------------------|------------------------------------------------|
| __exact       | =                          |                                                |
| __iexact      | =（忽略大小写）            | MODEL.objects.filter(field__iexact='**')       |
| __contains    | like BINARY '%**%'         | MODEL.objects.filter(field__contains='**')     |
| __icontains   | like '%**%'（忽略大小写 ） |                                                |
|               | 对于sqlite等同于icontains  |                                                |
| __gt          | >                          |                                                |
| __gte         | >=                         |                                                |
| __lt          | <                          |                                                |
| __lte         | <=                         |                                                |
| __in          | in(list范围)               |                                                |
| __startswith  | 以...开头                  |                                                |
| __istartswith | 以...开头，忽略大小写      |                                                |
| __endswith    | 以...结尾                  |                                                |
| __iendswith   | 以...结尾，忽略大小写      |                                                |
| __range       | select__where_between      | MODEL.objects.filter(field__range('**', '**')) |
| __year        | 日期字段年份               |                                                |
| __month       | 日期字段月份               |                                                |
| __day         | 日期字段的日               |                                                |
| __isnull      | True/False                 |                                                |

#####为了预防误删除掉某一个表内的所有数据，Django要求在删除表内所有数据时使用all()
delete_all ———— MODEL.objects.all().delete()
delete_one_line ———— MODEL.objects.get(field='zd').delete()

'''
在你视图的任何位置，临时插入一个 assert False 来触发出错页。
然后，你就可以看到局部变量和程序语句了。
Django 出错信息仅在 debug 模式下才会显现。
'''

###ValuesQuerySet————QuerySet的子集，返回[dict, dict, ...]（不是真正的列表 或 字典）
|            函数            |                            含义                           |
|----------------------------|-----------------------------------------------------------|
| vlaues()单条/多条记录      | <class 'dict'> /<class 'django.db.models.query.QuerySet'> |
| vlaues_list()单条/多条记录 | <class 'tuple'>/<class 'django.db.models.query.QuerySet'> |

