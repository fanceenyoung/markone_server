# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-08-04 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20180804_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.TextField(null=True),
        ),
    ]
