# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20151013_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cereal',
            name='carbs',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cereal',
            name='fiber',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
