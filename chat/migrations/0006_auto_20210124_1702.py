# Generated by Django 3.1.5 on 2021-01-24 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_auto_20210124_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat_log',
            name='room_name',
            field=models.CharField(max_length=20),
        ),
    ]