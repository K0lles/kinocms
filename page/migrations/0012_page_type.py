# Generated by Django 3.2.12 on 2022-09-18 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0011_auto_20220915_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='type',
            field=models.CharField(blank=True, choices=[('about_cinema', 'About cinema'), ('cafe_bar', 'Cafe bar'), ('vip_hall', 'Vip hall'), ('advertisment', 'Advertisment'), ('baby_room', 'Baby room')], default=True, max_length=55),
        ),
    ]
