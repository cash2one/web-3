# -*- coding: utf-8 -*-
# @Date:   2016-10-10 11:38:22
# @Last Modified time: 2016-10-11 11:40:38
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
# 打开/关闭模板调试模式
# 如果值是True，在模板渲染期间，抛出任何异常都将显示一个可爱的、详情报告的错误页面。
# 该页面包含该模板相关的代码段，并且使用适当的行高亮
#
TEMPLATE_DEBUG = False
#
# 当使用了不可用变量时模板系统输出的字符串
#
TEMPLATE_STRING_IF_INVALID = 'invalid'
TEMPLATES = [
    {
        #
        # 使用的模板引擎
        #
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'BACKEND': 'django.template.backends.jinja2.Jinja2',
        #
        # 模板引擎的别名
        #
        'NAME': '',
        #
        # 查找模板源文件的目录，按搜索顺序排列
        #
        'DIRS': [],
        #
        # 是否在已安装app内查找模板源文件
        #
        'APP_DIRS': True,
        #
        # 传递给该模板引擎（backend）的其他参数
        #
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
#
# 填充在RequestContext中的上下文的调用函数
# 这些函数获取一个request对象作为它的参数，返回一个将要填充至上下文项目的字典
# 省去每次使用 RequestContext 都指定 processors 的麻烦
#
TEMPLATE_CONTEXT_PROCESSORS = [
    'django.contrib.auth.context_processors.auth',
    'django.template.context_processors.debug',
    'django.template.context_processors.i18n',
    'django.template.context_processors.media',
    'django.template.context_processors.static',
    'django.template.context_processors.tz',
    # 'django.template.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'myapp.processor.foos',
    # 只要是调用的RequestContext，那么默认处理器中返回的对象都就将存储在context中
]
#
# 指定模板加载器————loader类型
#
TEMPLATE_LOADERS = [
    #
    # 从TEMPLATE_DIRS路径中加载模板
    #
    'django.template.loaders.filesystem.Loader',
    #
    # 在每一个INSTALLED_APPS注册的app目录下寻找templates子目录
    #
    'django.template.loaders.app_directories.Loader',
    # django.template.loaders.eggs.Loader————默认关闭，从app子目录template中加载egg文件中的模板
    # egg文件类似jar包，python中打包发布代码的一种方式
]
#
# 加载静态模板
#
TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, "templates"),
]
