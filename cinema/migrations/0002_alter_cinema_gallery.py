# Generated by Django 4.0.6 on 2022-07-19 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinema',
            name='gallery',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cinema.gallery', verbose_name='Галерея картинок'),
        ),
    ]