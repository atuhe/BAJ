from django.contrib import admin
from fuelcard.models import Pump, Ratings


class PumpAdmin(admin.ModelAdmin):
    list_display = ['pump_name', 'station_name', 'pump_category', ]
    ordering = ['pump_name']


class RatingsAdmin(admin.ModelAdmin):
    list_display = ['rate']


admin.site.register(Pump, PumpAdmin)
admin.site.register(Ratings, RatingsAdmin)
