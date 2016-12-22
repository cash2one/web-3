# -*- coding: utf-8 -*-
# @Date:   2016-12-22 14:33:23
# @Last Modified time: 2016-12-22 14:33:45
import random
from django.core.mail import send_mail, send_mass_mail
from cms.settings import DEFAULT_FROM_EMAIL


def send_email_code(address):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    random_list = random.sample(chars, 4)
    security_code = ''
    for i in random_list:
        security_code += i
    send_mail(
        '登录验证',
        '邮箱登录验证码%s' % security_code,
        DEFAULT_FROM_EMAIL,
        [address],
        fail_silently=False
    )
    return security_code
