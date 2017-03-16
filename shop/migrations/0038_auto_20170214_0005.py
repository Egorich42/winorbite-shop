# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-13 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0037_auto_20170214_0001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='second_parameter',
        ),
        migrations.RemoveField(
            model_name='product',
            name='second_parameter_value',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, db_index=True, max_length=200, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
