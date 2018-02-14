# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-14 19:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_auto_20180214_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollwaregroup',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='enrollware_groups', to=settings.AUTH_USER_MODEL, verbose_name='user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mapper',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='mappers', to=settings.AUTH_USER_MODEL, verbose_name='user'),
            preserve_default=False,
        ),
    ]
