# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-10 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0045_auto_20170301_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.ImageField(blank=True, upload_to='products/', verbose_name='Изображение'),
        ),
    ]
