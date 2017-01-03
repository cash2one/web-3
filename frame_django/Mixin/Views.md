###调用方式
- as_view()————类方法用来作为类的可调用入口————必须
    + Django的URL解析器将请求和关联的参数发送给一个可调用的函数
- 子类化并在子类中覆盖属性和方法
- 在URLconf 中用as_view()  调用的关键字参数配置类的属性

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
- paginate_by————一个页面显示的条目
- context_object_name————存放数据库搜索结果的变量名，用于模板循环，默认为object_list
- 数据查询model = ModelName————queryset = ModelName.objects.all()————et_queryset()
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
- model
- get_context_data
- pk_url_kwarg————定义用来获取对应的单条数据，需要传递主键的值
- get_object————获取 pk_url_kwarg 中所要查找的对象，类似于 ListView 中的 get_queryset 方法