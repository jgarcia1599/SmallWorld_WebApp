# Generated by Django 2.0.7 on 2019-08-02 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0012_meeting_benchmark'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meeting',
            old_name='benchmark',
            new_name='step',
        ),
        migrations.AddField(
            model_name='meeting',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
    ]
