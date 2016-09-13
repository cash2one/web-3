# coding:utf-8
from books.models import Publisher, Book
from django.views.generic import TemplateView, DetailView, ListView
from django.shortcuts import get_object_or_404

'''
def detail(request, product_id):
    p = Publisher.objects.get(pk=product_id)  # pk 表示主键

    # 使用传递的第三个参数作为内容渲染detail.html
    return render(request, 'products/detail.html', {'product': p})


def create(request):
    # 检查表单是否提交
    if request.method == 'POST':
        # 类似于RoR的 'create' 动作
        form = ProductForm(request.POST)  # 绑定于POST数据的表单
        if form.is_valid():  # 所有的验证通过
            new_product = form.save()
            return HttpResponseRedirect(new_product.get_absolute_url())
    else:
        # 类似于RoR的 'new' 动作
        form = ProductForm()  # 空的表单

    return render(request, 'products/create.html', {'form': form})
'''

'''
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')  # POST之后重定向
    else:
        form = ContactForm()  # An unbound form

    return render(request, 'contact.html', {'form': form})
'''


class AboutView(TemplateView):
    template_name = "publisher_list.html"


class PublisherDetailView(DetailView):
    template_name = "book_list.html"

    context_object_name = "book_list"

    model = Publisher  # 等价于快速声明的queryset = Publisher.objects.all()

    # model参数指定了视图(view)在哪个数据库模型之上进行操作，但是这个太不灵活了，我们可以使用 queryset参数来指定一个对象列表。
    queryset = Publisher.objects.all()

    # 子类化DetailView然后通过自己的 get_context_data方法的实现一些通用视图没有提供的额外信息。
    # 返回表示模板Context 的字典。传递的关键字参数将组成返回的Context。
    # 所有基于类的通用视图的这个模板Context，都包含一个view变量指向视图实例。
    def get_context_data(self, **kwargs):
        context = super(PublisherDetailView, self).get_context_data(
            **kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = Book.objects.all()
        # context['number'] = random.randrange(1, 100)
        return context

    # def get_object(self, queryset=None):
    #     return get_object_or_404(Product, key=self.kwargs.get('name'))
    # def get_context_data(self, **kwargs):
    #     # 先调用基类函数获取上下文
    #     context = super(ProductDetail, self).get_context_data(**kwargs)

    #     # 在相关产品(product)中添加
    #     context['related_products'] = self.get_object().related_products
    #     return context


class AcmeBookListView(ListView):
    context_object_name = "book_list"
    # 使用 queryset可以定义一个过滤的对象列表
    queryset = Book.objects.filter(publisher__name="Acme Publishing")
    template_name = "books/acme_list.html"

    # ListView 有一个 get_queryset() 方法来供我们重写在给定的列表页面中根据URL中的关键字来过滤对象。
    def get_queryset(self):
        publisher = get_object_or_404(Publisher, name__iexact=self.args[0])
        return Book.objects.filter(publisher=publisher)
