# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20151005_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='cereal',
            name='calories',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cereal',
            name='hctype',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cereal',
            name='manuf',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
