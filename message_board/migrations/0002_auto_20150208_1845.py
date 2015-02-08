# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('message_board', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'get_latest_by': 'creation_date'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'get_latest_by': 'last_modified'},
        ),
        migrations.AddField(
            model_name='message',
            name='last_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 8, 18, 45, 28, 153733, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
