#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.utils.encoding import python_2_unicode_compatible
from django.contrib import admin
from .models import GCategory, GObject


class GCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'icon']
    prepopulated_fields = {'slug': ('name', )}


class GObjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}



admin.site.register(GCategory, GCategoryAdmin)
admin.site.register(GObject, GObjectAdmin)
