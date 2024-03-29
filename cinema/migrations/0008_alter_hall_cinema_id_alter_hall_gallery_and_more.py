# Generated by Django 4.0.6 on 2022-08-10 12:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0007_hall_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hall',
            name='cinema_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cinema.cinema', verbose_name='Кінотеатр'),
        ),
        migrations.AlterField(
            model_name='hall',
            name='gallery',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cinema.gallery', verbose_name='Галерея картинок'),
        ),
        migrations.AlterField(
            model_name='hall',
            name='row_amount',
            field=models.IntegerField(blank=True, default=6, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='hall',
            name='seat_amount',
            field=models.IntegerField(blank=True, default=12, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='hall',
            name='seo',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cinema.seo', verbose_name='SEO блок'),
        ),
    ]
