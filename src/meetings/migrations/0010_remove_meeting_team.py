# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-06 02:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0009_auto_20180904_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='team',
        ),
    ]
