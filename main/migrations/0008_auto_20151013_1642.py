# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_cereal_manuf'),
    ]

    operations = [
        migrations.AddField(
            model_name='cereal',
            name='carbs',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cereal',
            name='fat',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cereal',
            name='fiber',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cereal',
            name='protein',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cereal',
            name='sodium',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cereal',
            name='sugars',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
