# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-04 06:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20171203_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='create_date',
            field=models.CharField(default='2017-12-04 06:02:30', max_length=40, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='last name'),
        ),
    ]
