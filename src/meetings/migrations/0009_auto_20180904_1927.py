# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-04 19:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TeamMap', '0008_auto_20180828_1436'),
        ('meetings', '0008_auto_20180904_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetingteam',
            name='meeting',
        ),
        migrations.RemoveField(
            model_name='meetingteam',
            name='team',
        ),
        migrations.AddField(
            model_name='meeting',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TeamMap.Team'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='MeetingTeam',
        ),
    ]
