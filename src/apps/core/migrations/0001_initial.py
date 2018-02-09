# Generated by Django 2.0.1 on 2018-02-09 12:24

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AHAClassSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_description', models.CharField(default='', max_length=256, verbose_name='class description')),
                ('occurrence', models.CharField(choices=[('SN', 'Single'), ('WK', 'Weekly'), ('MN', 'Monthly')], default='SN', max_length=2, verbose_name='occurrence')),
                ('date', models.DateField(verbose_name='date')),
                ('start', models.TimeField(verbose_name='start')),
                ('end', models.TimeField(verbose_name='end')),
            ],
            options={
                'verbose_name': 'aha class schedule',
                'verbose_name_plural': 'aha class schedules',
            },
        ),
        migrations.CreateModel(
            name='AHAField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='', max_length=64, verbose_name='type')),
                ('value', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='', max_length=128, verbose_name='value'), size=None)),
            ],
            options={
                'verbose_name': 'aha field',
                'verbose_name_plural': 'aha field',
            },
        ),
        migrations.CreateModel(
            name='AHAGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(default='', max_length=128, verbose_name='course')),
                ('location', models.CharField(default='', max_length=128, verbose_name='location')),
                ('instructor', models.CharField(default='', max_length=64, verbose_name='instructor')),
                ('training_center', models.CharField(default='', max_length=128, verbose_name='training center')),
                ('training_site', models.CharField(default='', max_length=128, verbose_name='training site')),
                ('roster_limit', models.IntegerField(default=0, verbose_name='max students')),
            ],
            options={
                'verbose_name': 'aha group',
                'verbose_name_plural': 'aha groups',
            },
        ),
        migrations.CreateModel(
            name='EnrollClassTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date')),
                ('start', models.TimeField(verbose_name='start')),
                ('end', models.TimeField(verbose_name='end')),
            ],
            options={
                'verbose_name': 'enroll class time',
                'verbose_name_plural': 'enroll class times',
            },
        ),
        migrations.CreateModel(
            name='EnrollWareGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.IntegerField(verbose_name='group id')),
                ('course', models.CharField(default='', max_length=128, verbose_name='course')),
                ('location', models.CharField(default='', max_length=128, verbose_name='location')),
                ('instructor', models.CharField(default='', max_length=64, verbose_name='instructor')),
                ('max_students', models.IntegerField(default=0, verbose_name='max students')),
                ('synced', models.BooleanField(default=False, verbose_name='synced')),
            ],
            options={
                'verbose_name': 'enroll group',
                'verbose_name_plural': 'enroll groups',
            },
        ),
        migrations.CreateModel(
            name='Mapper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enroll_value', models.CharField(default='', max_length=128, verbose_name='enroll value')),
                ('aha_value', models.CharField(default='', max_length=128, verbose_name='aha_value')),
                ('aha_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.AHAField', verbose_name='aha field')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'mapper',
                'verbose_name_plural': 'mappers',
            },
        ),
        migrations.AddField(
            model_name='enrollclasstime',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.EnrollWareGroup', verbose_name='group'),
        ),
        migrations.AddField(
            model_name='ahaclassschedule',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.AHAGroup', verbose_name='group'),
        ),
    ]
