# Generated by Django 4.1 on 2022-09-02 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_event_created_at_event_status_alter_event_seo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
    ]
