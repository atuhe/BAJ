from django.contrib import admin
from fuelcard.models import Pump


class PumpAdmin(admin.ModelAdmin):
    list_display = ['pump_name', 'station_name', 'pump_category', ]
    ordering = ['pump_name']


admin.site.register(Pump, PumpAdmin)
