# -*- coding: utf-8 -*-
# @Date:   2017-01-02 19:47:40
# @Last Modified time: 2017-01-02 19:59:30
#
# session————会话
#
# 密码哈希算法种子————一个随机字符串————越长越好
SECRET_KEY = '6a8w1=^^n-sj0=n$%gsj@=kk%#bg(943vnt1_vq3@ylhofrp%^'
#
# 是否每次request请求都保存session的内容，默认为False（需要的时候才送出cookie）
SESSION_SAVE_EVERY_REQUEST = False
#
# False————默认————使用SESSION_COOKIE_AGE设置
# True————浏览器关闭时，使cookie失效
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# session cookie在用户浏览器中保持时间————默认两周
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7 * 2
#
# 使用session cookies的站点————默认None————用于单个站点
# 设成一个字符串，如".example.com"————用于跨站点（cross-domain）的cookie
SESSION_COOKIE_DOMAIN = None
#
# 会话中使用的cookie的名字————任意的字符串————客户端用来识别session
# 服务器端session的session_key属性
# 数据库django_session表的主键
SESSION_COOKIE_NAME = "my_session_id"
#
# 是否在session中使用安全cookie
# True————cookie只通过HTTPS来安全传输
SESSION_COOKIE_SECURE = False
#
# session后端存储方式
# 默认使用数据库，manage.py migrate会创建保存会话数据的表
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
# 缓存
# SESSION_ENGINE ='django.contrib.sessions.backends.cache'
# 数据库+缓存
# SESSION_ENGINE ='django.contrib.sessions.backends.cached_db'
# 文件
# SESSION_ENGINE ='django.contrib.sessions.backends.file'
# 使用基于Cookie的会话————会话数据的存储将使用Django加密签名工具和SECRET_KEY设置
# SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
#
# session存储文件路径
SESSION_FILE_PATH = None
#
# 会话的序列化
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

'''
session 的数据存在数据库中

从内部来看，每个session都只是一个普通的Django model（在 django.contrib.sessions.models 中定义)

每个session都由一个随机的32字节哈希串来标识，并存储于cookie中
因为它是一个标准的模型，所以你可以使用Django数据库API来存取session

Session字典接受任何支持序列化的Python对象（参考pickle内建模块的文档）
Session 数据存在数据库表 django_session 中，在需要的时候才会读取
如果你从不使用 request.session ，Django不会动相关数据库表的一根毛

Django session 框架完全而且只能基于cookie，它不会把会话ID编码在URL中（让url难看，也让网站容易受到攻击）
通过 Referer header进行session ID窃听可以实施攻击
'''
