# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-20 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170410_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text_to_vk',
            field=models.TextField(blank=True, db_index=True, max_length=300, verbose_name='текст для контача'),
        ),
    ]
