# Generated by Django 3.0.5 on 2021-02-22 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210221_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='api.Title'),
        ),
    ]
