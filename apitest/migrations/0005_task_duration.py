# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0004_auto_20180123_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='duration',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
