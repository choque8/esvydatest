# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20180210_1534'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('control', models.ForeignKey(related_name='control_appointment', blank=True, to='users.Appointment', null=True)),
                ('first', models.ForeignKey(related_name='first_appointmet', blank=True, to='users.Appointment', null=True)),
            ],
        ),
    ]
