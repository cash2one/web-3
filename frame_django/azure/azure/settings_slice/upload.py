# -*- coding: utf-8 -*-
# @Date:   2016-10-10 14:57:04
# @Last Modified time: 2016-11-29 10:13:44
#
# 文件存储中间件
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
#
# 媒体文件绝对路径
MEDIA_ROOT = ''
#
# 媒体文件相对路径
MEDIA_URL = ''
#
# 文件上传中间件
FILE_UPLOAD_HANDLERS = [
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
]
#
# 文件小于2.5M时，django会将上传文件的全部内容读进内存，然后写入磁盘
FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440
#
# 文件大于2.5M时，django会把上传文件的临时文件
# 然后存放到系统临时文件夹中
FILE_UPLOAD_TEMP_DIR = None
#
# 文件、文件夹权限
# 没有给出或者是None，将获得独立于系统的行为
FILE_UPLOAD_PERMISSIONS = None
FILE_UPLOAD_DIRECTORY_PERMISSIONS = None
