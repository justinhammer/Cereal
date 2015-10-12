# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_cereal_manuf'),
    ]

    operations = [
        migrations.AddField(
            model_name='cereal',
            name='manuf',
            field=models.ForeignKey(blank=True, to='main.Manufacturer', null=True),
        ),
    ]
