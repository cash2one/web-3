# -*- coding: utf-8 -*-
# @Date:   2016-12-01 22:46:25
# @Last Modified time: 2017-01-02 21:23:54
#
import os
import platform
debug = True
if platform.system() == "Windows":
    debug = False
BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

###########
# 静态文件
###########
#
# 静态文件查找器
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',       # 从STATICFILES_DIRS目录查找————默认开
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',   # 从INSTALLED_APPS/static目录查找————默认开
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
]
#
# 不属于app的静态文件
STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, "cms/static"),
]
STATIC_ROOT = os.path.join(BASE_DIR, "static")  # 用于部署的绝对路径————默认None
                                                # python manage.py collectstatic————收集static文件并复制到STATIC_ROOT
STATIC_URL = '/static/'                         # 访问STATIC_ROOT静态文件的路径前缀————默认None
                                                # 结尾必须是反斜线（/static/），可以使用网络路径（http://***）
                                                # 可以在html里硬编码/static/，但是此路径可能发生变化，所以最好使用load标签
#
# 静态文件收集引擎
# 如果静态文件与Django在同一台服务器上，将使用默认引擎将静态文件收集到STATIC_ROOT中
# STATIC_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

###########
# 模板文件
###########
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # 模板引擎
        # 'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [                                                      # 为filesystem.Loader添加查找目录，按搜索顺序排列
            os.path.join(BASE_DIR, "cms/test_apps/../../tests/simple/test"),
        ],
        # 'APP_DIRS': True,                                            # 是否在已安装app内查找模板源文件，当loaders存在，APP_DIRS不要设置
        # 'NAME': '',                                                  # 模板引擎别名————在渲染时可以选择一个引擎
        'OPTIONS': {                                                   # 传递给模板引擎的其他参数————不同引擎参数不同
            #
            # 全局context处理器————获取一个request参数，返回一个字典
            # 只要调用RequestContext，全局context中返回的对象都将存储在context中
            #
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                #
                # user————当前登录的用户（如果用户没有登录，是一个 AnonymousUser 实例）
                # perms————一个auth.context_processors.PermWrapper实例，代表当前登录用户所拥有的权限
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'django.template.context_processors.i18n',       # LANGUAGES
                # 'django.template.context_processors.media',
                # 'django.template.context_processors.static',
                # 'django.template.context_processors.tz',
                # 'django.template.context_processors.csrf',       # 填充{% csrf_token %}————默认启用
                # 'myapp.processor.foos',
            ],
            'debug': debug,                                        # 模板调试模式
            'loaders': [                                           # 指定模板加载器
                'django.template.loaders.filesystem.Loader',       # 从TEMPLATE_DIRS目录加载模板————默认开
                'django.template.loaders.app_directories.Loader',  # 从INSTALLED_APPS/templates目录加载模板————默认开
                # 'django.template.loaders.eggs.Loader'            # 从INSTALLED_APPS/template中的egg文件（类似jar包）中加载————默认关
            ],
            'string_if_invalid': '',                               # 找不到变量时模板系统输出的字符串————默认空
        },
    },
]
# 旧版
# TEMPLATE_LOADERS = []
# TEMPLATE_DIRS = []
# TEMPLATE_CONTEXT_PROCESSORS = []
# TEMPLATE_DEBUG = True
# TEMPLATE_STRING_IF_INVALID = ""

###########
# 多媒体文件
###########
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'  # 文件存储中间件
MEDIA_ROOT = ''                                                       # 媒体文件绝对路径
MEDIA_URL = ''                                                        # 媒体文件相对路径
FILE_UPLOAD_HANDLERS = [                                              # 文件上传中间件
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
]
FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440                                 # 文件小于2.5M时，将上传文件内容读进内存，然后写入磁盘
FILE_UPLOAD_TEMP_DIR = None                                           # 存放到系统临时文件夹的路径
FILE_UPLOAD_PERMISSIONS = None                                        # 文件、文件夹权限，没有给出或者是None，将获得独立于系统的行为
FILE_UPLOAD_DIRECTORY_PERMISSIONS = None