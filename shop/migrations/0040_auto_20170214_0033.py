# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-13 21:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0039_auto_20170214_0023'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='category',
            index_together=set([('id', 'slug')]),
        ),
    ]
