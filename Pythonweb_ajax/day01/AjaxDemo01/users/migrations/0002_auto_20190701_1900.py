# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-01 11:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uname',
            field=models.CharField(max_length=30, unique=True, verbose_name='用户名'),
        ),
    ]
