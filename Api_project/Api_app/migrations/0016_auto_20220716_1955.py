# Generated by Django 3.2.13 on 2022-07-16 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api_app', '0015_db_apis'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='db_project_list',
            name='chose_apiconfigure',
        ),
        migrations.AddField(
            model_name='db_project_list',
            name='dck',
            field=models.CharField(blank=True, default='[]', max_length=500, null=True),
        ),
    ]
