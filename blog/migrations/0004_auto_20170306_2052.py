# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-06 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170301_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='story',
            field=models.CharField(blank=True, max_length=25000, verbose_name='Текст'),
        ),
    ]
