# Generated by Django 2.0.7 on 2020-05-13 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0018_auto_20190803_0202'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentormeeting',
            name='team_data',
            field=models.CharField(default='null', max_length=100000),
        ),
    ]
