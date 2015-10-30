# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_partier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partier',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='partier',
            name='longitude',
        ),
        migrations.AddField(
            model_name='partier',
            name='events_invited',
            field=models.ManyToManyField(to='backend.Event', related_name='events'),
        ),
        migrations.AddField(
            model_name='partier',
            name='litness',
            field=models.DecimalField(decimal_places=5, max_digits=13, null=True),
        ),
    ]
