# Generated by Django 2.2.2 on 2019-06-26 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20190626_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(unique=True, verbose_name=models.CharField(max_length=100)),
        ),
    ]
