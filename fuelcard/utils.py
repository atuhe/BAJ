from django.db.models import Sum
from fuelcard.models import Report, Ratings, ItemSales

from datetime import datetime
import logging


class NetSales:
    date = datetime.today()

    def __init__(self, date):
        self.date = date
    """
    A util class that returns the net sales of the different products
    """
    def pms(self):
        pms1 = Report.objects.filter(pump__pump_name='pms1').all().aggregate(Sum('net_sales'))[
                   'net_sales__sum'] or 0.00
        pms2 = Report.objects.filter(pump__pump_name='pms2').all().aggregate(Sum('net_sales'))[
                   'net_sales__sum'] or 0.00
        pms3 = Report.objects.filter(pump__pump_name='pms3').all().aggregate(Sum('net_sales'))[
                   'net_sales__sum'] or 0.00
        return pms1 + pms2 + pms3

    def ago(self):
        ago1 = Report.objects.filter(pump__pump_name='ago1').all().aggregate(Sum('net_sales'))[
                   'net_sales__sum'] or 0.00
        ago2 = Report.objects.filter(pump__pump_name='ago2').all().aggregate(Sum('net_sales'))[
                   'net_sales__sum'] or 0.00
        ago3 = Report.objects.filter(pump__pump_name='ago3').all().aggregate(Sum('net_sales'))[
                   'net_sales__sum'] or 0.00
        return ago1 + ago2 + ago3

    def bik(self):
        bik1 = Report.objects.filter(pump__pump_name='bik1').all().aggregate(Sum('net_sales'))[
                   'net_sales__sum'] or 0.00
        bik2 = Report.objects.filter(pump__pump_name='bik2').all().aggregate(Sum('net_sales'))[
                   'net_sales__sum'] or 0.00
        bik3 = Report.objects.filter(pump__pump_name='bik3').all().aggregate(Sum('net_sales'))[
                   'net_sales__sum'] or 0.00
        return bik1 + bik2 + bik3

    def total_other_sales(self):
        sales_list = ItemSales.objects.filter(date_created__date=self.date).order_by('-id')
        return sum([x.unit_price * x.quantity for x in sales_list])


class ProductRatings:
    date = datetime.today()

    def __init__(self, date):
        self.date = date

    def pms(self):
        try:
            ratings = Ratings.objects.get(date_created__date=self.date, pump__pump_category='Petrol')
            return ratings.rate
        except Exception as e:
            logging.error(e)
            return 0

    def ago(self):
        try:
            ratings = Ratings.objects.get(date_created__date=self.date, pump__pump_category='Diesel')
            return ratings.rate
        except Exception as e:
            logging.error(e)
            return 0

    def bik(self):
        try:
            ratings = Ratings.objects.get(date_created__date=self.date, pump__pump_category='Kerosene')
            return ratings.rate
        except Exception as e:
            logging.error(e)
            return 0



