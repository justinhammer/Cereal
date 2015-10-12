# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cereal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('manuf', models.CharField(max_length=255, null=True, blank=True)),
                ('hctype', models.CharField(max_length=255, null=True, blank=True)),
                ('calories', models.IntegerField(null=True, blank=True)),
            ],
        ),
    ]
