# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True)
    story = models.TextField(blank=True, verbose_name="Текст")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    class Meta:
        ordering = ['name']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
 

    def __str__(self):
        return self.name
