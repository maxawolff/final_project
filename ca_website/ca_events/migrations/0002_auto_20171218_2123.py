# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-18 21:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ca_events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='zip_code',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='zip_code',
            field=models.IntegerField(),
        ),
    ]