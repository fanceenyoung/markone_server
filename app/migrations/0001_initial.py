# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-07-01 08:46
from __future__ import unicode_literals

import app.models
from django.db import migrations, models
import jsonfield.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('email', models.CharField(blank=True, db_index=True, default=b'', max_length=512)),
                ('phone', models.CharField(blank=True, db_index=True, default=b'', max_length=32)),
                ('type', models.CharField(choices=[(b'VISITOR', b'Visitor'), (b'BUSINESS', b'Admin'), (b'SUPERUSER', b'Superuser'), (b'OTHER', b'Other')], default=b'VISITOR', max_length=16)),
                ('location', jsonfield.fields.JSONField(blank=True, default=dict)),
                ('country', models.CharField(blank=True, default=b'China', max_length=32)),
                ('avatar', models.CharField(blank=True, default=b'', max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', app.models.BaseUserManager()),
            ],
        ),
    ]
