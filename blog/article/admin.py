# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Category, Tag, Article

@admin.register(Category, Tag, Article)
class ArticleAdmin(admin.ModelAdmin):
    pass
