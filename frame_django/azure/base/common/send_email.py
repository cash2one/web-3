# -*- coding: utf-8 -*-
# @Date:   2016-12-19 14:33:18
# @Last Modified time: 2016-12-21 09:23:37
import random
# send_mail————每次发邮件都会建立一个连接
# send_mass_mail————建立单个连接发送多封邮件
# 一次性发送多封邮件时 send_mass_mail 要优于 send_mail
from django.core.mail import send_mail, send_mass_mail
from azure.settings import DEFAULT_FROM_EMAIL


def return_a_code(address):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    code = random.sample(chars, 4)
    str_code = ''
    for i in code:
        str_code += i
    #
    # 四个必选参数————主题、正文、寄信人、收件人列表
    send_mail(
        '登录验证',
        '邮箱登录验证码%s' % str_code,
        DEFAULT_FROM_EMAIL,
        [address],
        fail_silently=False
    )
    return str_code
