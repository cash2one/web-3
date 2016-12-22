###自定义验证机制时
- clean()和clean_<field>&()的最后必须返回验证完毕或修改后的值。
- 所有clean函数————如果验证成功则返回值，否则抛出ValidationError错误。如果有值返回，则放入form的cleaned_data字典中。

#####验证顺序
1. full_clean()————依次调用每个field的默认clean()函数————针对max_length，unique等约束进行验证；
2. clean_field_name()————自定义field验证函数————full_clean()都通过后调用；
3. clean()————form的clean()函数————最后调用；
    + 如果到这一步没有ValidationError抛出，那么cleaned_data字典就填满了有效数据；
    + 否则cleaned_data不存在，form的另外一个字典errors填上验证错误；

在template中，每个field获取自己错误的方式是：{{ form.username.errors }}。
如果有错误is_valid()返回False，否则返回True。