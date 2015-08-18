# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150716_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogentry',
            name='author',
            field=models.CharField(default='Salman Wahed', max_length=50),
            preserve_default=False,
        ),
    ]
