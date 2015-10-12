# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_manufacturer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cereal',
            name='manuf',
            field=models.ForeignKey(blank=True, to='main.Manufacturer', null=True),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='cereals',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
