# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-22 17:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeamMap', '0004_auto_20180822_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='accepting_members',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]