# Generated by Django 3.2.13 on 2022-07-16 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api_app', '0016_auto_20220716_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='db_project_list',
            name='dck',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
    ]
