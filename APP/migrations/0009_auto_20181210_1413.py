# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-12-10 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0008_auto_20181210_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
