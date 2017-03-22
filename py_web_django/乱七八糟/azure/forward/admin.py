from django.contrib import admin
from django.db import models
from django import forms


class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField:
            {
                'widget': forms.Textarea(
                    attrs={
                        'rows': 41,
                        'cols': 100
                    }
                )
            },
    }
    list_display = ('title', 'pub_date', 'poll_num')
