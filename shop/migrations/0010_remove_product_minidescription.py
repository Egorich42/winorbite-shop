# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-22 10:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20170122_1328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='miniDescription',
        ),
    ]
