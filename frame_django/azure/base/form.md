###自定义验证机制时
- clean()和clean_<field>&()的最后必须返回验证完毕或修改后的值。
- 所有clean函数————如果验证成功则返回值，否则抛出ValidationError错误。如果有值返回，则放入form的cleaned_data字典中。

#####验证顺序————full_clean()依次调用其它clean函数
1. _clean_fields()————针对每个field默认的max_length，unique等属性进行验证；
2. clean_field_name()————自定义field验证函数————full_clean()都通过后调用；
3. clean()————_clean_form()————最后调用————如果1没有通过，忽略第2步，进行第3步；
    + 如果到这一步没有ValidationError抛出，那么cleaned_data字典就填满了有效数据；
    + 否则cleaned_data不存在，form的另外一个字典errors填上验证错误；

在template中，每个field获取自己错误的方式是：{{ form.username.errors }}。
如果有错误is_valid()返回False，否则返回True。


####绑定数据到表单————接收一个字典————键对应表单类中的属性————us = UserForm(request.GET)
- us.is_bound————检验表单是否绑定
    + 未绑定的表单没有关联的数据，渲染时，表单为空或包含默认的值
    + 绑定的表单具有提交的数据，可以用来检验数据是否合法
    + 如果渲染一个不合法的绑定的表单，页面反馈ValidationError错误信息
- us.is_valid()————检验表单数据是否合法
    + us.is_valid!=True————带着表单返回到模板，表单不再为空，HTML表单将用之前提交的数据填充，然后可以根据要求编辑并改正它
    + us.is_valid=True————将合法的表单数据放到cleaned_data属性中