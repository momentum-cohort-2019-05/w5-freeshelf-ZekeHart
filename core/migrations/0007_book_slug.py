# Generated by Django 2.2.2 on 2019-06-26 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190625_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(null=True, unique=True, verbose_name=models.CharField(max_length=100)),
        ),
    ]
