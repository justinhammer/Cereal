from django.contrib import admin
from main.models import Cereal, Manufacturer

# Register your models here.


class CerealAdmin(admin.ModelAdmin):
    list_display = ('name', 'hctype', 'calories')


admin.site.register(Cereal, CerealAdmin)
admin.site.register(Manufacturer)
