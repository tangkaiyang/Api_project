# Generated by Django 3.2.13 on 2022-07-10 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api_app', '0012_db_power_list_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='db_project_list',
            name='L_data',
        ),
        migrations.RemoveField(
            model_name='db_project_list',
            name='P_data',
        ),
        migrations.RemoveField(
            model_name='db_project_list',
            name='mock',
        ),
        migrations.RemoveField(
            model_name='db_project_list',
            name='power',
        ),
        migrations.RemoveField(
            model_name='db_project_list',
            name='sign',
        ),
    ]
