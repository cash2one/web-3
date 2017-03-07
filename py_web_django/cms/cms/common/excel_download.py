# -*- coding: utf-8 -*-
# @Date:   2016-12-15 17:47:00
# @Last Modified time: 2016-12-15 17:47:28
#
# 导出excel公共方法
#
# xlsxwriter————生成、写入xlsx文件————操作xls会导致无法读取文件
# xlwt————生成、写入xls文件————操作xlsx会导致无法读取文件
# 运行脚本的时候不要开着excel文件

import xlsxwriter
import os
'''
使用codecs打开文件————必须
'''
import codecs
from django.http import HttpResponse, StreamingHttpResponse
from django.utils import timezone

# 指定settings————参考manage.py
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "azure.settings")

filepath = os.path.join(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )
    ), "temp\excel_temp\\")

# 显示本地时间
reportTime = timezone.localtime(timezone.now()).strftime("%Y-%m-%d")


# 生成excel，返回文件路径全称
def createExcel(xlsxname, titles, data_fields):
    # 尽量使用os连接连接，不要自己拼接字符串
    filename = os.path.join(filepath, reportTime + xlsxname + ".xlsx")
    # filename = filepath + reportTime + xlsxname + ".xlsx"
    # 创建（打开）工作薄
    workbook = xlsxwriter.Workbook(filename)
    # 创建工作表
    worksheet = workbook.add_worksheet()
    # 写入数据————worksheet.write(row, col, data)
    # 表头
    # 下标循环enumerate()————把一个list变成索引--元素对，在for循环中同时迭代索引和元素本身
    for col, title in enumerate(titles):
        worksheet.write(0, col, title)
        # worksheet.write(0, col, unicode(title, 'utf-8'))
    row = 1
    for data in data_fields:
        for col, value in enumerate(data):
            worksheet.write(row, col, value)
        row += 1
    workbook.close()
    return filename


# 文件流传输到浏览器，通常会以乱码形式显示到浏览器中
# 添加响应头，让文件流写入硬盘
def addResponseHeader(response, the_file_name):
    # 二进制流————pdf、xlsx等
    response['Content-Type'] = 'application/octet-stream'
    # excel————xls
    # response['Content-Type'] = 'application/vnd.ms-excel'
    '''
    文件传输时中文文件名转码————必须
    '''
    response['Content-Disposition'] = 'attachment; filename={0}'.format(the_file_name.encode('utf8'))
    return response


# 最简单的文件下载功能————将文件流放入HttpResponse对象
# 这种方式会占用大量的内存，适合小文件的下载
def excel_download(xlsxname, titles, data_fields):
    whole_file_name = createExcel(xlsxname, titles, data_fields)
    with codecs.open(whole_file_name) as f:
        c = f.read()
    response = HttpResponse(c)
    the_file_name = os.path.split(whole_file_name)[1]
    return addResponseHeader(response, the_file_name)


# 将下载功能优化为对大小文件均适合
def big_excel_download(xlsxname, titles, data_fields):
    whole_file_name = createExcel(xlsxname, titles, data_fields)

    def file_iterator(file_name, chunk_size=512):
        with codecs.open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    # StreamingHttpResponse————将迭代器作为传入参数，将文件流发送给浏览器
    response = StreamingHttpResponse(file_iterator(whole_file_name))
    the_file_name = os.path.split(whole_file_name)[1]
    return addResponseHeader(response, the_file_name)
