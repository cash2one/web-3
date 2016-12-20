# -*- coding: utf-8 -*-
# @Date:   2016-11-29 20:26:06
# @Last Modified time: 2016-11-29 20:38:11
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
#
# @method_decorator————给类视图添加装饰器
from django.utils.decorators import method_decorator
# @csrf_protect————让表单使用csrf_token
from django.views.decorators.csrf import csrf_protect
# @csrf_exempt————不让表单使用csrf_token
# from django.views.decorators.csrf import csrf_exempt
# @requires_csrf_token————与csrf_protect类似，但不会拒绝传入的请求
# from django.views.decorators.csrf import requires_csrf_token
# 强制视图发送CSRF cookie
# from django.views.decorators.csrf import ensure_csrf_cookie
#
#
# from django.views.decorators.cache import cache_page
from django.views.generic import ListView, View
# from django.views.generic import TemplateView
from base.security.security import create_pwd, create_session
from forms import UserForm
from models import SimpleUser, DownLoad
from common.excelDownload import big_excel_download
#
# Q(x=xxx)|Q(y=yyy)————x=xxx or y=yyy
# from django.db.models import Q
#
# Create your views here.



def login(request, param):
    # 视图函数传递的param————接收url匹配的参数
    # request.GET————获取url?name=param的参数
    if request.method == 'GET':
        fill = {}
        if param:
            # 填充{% csrf_token %}
            fill.update(form=param)
        fill.update(csrf(request))
        # 使用dict.get('key')取值，找不到返回None，不报错
        # 尽量避免使用dict['key']取值
        if request.GET.get('form_name') == "login":
            # 绑定数据到表单————接收一个字典————键对应表单类中的属性
            # us.is_bound————检验表单是否绑定（表单为空————未绑定）
            # 未绑定的表单没有关联的数据，当渲染给用户时，它将为空或包含默认的值
            # 绑定的表单具有提交的数据，可以用来检验数据是否合法
            # 如果渲染一个不合法的绑定的表单，它将包含内联的错误信息，告诉用户如何纠正数据
            us = UserForm(request.GET)
            # us.is_valid————检验表单数据是否合法
            # us.is_valid!=True————带着表单返回到模板，表单不再为空，HTML表单将用之前提交的数据填充，然后可以根据要求编辑并改正它
            # us.is_valid=True————将合法的表单数据放到cleaned_data属性中
            if us.is_valid():
                phone = us.cleaned_data['phone']  # 访问“清洁”的数据
                passwd = us.cleaned_data['passwd']
                # 验证获取的数据，并创建session对象
                if create_session(request, phone, passwd):
                    return HttpResponseRedirect('/base/download_list')
            return HttpResponse("用户名或密码错误")
        return render_to_response('base/login.html', fill)

    elif request.method == 'POST':
        data = None
        if request.POST["form_name"] == "new_register":
            phone = request.POST["phone"]
            passwd = request.POST["passwd"]
            passwd1 = request.POST["passwd1"]
            if not phone or not passwd or not passwd1:
                data = "用户名、密码不能为空"
            else:
                if passwd != passwd1:
                    data = "两次输入密码不一致"
                exist = SimpleUser.objects.filter(phone=phone)
                if exist:
                    data = "此电话号码已经被注册"
                if not data:
                    u = SimpleUser(
                        phone=phone,
                        passwd=create_pwd(passwd),
                    )
                    u.save()
                    data = "注册成功"
                    # return redirect(reverse('/base/download_list'))
            return HttpResponse(data)


class DownloadList(ListView):
    # 存放数据库搜索结果的变量名，用于模板循环
    # context_object_name = "object_list"

    template_name = 'base/download_list.html'

    # 一个页面显示的条目
    paginate_by = 2

    # 定义查询的model
    # model = DownLoad————queryset = DownLoad.objects.all()
    # queryset = DownLoad.objects.all().filter(file_name='255')
    # 重写get_queryset，替换model，利用get参数查询
    def get_queryset(self):
        list_d = DownLoad.objects.all()
        create_name = self.request.GET.get('create_name')
        file_name = self.request.GET.get('file_name')
        address = self.request.GET.get('address')
        if create_name:
            list_d = list_d.filter(create_name=create_name)
        if file_name:
            list_d = list_d.filter(file_name=file_name)
        if address:
            list_d = list_d.filter(address=address)
        return list_d

    # dispatch————类视图接受装饰器
    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super(DownloadList, self).dispatch(*args, **kwargs)

    # 重新get_context_data方法————添加额外的上下文数据
    def get_context_data(self, **kwargs):
        context = super(DownloadList, self).get_context_data(**kwargs)
        # 在上下文数据中添加file_name集合
        # annotate = DownLoad.objects.values('file_name').annotate()
        # context['annotate'] = annotate
        return context

    # def get_object(self, queryset=None):
    #     return get_object_or_404(Product, key=self.kwargs.get('name'))


# excel导出视图
def report_excel(request):
    # 文件名必须unicode
    # 编码一律使用unicode，避免出错
    xlsxname = u"下载信息表"
    titles = [u"文件名", u"创建人", u"下载地址"]
    # 调用DownloadList的get_queryset方法
    d = DownloadList()
    d.__init__(request=request)
    data = d.get_queryset()
    data_fields = []
    for i in data:
        row = [i.file_name, i.create_name, i.address]
        data_fields.append(row)
    # response = excel_download(xlsxname, titles, data_fields)
    response = big_excel_download(xlsxname, titles, data_fields)
    return response


# 基于类的表单处理视图
class AddDownload(View):
    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        return super(AddDownload, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = None
        # request.REQUEST————等于request.GET+request.POST，GET、POST更明确
        file_name = request.POST.get('file_name')
        create_name = request.POST.get('create_name')
        address = request.POST.get('address')
        if not file_name:
            data = "文件名添必填"
        if not create_name:
            data = "添加人必填"
        if not address:
            data = "文件链接必填"
        if not data:
            d = DownLoad(file_name=file_name, create_name=create_name, address=address)
            # save()————保存到数据库
            d.save()
            # 获取增加的这条数据的ID
            # id = d.id
            data = "ok"
        return HttpResponse(data)


# from django.shortcuts import get_object_or_404
# publisher = get_object_or_404(DownLoad, name__iexact=self.args[0])