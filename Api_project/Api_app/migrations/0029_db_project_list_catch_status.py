# Generated by Django 3.2.13 on 2022-09-03 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api_app', '0028_db_monitor'),
    ]

    operations = [
        migrations.AddField(
            model_name='db_project_list',
            name='catch_status',
            field=models.BooleanField(default=False),
        ),
    ]
