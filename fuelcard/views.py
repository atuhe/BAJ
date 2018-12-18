import logging
from django.views.generic import CreateView, TemplateView, ListView
from django.http import JsonResponse
from django.db.models import Q
from django.db.models import Sum
from rest_framework import status
from fuelcard.forms import ReportForm, TankForm
from fuelcard.models import Pump, Report, Tank
from fuelcard.serializers import ReportSerializer

from datetime import datetime


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class PumpView(ListView):
    template_name = 'pumps.html'
    model = Pump

    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)


class ReadingView(ListView, CreateView):
    model = Report
    form_class = ReportForm
    template_name = 'readings.html'

    # def get(self, request, *args, **kwargs):
    #     self.object = None
    #     return super().get(request, *args, **kwargs)

    def get_queryset(self):

        """Fetches Meter readings for that particular date"""

        day_report = super(ReadingView, self).get_queryset()
        day_report = day_report.filter(date_created__date=datetime.today()).order_by('-id')
        return day_report

    def get_context_data(self, **kwargs):
        try:
            pms1 = Q(pump__pump_name__contains='pms1')
            pms2 = Q(pump__pump_name__contains='pms2')
            pms3 = Q(pump__pump_name__contains='pms3')
            kwargs['pms_sales'] = Report.objects.filter(pms1 & pms2 & pms3).aggregate(Sum('net_sales'))
            kwargs['pms'] = Tank.objects.get(product_category='PMS')
        except Exception as e:
            logging.error(e)
        try:
            kwargs['truck'] = Tank.objects.get(product_category='TRUCK')
        except Exception as e:
            logging.error(e)
        try:
            ago1 = Q(pump__pump_name__contains='ago1')
            ago2 = Q(pump__pump_name__contains='ago2')
            ago3 = Q(pump__pump_name__contains='ago3')
            kwargs['ago_sales'] = Report.objects.filter(ago1 & ago2 & ago3).aggregate(Sum('net_sales'))
            kwargs['ago'] = Tank.objects.get(product_category='AGO')
        except Exception as e:
            logging.error(e)
        try:
            bik1 = Q(pump__pump_name__contains='bik1')
            bik2 = Q(pump__pump_name__contains='bik2')
            bik3 = Q(pump__pump_name__contains='bik3')
            bik_sales = Report.objects.filter(bik1 & bik2 & bik3).aggregate(Sum('net_sales'))
            kwargs['bik_sales'] = bik_sales
            kwargs['bik'] = Tank.objects.get(product_category='BIK')
            print(bik_sales)
        except Exception as e:
            logging.error(e)
        return kwargs


class TankReadingsView(ListView, CreateView):
    model = Tank
    form_class = TankForm
    template_name = 'tank_readings.html'

    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)

    def get_queryset(self):

        """Fetches tank readings for that particular date"""

        day_report = super(TankReadingsView, self).get_queryset()
        day_report = day_report.filter(date_created__date=datetime.today()).order_by('-id')
        return day_report

    def post(self, request, *args, **kwargs):
        self.object = None

        if self.request.is_ajax():
            product = self.request.POST.get('product')
            opening_stock = self.request.POST.get("openingStock")
            closing_stock = self.request.POST.get("closingStock")
            product_received = self.request.POST.get("productReceived")
            product_returned = self.request.POST.get("productReturned")
            try:
                tank_readings = Tank(product_category=product, opening_stock=opening_stock, closing_stock=closing_stock,
                                     product_received=product_received, product_returned=product_returned)
                tank_readings.save()
                message = {"status": "success"}
                return JsonResponse(message, status=status.HTTP_201_CREATED)
            except Exception as e:
                content = {'error saving data': str(e)}
                print(e)
                return JsonResponse(content, status=403)

        return super().post(request, *args, **kwargs)


class MeterReadingsView(ListView, CreateView):
    model = Report
    form_class = ReportForm
    template_name = 'meter_readings.html'

    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)

    def get_queryset(self):

        """Fetches reports for that particular date"""

        day_report = super(MeterReadingsView, self).get_queryset()
        day_report = day_report.filter(date_created__date=datetime.today()).order_by('-id')
        return day_report

    def post(self, request, *args, **kwargs):
        self.object = None
        if self.request.is_ajax():
            pump = self.request.POST.get('pump')
            opening_reading = self.request.POST.get("openingReading")
            closing_reading = self.request.POST.get("closingReading")
            meter_movement = self.request.POST.get("meterMovement")
            transfers = self.request.POST.get("transfers")
            net_sales = self.request.POST.get("netSales")
            try:
                pump_object = Pump.objects.get(id=pump)
                report = Report(pump=pump_object, opening_reading=opening_reading, closing_reading=closing_reading,
                                meter_movement=meter_movement, transfers=transfers, net_sales=net_sales)
                report.save()
                report_data = Report.objects.filter(id=report.id).all()
                serializer = ReportSerializer(report_data, many=True)
                return JsonResponse(serializer.data, safe=False)
            except Exception as e:
                content = {'error saving data': str(e)}
                return JsonResponse(content, status=status.HTTP_403_FORBIDDEN)

        return super().post(request, *args, **kwargs)
