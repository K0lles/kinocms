# Generated by Django 3.2.15 on 2022-09-23 20:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('admin_cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailfile',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
