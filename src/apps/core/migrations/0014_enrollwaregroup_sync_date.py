# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-19 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_ahagroup_cutoff_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollwaregroup',
            name='sync_date',
            field=models.DateTimeField(null=True, verbose_name='sync date'),
        ),
    ]