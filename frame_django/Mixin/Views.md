所有基于类的视图中定义的方法需要在类视图调用 as_view() 方法后被自动调用，因为 Django 的 URL 解析器将请求和关联的参数发送给一个可调用的函数而不是一个类，所以基于类的视图有一个 as_view() 类方法用来作为类的可调用入口。

###TemplateView————仅仅展示一个模板的视图
- 可以方便的定义要返回的模板但它不能把数据库中的内容查询展示出来。
- 可以直接传递少量简单的属性到类本身调用 as_view 方法中。

TemplateView继承自TemplateResponseMixin，ContextMixin以及View，所以它的调用思路————重写get方法，然后通过get方法将上面三个东西联系在一起。
```
class TemplateView(TemplateResponseMixin, ContextMixin, View):
    """
    A view that renders a template.  This view will also pass into the context
    any keyword arguments passed by the url conf.
    """
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
```
###ListView————用于获取存储在数据库中的某个 Model 的列表
- template_name————指定需要渲染的模板
- context_object_name————指定模板中使用的上下文变量名（默认"object_list"）
- model————指定数据的来源（获取表中所有数据）————context_object_name = model.objects.all()
- get_queryset
- get_context_data

取出指定 model 中的所有数据，指定变量名后传递给指定模板。

当需要使用过滤条件或者对数据进行一定的操作时，则需要重写 ListView 中获取数据的方法（get_queryset 方法）。

```
    def get_queryset(self):
        """
            重写 get_queryset 方法，取出发表的文章并转换文章格式
        """
        article_list = Article.objects.filter(status='p')
        for article in article_list:
            article.body = markdown2.markdown(article.body, extras=['fenced-code-blocks'], )
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        return super(IndexView, self).get_context_data(**kwargs)
```

###DetailView————获取每个数据的详细信息
- template_name
- context_object_name
- model
- get_context_data
- pk_url_kwarg————定义用来获取对应的单条数据，需要传递主键的值
- et_object————获取 pk_url_kwarg 中所要查找的对象，类似于 ListView 中的 get_queryset 方法
