# Generated by Django 3.2.4 on 2021-07-07 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brainstorm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brainstorm',
            name='pricing',
        ),
    ]
