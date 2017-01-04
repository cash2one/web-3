###调用方式
- as_view()————类方法用来作为类的可调用入口————必须
    + Django的URL解析器将请求和关联的参数发送给一个可调用的函数
- 子类化并在子类中覆盖属性和方法
- 在URLconf 中用as_view()  调用的关键字参数配置类的属性

###TemplateView————仅仅展示一个模板的视图
- template_name————定义要返回的模板
- 不能展示从数据库查询的内容，可以直接传递少量简单的属性到类本身调用as_view方法中
- 调用思路————通过重写get方法，将TemplateResponseMixin，ContextMixin、View联系在一起

```
def get(self, request, *args, **kwargs):
    context = self.get_context_data(**kwargs)
    return self.render_to_response(context)
```
###ListView————用于获取存储在数据库中的某个 Model 的列表
- template_name————指定需要渲染的模板
- paginate_by————一个页面显示的条目
- context_object_name————存放数据库搜索结果的变量名，用于模板循环，默认为object_list
- 数据查询model = ModelName————queryset = ModelName.objects.all()————get_queryset()
    + model————指定查询数据的model（获取表中所有数据）
        * context_object_name = model.objects.all()
    + queryset————定义更复杂的查询语句
        * queryset = ModelName.objects.all().filter(filter_name='***')
    + get_queryset()————重写get_queryset()，替换model，利用GET参数等进行更复杂的查询；
- get_context_data()————重写get_context_data()————添加额外的上下文数据

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
- model、queryset、get_queryset
- get_context_data
- pk_url_kwarg————接收一个来自url中的主键，然后会根据这个主键进行查询
- get_object————默认获取model.objects.filter(id=pk_url_kwarg)，类似ListView中的get_queryset 方法

```
def get_object(self):
    obj = super(ArticleDetailView, self).get_object()
    """
    以markdown形式展现
    """
    obj.body = markdown2.markdown(object.body)
    return obj
```
