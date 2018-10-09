from django.db import models


class Pump(models.Model):
    CHOICES_PRODUCT_TYPE = (("Petrol", "Petrol"), ("Diesel", "Diesel"), ("Kerosene", "Kerosene"))
    CHOICES_PUMP_NAME = (
        ("pms1", "pms1"), ("pms2", "pms2"), ("pms3", "pms3"), ("ago1", "ago1"), ("ago2", "ago2"), ("ago3", "ago3"),
        ("bik1", "bik1"), ("bik2", "bik2"), ("bik3", "bik3")
    )

    pump_name = models.CharField(choices=CHOICES_PUMP_NAME, max_length=20)
    pump_category = models.CharField(choices=CHOICES_PRODUCT_TYPE, max_length=20)
    opening_reading = models.FloatField()
    closing_reading = models.FloatField()
    transfers = models.FloatField()

    def meter_movement(self):
        return self.closing_reading - self.opening_reading

    def net_sales(self):
        return self.meter_movement() - self.transfers
