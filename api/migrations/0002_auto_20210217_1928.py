# Generated by Django 3.0.5 on 2021-02-17 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='id',
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(primary_key=True, serialize=False, unique=True, verbose_name='уникальное имя'),
        ),
    ]
