# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20150615_1527'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersociallink',
            old_name='url',
            new_name='link',
        ),
    ]
