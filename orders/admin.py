#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_field = ['product']

class OrderAdmin(admin.ModelAdmin):

    list_display = ['id',   'email', 'created', 'first_name', 'phone_number']
    list_filter = [ 'created']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
