from django.views.generic import CreateView, TemplateView, ListView, DetailView
from fuelcard.forms import ReportForm
from fuelcard.models import Pump, Report


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


class ReportView(CreateView):
    form_class = ReportForm
    template_name = 'report.html'

    def get(self, request, *args, **kwargs):
        self.object = None
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        pump = self.request.POST.get('pump')
        opening_reading = self.request.POST.get("openingReading")
        closing_reading = self.request.POST.get("closingReading")
        meter_movement = self.request.POST.get("meterMovement")
        transfers = self.request.POST.get("transfers")
        net_sales = self.request.POST.get("netSales")

        pump_object = Pump.objects.get(id=pump)

        report = Report(pump=pump_object, opening_reading=opening_reading, closing_reading=closing_reading,
                        meter_movement=meter_movement, transfers=transfers, net_sales=net_sales)
        report.save()

        return super().post(request, *args, **kwargs)
