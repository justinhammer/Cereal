from django.db import models

# Create your models here.


class Cereal(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    manuf = models.ForeignKey('main.Manufacturer', null=True, blank=True)
    hctype = models.CharField(max_length=255, null=True, blank=True)
    calories = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    cereals = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.name
