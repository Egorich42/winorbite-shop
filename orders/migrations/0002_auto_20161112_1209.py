# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-12 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='city',
        ),
        migrations.RemoveField(
            model_name='order',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='postal_code',
        ),
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=models.CharField(default='', max_length=12, verbose_name='Телефон'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(max_length=200, verbose_name='Как к вам обратиться?'),
        ),
    ]