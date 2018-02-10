# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_users_type_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('descrip', models.TextField(null=True, blank=True)),
                ('date', models.DateField(null=True, blank=True)),
                ('time', models.TimeField(null=True, blank=True)),
                ('first', models.NullBooleanField()),
                ('patient', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AppointmentState',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descrip', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'estado_actividad',
            },
        ),
        migrations.AddField(
            model_name='appointment',
            name='state',
            field=models.ForeignKey(blank=True, to='users.AppointmentState', null=True),
        ),
    ]
