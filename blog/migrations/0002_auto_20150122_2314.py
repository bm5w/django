# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.EmailField(max_length=75, default='a@a.com'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='first',
            field=models.CharField(max_length=50, default=datetime.datetime(2015, 1, 22, 23, 14, 21, 781669)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='last',
            field=models.CharField(max_length=50, default=datetime.datetime(2015, 1, 22, 23, 14, 27, 998259)),
            preserve_default=False,
        ),
    ]
