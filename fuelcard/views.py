from django.views.generic import CreateView, TemplateView, ListView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from fuelcard.forms import ReportForm
from fuelcard.models import Pump, Report
from fuelcard.serializers import ReportSerializer


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


class ReportView(ListView, CreateView):
    model = Report
    form_class = ReportForm
    ordering = ['-id']
    template_name = 'report.html'

    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)

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
                content = {'error saving data': e}
                return Response(content, status=status.HTTP_403_FORBIDDEN)

        return super().post(request, *args, **kwargs)
