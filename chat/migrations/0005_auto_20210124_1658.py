# Generated by Django 3.1.5 on 2021-01-24 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20210124_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat_log',
            name='room_name',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
