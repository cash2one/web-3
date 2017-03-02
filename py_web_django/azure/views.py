# -*- coding: utf-8 -*-
# @Date:   2016-11-29 20:26:06
# @Last Modified time: 2017-01-03 15:54:21
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
#
# @method_decorator————给类视图添加装饰器
from django.utils.decorators import method_decorator
#

from django.views.generic import ListView, View
# from django.views.generic import TemplateView
from login.common.security import create_pwd, create_session
from login.forms import UserForm
from login.models import SimpleUser, DownLoad
from base.common.excelDownload import big_excel_download


class DownloadList(ListView):

    template_name = 'login/download_list.html'

    # model = DownLoad————queryset = DownLoad.objects.all()
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
            d = DownLoad(file_name=file_name,
                         create_name=create_name, address=address)
            # save()————保存到数据库
            d.save()
            # 获取增加的这条数据的ID
            # id = d.id
            data = "ok"
        return HttpResponse(data)


# from django.shortcuts import get_object_or_404
# publisher = get_object_or_404(DownLoad, name__iexact=self.args[0])
