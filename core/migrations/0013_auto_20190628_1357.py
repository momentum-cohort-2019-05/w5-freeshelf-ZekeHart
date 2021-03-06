# Generated by Django 2.2.2 on 2019-06-28 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0012_auto_20190628_1233'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-date_added']},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(
                default=models.CharField(max_length=100),
                unique=False,
                verbose_name=models.CharField(max_length=100)),
        ),
        migrations.CreateModel(
            name='UserFavorite',
            fields=[
                ('id',
                 models.AutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('fav_book',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='core.Book')),
                ('user',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_added'],
                'unique_together': {('user', 'fav_book')},
            },
        ),
    ]
