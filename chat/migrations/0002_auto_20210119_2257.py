# Generated by Django 3.1.5 on 2021-01-19 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chat_log',
            options={'ordering': ['-timestamp']},
        ),
    ]