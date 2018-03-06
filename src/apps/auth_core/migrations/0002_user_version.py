# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-06 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='version',
            field=models.CharField(choices=[('lite', 'Lite'), ('pro', 'Pro')], default='lite', max_length=8),
        ),
    ]