# Generated by Django 3.2 on 2023-01-09 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_auto_20230109_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]