# Generated by Django 4.0.6 on 2022-08-22 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_alter_simpleuser_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='simpleuser',
            name='password1',
        ),
        migrations.AlterField(
            model_name='simpleuser',
            name='password',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Пароль'),
        ),
    ]
