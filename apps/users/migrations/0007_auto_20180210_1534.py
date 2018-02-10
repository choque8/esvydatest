# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_relationmedicpatient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationmedicpatient',
            name='medic',
            field=models.ForeignKey(related_name='medic_relation', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='relationmedicpatient',
            name='patient',
            field=models.ForeignKey(related_name='patient_relation', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
