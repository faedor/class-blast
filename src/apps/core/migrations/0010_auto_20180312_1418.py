# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-12 14:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_enrollwaregroup_available_to_export'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ahaclassschedule',
            name='group',
        ),
        migrations.DeleteModel(
            name='AHAClassSchedule',
        ),
        migrations.DeleteModel(
            name='AHAGroup',
        ),
    ]
