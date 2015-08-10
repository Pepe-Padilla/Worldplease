# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_blog_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='urlImg',
            field=models.URLField(null=True, blank=True),
        ),
    ]
