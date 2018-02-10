# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180210_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='medic',
            field=models.ForeignKey(related_name='medicuser', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(related_name='patientuser', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
