# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-25 09:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='simpleuser',
            unique_together=set([]),
        ),
    ]
