# -*- coding: utf-8 -*-
# @Date:   2016-10-10 14:07:36
# @Last Modified time: 2016-10-11 15:11:17
# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/
#
# 语言设置，默认'en-us'
#
LANGUAGE_CODE = 'zh-Hans'  # 'zh-cn'，旧版
#
# 时区
# 默认'America/Chicago'————美国/芝加哥
# 'UTC'————格林尼治
#
TIME_ZONE = 'Asia/Shanghai'
#
# 国际化————为了该软件在任何地区的潜在使用而进行程序设计的过程
# 字符串均翻译成与地域无关的显示控制值，如时间和日期
# 会给Django的运行增加一点点开销
#
USE_I18N = False
#
# 翻译文件所在目录，需要手工创建
#
LOCALE_PATHS = []
#
# 本地化
# 使用当前_地区_特定的格式，来展示日期、时间和数字
# 处理表单中输入的本地化
#
USE_L10N = False
#
# 所有的存储和内部处理，甚至包括直接print显示全都是UTC的
#
USE_TZ = True
