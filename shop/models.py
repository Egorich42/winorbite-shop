#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

class Category(models.Model):
    icon = models.ImageField(upload_to='products/', blank=True, verbose_name="Изображение")
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True,blank=True)

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'        

    def  __unicode__(self): 
        return self.name

    def get_absolute_url(self):
        return reverse('shop:category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', verbose_name="Категория")
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/', blank=True, verbose_name="Изображение товара")
    parameter = models.CharField(max_length=200, db_index=True, blank=True, verbose_name="Параметр")
    parameter_value =  models.CharField(max_length=50, db_index=True, blank=True, verbose_name="значение параметра")
    second_parameter = models.CharField(max_length=200, db_index=True, blank=True, verbose_name="Параметр")
    second_parameter_value = models.CharField(max_length=50, db_index=True, blank=True, verbose_name="значение параметра")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена бел.рубли")
    price_rub = models.DecimalField(max_digits=10,  blank=True, default='1',  decimal_places=2, verbose_name="Цена рубли")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
   
    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:ProductDetail', args=[self.id, self.slug])
