# Generated by Django 2.0.7 on 2019-07-29 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeamMap', '0014_auto_20190728_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='action_blueprint_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='team',
            name='become_educated_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='team',
            name='problem_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='team',
            name='solution_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='team',
            name='solution_results_done',
            field=models.BooleanField(default=False),
        ),
    ]
