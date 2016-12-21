from django.contrib.auth.hashers import *
from login.models import *


def create_pwd(ps):
    return make_password(ps, None, 'pbkdf2_sha256')


def check_pwd(phone, ps):
    try:
        u = SimpleUser.objects.get(phone=phone)
    except Exception, e:
        return False
    pwd_bool = check_password(ps, u.passwd)
    return pwd_bool


def create_session(request, phone, passwd):
    if check_pwd(phone, passwd):
        request.session['phone'] = phone
        request.session['passwd'] = passwd
        return True
    return False
