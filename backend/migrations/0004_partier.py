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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.FileField(upload_to='')),
                ('latitude', models.DecimalField(decimal_places=10, max_digits=13)),
                ('longitude', models.DecimalField(decimal_places=10, max_digits=13)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
