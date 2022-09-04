# Generated by Django 4.1 on 2022-09-01 20:25

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_mainpage_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainpage',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='mainpage',
            name='phone_number_first',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='mainpage',
            name='phone_number_second',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]