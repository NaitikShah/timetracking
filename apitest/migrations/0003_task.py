# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0002_auto_20180123_0548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('taskid', models.AutoField(serialize=False, primary_key=True)),
                ('taskname', models.CharField(max_length=200)),
                ('userid', models.ForeignKey(to='apitest.User', db_column='userid')),
            ],
            options={
                'db_table': 'TaskDetails',
            },
            bases=(models.Model,),
        ),
    ]
