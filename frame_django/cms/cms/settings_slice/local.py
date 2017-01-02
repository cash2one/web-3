# -*- coding: utf-8 -*-
# @Date:   2016-12-22 21:14:08
# @Last Modified time: 2017-01-02 19:41:10
#
# 语言设置，默认'en-us'
LANGUAGE_CODE = 'zh-Hans'  # 'zh-cn'，旧版
#
# 时区————timezone时间
# 'America/Chicago'————美国/芝加哥
# 'UTC'————格林尼治
# 模板展示的时候，使用 TIME_ZONE 中的设置自动把 UTC 时间转成 TIME_ZONE 所在时区的时间渲染
TIME_ZONE = 'Asia/Shanghai'
#
# 国际化————为了软件在任何地区的潜在使用而进行程序设计的过程
# 字符串均翻译成与地域无关的显示控制值，如时间和日期
# 会给Django的运行增加一点点开销
USE_I18N = True
#
# 本地化
# 使用当前_地区_特定的格式，来展示日期、时间和数字
# 处理表单中输入的本地化
USE_L10N = True
#
# 保证存储到数据库中的是 UTC
# 在函数之间传递时间参数时，时间已经转换成 UTC 时间
# 直接print显示是 UTC 时间
USE_TZ = True
# timezone.now()————UTC时间
# timezone.localtime(timezone.now())————本地时间
# 不用django的时区设置，数据库里是什么就是什么
# USE_TZ = False
#
# 翻译文件所在目录，需要手工创建
# LOCALE_PATHS = []
