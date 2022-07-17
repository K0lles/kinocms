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
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, verbose_name='Назва')),
                ('description', models.TextField(verbose_name='Опис')),
                ('main_photo', models.ImageField(upload_to='page/', verbose_name='Головна картинка')),
                ('status', models.BooleanField(default=True)),
                ('gallery', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cinema.gallery', verbose_name='Галерея картинок')),
                ('seo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cinema.seo')),
            ],
        ),
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number_first', models.DecimalField(decimal_places=0, max_digits=10)),
                ('phone_number_second', models.DecimalField(decimal_places=0, max_digits=10)),
                ('seo_text', models.TextField(verbose_name='SEO текст')),
                ('seo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cinema.seo')),
            ],
        ),
    ]
