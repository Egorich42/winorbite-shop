# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-13 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0040_auto_20170214_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='main_name',
            field=models.CharField(db_index=True, default='', max_length=200, verbose_name='Главное Название'),
            preserve_default=False,
        ),
    ]
