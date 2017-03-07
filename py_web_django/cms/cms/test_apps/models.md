###models
- 表名————app名称和模型的小写名称的组合
- 为每个表格自动添加一个id主键，可以重设（AutoField，自增整型）
- 添加 "_id" 后缀到外键字段名
- Django会自动适时将verbose_name首字母大写
- ManyToManyField和ForeignKey字段，第一个参数必须是模块类。因此，必须显式使用verbose_name这个参数名称。

IntegerField会忽略max_length

###默认值
- django会自动设置默认值（NOT NULL，""）；
- 时间、数字不接受空字符串，在这种情况下，NULL是唯一指定空值的方法；
    + blank=True————表单字段允许为NULL（默认是""）；
    + null=True————空值存储为NULL（不是""）————需要更新数据库，删除NOT NULL；
    + 数字型————IntegerField、BigIntegerField、DecimalField、FloatField(blank=True, null=True)；
        * IntegerField对应int类型，最多支持11位（实际是10）；
    + 时间型————TimeField、DateTimeField、DateField(blank=True, null=True)；
        * auto_now=True————默认当前但是不可修改；
        * auto_now_add=True————对象第一次被创建时自动设置当前时间；
        * default=timezone.now()————默认当前时间，但是可以更改；
        * 上述三者互斥；
- 布尔型字段————不能为null，必须指定默认值————BooleanField();
- 新添加字段后，必须设置默认值，才能同步；

ALTER TABLE tab_name ALTER COLUMN column_name DROP NOT NULL;

###内部类（class Meta）

|                   属性                  |                     含义                     |
|-----------------------------------------|----------------------------------------------|
| index_together = [["...", "..."],]      | 设置带有索引的字段组合，列表可以一维         |
| abstract = True                         | 抽象类————不会对应数据库表                   |
| app_label = 'my_app'                    | 当模型不在app包里时，指定模型类属于哪个app   |
| db_tablespace = 'abc'                   | 指定数据表空间（如oracle）                   |
| get_latest_by = time2                   | 依据DateField或DateTimeField字段获取最新对象 |
| managed = True                          | 根据模型类自动生成映射的数据库表             |
| order_with_respect_to                   | 多对多关系中，指向一个关联对象               |
|                                         | 得到get_XXX_order()和set_XXX_order()         |
| proxy                                   | 实现代理                                     |
| unique_together = (("name1", "name2"),) | 通过两个字段保持唯一性                       |
| default_related_name                    | 用于一个关联对象到当前对象的关系             |
| select_on_save                          | 默认为False，是否查询正在更新的行            |


```
class mcjAdmin(admin.ModelAdmin):
    ordering = ('-publication_date',)
    fields = ('column1', 'column2', ...)
    filter_horizontal = ('column1',...)
    raw_id_fields = ('column1',)
admin.site.register(mcj, mcjAdmin)
```
- date_hierarchy接受一个字符串*，对一个日期型字段进行层次划分。修改好后，页面中的列表顶端会有一个逐层深入的导航条。
- ordering选项基本像模块中class Meta的ordering那样工作，但它只用列表中的第一个字段名。如果要实现降序，仅需在传入的列表或元组的字段前加上一个减号(-)。
- fields选项，改变表单中的字段顺序。
- filter_horizontal，在这个元组中指定每个多对多字段的名字。
- filter_vertical，它像filter_horizontal那样工作，但控件都是垂直排列。
- filter_horizontal和filter_vertical选项只能用在多对多字段上，而不能用于ForeignKey字段。默认地，管理工具使用`下拉框`来展现`外键`字段。但是，正如`多对多字段`那样，有时候你不想忍受因装载并显示这些选项而产生的大量开销，以致于添加页面装载时间较久。解决这个问题的办法是使用`raw_id_fields`选项。它是一个包含外键字段名称的元组，它包含的字段将被展现成`文本框`，而不再是`下拉框`。