# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('resumen', models.CharField(max_length=500)),
                ('cuerpo', models.TextField(default=b'', null=True, blank=True)),
                ('urlImg', models.URLField()),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=3, choices=[(b'ADD', b'Created'), (b'PUB', b'Published'), (b'CAN', b'Canceled'), (b'BAN', b'Banned')])),
            ],
        ),
    ]
