# Generated by Django 3.2.12 on 2022-09-15 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0010_remove_contacts_seo'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='page',
            name='description_uk',
            field=models.TextField(null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='page',
            name='name_ru',
            field=models.CharField(max_length=55, null=True, verbose_name='Назва'),
        ),
        migrations.AddField(
            model_name='page',
            name='name_uk',
            field=models.CharField(max_length=55, null=True, verbose_name='Назва'),
        ),
    ]
