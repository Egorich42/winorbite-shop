#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify



class GCategory(models.Model):
    icon = models.ImageField(upload_to='products/', blank=True, verbose_name="Изображение категории")
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True, blank=True)

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self): 
        return self.name


class GObject(models.Model):
    category = models.ForeignKey(GCategory, related_name='products', verbose_name="Категория")
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True, blank=True, verbose_name="Слаг")
    image = models.ImageField(upload_to='products/', blank=True, verbose_name="Изображение")
    site = models.CharField(max_length=200, db_index=True, blank=True, verbose_name="Сайт")
    fb_group = models.CharField(max_length=200, db_index=True, blank=True,  verbose_name="Фейсбук")
    vk_group = models.CharField(max_length=200, db_index=True, blank=True,  verbose_name="Вконтакте")
    tw_chanel = models.CharField(max_length=200, db_index=True, blank=True,  verbose_name="Твиттер")
    inst_chanel = models.CharField(max_length=200, db_index=True, blank=True,  verbose_name="Инстаграм")
    date_of_event = models.CharField(max_length=200, db_index=True, blank=True, verbose_name="Дата")
    place =  models.CharField(max_length=200, db_index=True, blank=True,  verbose_name="Локация")
    location_x = models.CharField(max_length=200, db_index=True, blank=True,  verbose_name="Широта")
    location_y = models.CharField(max_length=200, db_index=True, blank=True, verbose_name="Долгота")
   
    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]
        verbose_name = 'Точка'
        verbose_name_plural = 'Точки'

    def __unicode__(self):
        return self.name

