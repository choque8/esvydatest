# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20180210_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelationMedicPatient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('medic', models.ForeignKey(related_name='medasdasdasic', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('patient', models.ForeignKey(related_name='paadastient', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
