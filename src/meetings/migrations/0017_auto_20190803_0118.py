# Generated by Django 2.0.7 on 2019-08-03 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0016_auto_20190803_0059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentormeeting',
            name='in_progress',
        ),
        migrations.RemoveField(
            model_name='mentormeeting',
            name='is_complete',
        ),
    ]
