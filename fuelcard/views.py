import logging
from django.views.generic import CreateView, TemplateView, ListView
from django.http import JsonResponse
from django.urls import reverse_lazy
from rest_framework import status
from fuelcard.forms import ReportForm, TankForm, ItemSalesForm
from fuelcard.models import Pump, Report, Tank, ItemSales
from fuelcard.serializers import ReportSerializer

from fuelcard.utils import NetSales, ProductRatings

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
    net_sales = NetSales(datetime.today())

    def get_context_data(self, **kwargs):
        self.object = None
        context = super(ReadingView, self).get_context_data(**kwargs)
        try:
            pms_meter_sales = self.net_sales.pms()
            pms = Tank.objects.get(product_category='PMS', date_created__date=datetime.today())
            pms_daily_variations = pms_meter_sales - pms.tank_sales()
            context['pms_sales'] = pms_meter_sales
            context['pms'] = pms
            context['pms_daily_variations'] = pms_daily_variations
        except Exception as e:
            logging.error(e)
        try:
            context['truck'] = Tank.objects.get(product_category='TRUCK')
        except Exception as e:
            logging.error(e)
        try:
            ago_meter_sales = self.net_sales.ago()
            ago = Tank.objects.get(product_category='AGO', date_created__date=datetime.today())
            ago_daily_variations = ago_meter_sales - ago.tank_sales()
            context['ago_sales'] = ago_meter_sales
            context['ago'] = ago
            context['ago_daily_variations'] = ago_daily_variations

        except Exception as e:
            logging.error(e)
        try:
            bik_meter_sales = self.net_sales.bik()
            bik = Tank.objects.get(product_category='BIK', date_created__date=datetime.today())
            bik_daily_variations = bik_meter_sales - bik.tank_sales()
            context['bik_sales'] = bik_meter_sales
            context['bik'] = bik
            context['bik_daily_variations'] = bik_daily_variations
        except Exception as e:
            logging.error(e)
        return context

    def get_queryset(self):

        """Fetches Meter readings for that particular date"""

        day_report = super(ReadingView, self).get_queryset()
        day_report = day_report.filter(date_created__date=datetime.today()).order_by('-id')
        return day_report


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


class SalesReport(TemplateView):
    template_name = 'sales.html'
    net_sales_object = NetSales(datetime.today())
    product_ratings = ProductRatings(datetime.today())

    def get_context_data(self, **kwargs):
        self.object = None
        context = super(SalesReport, self).get_context_data(**kwargs)
        pms_amount = self.net_sales_object.pms() * self.product_ratings.pms()
        context['pms_ratings'] = self.product_ratings.pms()
        context['pms_amount'] = pms_amount

        ago_amount = self.net_sales_object.ago() * self.product_ratings.ago()
        context['ago_ratings'] = self.product_ratings.ago()
        context['ago_amount'] = ago_amount

        bik_amount = self.net_sales_object.bik() * self.product_ratings.bik()
        context['bik_amount'] = bik_amount
        context['bik_ratings'] = self.product_ratings.bik()

        fuel_sales = pms_amount + ago_amount + bik_amount
        other_sales = self.net_sales_object.total_other_sales()
        gross_sales = fuel_sales + other_sales
        context['gross_sales'] = gross_sales

        context['pms'] = self.net_sales_object.pms()
        context['ago'] = self.net_sales_object.ago()
        context['bik'] = self.net_sales_object.bik()

        sales_list = ItemSales.objects.filter(date_created__date=datetime.today()).order_by('-id')
        context['total_item_sales'] = self.net_sales_object.total_other_sales()
        context['object_list'] = sales_list
        return context


class Sales(CreateView):
    template_name = 'sales_item.html'
    form_class = ItemSalesForm
    success_url = reverse_lazy('sales')

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
