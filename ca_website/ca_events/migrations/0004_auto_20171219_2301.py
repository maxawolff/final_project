# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-19 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ca_events', '0003_auto_20171219_2202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='events',
            name='event_format',
        ),
        migrations.AddField(
            model_name='events',
            name='contact_phone',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='event_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='events',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
