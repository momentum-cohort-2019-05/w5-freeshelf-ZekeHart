# Generated by Django 2.2.2 on 2019-06-28 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20190628_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]