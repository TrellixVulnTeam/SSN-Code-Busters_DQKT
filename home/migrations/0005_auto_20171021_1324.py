# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-21 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20171021_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contests',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='contests',
            name='end_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='contests',
            name='start_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]