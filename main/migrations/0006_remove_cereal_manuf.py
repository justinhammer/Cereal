# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20151005_2215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cereal',
            name='manuf',
        ),
    ]
