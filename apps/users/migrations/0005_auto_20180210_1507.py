# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180210_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='medic',
            field=models.ForeignKey(related_name='medic', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(related_name='patient', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
