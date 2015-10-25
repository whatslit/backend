# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_event_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='creator_id',
        ),
    ]
