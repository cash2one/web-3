# -*- coding: utf-8 -*-
# @Date:   2016-12-19 14:33:18
# @Last Modified time: 2016-12-19 14:36:43
import random
# send_mail 每次发邮件都会建立一个连接，发多封邮件时建立多个连接
# send_mass_mail 是建立单个连接发送多封邮件
# 所以一次性发送多封邮件时 send_mass_mail 要优于 send_mail
from django.core.mail import send_mail, send_mass_mail


def return_a_code(address):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    code = random.sample(chars, 4)
    str = ''
    for i in code:
        str += i
    #
    # 四个必选参数————主题、正文、寄信人、收件人列表
    send_mail(
        '登录验证',
        '邮箱登录验证码%s'% str,
        '2271404280@qq.com',
        [address],
        fail_silently=False
    )
    return str

