# Generated by Django 4.0.6 on 2022-08-02 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0005_alter_photo_gallery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seo',
            name='description',
        ),
        migrations.AddField(
            model_name='seo',
            name='seo_description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='seo',
            name='keyword',
            field=models.CharField(max_length=155, verbose_name='Keywords'),
        ),
        migrations.AlterField(
            model_name='seo',
            name='title',
            field=models.CharField(max_length=55, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='seo',
            name='url',
            field=models.URLField(verbose_name='Url'),
        ),
    ]