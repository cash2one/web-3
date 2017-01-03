# -*- coding: utf-8 -*-
# @Date:   2016-12-22 14:33:23
# @Last Modified time: 2016-12-22 14:33:
#
"""
EmailMessage
django.core.mail.send_mail()————EmailMessage类的一个发送e-mail的函数；
    + 服务器需要配置成能够对外发送邮件，并且在Django中设置出站服务器地址；
更高级的方法，比如附件，多部分邮件，以及对于邮件头部的完整控制；
"""
import random
from django.core.mail import send_mail, send_mass_mail
from cms.settings import DEFAULT_FROM_EMAIL


def send_email_code(address):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    random_list = random.sample(chars, 4)
    security_code = ''
    for i in random_list:
        security_code += i
    # 四个必选参数————主题、正文、寄信人、收件人列表
    send_mail(
        '登录验证',
        '邮箱登录验证码%s' % security_code,
        DEFAULT_FROM_EMAIL,
        [address],
        fail_silently=False
    )
    return security_code
