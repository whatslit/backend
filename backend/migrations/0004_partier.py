# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0003_remove_event_creator_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partier',
            fields=[

                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('profile_image', models.FileField(upload_to='')),
                ('litness', models.DecimalField(decimal_places=5, max_digits=13, null=True)),
                ('events_invited', models.ManyToManyField(to='backend.Event', related_name='events')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
