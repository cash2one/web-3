# -*- coding: utf-8 -*-
# @Date:   2016-12-22 21:14:08
# @Last Modified time: 2017-01-02 19:41:10
#
LANGUAGE_CODE = 'zh-Hans'    # 语言设置，默认'en-us'，'zh-cn'，旧版
TIME_ZONE = 'Asia/Shanghai'  # 时区————timezone时间
                             # 'America/Chicago'————美国/芝加哥
                             # 'UTC'————格林尼治
                             # 模板渲染的时候，使用 TIME_ZONE 中的设置自动把 UTC 时间转成 TIME_ZONE 所在时区的时间
USE_I18N = True              # 国际化————为了软件在任何地区的潜在使用而进行程序设计的过程
                             # 字符串均翻译成与地域无关的显示控制值，如时间和日期（会增加一点运行开销）
USE_L10N = True              # 本地化
USE_TZ = True                # 使用当前地区特定的格式，来展示日期、时间和数字
                             # 处理表单中输入的本地化
# USE_TZ = False             # 不用django的时区设置，数据库里是什么就是什么
#
# timezone.now()————UTC时间
# timezone.localtime(timezone.now())————本地时间
#
# LOCALE_PATHS = []          # 翻译文件所在目录
