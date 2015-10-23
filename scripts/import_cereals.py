#!/usr/bin/env python

import csv
import sys
import os

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
import django
django.setup()

from main.models import Cereal, Manufacturer

print os.path.abspath(__file__)

dir_name = os.path.dirname(os.path.abspath(__file__))
file_name = "cereal.csv"

cereal_csv = os.path.join(dir_name, file_name)

csv_file = open(cereal_csv, 'r')

reader = csv.DictReader(csv_file)

for row in reader:
    new_manufacturer, created = Manufacturer.objects.get_or_create(name=row['Manufacturer'])

    new_cereal, created = Cereal.objects.get_or_create(name=row['Cereal Name'])
    new_cereal.manuf = new_manufacturer
    new_cereal.hctype = row['Type']
    new_cereal.calories = row['Calories']
    new_cereal.protein = row['Protein (g)']
    new_cereal.fat = row['Fat']
    new_cereal.sodium = row['Sodium']
    new_cereal.fiber = row['Dietary Fiber']
    new_cereal.carbs = row['Carbs']
    new_cereal.sugars = row['Sugars']

    new_cereal.cereal = new_cereal

    new_cereal.save()
