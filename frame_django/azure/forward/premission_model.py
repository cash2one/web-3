# -*- coding: utf-8 -*-
# @Date:   2016-12-20 09:58:41
# @Last Modified time: 2016-12-20 09:59:24
#
# from django.contrib.auth.models import Permission
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.utils import six
from django.db import models


class PermissionManager(models.Manager):
    use_in_migrations = True

    def get_by_natural_key(self, codename, app_label, model):
        return self.get(
            codename=codename,
            content_type=ContentType.objects.db_manager(self.db).get_by_natural_key(app_label, model),
        )


@python_2_unicode_compatible
class Permission(models.Model):
    """
    The permissions system provides a way to assign permissions to specific
    users and groups of users.

    The permission system is used by the Django admin site, but may also be
    useful in your own code. The Django admin site uses permissions as follows:

        - The "add" permission limits the user's ability to view the "add" form
          and add an object.
        - The "change" permission limits a user's ability to view the change
          list, view the "change" form and change an object.
        - The "delete" permission limits the ability to delete an object.

    Permissions are set globally per type of object, not per specific object
    instance. It is possible to say "Mary may change news stories," but it's
    not currently possible to say "Mary may change news stories, but only the
    ones she created herself" or "Mary may only change news stories that have a
    certain status or publication date."

    Three basic permissions -- add, change and delete -- are automatically
    created for each Django model.
    """
    name = models.CharField(_('name'), max_length=255)
    content_type = models.ForeignKey(
        ContentType,
        models.CASCADE,
        verbose_name=_('content type'),
    )
    codename = models.CharField(_('codename'), max_length=100)
    objects = PermissionManager()

    class Meta:
        verbose_name = _('permission')
        verbose_name_plural = _('permissions')
        unique_together = (('content_type', 'codename'),)
        ordering = ('content_type__app_label', 'content_type__model',
                    'codename')

    def __str__(self):
        return "%s | %s | %s" % (
            six.text_type(self.content_type.app_label),
            six.text_type(self.content_type),
            six.text_type(self.name))

    def natural_key(self):
        return (self.codename,) + self.content_type.natural_key()
    natural_key.dependencies = ['contenttypes.contenttype']


# 创建自定义权限
def test_premission():
    content_type = ContentType.objects.get_for_model(SimpleUser)
    # 每个permission都是django.contrib.auth.Permission类型的实例
    #
    # content_type————反应了permission属于哪个model
    # codename————代码逻辑中检查权限时要用
    # name————permission的描述，将permission打印到屏幕或页面时默认显示
    premission = Permission.objects.create(
        codename = "test",
        name = "can test",
        content_type = content_type
    )
    return premission
