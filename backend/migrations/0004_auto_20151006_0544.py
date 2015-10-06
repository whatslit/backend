# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20151006_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='comments',
            field=models.ForeignKey(to='backend.Comment', null=True),
        ),
    ]
