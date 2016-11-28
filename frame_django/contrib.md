###django.contrib包————Django自带的很多优秀附加组件
- 管理工具（django.contrib.admin）
- 用户鉴别系统（django.contrib.auth）
- 支持匿名会话（django.contrib.sessioins）
- 用户评注系统（django.contrib.comments）
- 这些配置是可选的，可以在INSTALLED_APPS中添加。

django.contrib是一套庞大的功能集，它是Django基本代码的组成部分，Django框架就是由众多包含附加组件(add-on)的基本代码构成的。


把'django.contrib.auth'加进INSTALLED_APPS后，第一次运行syncdb命令时, 系统会请你创建一个超级用户。  
将admin访问配置在URLconf(url(r'^admin/', admin.site.urls))中。  

Django管理工具是否被翻译成你想要的语言：
添加`django.middleware.locale.LocaleMiddleware`到`MIDDLEWARE_CLASSES`设置中，并确保它在`django.contrib.sessions.middleware.SessionMiddleware`之后。  
将Models加入到Admin管理中：  
from django.contrib import admin  
from mysite.books.models import mcj  

admin.site.register(mcj)将模块注册到管理工具中。  

class mcjAdmin(admin.ModelAdmin):  
    list_display = ('column1', 'column2', 'column3')  
    search_fields = ('column1', 'column2')  
    list_filter = ('column1',)  
    ordering = ('-publication_date',)  
    fields = ('column1', 'column2', ...)  
    filter_horizontal = ('column1',...)  
    raw_id_fields = ('column1',)  

admin.site.register(mcj, mcjAdmin)  

- list_display，它是一个字段名称的元组，用于列表显示。当然，这些字段名称必须是模块中有的。配合register()的第二个参数，显示出除__unicode__之外的字段。
- search_fields()，添加一个快速查询栏。
- list_filter()，用字段元组创建过滤器。Django为日期型字段提供了快捷过滤方式，它包含：今天、过往七天、当月和今年。
- date_hierarchy接受一个字符串*，对一个日期型字段进行层次划分。修改好后，页面中的列表顶端会有一个逐层深入的导航条。
- ordering选项基本像模块中class Meta的ordering那样工作，但它只用列表中的第一个字段名。如果要实现降序，仅需在传入的列表或元组的字段前加上一个减号(-)。
- fields选项，改变表单中的字段顺序。  
- filter_horizontal，在这个元组中指定每个多对多字段的名字。
- filter_vertical，它像filter_horizontal那样工作，但控件都是垂直排列。
- filter_horizontal和filter_vertical选项只能用在多对多字段上，而不能用于ForeignKey字段。默认地，管理工具使用`下拉框`来展现`外键`字段。但是，正如`多对多字段`那样，有时候你不想忍受因装载并显示这些选项而产生的大量开销，以致于添加页面装载时间较久。解决这个问题的办法是使用`raw_id_fields`选项。它是一个包含外键字段名称的元组，它包含的字段将被展现成`文本框`，而不再是`下拉框`。
- admin.site.register()函数接受一个ModelAdmin子类作为第二个参数。如果你忽略第二个参数，Django将使用默认的选项。
-   

