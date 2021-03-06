# Generated by Django 4.0.6 on 2022-07-17 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, verbose_name='Назва')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата публікації')),
                ('description', models.TextField(verbose_name='Опис')),
                ('logo', models.ImageField(upload_to='event/logo/', verbose_name='Головна картинка')),
                ('url', models.URLField(verbose_name='Посилання на відео')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.gallery', verbose_name='Галерея картинок')),
                ('seo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cinema.seo')),
            ],
        ),
    ]
