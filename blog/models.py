#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/', blank=True, verbose_name="Изображение")
    story = models.TextField(blank=True, verbose_name="Текст")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    class Meta:
        ordering = ['name']
        index_together = [['slug']]
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def get_post_url(self):
        return reverse('blog:post_detail', args=[self.slug])

    def __unicode__(self):
        return self.name
