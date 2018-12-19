from django.db import models


class Pump(models.Model):
    CHOICES_PRODUCT_TYPE = (("Petrol", "Petrol"), ("Diesel", "Diesel"), ("Kerosene", "Kerosene"))
    CHOICES_PUMP_NAME = (
        ("pms1", "pms1"), ("pms2", "pms2"), ("pms3", "pms3"), ("ago1", "ago1"), ("ago2", "ago2"), ("ago3", "ago3"),
        ("bik1", "bik1"), ("bik2", "bik2"), ("bik3", "bik3")
    )

    pump_name = models.CharField(choices=CHOICES_PUMP_NAME, max_length=20)
    pump_category = models.CharField(choices=CHOICES_PRODUCT_TYPE, max_length=20)
    station_name = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.pump_name


class Ratings(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    pump = models.ForeignKey(Pump, on_delete=models.CASCADE)
    rate = models.FloatField()


class Report(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    pump = models.ForeignKey(Pump, on_delete=models.CASCADE)
    opening_reading = models.FloatField()
    closing_reading = models.FloatField()
    meter_movement = models.FloatField()
    transfers = models.FloatField()
    net_sales = models.FloatField()

    def __str__(self):
        return self.pump.pump_name


class Tank(models.Model):
    CHOICES_PRODUCT = (("PMS", "PMS"), ("TRUCK", "TRUCK"), ("AGO", "AGO"), ("BIK", "BIK"))
    date_created = models.DateTimeField(auto_now_add=True)
    product_category = models.CharField(choices=CHOICES_PRODUCT, max_length=10)
    opening_stock = models.FloatField()
    product_received = models.FloatField()
    product_returned = models.FloatField()
    closing_stock = models.FloatField()

    def total_stock(self):
        return self.opening_stock + self.product_received + self.product_returned

    def tank_sales(self):
        return self.total_stock() - self.closing_stock

    def __str__(self):
        return self.product_category


class ItemSales(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    product = models.CharField(max_length=30)
    quantity = models.IntegerField()
    unit_price = models.FloatField()

    def value(self):
        return self.unit_price * self.quantity

