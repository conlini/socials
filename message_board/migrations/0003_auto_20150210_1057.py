# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message_board', '0002_auto_20150208_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='topic',
            field=models.ForeignKey(to='message_board.Topic', null=True),
            preserve_default=True,
        ),
    ]
