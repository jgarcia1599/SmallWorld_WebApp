# Generated by Django 2.0.7 on 2019-07-29 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeamMap', '0015_auto_20190729_0124'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='action_blueprint_progress',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='team',
            name='become_educated_progress',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='team',
            name='problem_progress',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='team',
            name='solution_progress',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='team',
            name='solution_results_progress',
            field=models.BooleanField(default=False),
        ),
    ]