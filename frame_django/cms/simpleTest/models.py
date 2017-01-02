from __future__ import unicode_literals

from django.db import models

# Create your models here.


class EmailLogin(models.Model):
    email = models.EmailField()
    random = models.CharField(max_length=4)
    is_active = models.SmallIntegerField()
