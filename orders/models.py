#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from shop.models import Product
from django import forms
from django.shortcuts import render


class Order(models.Model):
    first_name = models.CharField(verbose_name='Ваше имя', max_length=200)
    email =  models.EmailField(verbose_name='Ваш e-mail', blank = True)
    phone_number = models.CharField(verbose_name='Ваш номер телефона', max_length=12)
    created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)


    class Meta:
        ordering = ('-created', )
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ: {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items')
    product = models.ForeignKey(Product, related_name='order_items')
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
