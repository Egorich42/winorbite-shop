# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-13 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0026_auto_20170213_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
    ]
