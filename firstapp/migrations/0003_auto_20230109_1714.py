# Generated by Django 3.2 on 2023-01-09 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_auto_20230109_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fname',
            field=models.CharField(max_length=24),
        ),
        migrations.AlterField(
            model_name='user',
            name='lname',
            field=models.CharField(max_length=24),
        ),
    ]
