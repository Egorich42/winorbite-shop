# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-22 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20170120_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_side',
            field=models.ImageField(blank=True, upload_to='products/', verbose_name='Изображение товара'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_side2',
            field=models.ImageField(blank=True, upload_to='products/', verbose_name='Изображение товара'),
        ),
    ]
