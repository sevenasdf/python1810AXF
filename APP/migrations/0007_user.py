# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-12-08 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0006_goods'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=80, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('addr', models.CharField(max_length=256)),
                ('img', models.CharField(max_length=100)),
                ('rank', models.IntegerField(default=1)),
                ('token', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'axf_user',
            },
        ),
    ]
