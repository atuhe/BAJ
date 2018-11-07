from django.views.generic import CreateView, TemplateView, ListView
from fuelcard.forms import ReportForm
from fuelcard.models import Pump


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
