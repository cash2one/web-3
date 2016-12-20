# -*- coding: utf-8 -*-
# @Date:   2016-12-20 09:43:22
# @Last Modified time: 2016-12-20 09:44:20
#
from django.db import models
#
# django自带的用户登录信息模型————AUTH_USER_MODEL = 'auth.User'
# 修改方式————继承、扩展、自定义
# 在创建任何迁移或者第一次运行 manage.py migrate 前设置它
# from django.contrib.auth.models import User
#
# 引用User模型————如果直接引用User（例如：通过一个外键引用它），代码将不能工作
# from django.contrib.auth import get_user_model


class AbstractUser(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """
    username_validator = UnicodeUsernameValidator() if six.PY3 else ASCIIUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)


'''
class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.
    Username, password and email are required. Other fields are optional.
    """
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
'''

# 扩展自带User————存储新字段到已有的User里
class UserProfile(models.Model):
    # OneToOneField————关联到一个存储额外信息的Model
    user = models.OneToOneField(User)
    department = models.CharField(max_length=100)
