#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
import vk
token = 'https://oauth.vk.com/blank.html#access_token=428d4056e19bbcb3045aa198eaf5efc0b8ce3b68ae4e2405a81dd177a23df83fc40052d7623d8e45d0c9e&expires_in=0&user_id=31383913'
session = vk.AuthSession('6049127', 'zonaegora@mail.ru', 'elonbatya42r',  scope='wall, messages')
vk_api = vk.API(session)
blog_link = 'http://winorbite.com/blog/'

class Post(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/', blank=True, verbose_name="Изображение")
    story = models.TextField(blank=True, verbose_name="Текст")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    text_to_vk = models.TextField(max_length=300, blank=True, db_index=True, verbose_name="текст для контача")

    class Meta:
        ordering = ['name']
        index_together = [['slug']]
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def get_post_url(self):
        return reverse('blog:post_detail', args=[self.slug])

    def __unicode__(self):
        return self.name
