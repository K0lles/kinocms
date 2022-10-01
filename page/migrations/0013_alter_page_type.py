# Generated by Django 3.2.12 on 2022-09-18 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0012_page_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='type',
            field=models.CharField(blank=True, choices=[('about_cinema', 'About cinema'), ('cafe_bar', 'Cafe bar'), ('vip_hall', 'Vip hall'), ('advertisment', 'Advertisment'), ('baby_room', 'Baby room')], max_length=55, null=True),
        ),
    ]