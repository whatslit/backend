# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('creator_id', models.IntegerField()),
                ('time_posted', models.DateTimeField()),
                ('was_removed', models.BooleanField(default=False)),
                ('content', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('creator_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('event_type', models.CharField(choices=[('PA', 'Party'), ('CO', 'Concert')], default='PA', max_length=2)),
                ('was_removed', models.BooleanField(default=False)),
                ('time_posted', models.DateTimeField()),
                ('description', models.CharField(max_length=1000)),
                ('latitude', models.DecimalField(max_digits=13, decimal_places=10)),
                ('longitude', models.DecimalField(max_digits=13, decimal_places=10)),
                ('score', models.DecimalField(max_digits=8, decimal_places=3)),
                ('comments', models.ForeignKey(to='backend.Comment', null=True)),
            ],
        ),
    ]
