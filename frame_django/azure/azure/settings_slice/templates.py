# -*- coding: utf-8 -*-
# @Date:   2016-11-28 11:03:52
# @Last Modified time: 2016-12-08 13:28:48
#
import os
import platform
debug = True
if platform.system() == "Windows":
    debug = False
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TEMPLATES = [
    {
        # 模板引擎
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'BACKEND': 'django.template.backends.jinja2.Jinja2',

        # 为filesystem.Loader添加查找目录，按搜索顺序排列
        'DIRS': [],
        #
        # 是否在已安装app内查找模板源文件
        # 当loaders存在，APP_DIRS不要设置
        # 'APP_DIRS': True,
        #
        # 模板引擎别名————在渲染时可以选择一个引擎
        # 'NAME': '',
        #
        # 传递给模板引擎的其他参数————不同引擎参数不同
        'OPTIONS': {
            # 全局context处理器————上下文调用函数————获取一个request对象作为参数，返回一个字典
            # 只要调用RequestContext，默认处理器中返回的对象都将存储在context中
            # 省去每次使用 RequestContext 都指定 processors 的麻烦
            'context_processors': [
                #
                # debug————True
                # sql_queries————[{'sql': ..., 'time':
                # ...},...]————请求期间到目前为止每个SQL 查询及花费的时间————按查询的顺序排序
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                #
                # user————当前登录的用户（如果用户没有登录，是一个 AnonymousUser 实例）
                # perms————一个auth.context_processors.PermWrapper实例，代表当前登录用户所拥有的权限
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #
                # LANGUAGES
                # 'django.template.context_processors.i18n',
                # 'django.template.context_processors.media',
                # 'django.template.context_processors.static',
                # 'django.template.context_processors.tz',
                #
                # 填充{% csrf_token %}————默认启用
                # 'django.template.context_processors.csrf',
                # 'myapp.processor.foos',
            ],
            # 打开模板调试模式————显示错误详情报告的页面
            'debug': debug,
            # 指定模板加载器
            'loaders': [
                # 从TEMPLATE_DIRS目录加载模板————默认开
                'django.template.loaders.filesystem.Loader',
                # 从每一个INSTALLED_APPS/templates目录加载模板————默认开
                'django.template.loaders.app_directories.Loader',
                # 从INSTALLED_APPS/template中的egg文件（类似jar包）中加载————默认关
                # 'django.template.loaders.eggs.Loader'
            ],
            # 当使用了不可用变量时模板系统输出的字符串————默认空
            'string_if_invalid':'',
        },
    },
]
# 旧版
# TEMPLATE_LOADERS = []
# TEMPLATE_DIRS = []
# TEMPLATE_CONTEXT_PROCESSORS = []
# TEMPLATE_DEBUG = True
# TEMPLATE_STRING_IF_INVALID = ""
